from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.common_request_header import CommonRequestHeader
    from ..models.create_order_contact_info import CreateOrderContactInfo
    from ..models.create_order_pax_room import CreateOrderPaxRoom


T = TypeVar("T", bound="CreateOrderCreateOrderRequest")


@_attrs_define
class CreateOrderCreateOrderRequest:
    """
    Attributes:
        agent_ref_id (str | Unset): Unique agent reference ID to identify a booking; maximum length is 128 characters.
            Note! Reserving with the same AgentRefID will not create a new reservation; instead, the original reservation
            information will be returned. Example: 213415.
        check_in (str | Unset): Check-in date, format: “2006-01-02”. Example: 2018-08-15.
        check_out (str | Unset): Check-out date, format: “2006-01-02”. Example: 2018-08-18.
        contact_info (CreateOrderContactInfo | Unset):
        currency_code (str | Unset): Currency code. Example: CNY.
        hotel_code (int | Unset): TourMind Hotel ID; only one ID is required in this request. Example: 235113.
        pax_rooms (list[CreateOrderPaxRoom] | Unset): Request room occupancies. Note: Currently, only the same number of
            adults and children is supported for each room; for multiple rooms, you only need to fill in one object.
        rate_code (str | Unset): TourMind Rate ID. Example: 2132151.
        request_header (CommonRequestHeader | Unset):
        special_request (str | Unset): Special customer requests. Example: Non-smoking room.
        total_price (float | Unset): Total price for the booking returned from the CheckRoomRateResponse. Example:
            88.88.
    """

    agent_ref_id: str | Unset = UNSET
    check_in: str | Unset = UNSET
    check_out: str | Unset = UNSET
    contact_info: CreateOrderContactInfo | Unset = UNSET
    currency_code: str | Unset = UNSET
    hotel_code: int | Unset = UNSET
    pax_rooms: list[CreateOrderPaxRoom] | Unset = UNSET
    rate_code: str | Unset = UNSET
    request_header: CommonRequestHeader | Unset = UNSET
    special_request: str | Unset = UNSET
    total_price: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_ref_id = self.agent_ref_id

        check_in = self.check_in

        check_out = self.check_out

        contact_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_info, Unset):
            contact_info = self.contact_info.to_dict()

        currency_code = self.currency_code

        hotel_code = self.hotel_code

        pax_rooms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pax_rooms, Unset):
            pax_rooms = []
            for pax_rooms_item_data in self.pax_rooms:
                pax_rooms_item = pax_rooms_item_data.to_dict()
                pax_rooms.append(pax_rooms_item)

        rate_code = self.rate_code

        request_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_header, Unset):
            request_header = self.request_header.to_dict()

        special_request = self.special_request

        total_price = self.total_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_ref_id is not UNSET:
            field_dict["AgentRefID"] = agent_ref_id
        if check_in is not UNSET:
            field_dict["CheckIn"] = check_in
        if check_out is not UNSET:
            field_dict["CheckOut"] = check_out
        if contact_info is not UNSET:
            field_dict["ContactInfo"] = contact_info
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code
        if hotel_code is not UNSET:
            field_dict["HotelCode"] = hotel_code
        if pax_rooms is not UNSET:
            field_dict["PaxRooms"] = pax_rooms
        if rate_code is not UNSET:
            field_dict["RateCode"] = rate_code
        if request_header is not UNSET:
            field_dict["RequestHeader"] = request_header
        if special_request is not UNSET:
            field_dict["SpecialRequest"] = special_request
        if total_price is not UNSET:
            field_dict["TotalPrice"] = total_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_request_header import CommonRequestHeader
        from ..models.create_order_contact_info import CreateOrderContactInfo
        from ..models.create_order_pax_room import CreateOrderPaxRoom

        d = dict(src_dict)
        agent_ref_id = d.pop("AgentRefID", UNSET)

        check_in = d.pop("CheckIn", UNSET)

        check_out = d.pop("CheckOut", UNSET)

        _contact_info = d.pop("ContactInfo", UNSET)
        contact_info: CreateOrderContactInfo | Unset
        if isinstance(_contact_info, Unset):
            contact_info = UNSET
        else:
            contact_info = CreateOrderContactInfo.from_dict(_contact_info)

        currency_code = d.pop("CurrencyCode", UNSET)

        hotel_code = d.pop("HotelCode", UNSET)

        _pax_rooms = d.pop("PaxRooms", UNSET)
        pax_rooms: list[CreateOrderPaxRoom] | Unset = UNSET
        if _pax_rooms is not UNSET:
            pax_rooms = []
            for pax_rooms_item_data in _pax_rooms:
                pax_rooms_item = CreateOrderPaxRoom.from_dict(pax_rooms_item_data)

                pax_rooms.append(pax_rooms_item)

        rate_code = d.pop("RateCode", UNSET)

        _request_header = d.pop("RequestHeader", UNSET)
        request_header: CommonRequestHeader | Unset
        if isinstance(_request_header, Unset):
            request_header = UNSET
        else:
            request_header = CommonRequestHeader.from_dict(_request_header)

        special_request = d.pop("SpecialRequest", UNSET)

        total_price = d.pop("TotalPrice", UNSET)

        create_order_create_order_request = cls(
            agent_ref_id=agent_ref_id,
            check_in=check_in,
            check_out=check_out,
            contact_info=contact_info,
            currency_code=currency_code,
            hotel_code=hotel_code,
            pax_rooms=pax_rooms,
            rate_code=rate_code,
            request_header=request_header,
            special_request=special_request,
            total_price=total_price,
        )

        create_order_create_order_request.additional_properties = d
        return create_order_create_order_request

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
