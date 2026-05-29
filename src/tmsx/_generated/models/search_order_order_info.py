from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.create_order_pax_room import CreateOrderPaxRoom


T = TypeVar("T", bound="SearchOrderOrderInfo")


@_attrs_define
class SearchOrderOrderInfo:
    """
    Attributes:
        agent_ref_id (str | Unset): Agent reference ID; Example: 213415.
        currency_code (str | Unset): Currency code. Example: CNY.
        hotel_confirmation_no (str | Unset): Hotel confirmation number. Example: 10470374.
        order_status (str | Unset): Order status.
            <br><table><tr><th>OrderStatus</th><th>Description</th></tr><tr><td>PENDING</td><td>Booking confirmation
            pending.</td></tr><tr><td>CONFIRMED</td><td>Booking confirmed.</td></tr><tr><td>CANCELLED</td><td>Booking
            cancelled.</td></tr><tr><td>FAILED</td><td>Booking confirmation failed.</td></tr></table> Example: CANCELLED.
        reservation_id (str | Unset): Tourmind order ID Example: 10470374.
        total_price (float | Unset): Total price of the booking. Example: 888.89.
        hotel_code (int | Unset): Tourmind hotel ID.
        room_count (int | Unset): Number of rooms.
        check_in (str | Unset): Check-in date. Format YYYY-MM-DD. Example: 2020-01-01.
        check_out (str | Unset): Check-out date. Format YYYY-MM-DD. Example: 2020-01-02.
        pax_rooms (list[CreateOrderPaxRoom] | Unset): Room occupancy details with guest names.
        contact (str | Unset): Contact person name.
        contact_phone (str | Unset): Contact phone number.
        booking_time (str | Unset): Booking creation time. Example: 2020-01-03 12:00:00.
    """

    agent_ref_id: str | Unset = UNSET
    currency_code: str | Unset = UNSET
    hotel_confirmation_no: str | Unset = UNSET
    order_status: str | Unset = UNSET
    reservation_id: str | Unset = UNSET
    total_price: float | Unset = UNSET
    hotel_code: int | Unset = UNSET
    room_count: int | Unset = UNSET
    check_in: str | Unset = UNSET
    check_out: str | Unset = UNSET
    pax_rooms: list[CreateOrderPaxRoom] | Unset = UNSET
    contact: str | Unset = UNSET
    contact_phone: str | Unset = UNSET
    booking_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_ref_id = self.agent_ref_id

        currency_code = self.currency_code

        hotel_confirmation_no = self.hotel_confirmation_no

        order_status = self.order_status

        reservation_id = self.reservation_id

        total_price = self.total_price

        hotel_code = self.hotel_code

        room_count = self.room_count

        check_in = self.check_in

        check_out = self.check_out

        pax_rooms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pax_rooms, Unset):
            pax_rooms = []
            for pax_rooms_item_data in self.pax_rooms:
                pax_rooms_item = pax_rooms_item_data.to_dict()
                pax_rooms.append(pax_rooms_item)

        contact = self.contact

        contact_phone = self.contact_phone

        booking_time = self.booking_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_ref_id is not UNSET:
            field_dict["AgentRefID"] = agent_ref_id
        if currency_code is not UNSET:
            field_dict["CurrencyCode"] = currency_code
        if hotel_confirmation_no is not UNSET:
            field_dict["HotelConfirmationNo"] = hotel_confirmation_no
        if order_status is not UNSET:
            field_dict["OrderStatus"] = order_status
        if reservation_id is not UNSET:
            field_dict["ReservationID"] = reservation_id
        if total_price is not UNSET:
            field_dict["TotalPrice"] = total_price
        if hotel_code is not UNSET:
            field_dict["HotelCode"] = hotel_code
        if room_count is not UNSET:
            field_dict["RoomCount"] = room_count
        if check_in is not UNSET:
            field_dict["CheckIn"] = check_in
        if check_out is not UNSET:
            field_dict["CheckOut"] = check_out
        if pax_rooms is not UNSET:
            field_dict["PaxRooms"] = pax_rooms
        if contact is not UNSET:
            field_dict["Contact"] = contact
        if contact_phone is not UNSET:
            field_dict["ContactPhone"] = contact_phone
        if booking_time is not UNSET:
            field_dict["BookingTime"] = booking_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_order_pax_room import CreateOrderPaxRoom

        d = dict(src_dict)
        agent_ref_id = d.pop("AgentRefID", UNSET)

        currency_code = d.pop("CurrencyCode", UNSET)

        hotel_confirmation_no = d.pop("HotelConfirmationNo", UNSET)

        order_status = d.pop("OrderStatus", UNSET)

        reservation_id = d.pop("ReservationID", UNSET)

        total_price = d.pop("TotalPrice", UNSET)

        hotel_code = d.pop("HotelCode", UNSET)

        room_count = d.pop("RoomCount", UNSET)

        check_in = d.pop("CheckIn", UNSET)

        check_out = d.pop("CheckOut", UNSET)

        _pax_rooms = d.pop("PaxRooms", UNSET)
        pax_rooms: list[CreateOrderPaxRoom] | Unset = UNSET
        if _pax_rooms is not UNSET:
            pax_rooms = []
            for pax_rooms_item_data in _pax_rooms:
                pax_rooms_item = CreateOrderPaxRoom.from_dict(pax_rooms_item_data)

                pax_rooms.append(pax_rooms_item)

        contact = d.pop("Contact", UNSET)

        contact_phone = d.pop("ContactPhone", UNSET)

        booking_time = d.pop("BookingTime", UNSET)

        search_order_order_info = cls(
            agent_ref_id=agent_ref_id,
            currency_code=currency_code,
            hotel_confirmation_no=hotel_confirmation_no,
            order_status=order_status,
            reservation_id=reservation_id,
            total_price=total_price,
            hotel_code=hotel_code,
            room_count=room_count,
            check_in=check_in,
            check_out=check_out,
            pax_rooms=pax_rooms,
            contact=contact,
            contact_phone=contact_phone,
            booking_time=booking_time,
        )

        search_order_order_info.additional_properties = d
        return search_order_order_info

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
