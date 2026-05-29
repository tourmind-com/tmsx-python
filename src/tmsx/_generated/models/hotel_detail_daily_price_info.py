from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="HotelDetailDailyPriceInfo")


@_attrs_define
class HotelDetailDailyPriceInfo:
    """
    Attributes:
        count (int | Unset): this is daily inventory count
        date (str | Unset): Date, format: "2006-01-02"
        price (float | Unset): Price for 1 room per night.
    """

    count: int | Unset = UNSET
    date: str | Unset = UNSET
    price: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        date = self.date

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["Count"] = count
        if date is not UNSET:
            field_dict["Date"] = date
        if price is not UNSET:
            field_dict["Price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("Count", UNSET)

        date = d.pop("Date", UNSET)

        price = d.pop("Price", UNSET)

        hotel_detail_daily_price_info = cls(
            count=count,
            date=date,
            price=price,
        )

        hotel_detail_daily_price_info.additional_properties = d
        return hotel_detail_daily_price_info

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
