from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.room_avail_date_range import RoomAvailDateRange
    from ..models.room_avail_low_price_range import RoomAvailLowPriceRange


T = TypeVar("T", bound="RoomAvailLowPricePeriod")


@_attrs_define
class RoomAvailLowPricePeriod:
    """
    Attributes:
        current_price (float | Unset): Current price of the hotel
        date_range (RoomAvailDateRange | Unset):
        low_price_range (RoomAvailLowPriceRange | Unset):
        update_time (str | Unset): Last update time of the price prediction
    """

    current_price: float | Unset = UNSET
    date_range: RoomAvailDateRange | Unset = UNSET
    low_price_range: RoomAvailLowPriceRange | Unset = UNSET
    update_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_price = self.current_price

        date_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_range, Unset):
            date_range = self.date_range.to_dict()

        low_price_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.low_price_range, Unset):
            low_price_range = self.low_price_range.to_dict()

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_price is not UNSET:
            field_dict["CurrentPrice"] = current_price
        if date_range is not UNSET:
            field_dict["DateRange"] = date_range
        if low_price_range is not UNSET:
            field_dict["LowPriceRange"] = low_price_range
        if update_time is not UNSET:
            field_dict["UpdateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.room_avail_date_range import RoomAvailDateRange
        from ..models.room_avail_low_price_range import RoomAvailLowPriceRange

        d = dict(src_dict)
        current_price = d.pop("CurrentPrice", UNSET)

        _date_range = d.pop("DateRange", UNSET)
        date_range: RoomAvailDateRange | Unset
        if isinstance(_date_range, Unset):
            date_range = UNSET
        else:
            date_range = RoomAvailDateRange.from_dict(_date_range)

        _low_price_range = d.pop("LowPriceRange", UNSET)
        low_price_range: RoomAvailLowPriceRange | Unset
        if isinstance(_low_price_range, Unset):
            low_price_range = UNSET
        else:
            low_price_range = RoomAvailLowPriceRange.from_dict(_low_price_range)

        update_time = d.pop("UpdateTime", UNSET)

        room_avail_low_price_period = cls(
            current_price=current_price,
            date_range=date_range,
            low_price_range=low_price_range,
            update_time=update_time,
        )

        room_avail_low_price_period.additional_properties = d
        return room_avail_low_price_period

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
