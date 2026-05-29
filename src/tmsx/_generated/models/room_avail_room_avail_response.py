from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.common_error import CommonError
    from ..models.common_response_header import CommonResponseHeader
    from ..models.room_avail_hotel import RoomAvailHotel


T = TypeVar("T", bound="RoomAvailRoomAvailResponse")


@_attrs_define
class RoomAvailRoomAvailResponse:
    """
    Attributes:
        error (CommonError | Unset):
        hotels (list[RoomAvailHotel] | Unset): Hotel information.
        response_header (CommonResponseHeader | Unset):
    """

    error: CommonError | Unset = UNSET
    hotels: list[RoomAvailHotel] | Unset = UNSET
    response_header: CommonResponseHeader | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        hotels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hotels, Unset):
            hotels = []
            for hotels_item_data in self.hotels:
                hotels_item = hotels_item_data.to_dict()
                hotels.append(hotels_item)

        response_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_header, Unset):
            response_header = self.response_header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["Error"] = error
        if hotels is not UNSET:
            field_dict["Hotels"] = hotels
        if response_header is not UNSET:
            field_dict["ResponseHeader"] = response_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_error import CommonError
        from ..models.common_response_header import CommonResponseHeader
        from ..models.room_avail_hotel import RoomAvailHotel

        d = dict(src_dict)
        _error = d.pop("Error", UNSET)
        error: CommonError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = CommonError.from_dict(_error)

        _hotels = d.pop("Hotels", UNSET)
        hotels: list[RoomAvailHotel] | Unset = UNSET
        if _hotels is not UNSET:
            hotels = []
            for hotels_item_data in _hotels:
                hotels_item = RoomAvailHotel.from_dict(hotels_item_data)

                hotels.append(hotels_item)

        _response_header = d.pop("ResponseHeader", UNSET)
        response_header: CommonResponseHeader | Unset
        if isinstance(_response_header, Unset):
            response_header = UNSET
        else:
            response_header = CommonResponseHeader.from_dict(_response_header)

        room_avail_room_avail_response = cls(
            error=error,
            hotels=hotels,
            response_header=response_header,
        )

        room_avail_room_avail_response.additional_properties = d
        return room_avail_room_avail_response

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
