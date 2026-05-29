from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CommonError")


@_attrs_define
class CommonError:
    """
    Attributes:
        error_code (str | Unset): Error code.
            <br><table><tr><th>ErrorCode</th><th>Description</th></tr><tr><td>101</td><td>No payload in the
            request.</td></tr><tr><td>102</td><td>Invalid format of the request.</td></tr><tr><td>103</td><td>Request data
            validation failed.</td></tr><tr><td>104</td><td>Service error.</td></tr><tr><td>105</td><td>API user
            authentication error; invalid AgentCode, Username, or Password.</td></tr></table> Example: 101.
        error_message (str | Unset): Error message. Example: invaild param.
    """

    error_code: str | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_code = d.pop("ErrorCode", UNSET)

        error_message = d.pop("ErrorMessage", UNSET)

        common_error = cls(
            error_code=error_code,
            error_message=error_message,
        )

        common_error.additional_properties = d
        return common_error

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
