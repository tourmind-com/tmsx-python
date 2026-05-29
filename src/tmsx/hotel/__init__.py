"""TMSX hotel-API surface.

Usage:
    from tmsx.hotel import Client

    client = Client(
        agent_code="tms_test",
        username="tms_test",
        password="tms_test",
        base_url="http://developers.tourmind.cn",
    )
    regions = client.list_regions(country_code="CN")
    print(regions.regions[0].name)

See `tmsx.hotel.AsyncClient` for the async variant.
"""

from tmsx.hotel._client import AsyncClient, Client

__all__ = ["AsyncClient", "Client"]
