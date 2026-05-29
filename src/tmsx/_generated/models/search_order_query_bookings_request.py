from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.common_request_header import CommonRequestHeader


T = TypeVar("T", bound="SearchOrderQueryBookingsRequest")


@_attrs_define
class SearchOrderQueryBookingsRequest:
    """
    Attributes:
        date_type (str): Date type for date range query. Possible values: CheckIn (check-in date), CheckOut (check-out
            date), Booking (booking date). Example: CheckIn.
        from_ (str): Start date for the query range. Format YYYY-MM-DD. The date span (To minus From) must be <= 31
            days. Example: 2024-01-01.
        to (str): End date for the query range. Format YYYY-MM-DD. The date span (To minus From) must be <= 31 days.
            Example: 2024-01-31.
        page (int): Page number for pagination. Must be >= 1. Example: 1.
        page_size (int): Number of results per page. Must be between 1 and 500. Example: 50.
        request_header (CommonRequestHeader):
    """

    date_type: str
    from_: str
    to: str
    page: int
    page_size: int
    request_header: CommonRequestHeader
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_type = self.date_type

        from_ = self.from_

        to = self.to

        page = self.page

        page_size = self.page_size

        request_header = self.request_header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DateType": date_type,
                "From": from_,
                "To": to,
                "Page": page,
                "PageSize": page_size,
                "RequestHeader": request_header,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_request_header import CommonRequestHeader

        d = dict(src_dict)
        date_type = d.pop("DateType")

        from_ = d.pop("From")

        to = d.pop("To")

        page = d.pop("Page")

        page_size = d.pop("PageSize")

        request_header = CommonRequestHeader.from_dict(d.pop("RequestHeader"))

        search_order_query_bookings_request = cls(
            date_type=date_type,
            from_=from_,
            to=to,
            page=page,
            page_size=page_size,
            request_header=request_header,
        )

        search_order_query_bookings_request.additional_properties = d
        return search_order_query_bookings_request

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
