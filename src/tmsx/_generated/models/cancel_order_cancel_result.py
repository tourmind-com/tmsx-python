from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CancelOrderCancelResult")


@_attrs_define
class CancelOrderCancelResult:
    """
    Attributes:
        cancel_fee (float | Unset): Cancellation penalty fee charged. Example: 42.
        currency_code (str | Unset): Currency code for the charge amount. Example: CNY.
        order_status (str | Unset): Order status.
            <br><table><tr><th>OrderStatus</th><th>Description</th></tr><tr><td>PENDING</td><td>Booking confirmation
            pending.</td></tr><tr><td>CONFIRMED</td><td>Booking confirmed.</td></tr><tr><td>CANCELLED</td><td>Booking
            cancelled.</td></tr><tr><td>FAILED</td><td>Booking confirmation failed.</td></tr></table> Example: CANCELLED.
    """

    cancel_fee: float | Unset = UNSET
    currency_code: str | Unset = UNSET
    order_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancel_fee = self.cancel_fee

        currency_code = self.currency_code

        order_status = self.order_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancel_fee is not UNSET:
            field_dict["CancelFee"] = cancel_fee
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code
        if order_status is not UNSET:
            field_dict["OrderStatus"] = order_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancel_fee = d.pop("CancelFee", UNSET)

        currency_code = d.pop("CurrencyCode", UNSET)

        order_status = d.pop("OrderStatus", UNSET)

        cancel_order_cancel_result = cls(
            cancel_fee=cancel_fee,
            currency_code=currency_code,
            order_status=order_status,
        )

        cancel_order_cancel_result.additional_properties = d
        return cancel_order_cancel_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
