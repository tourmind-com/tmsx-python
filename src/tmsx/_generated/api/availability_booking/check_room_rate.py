from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.common_error import CommonError
from ...models.room_avail_room_avail_request import RoomAvailRoomAvailRequest
from ...models.room_avail_room_avail_response import RoomAvailRoomAvailResponse


def _get_kwargs(
    *,
    body: RoomAvailRoomAvailRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/CheckRoomRate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommonError | RoomAvailRoomAvailResponse:
    if response.status_code == 200:
        response_200 = RoomAvailRoomAvailResponse.from_dict(response.json())

        return response_200

    response_default = CommonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommonError | RoomAvailRoomAvailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RoomAvailRoomAvailRequest,
) -> Response[CommonError | RoomAvailRoomAvailResponse]:
    """Prebook

     Check the availability and price of a specific room rate selected, usually requested when the user
    selects a room to book and submits a booking. <br><br>

    Args:
        body (RoomAvailRoomAvailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | RoomAvailRoomAvailResponse]
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
    body: RoomAvailRoomAvailRequest,
) -> CommonError | RoomAvailRoomAvailResponse | None:
    """Prebook

     Check the availability and price of a specific room rate selected, usually requested when the user
    selects a room to book and submits a booking. <br><br>

    Args:
        body (RoomAvailRoomAvailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | RoomAvailRoomAvailResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RoomAvailRoomAvailRequest,
) -> Response[CommonError | RoomAvailRoomAvailResponse]:
    """Prebook

     Check the availability and price of a specific room rate selected, usually requested when the user
    selects a room to book and submits a booking. <br><br>

    Args:
        body (RoomAvailRoomAvailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | RoomAvailRoomAvailResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RoomAvailRoomAvailRequest,
) -> CommonError | RoomAvailRoomAvailResponse | None:
    """Prebook

     Check the availability and price of a specific room rate selected, usually requested when the user
    selects a room to book and submits a booking. <br><br>

    Args:
        body (RoomAvailRoomAvailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | RoomAvailRoomAvailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
