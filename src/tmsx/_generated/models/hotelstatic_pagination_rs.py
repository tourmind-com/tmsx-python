from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="HotelstaticPaginationRS")


@_attrs_define
class HotelstaticPaginationRS:
    """
    Attributes:
        page_count (int | Unset): Total number of pages. Example: 1.
        total_count (int | Unset): Total number of records. Example: 10.
    """

    page_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_count = self.page_count

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_count is not UNSET:
            field_dict["PageCount"] = page_count
        if total_count is not UNSET:
            field_dict["TotalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_count = d.pop("PageCount", UNSET)

        total_count = d.pop("TotalCount", UNSET)

        hotelstatic_pagination_rs = cls(
            page_count=page_count,
            total_count=total_count,
        )

        hotelstatic_pagination_rs.additional_properties = d
        return hotelstatic_pagination_rs

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
