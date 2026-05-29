from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.hotelstatic_image import HotelstaticImage


T = TypeVar("T", bound="HotelstaticHotelInfo")


@_attrs_define
class HotelstaticHotelInfo:
    """
    Attributes:
        address (str | Unset): Hotel address. Example: 3007 Santa Monica Blvd, 90404.
        address_cn (str | Unset): Hotel address in Chinese.
        city_code (str | Unset): City code.,Matched region ID. Example: 14209.
        city_name (str | Unset): City name. Example: ShangHai.
        city_name_cn (str | Unset): City name in Chinese. Example: Shanghai.
        country_code (str | Unset): Country code.，ISO 3166-1 alpha-2, e.g., China: CN. Example: CN.
        hotel_id (str | Unset): TourMind hotel ID. Example: 739315.
        images (list[HotelstaticImage] | Unset):
        latitude (str | Unset): Latitude. Example: 34.03644.
        longitude (str | Unset): Longitude. Example: -118.47048.
        name (str | Unset): Hotel name. Example: Days Inn Santa Monica/Los Angeles.
        name_cn (str | Unset): Hotel name in Chinese.
        phone (str | Unset): Hotel phone number. Example: 1523333333.
        star_rating (str | Unset): Hotel star rating. Example: 5.
    """

    address: str | Unset = UNSET
    address_cn: str | Unset = UNSET
    city_code: str | Unset = UNSET
    city_name: str | Unset = UNSET
    city_name_cn: str | Unset = UNSET
    country_code: str | Unset = UNSET
    hotel_id: str | Unset = UNSET
    images: list[HotelstaticImage] | Unset = UNSET
    latitude: str | Unset = UNSET
    longitude: str | Unset = UNSET
    name: str | Unset = UNSET
    name_cn: str | Unset = UNSET
    phone: str | Unset = UNSET
    star_rating: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        address_cn = self.address_cn

        city_code = self.city_code

        city_name = self.city_name

        city_name_cn = self.city_name_cn

        country_code = self.country_code

        hotel_id = self.hotel_id

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        latitude = self.latitude

        longitude = self.longitude

        name = self.name

        name_cn = self.name_cn

        phone = self.phone

        star_rating = self.star_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if address_cn is not UNSET:
            field_dict["Address_CN"] = address_cn
        if city_code is not UNSET:
            field_dict["CityCode"] = city_code
        if city_name is not UNSET:
            field_dict["CityName"] = city_name
        if city_name_cn is not UNSET:
            field_dict["CityNameCN"] = city_name_cn
        if country_code is not UNSET:
            field_dict["CountryCode"] = country_code
        if hotel_id is not UNSET:
            field_dict["HotelId"] = hotel_id
        if images is not UNSET:
            field_dict["Images"] = images
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if name is not UNSET:
            field_dict["Name"] = name
        if name_cn is not UNSET:
            field_dict["Name_CN"] = name_cn
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if star_rating is not UNSET:
            field_dict["StarRating"] = star_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotelstatic_image import HotelstaticImage

        d = dict(src_dict)
        address = d.pop("Address", UNSET)

        address_cn = d.pop("Address_CN", UNSET)

        city_code = d.pop("CityCode", UNSET)

        city_name = d.pop("CityName", UNSET)

        city_name_cn = d.pop("CityNameCN", UNSET)

        country_code = d.pop("CountryCode", UNSET)

        hotel_id = d.pop("HotelId", UNSET)

        _images = d.pop("Images", UNSET)
        images: list[HotelstaticImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = HotelstaticImage.from_dict(images_item_data)

                images.append(images_item)

        latitude = d.pop("Latitude", UNSET)

        longitude = d.pop("Longitude", UNSET)

        name = d.pop("Name", UNSET)

        name_cn = d.pop("Name_CN", UNSET)

        phone = d.pop("Phone", UNSET)

        star_rating = d.pop("StarRating", UNSET)

        hotelstatic_hotel_info = cls(
            address=address,
            address_cn=address_cn,
            city_code=city_code,
            city_name=city_name,
            city_name_cn=city_name_cn,
            country_code=country_code,
            hotel_id=hotel_id,
            images=images,
            latitude=latitude,
            longitude=longitude,
            name=name,
            name_cn=name_cn,
            phone=phone,
            star_rating=star_rating,
        )

        hotelstatic_hotel_info.additional_properties = d
        return hotelstatic_hotel_info

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
