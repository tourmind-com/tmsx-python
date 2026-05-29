from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CommonResponseHeader")


@_attrs_define
class CommonResponseHeader:
    """
    Attributes:
        response_time (str | Unset): Response timestamp, format: “2006-01-02 15:04:05”. Example: 2018-07-26 09:51:32.
        transaction_id (str | Unset): This value must match the TransactionID in the request.. Example:
            6ba7b810-9dad-11d1-80b4-00c04fd430c8.
    """

    response_time: str | Unset = UNSET
    transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response_time = self.response_time

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response_time is not UNSET:
            field_dict["ResponseTime"] = response_time
        if transaction_id is not UNSET:
            field_dict["TransactionID"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response_time = d.pop("ResponseTime", UNSET)

        transaction_id = d.pop("TransactionID", UNSET)

        common_response_header = cls(
            response_time=response_time,
            transaction_id=transaction_id,
        )

        common_response_header.additional_properties = d
        return common_response_header

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
