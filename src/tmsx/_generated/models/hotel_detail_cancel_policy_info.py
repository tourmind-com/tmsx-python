from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="HotelDetailCancelPolicyInfo")


@_attrs_define
class HotelDetailCancelPolicyInfo:
    """
    Attributes:
        amount (float | Unset): Cancellation charge amount.
        currency_code (str | Unset): Currency for the cancellation charge amount.
        end_date_time (str | Unset): Cancellation policy window end, format: “2006-01-02“.
        from_ (str | Unset): Specific start time, format: "2006-01-02 15:04:05"
        start_date_time (str | Unset): Cancellation policy window start, format: "2006-01-02".
        to (str | Unset): Specific end time, format: "2006-01-02 15:04:05"
    """

    amount: float | Unset = UNSET
    currency_code: str | Unset = UNSET
    end_date_time: str | Unset = UNSET
    from_: str | Unset = UNSET
    start_date_time: str | Unset = UNSET
    to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency_code = self.currency_code

        end_date_time = self.end_date_time

        from_ = self.from_

        start_date_time = self.start_date_time

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["Amount"] = amount
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code
        if end_date_time is not UNSET:
            field_dict["EndDateTime"] = end_date_time
        if from_ is not UNSET:
            field_dict["From"] = from_
        if start_date_time is not UNSET:
            field_dict["StartDateTime"] = start_date_time
        if to is not UNSET:
            field_dict["To"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("Amount", UNSET)

        currency_code = d.pop("CurrencyCode", UNSET)

        end_date_time = d.pop("EndDateTime", UNSET)

        from_ = d.pop("From", UNSET)

        start_date_time = d.pop("StartDateTime", UNSET)

        to = d.pop("To", UNSET)

        hotel_detail_cancel_policy_info = cls(
            amount=amount,
            currency_code=currency_code,
            end_date_time=end_date_time,
            from_=from_,
            start_date_time=start_date_time,
            to=to,
        )

        hotel_detail_cancel_policy_info.additional_properties = d
        return hotel_detail_cancel_policy_info

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
