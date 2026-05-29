from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="RegionListRegion")


@_attrs_define
class RegionListRegion:
    """
    Attributes:
        country_code (str | Unset): ISO 3166-1 alpha-2, e.g., China: CN., Example: 231.
        name (str | Unset): Region name. Example: ShangHai.
        name_cn (str | Unset): Region name in Chinese. (Nullable.) Example: Shanghai.
        region_id (str | Unset): TourMind region ID. Example: 21312541.
        region_name_long (str | Unset): Region name Example: Shanghai, China.
        region_name_long_cn (str | Unset): Full region name in Chinese. Example: Shanghai, China.
    """

    country_code: str | Unset = UNSET
    name: str | Unset = UNSET
    name_cn: str | Unset = UNSET
    region_id: str | Unset = UNSET
    region_name_long: str | Unset = UNSET
    region_name_long_cn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        name = self.name

        name_cn = self.name_cn

        region_id = self.region_id

        region_name_long = self.region_name_long

        region_name_long_cn = self.region_name_long_cn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_code is not UNSET:
            field_dict["CountryCode"] = country_code
        if name is not UNSET:
            field_dict["Name"] = name
        if name_cn is not UNSET:
            field_dict["NameCN"] = name_cn
        if region_id is not UNSET:
            field_dict["RegionID"] = region_id
        if region_name_long is not UNSET:
            field_dict["RegionNameLong"] = region_name_long
        if region_name_long_cn is not UNSET:
            field_dict["RegionNameLongCN"] = region_name_long_cn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("CountryCode", UNSET)

        name = d.pop("Name", UNSET)

        name_cn = d.pop("NameCN", UNSET)

        region_id = d.pop("RegionID", UNSET)

        region_name_long = d.pop("RegionNameLong", UNSET)

        region_name_long_cn = d.pop("RegionNameLongCN", UNSET)

        region_list_region = cls(
            country_code=country_code,
            name=name,
            name_cn=name_cn,
            region_id=region_id,
            region_name_long=region_name_long,
            region_name_long_cn=region_name_long_cn,
        )

        region_list_region.additional_properties = d
        return region_list_region

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
