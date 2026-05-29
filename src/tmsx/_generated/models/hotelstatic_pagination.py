from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="HotelstaticPagination")


@_attrs_define
class HotelstaticPagination:
    """
    Attributes:
        page_index (Any | Unset): PageIndex needs to accommodate both string and integer types. [1 or '1'] Example: 1.
        page_size (int | Unset): Items per page. Example: 10.
    """

    page_index: Any | Unset = UNSET
    page_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_index = self.page_index

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_index is not UNSET:
            field_dict["PageIndex"] = page_index
        if page_size is not UNSET:
            field_dict["PageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_index = d.pop("PageIndex", UNSET)

        page_size = d.pop("PageSize", UNSET)

        hotelstatic_pagination = cls(
            page_index=page_index,
            page_size=page_size,
        )

        hotelstatic_pagination.additional_properties = d
        return hotelstatic_pagination

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
