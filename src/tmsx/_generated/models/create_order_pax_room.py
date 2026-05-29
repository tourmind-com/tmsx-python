from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.create_order_pax_name import CreateOrderPaxName


T = TypeVar("T", bound="CreateOrderPaxRoom")


@_attrs_define
class CreateOrderPaxRoom:
    """
    Attributes:
        adults (int | Unset):  Example: 2.
        children (int | Unset):
        children_ages (list[int] | Unset): Children's ages; the count of the array must equal the number of children.
        pax_names (list[CreateOrderPaxName] | Unset):
        room_count (int | Unset):  Example: 1.
    """

    adults: int | Unset = UNSET
    children: int | Unset = UNSET
    children_ages: list[int] | Unset = UNSET
    pax_names: list[CreateOrderPaxName] | Unset = UNSET
    room_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adults = self.adults

        children = self.children

        children_ages: list[int] | Unset = UNSET
        if not isinstance(self.children_ages, Unset):
            children_ages = self.children_ages

        pax_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pax_names, Unset):
            pax_names = []
            for pax_names_item_data in self.pax_names:
                pax_names_item = pax_names_item_data.to_dict()
                pax_names.append(pax_names_item)

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
        if pax_names is not UNSET:
            field_dict["PaxNames"] = pax_names
        if room_count is not UNSET:
            field_dict["RoomCount"] = room_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_order_pax_name import CreateOrderPaxName

        d = dict(src_dict)
        adults = d.pop("Adults", UNSET)

        children = d.pop("Children", UNSET)

        children_ages = cast(list[int], d.pop("ChildrenAges", UNSET))

        _pax_names = d.pop("PaxNames", UNSET)
        pax_names: list[CreateOrderPaxName] | Unset = UNSET
        if _pax_names is not UNSET:
            pax_names = []
            for pax_names_item_data in _pax_names:
                pax_names_item = CreateOrderPaxName.from_dict(pax_names_item_data)

                pax_names.append(pax_names_item)

        room_count = d.pop("RoomCount", UNSET)

        create_order_pax_room = cls(
            adults=adults,
            children=children,
            children_ages=children_ages,
            pax_names=pax_names,
            room_count=room_count,
        )

        create_order_pax_room.additional_properties = d
        return create_order_pax_room

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
