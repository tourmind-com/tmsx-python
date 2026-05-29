from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="RoomAvailMealInfo")


@_attrs_define
class RoomAvailMealInfo:
    """
    Attributes:
        meal_count (int | Unset): Number of free meals offered. Example: 2.
        meal_type (str | Unset): Meal type <br><table><tr><th>MealType</th><th>Description</th></tr><tr><td>1</td><td>No
            Breakfast</td></tr><tr><td>2</td><td>Breakfast</td></tr></table> Example: breakfast.
    """

    meal_count: int | Unset = UNSET
    meal_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meal_count = self.meal_count

        meal_type = self.meal_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meal_count is not UNSET:
            field_dict["MealCount"] = meal_count
        if meal_type is not UNSET:
            field_dict["MealType"] = meal_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        meal_count = d.pop("MealCount", UNSET)

        meal_type = d.pop("MealType", UNSET)

        room_avail_meal_info = cls(
            meal_count=meal_count,
            meal_type=meal_type,
        )

        room_avail_meal_info.additional_properties = d
        return room_avail_meal_info

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
