"""Contains all the data models used in inputs/outputs"""

from .cancel_order_cancel_order_request import CancelOrderCancelOrderRequest
from .cancel_order_cancel_order_response import CancelOrderCancelOrderResponse
from .cancel_order_cancel_result import CancelOrderCancelResult
from .common_error import CommonError
from .common_request_header import CommonRequestHeader
from .common_response_header import CommonResponseHeader
from .create_order_contact_info import CreateOrderContactInfo
from .create_order_create_order_request import CreateOrderCreateOrderRequest
from .create_order_create_order_response import CreateOrderCreateOrderResponse
from .create_order_order_info import CreateOrderOrderInfo
from .create_order_pax_name import CreateOrderPaxName
from .create_order_pax_room import CreateOrderPaxRoom
from .hotel_detail_cancel_policy_info import HotelDetailCancelPolicyInfo
from .hotel_detail_daily_price_info import HotelDetailDailyPriceInfo
from .hotel_detail_hotel import HotelDetailHotel
from .hotel_detail_hotel_detail_request import HotelDetailHotelDetailRequest
from .hotel_detail_hotel_detail_response import HotelDetailHotelDetailResponse
from .hotel_detail_meal_info import HotelDetailMealInfo
from .hotel_detail_pax_room_rq import HotelDetailPaxRoomRQ
from .hotel_detail_rate_info import HotelDetailRateInfo
from .hotel_detail_room_type import HotelDetailRoomType
from .hotelstatic_hotel_info import HotelstaticHotelInfo
from .hotelstatic_hotel_static_list_request import HotelstaticHotelStaticListRequest
from .hotelstatic_hotel_static_list_response import HotelstaticHotelStaticListResponse
from .hotelstatic_hotel_static_list_result import HotelstaticHotelStaticListResult
from .hotelstatic_image import HotelstaticImage
from .hotelstatic_image_links import HotelstaticImageLinks
from .hotelstatic_link import HotelstaticLink
from .hotelstatic_pagination import HotelstaticPagination
from .hotelstatic_pagination_rs import HotelstaticPaginationRS
from .region_list_region import RegionListRegion
from .region_list_region_list_request import RegionListRegionListRequest
from .region_list_region_list_response import RegionListRegionListResponse
from .region_list_region_list_result import RegionListRegionListResult
from .room_avail_cancel_policy_info import RoomAvailCancelPolicyInfo
from .room_avail_daily_price_info import RoomAvailDailyPriceInfo
from .room_avail_date_range import RoomAvailDateRange
from .room_avail_hotel import RoomAvailHotel
from .room_avail_low_price_period import RoomAvailLowPricePeriod
from .room_avail_low_price_range import RoomAvailLowPriceRange
from .room_avail_meal_info import RoomAvailMealInfo
from .room_avail_pax_room_rq import RoomAvailPaxRoomRQ
from .room_avail_rate_info import RoomAvailRateInfo
from .room_avail_room_avail_request import RoomAvailRoomAvailRequest
from .room_avail_room_avail_response import RoomAvailRoomAvailResponse
from .room_avail_room_type import RoomAvailRoomType
from .room_static_model_room_static_request import RoomStaticModelRoomStaticRequest
from .room_static_model_room_static_response import RoomStaticModelRoomStaticResponse
from .room_static_model_room_type_info import RoomStaticModelRoomTypeInfo
from .search_order_order_info import SearchOrderOrderInfo
from .search_order_order_list import SearchOrderOrderList
from .search_order_query_bookings_request import SearchOrderQueryBookingsRequest
from .search_order_query_bookings_response import SearchOrderQueryBookingsResponse
from .search_order_query_order_request import SearchOrderQueryOrderRequest
from .search_order_query_order_response import SearchOrderQueryOrderResponse

__all__ = (
    "CancelOrderCancelOrderRequest",
    "CancelOrderCancelOrderResponse",
    "CancelOrderCancelResult",
    "CommonError",
    "CommonRequestHeader",
    "CommonResponseHeader",
    "CreateOrderContactInfo",
    "CreateOrderCreateOrderRequest",
    "CreateOrderCreateOrderResponse",
    "CreateOrderOrderInfo",
    "CreateOrderPaxName",
    "CreateOrderPaxRoom",
    "HotelDetailCancelPolicyInfo",
    "HotelDetailDailyPriceInfo",
    "HotelDetailHotel",
    "HotelDetailHotelDetailRequest",
    "HotelDetailHotelDetailResponse",
    "HotelDetailMealInfo",
    "HotelDetailPaxRoomRQ",
    "HotelDetailRateInfo",
    "HotelDetailRoomType",
    "HotelstaticHotelInfo",
    "HotelstaticHotelStaticListRequest",
    "HotelstaticHotelStaticListResponse",
    "HotelstaticHotelStaticListResult",
    "HotelstaticImage",
    "HotelstaticImageLinks",
    "HotelstaticLink",
    "HotelstaticPagination",
    "HotelstaticPaginationRS",
    "RegionListRegion",
    "RegionListRegionListRequest",
    "RegionListRegionListResponse",
    "RegionListRegionListResult",
    "RoomAvailCancelPolicyInfo",
    "RoomAvailDailyPriceInfo",
    "RoomAvailDateRange",
    "RoomAvailHotel",
    "RoomAvailLowPricePeriod",
    "RoomAvailLowPriceRange",
    "RoomAvailMealInfo",
    "RoomAvailPaxRoomRQ",
    "RoomAvailRateInfo",
    "RoomAvailRoomAvailRequest",
    "RoomAvailRoomAvailResponse",
    "RoomAvailRoomType",
    "RoomStaticModelRoomStaticRequest",
    "RoomStaticModelRoomStaticResponse",
    "RoomStaticModelRoomTypeInfo",
    "SearchOrderOrderInfo",
    "SearchOrderOrderList",
    "SearchOrderQueryBookingsRequest",
    "SearchOrderQueryBookingsResponse",
    "SearchOrderQueryOrderRequest",
    "SearchOrderQueryOrderResponse",
)
