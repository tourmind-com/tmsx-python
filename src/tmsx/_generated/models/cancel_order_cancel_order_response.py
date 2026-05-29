from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.cancel_order_cancel_result import CancelOrderCancelResult
    from ..models.common_error import CommonError
    from ..models.common_response_header import CommonResponseHeader


T = TypeVar("T", bound="CancelOrderCancelOrderResponse")


@_attrs_define
class CancelOrderCancelOrderResponse:
    """
    Attributes:
        cancel_result (CancelOrderCancelResult | Unset):
        error (CommonError | Unset):
        response_header (CommonResponseHeader | Unset):
    """

    cancel_result: CancelOrderCancelResult | Unset = UNSET
    error: CommonError | Unset = UNSET
    response_header: CommonResponseHeader | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancel_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cancel_result, Unset):
            cancel_result = self.cancel_result.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        response_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_header, Unset):
            response_header = self.response_header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancel_result is not UNSET:
            field_dict["CancelResult"] = cancel_result
        if error is not UNSET:
            field_dict["Error"] = error
        if response_header is not UNSET:
            field_dict["ResponseHeader"] = response_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cancel_order_cancel_result import CancelOrderCancelResult
        from ..models.common_error import CommonError
        from ..models.common_response_header import CommonResponseHeader

        d = dict(src_dict)
        _cancel_result = d.pop("CancelResult", UNSET)
        cancel_result: CancelOrderCancelResult | Unset
        if isinstance(_cancel_result, Unset):
            cancel_result = UNSET
        else:
            cancel_result = CancelOrderCancelResult.from_dict(_cancel_result)

        _error = d.pop("Error", UNSET)
        error: CommonError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = CommonError.from_dict(_error)

        _response_header = d.pop("ResponseHeader", UNSET)
        response_header: CommonResponseHeader | Unset
        if isinstance(_response_header, Unset):
            response_header = UNSET
        else:
            response_header = CommonResponseHeader.from_dict(_response_header)

        cancel_order_cancel_order_response = cls(
            cancel_result=cancel_result,
            error=error,
            response_header=response_header,
        )

        cancel_order_cancel_order_response.additional_properties = d
        return cancel_order_cancel_order_response

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
