from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.common_error import CommonError
from ...models.room_static_model_room_static_request import (
    RoomStaticModelRoomStaticRequest,
)
from ...models.room_static_model_room_static_response import (
    RoomStaticModelRoomStaticResponse,
)


def _get_kwargs(
    *,
    body: RoomStaticModelRoomStaticRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/RoomStaticList",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommonError | RoomStaticModelRoomStaticResponse:
    if response.status_code == 200:
        response_200 = RoomStaticModelRoomStaticResponse.from_dict(response.json())

        return response_200

    response_default = CommonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommonError | RoomStaticModelRoomStaticResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RoomStaticModelRoomStaticRequest,
) -> Response[CommonError | RoomStaticModelRoomStaticResponse]:
    """Hotel Room Type List

     Retrieve the list of room information of sepecific hotels.

    Args:
        body (RoomStaticModelRoomStaticRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | RoomStaticModelRoomStaticResponse]
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
    body: RoomStaticModelRoomStaticRequest,
) -> CommonError | RoomStaticModelRoomStaticResponse | None:
    """Hotel Room Type List

     Retrieve the list of room information of sepecific hotels.

    Args:
        body (RoomStaticModelRoomStaticRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | RoomStaticModelRoomStaticResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RoomStaticModelRoomStaticRequest,
) -> Response[CommonError | RoomStaticModelRoomStaticResponse]:
    """Hotel Room Type List

     Retrieve the list of room information of sepecific hotels.

    Args:
        body (RoomStaticModelRoomStaticRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | RoomStaticModelRoomStaticResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RoomStaticModelRoomStaticRequest,
) -> CommonError | RoomStaticModelRoomStaticResponse | None:
    """Hotel Room Type List

     Retrieve the list of room information of sepecific hotels.

    Args:
        body (RoomStaticModelRoomStaticRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | RoomStaticModelRoomStaticResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
