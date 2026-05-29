from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.room_avail_rate_info import RoomAvailRateInfo


T = TypeVar("T", bound="RoomAvailRoomType")


@_attrs_define
class RoomAvailRoomType:
    """
    Attributes:
        bed_type_desc (str | Unset): Bed type description.
        bed_type_desc_cn (str | Unset): Bed type description in Chinese.
        name (str | Unset): Aggregated room type name, cleaner and easier to display, recommended. Note: in rare cases,
            it may differ from the sub-room name in RateInfo. Example: Suite 3 bedrooms.
        name_cn (str | Unset): Aggregated room type name in Chinese, cleaner and easier to display, recommended. Note:
            in rare cases, it may differ from the sub-room name in RateInfo. Example: Triple Room.
        rate_infos (list[RoomAvailRateInfo] | Unset): A list of rates for a room type; at least one rate will be
            returned.
        room_type_code (str | Unset): TourMind room type code, which is a unique identifier across all TourMind hotels.
            Example: 4613.
    """

    bed_type_desc: str | Unset = UNSET
    bed_type_desc_cn: str | Unset = UNSET
    name: str | Unset = UNSET
    name_cn: str | Unset = UNSET
    rate_infos: list[RoomAvailRateInfo] | Unset = UNSET
    room_type_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bed_type_desc = self.bed_type_desc

        bed_type_desc_cn = self.bed_type_desc_cn

        name = self.name

        name_cn = self.name_cn

        rate_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rate_infos, Unset):
            rate_infos = []
            for rate_infos_item_data in self.rate_infos:
                rate_infos_item = rate_infos_item_data.to_dict()
                rate_infos.append(rate_infos_item)

        room_type_code = self.room_type_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bed_type_desc is not UNSET:
            field_dict["BedTypeDesc"] = bed_type_desc
        if bed_type_desc_cn is not UNSET:
            field_dict["BedTypeDescCN"] = bed_type_desc_cn
        if name is not UNSET:
            field_dict["Name"] = name
        if name_cn is not UNSET:
            field_dict["NameCN"] = name_cn
        if rate_infos is not UNSET:
            field_dict["RateInfos"] = rate_infos
        if room_type_code is not UNSET:
            field_dict["RoomTypeCode"] = room_type_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.room_avail_rate_info import RoomAvailRateInfo

        d = dict(src_dict)
        bed_type_desc = d.pop("BedTypeDesc", UNSET)

        bed_type_desc_cn = d.pop("BedTypeDescCN", UNSET)

        name = d.pop("Name", UNSET)

        name_cn = d.pop("NameCN", UNSET)

        _rate_infos = d.pop("RateInfos", UNSET)
        rate_infos: list[RoomAvailRateInfo] | Unset = UNSET
        if _rate_infos is not UNSET:
            rate_infos = []
            for rate_infos_item_data in _rate_infos:
                rate_infos_item = RoomAvailRateInfo.from_dict(rate_infos_item_data)

                rate_infos.append(rate_infos_item)

        room_type_code = d.pop("RoomTypeCode", UNSET)

        room_avail_room_type = cls(
            bed_type_desc=bed_type_desc,
            bed_type_desc_cn=bed_type_desc_cn,
            name=name,
            name_cn=name_cn,
            rate_infos=rate_infos,
            room_type_code=room_type_code,
        )

        room_avail_room_type.additional_properties = d
        return room_avail_room_type

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
