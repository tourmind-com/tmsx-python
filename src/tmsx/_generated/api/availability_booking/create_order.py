from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.common_error import CommonError
from ...models.create_order_create_order_request import CreateOrderCreateOrderRequest
from ...models.create_order_create_order_response import CreateOrderCreateOrderResponse


def _get_kwargs(
    *,
    body: CreateOrderCreateOrderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/CreateOrder",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommonError | CreateOrderCreateOrderResponse:
    if response.status_code == 200:
        response_200 = CreateOrderCreateOrderResponse.from_dict(response.json())

        return response_200

    response_default = CommonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommonError | CreateOrderCreateOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrderCreateOrderRequest,
) -> Response[CommonError | CreateOrderCreateOrderResponse]:
    """Booking

     Booking

    Note: If the request times out, returns a PENDING status, or returns an error, please poll the
    Retrieve Booking API to obtain the final status of the booking.

    Args:
        body (CreateOrderCreateOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | CreateOrderCreateOrderResponse]
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
    body: CreateOrderCreateOrderRequest,
) -> CommonError | CreateOrderCreateOrderResponse | None:
    """Booking

     Booking

    Note: If the request times out, returns a PENDING status, or returns an error, please poll the
    Retrieve Booking API to obtain the final status of the booking.

    Args:
        body (CreateOrderCreateOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | CreateOrderCreateOrderResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrderCreateOrderRequest,
) -> Response[CommonError | CreateOrderCreateOrderResponse]:
    """Booking

     Booking

    Note: If the request times out, returns a PENDING status, or returns an error, please poll the
    Retrieve Booking API to obtain the final status of the booking.

    Args:
        body (CreateOrderCreateOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CommonError | CreateOrderCreateOrderResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrderCreateOrderRequest,
) -> CommonError | CreateOrderCreateOrderResponse | None:
    """Booking

     Booking

    Note: If the request times out, returns a PENDING status, or returns an error, please poll the
    Retrieve Booking API to obtain the final status of the booking.

    Args:
        body (CreateOrderCreateOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CommonError | CreateOrderCreateOrderResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
