from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateOrderOrderInfo")


@_attrs_define
class CreateOrderOrderInfo:
    """
    Attributes:
        order_status (str | Unset): Order status.
            <br><table><tr><th>OrderStatus</th><th>Description</th></tr><tr><td>PENDING</td><td>Booking confirmation
            pending.</td></tr><tr><td>CONFIRMED</td><td>Booking confirmed.</td></tr><tr><td>CANCELLED</td><td>Booking
            cancelled.</td></tr><tr><td>FAILED</td><td>Booking confirmation failed.</td></tr></table> Example: CONFIRMED.
        reservation_id (str | Unset): Tourmind order ID Example: 10470379.
    """

    order_status: str | Unset = UNSET
    reservation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_status = self.order_status

        reservation_id = self.reservation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_status is not UNSET:
            field_dict["OrderStatus"] = order_status
        if reservation_id is not UNSET:
            field_dict["ReservationID"] = reservation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_status = d.pop("OrderStatus", UNSET)

        reservation_id = d.pop("ReservationID", UNSET)

        create_order_order_info = cls(
            order_status=order_status,
            reservation_id=reservation_id,
        )

        create_order_order_info.additional_properties = d
        return create_order_order_info

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
