# tmsx · Python SDK for the Tourmind TMS hotel API

```bash
pip install tmsx        # once published — current source: github.com/tourmind-com/tmsx-python
```

Source repo (post-extract from `tms-doc`): [`tourmind-com/tmsx-python`](https://github.com/tourmind-com/tmsx-python).
Spec + test cases live in [`tourmind-com/tmsx-platform`](https://github.com/tourmind-com/tmsx-platform) per ADR-002.

## Quick start

```python
from tmsx.hotel import Client

with Client(
    agent_code="tms_test",
    username="tms_test",
    password="tms_test",
    base_url="http://developers.tourmind.cn",
) as client:
    regions = client.list_regions(country_code="CN")
    for region in regions.region_list_result.regions:
        print(region.region_id, region.name)
```

The SDK injects the TMSX auth scheme (`X-Agent-Code` / `X-Username` headers + the
`RequestHeader` body envelope with `Password`, `RequestTime`, `TransactionID`) on
every request — see `sdk/AUTH.md`. Callers never touch `RequestHeader`.

## Async

```python
from tmsx.hotel import AsyncClient

async with AsyncClient(agent_code=..., username=..., password=...) as client:
    regions = await client.list_regions(country_code="CN")
```

## Errors

The TMSX API signals failures via `Error.ErrorCode` in an HTTP-200 body. The SDK
translates that into typed exceptions:

| Error code | Exception |
|---|---|
| 105 | `tmsx.TMSXAuthError` |
| 101 / 102 / 103 | `tmsx.TMSXValidationError` |
| Other | `tmsx.TMSXError` |
| Transport / parse | `tmsx.TMSXClientError` |

All carry `code`, `message`, and (where available) `transaction_id` attributes for
log correlation and support tickets.

## Layout

```
sdk/python/
├── pyproject.toml
├── src/tmsx/
│   ├── __init__.py        # public exceptions + version
│   ├── exceptions.py      # TMSXError hierarchy
│   ├── hotel/
│   │   ├── __init__.py    # exports Client + AsyncClient
│   │   └── _client.py     # facade + auth transport
│   └── _generated/        # AUTO-GENERATED — do not edit by hand
├── examples/canonical_flow.py
└── tests/                 # TODO — TECH-1100 harness will live here
```

## Regenerating the low-level client

The `tmsx._generated` package is produced from `sdk/tmsx-hotel-spec.yaml` by
`openapi-python-client`. To regenerate after the spec changes:

```bash
cd sdk/python
uvx --from openapi-python-client openapi-python-client generate \
  --path ../tmsx-hotel-spec.yaml \
  --config codegen-config.yaml \
  --meta none --overwrite \
  --output-path src/tmsx/_generated
```

The facade in `tmsx.hotel._client` may need import-name updates if the generator's
class names change — see the import block at the top of that file.

## Build / install locally

```bash
cd sdk/python
uv sync                 # install deps incl. dev
uv run python examples/canonical_flow.py
```

