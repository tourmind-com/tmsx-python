from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.hotelstatic_image_links import HotelstaticImageLinks


T = TypeVar("T", bound="HotelstaticImage")


@_attrs_define
class HotelstaticImage:
    """
    Attributes:
        caption (str | Unset):
        category (int | Unset):
        hero_image (bool | Unset):
        links (HotelstaticImageLinks | Unset):
    """

    caption: str | Unset = UNSET
    category: int | Unset = UNSET
    hero_image: bool | Unset = UNSET
    links: HotelstaticImageLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caption = self.caption

        category = self.category

        hero_image = self.hero_image

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caption is not UNSET:
            field_dict["caption"] = caption
        if category is not UNSET:
            field_dict["category"] = category
        if hero_image is not UNSET:
            field_dict["hero_image"] = hero_image
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hotelstatic_image_links import HotelstaticImageLinks

        d = dict(src_dict)
        caption = d.pop("caption", UNSET)

        category = d.pop("category", UNSET)

        hero_image = d.pop("hero_image", UNSET)

        _links = d.pop("links", UNSET)
        links: HotelstaticImageLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = HotelstaticImageLinks.from_dict(_links)

        hotelstatic_image = cls(
            caption=caption,
            category=category,
            hero_image=hero_image,
            links=links,
        )

        hotelstatic_image.additional_properties = d
        return hotelstatic_image

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
