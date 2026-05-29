"""High-level Client / AsyncClient facade for the TMSX hotel API.

Wraps the auto-generated `tmsx._generated` low-level client with:
- automatic injection of the dual-channel TMSX auth (HTTP headers + RequestHeader
  body envelope), so callers never write boilerplate auth code
- translation of body-level `Error.ErrorCode` envelopes into Python exceptions
- ergonomic kwargs-based call sites that mirror the operation contract

See `https://github.com/tourmind-com/tmsx-platform/blob/main/AUTH.md` for the auth scheme this implements.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from typing import Any, TypeVar

import httpx
from httpx._content import ByteStream  # noqa: PLC2701 — stable private API

from tmsx._generated import client as _gen_client
from tmsx._generated.api.availability_booking import (
    cancel_order as _cancel_order,
    check_room_rate as _check_room_rate,
    create_order as _create_order,
    hotel_detail as _hotel_detail,
    query_bookings as _query_bookings,
    search_order as _search_order,
)
from tmsx._generated.api.static_data import (
    hotel_static_list as _hotel_static_list,
    region_list as _region_list,
    room_type_static as _room_type_static,
)
from tmsx._generated.models import (
    CancelOrderCancelOrderRequest,
    CancelOrderCancelOrderResponse,
    CommonError,
    CreateOrderCreateOrderRequest,
    CreateOrderCreateOrderResponse,
    HotelDetailHotelDetailRequest,
    HotelDetailHotelDetailResponse,
    HotelstaticHotelStaticListRequest,
    HotelstaticHotelStaticListResponse,
    RegionListRegionListRequest,
    RegionListRegionListResponse,
    RoomAvailRoomAvailRequest,
    RoomAvailRoomAvailResponse,
    RoomStaticModelRoomStaticRequest,
    RoomStaticModelRoomStaticResponse,
    SearchOrderQueryBookingsRequest,
    SearchOrderQueryBookingsResponse,
    SearchOrderQueryOrderRequest,
    SearchOrderQueryOrderResponse,
)
from tmsx.exceptions import TMSXClientError, from_error_code

_RequestBody = TypeVar("_RequestBody")
_ResponseBody = TypeVar("_ResponseBody")

DEFAULT_BASE_URL = "http://developers.tourmind.cn"
DEFAULT_TIMEOUT_SECONDS = 30.0


def _iso_now() -> str:
    """ISO 8601 timestamp with millisecond precision and trailing 'Z', as required by TMSX."""
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{now.microsecond // 1000:03d}Z"


def _new_transaction_id() -> str:
    """Fresh UUID v4 — TMSX echoes this in the response for correlation."""
    return str(uuid.uuid4())


def _build_request_header(agent_code: str, username: str, password: str) -> dict[str, str]:
    """Build a fresh RequestHeader envelope. New TransactionID per call."""
    return {
        "AgentCode": agent_code,
        "UserName": username,
        "Password": password,
        "RequestTime": _iso_now(),
        "TransactionID": _new_transaction_id(),
    }


def _inject_body_envelope(request: httpx.Request, header_factory) -> None:
    """Mutate `request` in-place to add the RequestHeader body envelope if missing.

    No-op for requests with non-JSON or empty bodies.

    httpx ships the request via `request.stream`, so we must replace BOTH `_content`
    and `stream` (and the content-length header) for the mutation to actually reach
    the wire.
    """
    request.read()  # ensure stream is materialized into _content
    if not request.content:
        return
    content_type = request.headers.get("content-type", "")
    if "application/json" not in content_type:
        return
    try:
        body = json.loads(request.content)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return  # not our problem to fix non-JSON bodies
    if not isinstance(body, dict):
        return
    if body.get("RequestHeader"):
        return  # caller already supplied one — respect it
    body["RequestHeader"] = header_factory()
    new_content = json.dumps(body).encode("utf-8")
    request._content = new_content  # noqa: SLF001 — httpx private but stable across versions
    request.stream = ByteStream(new_content)
    request.headers["content-length"] = str(len(new_content))


def _check_for_error(parsed: Any) -> None:
    """If the parsed response carries an Error envelope, raise the matching exception."""
    if parsed is None:
        return
    if isinstance(parsed, CommonError):
        raise from_error_code(parsed.error_code, parsed.error_message or "TMSX API error")
    error = getattr(parsed, "error", None)
    if error is not None and getattr(error, "error_code", None):
        response_header = getattr(parsed, "response_header", None)
        transaction_id = getattr(response_header, "transaction_id", None) if response_header else None
        raise from_error_code(
            error.error_code,
            error.error_message or "TMSX API error",
            transaction_id=transaction_id,
        )


class _TmsxAuthTransport(httpx.HTTPTransport):
    """httpx transport that injects TMSX auth (headers + body envelope) on every request."""

    def __init__(
        self,
        *,
        agent_code: str,
        username: str,
        password: str,
        verify: bool = True,
    ) -> None:
        super().__init__(verify=verify)
        self._agent_code = agent_code
        self._username = username
        self._password = password

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.headers["X-Agent-Code"] = self._agent_code
        request.headers["X-Username"] = self._username
        _inject_body_envelope(
            request,
            lambda: _build_request_header(self._agent_code, self._username, self._password),
        )
        return super().handle_request(request)


class _TmsxAsyncAuthTransport(httpx.AsyncHTTPTransport):
    """Async counterpart of _TmsxAuthTransport."""

    def __init__(
        self,
        *,
        agent_code: str,
        username: str,
        password: str,
        verify: bool = True,
    ) -> None:
        super().__init__(verify=verify)
        self._agent_code = agent_code
        self._username = username
        self._password = password

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        request.headers["X-Agent-Code"] = self._agent_code
        request.headers["X-Username"] = self._username
        _inject_body_envelope(
            request,
            lambda: _build_request_header(self._agent_code, self._username, self._password),
        )
        return await super().handle_async_request(request)


class Client:
    """Synchronous TMSX hotel-API client.

    Example:
        >>> client = Client(
        ...     agent_code="tms_test",
        ...     username="tms_test",
        ...     password="tms_test",
        ... )
        >>> regions = client.list_regions(country_code="CN")
        >>> regions.region_list_result.regions[0].name
        'Région Test'
    """

    def __init__(
        self,
        *,
        agent_code: str,
        username: str,
        password: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        verify_ssl: bool = True,
    ) -> None:
        transport = _TmsxAuthTransport(
            agent_code=agent_code,
            username=username,
            password=password,
            verify=verify_ssl,
        )
        httpx_client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            transport=transport,
            headers={"Accept": "application/json"},
        )
        self._inner = _gen_client.Client(base_url=base_url).set_httpx_client(httpx_client)
        self._httpx_client = httpx_client

    def close(self) -> None:
        self._httpx_client.close()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        self.close()

    # --- StaticData ----------------------------------------------------------

    def list_regions(self, *, country_code: str | None = None) -> RegionListRegionListResponse:
        """Retrieve the list of regions, optionally filtered by `country_code` (e.g. `CN`)."""
        body = RegionListRegionListRequest()
        if country_code is not None:
            body.country_code = country_code
        return self._call(_region_list.sync, body)

    def list_hotels(self, body: HotelstaticHotelStaticListRequest) -> HotelstaticHotelStaticListResponse:
        """Retrieve static data for hotels."""
        return self._call(_hotel_static_list.sync, body)

    def list_room_types(self, body: RoomStaticModelRoomStaticRequest) -> RoomStaticModelRoomStaticResponse:
        """Retrieve room-type static data for specific hotels."""
        return self._call(_room_type_static.sync, body)

    # --- Availability & Booking ---------------------------------------------

    def search_hotel(self, body: HotelDetailHotelDetailRequest) -> HotelDetailHotelDetailResponse:
        """Search room rates / availability for a specific property."""
        return self._call(_hotel_detail.sync, body)

    def check_room_rate(self, body: RoomAvailRoomAvailRequest) -> RoomAvailRoomAvailResponse:
        """Prebook — check availability + price of a specific room rate."""
        return self._call(_check_room_rate.sync, body)

    def create_order(self, body: CreateOrderCreateOrderRequest) -> CreateOrderCreateOrderResponse:
        """Create a booking. Poll `search_order` for final status on PENDING/timeout/error."""
        return self._call(_create_order.sync, body)

    def search_order(self, body: SearchOrderQueryOrderRequest) -> SearchOrderQueryOrderResponse:
        """Retrieve a booking by reference."""
        return self._call(_search_order.sync, body)

    def query_bookings(self, body: SearchOrderQueryBookingsRequest) -> SearchOrderQueryBookingsResponse:
        """List bookings by date range with pagination."""
        return self._call(_query_bookings.sync, body)

    def cancel_order(self, body: CancelOrderCancelOrderRequest) -> CancelOrderCancelOrderResponse:
        """Cancel a refundable or pending booking."""
        return self._call(_cancel_order.sync, body)

    # --- Internals ----------------------------------------------------------

    def _call(self, fn, body):
        try:
            parsed = fn(client=self._inner, body=body)
        except httpx.HTTPError as exc:
            raise TMSXClientError(f"transport error: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise TMSXClientError(f"API returned non-JSON response: {exc}") from exc
        _check_for_error(parsed)
        return parsed


class AsyncClient:
    """Asynchronous TMSX hotel-API client. Same surface as `Client`, but every operation is `await`able."""

    def __init__(
        self,
        *,
        agent_code: str,
        username: str,
        password: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        verify_ssl: bool = True,
    ) -> None:
        transport = _TmsxAsyncAuthTransport(
            agent_code=agent_code,
            username=username,
            password=password,
            verify=verify_ssl,
        )
        async_httpx = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            transport=transport,
            headers={"Accept": "application/json"},
        )
        # The generated client supports both sync + async via separate getters; we set the async one.
        self._inner = _gen_client.Client(base_url=base_url)
        self._inner._async_client = async_httpx  # noqa: SLF001
        self._async_httpx = async_httpx

    async def aclose(self) -> None:
        await self._async_httpx.aclose()

    async def __aenter__(self) -> "AsyncClient":
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        await self.aclose()

    async def list_regions(self, *, country_code: str | None = None) -> RegionListRegionListResponse:
        body = RegionListRegionListRequest()
        if country_code is not None:
            body.country_code = country_code
        return await self._call(_region_list.asyncio, body)

    async def list_hotels(self, body: HotelstaticHotelStaticListRequest) -> HotelstaticHotelStaticListResponse:
        return await self._call(_hotel_static_list.asyncio, body)

    async def list_room_types(self, body: RoomStaticModelRoomStaticRequest) -> RoomStaticModelRoomStaticResponse:
        return await self._call(_room_type_static.asyncio, body)

    async def search_hotel(self, body: HotelDetailHotelDetailRequest) -> HotelDetailHotelDetailResponse:
        return await self._call(_hotel_detail.asyncio, body)

    async def check_room_rate(self, body: RoomAvailRoomAvailRequest) -> RoomAvailRoomAvailResponse:
        return await self._call(_check_room_rate.asyncio, body)

    async def create_order(self, body: CreateOrderCreateOrderRequest) -> CreateOrderCreateOrderResponse:
        return await self._call(_create_order.asyncio, body)

    async def search_order(self, body: SearchOrderQueryOrderRequest) -> SearchOrderQueryOrderResponse:
        return await self._call(_search_order.asyncio, body)

    async def query_bookings(self, body: SearchOrderQueryBookingsRequest) -> SearchOrderQueryBookingsResponse:
        return await self._call(_query_bookings.asyncio, body)

    async def cancel_order(self, body: CancelOrderCancelOrderRequest) -> CancelOrderCancelOrderResponse:
        return await self._call(_cancel_order.asyncio, body)

    async def _call(self, fn, body):
        try:
            parsed = await fn(client=self._inner, body=body)
        except httpx.HTTPError as exc:
            raise TMSXClientError(f"transport error: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise TMSXClientError(f"API returned non-JSON response: {exc}") from exc
        _check_for_error(parsed)
        return parsed
