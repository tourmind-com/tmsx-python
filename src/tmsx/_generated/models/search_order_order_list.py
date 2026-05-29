from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.search_order_order_info import SearchOrderOrderInfo


T = TypeVar("T", bound="SearchOrderOrderList")


@_attrs_define
class SearchOrderOrderList:
    """
    Attributes:
        order_list (list[SearchOrderOrderInfo] | Unset): List of orders.
        page (int | Unset): Current page number. Example: 1.
        page_size (int | Unset): Page size. Example: 50.
        total (int | Unset): Total number of orders matching the query. Example: 100.
    """

    order_list: list[SearchOrderOrderInfo] | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_list, Unset):
            order_list = []
            for order_list_item_data in self.order_list:
                order_list_item = order_list_item_data.to_dict()
                order_list.append(order_list_item)

        page = self.page

        page_size = self.page_size

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_list is not UNSET:
            field_dict["OrderList"] = order_list
        if page is not UNSET:
            field_dict["Page"] = page
        if page_size is not UNSET:
            field_dict["PageSize"] = page_size
        if total is not UNSET:
            field_dict["Total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_order_order_info import SearchOrderOrderInfo

        d = dict(src_dict)
        _order_list = d.pop("OrderList", UNSET)
        order_list: list[SearchOrderOrderInfo] | Unset = UNSET
        if _order_list is not UNSET:
            order_list = []
            for order_list_item_data in _order_list:
                order_list_item = SearchOrderOrderInfo.from_dict(order_list_item_data)

                order_list.append(order_list_item)

        page = d.pop("Page", UNSET)

        page_size = d.pop("PageSize", UNSET)

        total = d.pop("Total", UNSET)

        search_order_order_list = cls(
            order_list=order_list,
            page=page,
            page_size=page_size,
            total=total,
        )

        search_order_order_list.additional_properties = d
        return search_order_order_list

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
