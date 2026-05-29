from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.common_request_header import CommonRequestHeader


T = TypeVar("T", bound="SearchOrderQueryOrderRequest")


@_attrs_define
class SearchOrderQueryOrderRequest:
    """
    Attributes:
        agent_ref_id (str | Unset): Agent reference ID provided in the CreateOrder request; maximum length is 128.
            Example: 21345555.
        request_header (CommonRequestHeader | Unset):
    """

    agent_ref_id: str | Unset = UNSET
    request_header: CommonRequestHeader | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_ref_id = self.agent_ref_id

        request_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_header, Unset):
            request_header = self.request_header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_ref_id is not UNSET:
            field_dict["AgentRefID"] = agent_ref_id
        if request_header is not UNSET:
            field_dict["RequestHeader"] = request_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_request_header import CommonRequestHeader

        d = dict(src_dict)
        agent_ref_id = d.pop("AgentRefID", UNSET)

        _request_header = d.pop("RequestHeader", UNSET)
        request_header: CommonRequestHeader | Unset
        if isinstance(_request_header, Unset):
            request_header = UNSET
        else:
            request_header = CommonRequestHeader.from_dict(_request_header)

        search_order_query_order_request = cls(
            agent_ref_id=agent_ref_id,
            request_header=request_header,
        )

        search_order_query_order_request.additional_properties = d
        return search_order_query_order_request

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
