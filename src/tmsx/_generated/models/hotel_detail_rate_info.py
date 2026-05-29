from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.hotel_detail_cancel_policy_info import HotelDetailCancelPolicyInfo
    from ..models.hotel_detail_daily_price_info import HotelDetailDailyPriceInfo
    from ..models.hotel_detail_meal_info import HotelDetailMealInfo


T = TypeVar("T", bound="HotelDetailRateInfo")


@_attrs_define
class HotelDetailRateInfo:
    """
    Attributes:
        allotment (int | Unset): Available room inventory count. Example: 2.
        cancel_policy_infos (list[HotelDetailCancelPolicyInfo] | Unset): Cancellation policy information.
        currency_code (str | Unset): Currency code. Example: CNY.
        daily_price_info (list[HotelDetailDailyPriceInfo] | Unset): Daily pricing information for the hotel.
        invoice_info (int | Unset): Invoice information: 1: Hotel invoice, 2: TourMind invoice
        meal_info (HotelDetailMealInfo | Unset):
        name (str | Unset): Sub-room name, i.e. the original room name from the supplier/hotel system. More accurate
            than the aggregated name in RoomType, but results in more static room entries. In rare cases, sub-rooms may be
            incorrectly mapped to their parent room type. Example: SUITE THREE BEDROOMS.
        name_cn (str | Unset): Sub-room name in Chinese, i.e. the original room name from the supplier/hotel system.
            More accurate than the aggregated name in RoomType, but results in more static room entries. In rare cases, sub-
            rooms may be incorrectly mapped to their parent room type.
        rate_code (str | Unset): Rate identifier for a sellable product; this code is unique across all TourMind hotels.
            Example: 13800206.
        refundable (bool | Unset):
        total_price (float | Unset): Total price; this is the total amount charged. Example: 688.88.
        bed_type_desc (str | Unset): Bed type description.
        bed_type_desc_cn (str | Unset): Bed type description in Chinese.
    """

    allotment: int | Unset = UNSET
    cancel_policy_infos: list[HotelDetailCancelPolicyInfo] | Unset = UNSET
    currency_code: str | Unset = UNSET
    daily_price_info: list[HotelDetailDailyPriceInfo] | Unset = UNSET
    invoice_info: int | Unset = UNSET
    meal_info: HotelDetailMealInfo | Unset = UNSET
    name: str | Unset = UNSET
    name_cn: str | Unset = UNSET
    rate_code: str | Unset = UNSET
    refundable: bool | Unset = UNSET
    total_price: float | Unset = UNSET
    bed_type_desc: str | Unset = UNSET
    bed_type_desc_cn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allotment = self.allotment

        cancel_policy_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cancel_policy_infos, Unset):
            cancel_policy_infos = []
            for cancel_policy_infos_item_data in self.cancel_policy_infos:
                cancel_policy_infos_item = cancel_policy_infos_item_data.to_dict()
                cancel_policy_infos.append(cancel_policy_infos_item)

        currency_code = self.currency_code

        daily_price_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.daily_price_info, Unset):
            daily_price_info = []
            for daily_price_info_item_data in self.daily_price_info:
                daily_price_info_item = daily_price_info_item_data.to_dict()
                daily_price_info.append(daily_price_info_item)

        invoice_info = self.invoice_info

        meal_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meal_info, Unset):
            meal_info = self.meal_info.to_dict()

        name = self.name

        name_cn = self.name_cn

        rate_code = self.rate_code

        refundable = self.refundable

        total_price = self.total_price

        bed_type_desc = self.bed_type_desc

        bed_type_desc_cn = self.bed_type_desc_cn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allotment is not UNSET:
            field_dict["Allotment"] = allotment
        if cancel_policy_infos is not UNSET:
            field_dict["CancelPolicyInfos"] = cancel_policy_infos
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code
        if daily_price_info is not UNSET:
            field_dict["DailyPriceInfo"] = daily_price_info
        if invoice_info is not UNSET:
            field_dict["InvoiceInfo"] = invoice_info
        if meal_info is not UNSET:
            field_dict["MealInfo"] = meal_info
        if name is not UNSET:
            field_dict["Name"] = name
        if name_cn is not UNSET:
            field_dict["NameCN"] = name_cn
        if rate_code is not UNSET:
            field_dict["RateCode"] = rate_code
        if refundable is not UNSET:
            field_dict["Refundable"] = refundable
        if total_price is not UNSET:
            field_dict["TotalPrice"] = total_price
        if bed_type_desc is not UNSET:
            field_dict["bedTypeDesc"] = bed_type_desc
        if bed_type_desc_cn is not UNSET:
            field_dict["bedTypeDescCN"] = bed_type_desc_cn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotel_detail_cancel_policy_info import HotelDetailCancelPolicyInfo
        from ..models.hotel_detail_daily_price_info import HotelDetailDailyPriceInfo
        from ..models.hotel_detail_meal_info import HotelDetailMealInfo

        d = dict(src_dict)
        allotment = d.pop("Allotment", UNSET)

        _cancel_policy_infos = d.pop("CancelPolicyInfos", UNSET)
        cancel_policy_infos: list[HotelDetailCancelPolicyInfo] | Unset = UNSET
        if _cancel_policy_infos is not UNSET:
            cancel_policy_infos = []
            for cancel_policy_infos_item_data in _cancel_policy_infos:
                cancel_policy_infos_item = HotelDetailCancelPolicyInfo.from_dict(
                    cancel_policy_infos_item_data
                )

                cancel_policy_infos.append(cancel_policy_infos_item)

        currency_code = d.pop("CurrencyCode", UNSET)

        _daily_price_info = d.pop("DailyPriceInfo", UNSET)
        daily_price_info: list[HotelDetailDailyPriceInfo] | Unset = UNSET
        if _daily_price_info is not UNSET:
            daily_price_info = []
            for daily_price_info_item_data in _daily_price_info:
                daily_price_info_item = HotelDetailDailyPriceInfo.from_dict(
                    daily_price_info_item_data
                )

                daily_price_info.append(daily_price_info_item)

        invoice_info = d.pop("InvoiceInfo", UNSET)

        _meal_info = d.pop("MealInfo", UNSET)
        meal_info: HotelDetailMealInfo | Unset
        if isinstance(_meal_info, Unset):
            meal_info = UNSET
        else:
            meal_info = HotelDetailMealInfo.from_dict(_meal_info)

        name = d.pop("Name", UNSET)

        name_cn = d.pop("NameCN", UNSET)

        rate_code = d.pop("RateCode", UNSET)

        refundable = d.pop("Refundable", UNSET)

        total_price = d.pop("TotalPrice", UNSET)

        bed_type_desc = d.pop("bedTypeDesc", UNSET)

        bed_type_desc_cn = d.pop("bedTypeDescCN", UNSET)

        hotel_detail_rate_info = cls(
            allotment=allotment,
            cancel_policy_infos=cancel_policy_infos,
            currency_code=currency_code,
            daily_price_info=daily_price_info,
            invoice_info=invoice_info,
            meal_info=meal_info,
            name=name,
            name_cn=name_cn,
            rate_code=rate_code,
            refundable=refundable,
            total_price=total_price,
            bed_type_desc=bed_type_desc,
            bed_type_desc_cn=bed_type_desc_cn,
        )

        hotel_detail_rate_info.additional_properties = d
        return hotel_detail_rate_info

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
