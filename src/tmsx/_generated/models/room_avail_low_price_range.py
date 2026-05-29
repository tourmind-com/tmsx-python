from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="RoomAvailLowPriceRange")


@_attrs_define
class RoomAvailLowPriceRange:
    """
    Attributes:
        currency_code (str | Unset): Currency code for the prices
        max_ (float | Unset): Maximum price in the range
        min_ (float | Unset): Minimum price in the range
    """

    currency_code: str | Unset = UNSET
    max_: float | Unset = UNSET
    min_: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        max_ = self.max_

        min_ = self.min_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code
        if max_ is not UNSET:
            field_dict["Max"] = max_
        if min_ is not UNSET:
            field_dict["Min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("CurrencyCode", UNSET)

        max_ = d.pop("Max", UNSET)

        min_ = d.pop("Min", UNSET)

        room_avail_low_price_range = cls(
            currency_code=currency_code,
            max_=max_,
            min_=min_,
        )

        room_avail_low_price_range.additional_properties = d
        return room_avail_low_price_range

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
