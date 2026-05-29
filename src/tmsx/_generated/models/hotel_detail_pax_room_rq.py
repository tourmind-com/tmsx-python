from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="HotelDetailPaxRoomRQ")


@_attrs_define
class HotelDetailPaxRoomRQ:
    """
    Attributes:
        adults (int | Unset): Number of adults per room. Example: 4.
        children (int | Unset): Number of children per room.
        children_ages (list[int] | Unset): Children's ages; the count of the array must equal the number of children.
        room_count (int | Unset): Room count. Example: 2.
    """

    adults: int | Unset = UNSET
    children: int | Unset = UNSET
    children_ages: list[int] | Unset = UNSET
    room_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adults = self.adults

        children = self.children

        children_ages: list[int] | Unset = UNSET
        if not isinstance(self.children_ages, Unset):
            children_ages = self.children_ages

        room_count = self.room_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adults is not UNSET:
            field_dict["Adults"] = adults
        if children is not UNSET:
            field_dict["Children"] = children
        if children_ages is not UNSET:
            field_dict["ChildrenAges"] = children_ages
        if room_count is not UNSET:
            field_dict["RoomCount"] = room_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        adults = d.pop("Adults", UNSET)

        children = d.pop("Children", UNSET)

        children_ages = cast(list[int], d.pop("ChildrenAges", UNSET))

        room_count = d.pop("RoomCount", UNSET)

        hotel_detail_pax_room_rq = cls(
            adults=adults,
            children=children,
            children_ages=children_ages,
            room_count=room_count,
        )

        hotel_detail_pax_room_rq.additional_properties = d
        return hotel_detail_pax_room_rq

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
