from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.common_request_header import CommonRequestHeader
    from ..models.room_avail_pax_room_rq import RoomAvailPaxRoomRQ


T = TypeVar("T", bound="RoomAvailRoomAvailRequest")


@_attrs_define
class RoomAvailRoomAvailRequest:
    """
    Attributes:
        check_in (str | Unset): Check-in date, format: “2006-01-02”. Example: 2018-08-25.
        check_out (str | Unset): Check-out date, format: “2006-01-02”. Example: 2018-08-26.
        hotel_codes (list[int] | Unset): TourMind Hotel ID; only one ID is required in this request.
        nationality (str | Unset): Nationality. Example: CN.
        pax_rooms (list[RoomAvailPaxRoomRQ] | Unset): Request room occupancies. Note: Currently, only the same number of
            adults and children is supported for each room.
        rate_code (str | Unset): TourMind Rate ID. Example: 13800206.
        request_header (CommonRequestHeader | Unset):
    """

    check_in: str | Unset = UNSET
    check_out: str | Unset = UNSET
    hotel_codes: list[int] | Unset = UNSET
    nationality: str | Unset = UNSET
    pax_rooms: list[RoomAvailPaxRoomRQ] | Unset = UNSET
    rate_code: str | Unset = UNSET
    request_header: CommonRequestHeader | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_in = self.check_in

        check_out = self.check_out

        hotel_codes: list[int] | Unset = UNSET
        if not isinstance(self.hotel_codes, Unset):
            hotel_codes = self.hotel_codes

        nationality = self.nationality

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_in is not UNSET:
            field_dict["CheckIn"] = check_in
        if check_out is not UNSET:
            field_dict["CheckOut"] = check_out
        if hotel_codes is not UNSET:
            field_dict["HotelCodes"] = hotel_codes
        if nationality is not UNSET:
            field_dict["Nationality"] = nationality
        if pax_rooms is not UNSET:
            field_dict["PaxRooms"] = pax_rooms
        if rate_code is not UNSET:
            field_dict["RateCode"] = rate_code
        if request_header is not UNSET:
            field_dict["RequestHeader"] = request_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_request_header import CommonRequestHeader
        from ..models.room_avail_pax_room_rq import RoomAvailPaxRoomRQ

        d = dict(src_dict)
        check_in = d.pop("CheckIn", UNSET)

        check_out = d.pop("CheckOut", UNSET)

        hotel_codes = cast(list[int], d.pop("HotelCodes", UNSET))

        nationality = d.pop("Nationality", UNSET)

        _pax_rooms = d.pop("PaxRooms", UNSET)
        pax_rooms: list[RoomAvailPaxRoomRQ] | Unset = UNSET
        if _pax_rooms is not UNSET:
            pax_rooms = []
            for pax_rooms_item_data in _pax_rooms:
                pax_rooms_item = RoomAvailPaxRoomRQ.from_dict(pax_rooms_item_data)

                pax_rooms.append(pax_rooms_item)

        rate_code = d.pop("RateCode", UNSET)

        _request_header = d.pop("RequestHeader", UNSET)
        request_header: CommonRequestHeader | Unset
        if isinstance(_request_header, Unset):
            request_header = UNSET
        else:
            request_header = CommonRequestHeader.from_dict(_request_header)

        room_avail_room_avail_request = cls(
            check_in=check_in,
            check_out=check_out,
            hotel_codes=hotel_codes,
            nationality=nationality,
            pax_rooms=pax_rooms,
            rate_code=rate_code,
            request_header=request_header,
        )

        room_avail_room_avail_request.additional_properties = d
        return room_avail_room_avail_request

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
