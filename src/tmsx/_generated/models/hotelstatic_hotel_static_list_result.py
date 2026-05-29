from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.hotelstatic_hotel_info import HotelstaticHotelInfo
    from ..models.hotelstatic_pagination_rs import HotelstaticPaginationRS


T = TypeVar("T", bound="HotelstaticHotelStaticListResult")


@_attrs_define
class HotelstaticHotelStaticListResult:
    """
    Attributes:
        hotels (list[HotelstaticHotelInfo] | Unset): Hotel information.
        pagination (HotelstaticPaginationRS | Unset):
    """

    hotels: list[HotelstaticHotelInfo] | Unset = UNSET
    pagination: HotelstaticPaginationRS | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hotels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hotels, Unset):
            hotels = []
            for hotels_item_data in self.hotels:
                hotels_item = hotels_item_data.to_dict()
                hotels.append(hotels_item)

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hotels is not UNSET:
            field_dict["Hotels"] = hotels
        if pagination is not UNSET:
            field_dict["Pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotelstatic_hotel_info import HotelstaticHotelInfo
        from ..models.hotelstatic_pagination_rs import HotelstaticPaginationRS

        d = dict(src_dict)
        _hotels = d.pop("Hotels", UNSET)
        hotels: list[HotelstaticHotelInfo] | Unset = UNSET
        if _hotels is not UNSET:
            hotels = []
            for hotels_item_data in _hotels:
                hotels_item = HotelstaticHotelInfo.from_dict(hotels_item_data)

                hotels.append(hotels_item)

        _pagination = d.pop("Pagination", UNSET)
        pagination: HotelstaticPaginationRS | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = HotelstaticPaginationRS.from_dict(_pagination)

        hotelstatic_hotel_static_list_result = cls(
            hotels=hotels,
            pagination=pagination,
        )

        hotelstatic_hotel_static_list_result.additional_properties = d
        return hotelstatic_hotel_static_list_result

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
