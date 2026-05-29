from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateOrderContactInfo")


@_attrs_define
class CreateOrderContactInfo:
    """
    Attributes:
        email (str | Unset): Email of the booking contact. Example: xxx@google.com.
        first_name (str | Unset): First Name of the booking contact. Example: Tom.
        last_name (str | Unset): Last Name of the booking contact. Example: Lee.
        phone_no (str | Unset): Phone number of the booking contact. Example: 1521777777.
    """

    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    phone_no: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        phone_no = self.phone_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["Email"] = email
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if last_name is not UNSET:
            field_dict["LastName"] = last_name
        if phone_no is not UNSET:
            field_dict["PhoneNo"] = phone_no

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("Email", UNSET)

        first_name = d.pop("FirstName", UNSET)

        last_name = d.pop("LastName", UNSET)

        phone_no = d.pop("PhoneNo", UNSET)

        create_order_contact_info = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
        )

        create_order_contact_info.additional_properties = d
        return create_order_contact_info

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
