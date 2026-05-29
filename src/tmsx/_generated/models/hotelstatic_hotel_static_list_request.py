from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.common_request_header import CommonRequestHeader
    from ..models.hotelstatic_pagination import HotelstaticPagination


T = TypeVar("T", bound="HotelstaticHotelStaticListRequest")


@_attrs_define
class HotelstaticHotelStaticListRequest:
    """
    Attributes:
        country_code (str | Unset): Country code. Example: CN.
        hotel_ids (list[int] | Unset): Identifiers for specific hotels..
        pagination (HotelstaticPagination | Unset):
        request_header (CommonRequestHeader | Unset):
    """

    country_code: str | Unset = UNSET
    hotel_ids: list[int] | Unset = UNSET
    pagination: HotelstaticPagination | Unset = UNSET
    request_header: CommonRequestHeader | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        hotel_ids: list[int] | Unset = UNSET
        if not isinstance(self.hotel_ids, Unset):
            hotel_ids = self.hotel_ids

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        request_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_header, Unset):
            request_header = self.request_header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_code is not UNSET:
            field_dict["CountryCode"] = country_code
        if hotel_ids is not UNSET:
            field_dict["HotelIds"] = hotel_ids
        if pagination is not UNSET:
            field_dict["Pagination"] = pagination
        if request_header is not UNSET:
            field_dict["RequestHeader"] = request_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_request_header import CommonRequestHeader
        from ..models.hotelstatic_pagination import HotelstaticPagination

        d = dict(src_dict)
        country_code = d.pop("CountryCode", UNSET)

        hotel_ids = cast(list[int], d.pop("HotelIds", UNSET))

        _pagination = d.pop("Pagination", UNSET)
        pagination: HotelstaticPagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = HotelstaticPagination.from_dict(_pagination)

        _request_header = d.pop("RequestHeader", UNSET)
        request_header: CommonRequestHeader | Unset
        if isinstance(_request_header, Unset):
            request_header = UNSET
        else:
            request_header = CommonRequestHeader.from_dict(_request_header)

        hotelstatic_hotel_static_list_request = cls(
            country_code=country_code,
            hotel_ids=hotel_ids,
            pagination=pagination,
            request_header=request_header,
        )

        hotelstatic_hotel_static_list_request.additional_properties = d
        return hotelstatic_hotel_static_list_request

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
