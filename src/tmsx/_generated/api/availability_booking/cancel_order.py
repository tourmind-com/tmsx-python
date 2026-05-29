from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.cancel_order_cancel_order_request import CancelOrderCancelOrderRequest
from ...models.cancel_order_cancel_order_response import CancelOrderCancelOrderResponse
from ...models.common_error import CommonError


def _get_kwargs(
    *,
    body: CancelOrderCancelOrderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/CancelOrder",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelOrderCancelOrderResponse | CommonError:
    if response.status_code == 200:
        response_200 = CancelOrderCancelOrderResponse.from_dict(response.json())

        return response_200

    response_default = CommonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CancelOrderCancelOrderResponse | CommonError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CancelOrderCancelOrderRequest,
) -> Response[CancelOrderCancelOrderResponse | CommonError]:
    """Cancel

     Send a cancel request to cancel refundable and pending bookings.

    Note: If the request times out or returns an error, please poll the Retrieve Booking API to obtain
    the final status of the booking.

    Args:
        body (CancelOrderCancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelOrderCancelOrderResponse | CommonError]
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
    body: CancelOrderCancelOrderRequest,
) -> CancelOrderCancelOrderResponse | CommonError | None:
    """Cancel

     Send a cancel request to cancel refundable and pending bookings.

    Note: If the request times out or returns an error, please poll the Retrieve Booking API to obtain
    the final status of the booking.

    Args:
        body (CancelOrderCancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelOrderCancelOrderResponse | CommonError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CancelOrderCancelOrderRequest,
) -> Response[CancelOrderCancelOrderResponse | CommonError]:
    """Cancel

     Send a cancel request to cancel refundable and pending bookings.

    Note: If the request times out or returns an error, please poll the Retrieve Booking API to obtain
    the final status of the booking.

    Args:
        body (CancelOrderCancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelOrderCancelOrderResponse | CommonError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CancelOrderCancelOrderRequest,
) -> CancelOrderCancelOrderResponse | CommonError | None:
    """Cancel

     Send a cancel request to cancel refundable and pending bookings.

    Note: If the request times out or returns an error, please poll the Retrieve Booking API to obtain
    the final status of the booking.

    Args:
        body (CancelOrderCancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelOrderCancelOrderResponse | CommonError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
