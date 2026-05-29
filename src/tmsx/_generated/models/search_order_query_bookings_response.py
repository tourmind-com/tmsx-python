from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.common_error import CommonError
    from ..models.common_response_header import CommonResponseHeader
    from ..models.search_order_order_list import SearchOrderOrderList


T = TypeVar("T", bound="SearchOrderQueryBookingsResponse")


@_attrs_define
class SearchOrderQueryBookingsResponse:
    """
    Attributes:
        error (CommonError | Unset):
        order_list (SearchOrderOrderList | Unset):
        response_header (CommonResponseHeader | Unset):
    """

    error: CommonError | Unset = UNSET
    order_list: SearchOrderOrderList | Unset = UNSET
    response_header: CommonResponseHeader | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        order_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.order_list, Unset):
            order_list = self.order_list.to_dict()

        response_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_header, Unset):
            response_header = self.response_header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["Error"] = error
        if order_list is not UNSET:
            field_dict["OrderList"] = order_list
        if response_header is not UNSET:
            field_dict["ResponseHeader"] = response_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_error import CommonError
        from ..models.common_response_header import CommonResponseHeader
        from ..models.search_order_order_list import SearchOrderOrderList

        d = dict(src_dict)
        _error = d.pop("Error", UNSET)
        error: CommonError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = CommonError.from_dict(_error)

        _order_list = d.pop("OrderList", UNSET)
        order_list: SearchOrderOrderList | Unset
        if isinstance(_order_list, Unset):
            order_list = UNSET
        else:
            order_list = SearchOrderOrderList.from_dict(_order_list)

        _response_header = d.pop("ResponseHeader", UNSET)
        response_header: CommonResponseHeader | Unset
        if isinstance(_response_header, Unset):
            response_header = UNSET
        else:
            response_header = CommonResponseHeader.from_dict(_response_header)

        search_order_query_bookings_response = cls(
            error=error,
            order_list=order_list,
            response_header=response_header,
        )

        search_order_query_bookings_response.additional_properties = d
        return search_order_query_bookings_response

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
