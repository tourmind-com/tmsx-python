"""Tiny path-accessor for the test runner.

Supports dotted-and-bracketed paths against nested dicts/lists, with one filter
form: `[?Field==value]` or `[?Field!=value]`. Not JMESPath — just the minimum we
need to query a TMSX response shape from a YAML test case.

Examples:
    "HotelDetailResult.Hotels[0].RoomTypes[0].RateInfos[0].RateId"
    "HotelDetailResult.Hotels[0].RoomTypes[0].RateInfos[?Refundable==true][0]"
    "Error.ErrorCode"
"""

from __future__ import annotations

import re
from typing import Any

_TOKEN = re.compile(r"""
    \.                    |  # dot separator
    \[(\d+)\]              |  # index: [0]
    \[\?([A-Za-z_][\w.]*)(==|!=)([^\]]+)\]  |  # filter: [?Foo==bar]
    ([A-Za-z_][\w]*)         # bare key
""", re.VERBOSE)


def _coerce_literal(text: str) -> Any:
    text = text.strip()
    if text in ("true", "True"):
        return True
    if text in ("false", "False"):
        return False
    if text in ("null", "None"):
        return None
    if text.startswith(("'", '"')) and text.endswith(("'", '"')):
        return text[1:-1]
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        pass
    return text


_MISSING = object()


def get(obj: Any, path: str) -> Any:
    """Resolve `path` against `obj`. Returns `MISSING` if any step fails."""
    if not path:
        return obj
    current: Any = obj
    pos = 0
    while pos < len(path):
        match = _TOKEN.match(path, pos)
        if not match:
            return _MISSING
        idx, filter_key, filter_op, filter_val, bare_key = match.groups()
        pos = match.end()
        if match.group(0) == ".":
            continue
        if idx is not None:
            if not isinstance(current, list) or int(idx) >= len(current):
                return _MISSING
            current = current[int(idx)]
        elif filter_key is not None:
            if not isinstance(current, list):
                return _MISSING
            literal = _coerce_literal(filter_val)
            predicate = (lambda item: get(item, filter_key) == literal) if filter_op == "==" else (lambda item: get(item, filter_key) != literal)
            filtered = [item for item in current if predicate(item)]
            current = filtered  # leave as list; next [N] will index it
        elif bare_key is not None:
            if not isinstance(current, dict) or bare_key not in current:
                return _MISSING
            current = current[bare_key]
    return current


def is_missing(value: Any) -> bool:
    return value is _MISSING
