from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="RoomStaticModelRoomTypeInfo")


@_attrs_define
class RoomStaticModelRoomTypeInfo:
    """
    Attributes:
        bed_type_desc (str | Unset):
        bed_type_desc_cn (str | Unset):
        max_occupancy (int | Unset):
        room_type_code (str | Unset):
        room_type_name (str | Unset):
        room_type_name_cn (str | Unset):
    """

    bed_type_desc: str | Unset = UNSET
    bed_type_desc_cn: str | Unset = UNSET
    max_occupancy: int | Unset = UNSET
    room_type_code: str | Unset = UNSET
    room_type_name: str | Unset = UNSET
    room_type_name_cn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bed_type_desc = self.bed_type_desc

        bed_type_desc_cn = self.bed_type_desc_cn

        max_occupancy = self.max_occupancy

        room_type_code = self.room_type_code

        room_type_name = self.room_type_name

        room_type_name_cn = self.room_type_name_cn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bed_type_desc is not UNSET:
            field_dict["BedTypeDesc"] = bed_type_desc
        if bed_type_desc_cn is not UNSET:
            field_dict["BedTypeDescCN"] = bed_type_desc_cn
        if max_occupancy is not UNSET:
            field_dict["MaxOccupancy"] = max_occupancy
        if room_type_code is not UNSET:
            field_dict["RoomTypeCode"] = room_type_code
        if room_type_name is not UNSET:
            field_dict["RoomTypeName"] = room_type_name
        if room_type_name_cn is not UNSET:
            field_dict["RoomTypeNameCN"] = room_type_name_cn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bed_type_desc = d.pop("BedTypeDesc", UNSET)

        bed_type_desc_cn = d.pop("BedTypeDescCN", UNSET)

        max_occupancy = d.pop("MaxOccupancy", UNSET)

        room_type_code = d.pop("RoomTypeCode", UNSET)

        room_type_name = d.pop("RoomTypeName", UNSET)

        room_type_name_cn = d.pop("RoomTypeNameCN", UNSET)

        room_static_model_room_type_info = cls(
            bed_type_desc=bed_type_desc,
            bed_type_desc_cn=bed_type_desc_cn,
            max_occupancy=max_occupancy,
            room_type_code=room_type_code,
            room_type_name=room_type_name,
            room_type_name_cn=room_type_name_cn,
        )

        room_static_model_room_type_info.additional_properties = d
        return room_static_model_room_type_info

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
