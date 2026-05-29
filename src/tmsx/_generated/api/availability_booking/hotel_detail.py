from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.common_error import CommonError
from ...models.hotel_detail_hotel_detail_request import HotelDetailHotelDetailRequest
from ...models.hotel_detail_hotel_detail_response import HotelDetailHotelDetailResponse


def _get_kwargs(
    *,
    body: HotelDetailHotelDetailRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/HotelDetail",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommonError | HotelDetailHotelDetailResponse:
    if response.status_code == 200:
        response_200 = HotelDetailHotelDetailResponse.from_dict(response.json())

        return response_200

    response_default = CommonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommonError | HotelDetailHotelDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: HotelDetailHotelDetailRequest,
) -> Response[CommonError | HotelDetailHotelDetailResponse]:
    """Search

     Search hotel room rates and available inventory for a specific property, enabling users to view
    detailed room availability and pricing information.

    Args:
        body (HotelDetailHotelDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | HotelDetailHotelDetailResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: HotelDetailHotelDetailRequest,
) -> CommonError | HotelDetailHotelDetailResponse | None:
    """Search

     Search hotel room rates and available inventory for a specific property, enabling users to view
    detailed room availability and pricing information.

    Args:
        body (HotelDetailHotelDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | HotelDetailHotelDetailResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: HotelDetailHotelDetailRequest,
) -> Response[CommonError | HotelDetailHotelDetailResponse]:
    """Search

     Search hotel room rates and available inventory for a specific property, enabling users to view
    detailed room availability and pricing information.

    Args:
        body (HotelDetailHotelDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | HotelDetailHotelDetailResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: HotelDetailHotelDetailRequest,
) -> CommonError | HotelDetailHotelDetailResponse | None:
    """Search

     Search hotel room rates and available inventory for a specific property, enabling users to view
    detailed room availability and pricing information.

    Args:
        body (HotelDetailHotelDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | HotelDetailHotelDetailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
