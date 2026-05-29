from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.region_list_region import RegionListRegion


T = TypeVar("T", bound="RegionListRegionListResult")


@_attrs_define
class RegionListRegionListResult:
    """
    Attributes:
        regions (list[RegionListRegion] | Unset):
    """

    regions: list[RegionListRegion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regions is not UNSET:
            field_dict["Regions"] = regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_list_region import RegionListRegion

        d = dict(src_dict)
        _regions = d.pop("Regions", UNSET)
        regions: list[RegionListRegion] | Unset = UNSET
        if _regions is not UNSET:
            regions = []
            for regions_item_data in _regions:
                regions_item = RegionListRegion.from_dict(regions_item_data)

                regions.append(regions_item)

        region_list_region_list_result = cls(
            regions=regions,
        )

        region_list_region_list_result.additional_properties = d
        return region_list_region_list_result

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
