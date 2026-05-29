from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateOrderPaxName")


@_attrs_define
class CreateOrderPaxName:
    """
    Attributes:
        first_name (str | Unset):  Example: Tom.
        last_name (str | Unset):  Example: Lee.
        type_ (str | Unset): ADU represents Adult, CHI represents Child. Example: ADU.
    """

    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        type_ = d.pop("Type", UNSET)

        create_order_pax_name = cls(
            first_name=first_name,
            last_name=last_name,
            type_=type_,
        )

        create_order_pax_name.additional_properties = d
        return create_order_pax_name

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
