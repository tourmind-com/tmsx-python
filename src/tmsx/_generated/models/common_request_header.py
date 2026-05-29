from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CommonRequestHeader")


@_attrs_define
class CommonRequestHeader:
    """
    Attributes:
        agent_code (str | Unset): Unique code for the agent provided by TourMind. Example: tms_test.
        password (str | Unset): Password for the API request. Example: tms_test.
        request_time (str | Unset): Request timestamp in ISO 8601 format with millisecond precision, e.g.,
            "2006-01-02T15:04:05.123Z". Example: 2018-07-26T09:51:32.123Z.
        transaction_id (str | Unset): Identifier for tracing API requests, such as using a GUID. Example:
            6ba7b810-9dad-11d1-80b4-00c04fd430c8.
        user_name (str | Unset): Username for the API request. Example: tms_test.
    """

    agent_code: str | Unset = UNSET
    password: str | Unset = UNSET
    request_time: str | Unset = UNSET
    transaction_id: str | Unset = UNSET
    user_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_code = self.agent_code

        password = self.password

        request_time = self.request_time

        transaction_id = self.transaction_id

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_code is not UNSET:
            field_dict["AgentCode"] = agent_code
        if password is not UNSET:
            field_dict["Password"] = password
        if request_time is not UNSET:
            field_dict["RequestTime"] = request_time
        if transaction_id is not UNSET:
            field_dict["TransactionID"] = transaction_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_code = d.pop("AgentCode", UNSET)

        password = d.pop("Password", UNSET)

        request_time = d.pop("RequestTime", UNSET)

        transaction_id = d.pop("TransactionID", UNSET)

        user_name = d.pop("UserName", UNSET)

        common_request_header = cls(
            agent_code=agent_code,
            password=password,
            request_time=request_time,
            transaction_id=transaction_id,
            user_name=user_name,
        )

        common_request_header.additional_properties = d
        return common_request_header

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
