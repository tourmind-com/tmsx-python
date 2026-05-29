from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.room_avail_low_price_period import RoomAvailLowPricePeriod
    from ..models.room_avail_room_type import RoomAvailRoomType


T = TypeVar("T", bound="RoomAvailHotel")


@_attrs_define
class RoomAvailHotel:
    """
    Attributes:
        check_in (str | Unset): Check-in date, format: “2006-01-02”. Example: 2018-08-25.
        check_out (str | Unset): Check-out date, format: “2006-01-02”. Example: 2018-08-26.
        hotel_code (str | Unset): Hotel code. Example: 740650.
        low_price_period (RoomAvailLowPricePeriod | Unset):
        room_types (list[RoomAvailRoomType] | Unset): Room types available based on the search criteria.
    """

    check_in: str | Unset = UNSET
    check_out: str | Unset = UNSET
    hotel_code: str | Unset = UNSET
    low_price_period: RoomAvailLowPricePeriod | Unset = UNSET
    room_types: list[RoomAvailRoomType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_in = self.check_in

        check_out = self.check_out

        hotel_code = self.hotel_code

        low_price_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.low_price_period, Unset):
            low_price_period = self.low_price_period.to_dict()

        room_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.room_types, Unset):
            room_types = []
            for room_types_item_data in self.room_types:
                room_types_item = room_types_item_data.to_dict()
                room_types.append(room_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_in is not UNSET:
            field_dict["CheckIn"] = check_in
        if check_out is not UNSET:
            field_dict["CheckOut"] = check_out
        if hotel_code is not UNSET:
            field_dict["HotelCode"] = hotel_code
        if low_price_period is not UNSET:
            field_dict["LowPricePeriod"] = low_price_period
        if room_types is not UNSET:
            field_dict["RoomTypes"] = room_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.room_avail_low_price_period import RoomAvailLowPricePeriod
        from ..models.room_avail_room_type import RoomAvailRoomType

        d = dict(src_dict)
        check_in = d.pop("CheckIn", UNSET)

        check_out = d.pop("CheckOut", UNSET)

        hotel_code = d.pop("HotelCode", UNSET)

        _low_price_period = d.pop("LowPricePeriod", UNSET)
        low_price_period: RoomAvailLowPricePeriod | Unset
        if isinstance(_low_price_period, Unset):
            low_price_period = UNSET
        else:
            low_price_period = RoomAvailLowPricePeriod.from_dict(_low_price_period)

        _room_types = d.pop("RoomTypes", UNSET)
        room_types: list[RoomAvailRoomType] | Unset = UNSET
        if _room_types is not UNSET:
            room_types = []
            for room_types_item_data in _room_types:
                room_types_item = RoomAvailRoomType.from_dict(room_types_item_data)

                room_types.append(room_types_item)

        room_avail_hotel = cls(
            check_in=check_in,
            check_out=check_out,
            hotel_code=hotel_code,
            low_price_period=low_price_period,
            room_types=room_types,
        )

        room_avail_hotel.additional_properties = d
        return room_avail_hotel

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
