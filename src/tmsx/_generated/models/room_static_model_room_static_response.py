from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.common_error import CommonError
    from ..models.common_response_header import CommonResponseHeader
    from ..models.room_static_model_room_type_info import RoomStaticModelRoomTypeInfo


T = TypeVar("T", bound="RoomStaticModelRoomStaticResponse")


@_attrs_define
class RoomStaticModelRoomStaticResponse:
    """
    Attributes:
        error (CommonError | Unset):
        response_header (CommonResponseHeader | Unset):
        room_types (list[RoomStaticModelRoomTypeInfo] | Unset):
    """

    error: CommonError | Unset = UNSET
    response_header: CommonResponseHeader | Unset = UNSET
    room_types: list[RoomStaticModelRoomTypeInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        response_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_header, Unset):
            response_header = self.response_header.to_dict()

        room_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.room_types, Unset):
            room_types = []
            for room_types_item_data in self.room_types:
                room_types_item = room_types_item_data.to_dict()
                room_types.append(room_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["Error"] = error
        if response_header is not UNSET:
            field_dict["ResponseHeader"] = response_header
        if room_types is not UNSET:
            field_dict["RoomTypes"] = room_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_error import CommonError
        from ..models.common_response_header import CommonResponseHeader
        from ..models.room_static_model_room_type_info import (
            RoomStaticModelRoomTypeInfo,
        )

        d = dict(src_dict)
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

        _room_types = d.pop("RoomTypes", UNSET)
        room_types: list[RoomStaticModelRoomTypeInfo] | Unset = UNSET
        if _room_types is not UNSET:
            room_types = []
            for room_types_item_data in _room_types:
                room_types_item = RoomStaticModelRoomTypeInfo.from_dict(
                    room_types_item_data
                )

                room_types.append(room_types_item)

        room_static_model_room_static_response = cls(
            error=error,
            response_header=response_header,
            room_types=room_types,
        )

        room_static_model_room_static_response.additional_properties = d
        return room_static_model_room_static_response

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
