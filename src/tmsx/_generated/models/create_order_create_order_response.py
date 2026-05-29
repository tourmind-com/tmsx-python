from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.common_error import CommonError
    from ..models.common_response_header import CommonResponseHeader
    from ..models.create_order_order_info import CreateOrderOrderInfo


T = TypeVar("T", bound="CreateOrderCreateOrderResponse")


@_attrs_define
class CreateOrderCreateOrderResponse:
    """
    Attributes:
        error (CommonError | Unset):
        order_info (CreateOrderOrderInfo | Unset):
        reservation_id (str | Unset): Tourmind order ID Example: 10470379.
        response_header (CommonResponseHeader | Unset):
    """

    error: CommonError | Unset = UNSET
    order_info: CreateOrderOrderInfo | Unset = UNSET
    reservation_id: str | Unset = UNSET
    response_header: CommonResponseHeader | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        order_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.order_info, Unset):
            order_info = self.order_info.to_dict()

        reservation_id = self.reservation_id

        response_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_header, Unset):
            response_header = self.response_header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["Error"] = error
        if order_info is not UNSET:
            field_dict["OrderInfo"] = order_info
        if reservation_id is not UNSET:
            field_dict["ReservationID"] = reservation_id
        if response_header is not UNSET:
            field_dict["ResponseHeader"] = response_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_error import CommonError
        from ..models.common_response_header import CommonResponseHeader
        from ..models.create_order_order_info import CreateOrderOrderInfo

        d = dict(src_dict)
        _error = d.pop("Error", UNSET)
        error: CommonError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = CommonError.from_dict(_error)

        _order_info = d.pop("OrderInfo", UNSET)
        order_info: CreateOrderOrderInfo | Unset
        if isinstance(_order_info, Unset):
            order_info = UNSET
        else:
            order_info = CreateOrderOrderInfo.from_dict(_order_info)

        reservation_id = d.pop("ReservationID", UNSET)

        _response_header = d.pop("ResponseHeader", UNSET)
        response_header: CommonResponseHeader | Unset
        if isinstance(_response_header, Unset):
            response_header = UNSET
        else:
            response_header = CommonResponseHeader.from_dict(_response_header)

        create_order_create_order_response = cls(
            error=error,
            order_info=order_info,
            reservation_id=reservation_id,
            response_header=response_header,
        )

        create_order_create_order_response.additional_properties = d
        return create_order_create_order_response

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
