"""Test-runner CLI: load YAML cases, execute against the TMSX hotel sandbox, report.

Usage:
    tmsx-test-runner --list
    tmsx-test-runner --case TC-HOTEL-001
    tmsx-test-runner --all
    tmsx-test-runner --case TC-HOTEL-004 --agent-code XXX --username YYY --password ZZZ
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from copy import deepcopy
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import yaml

_DEBUG = bool(os.environ.get("TMSX_DEBUG"))

from tmsx._generated.models import (
    CancelOrderCancelOrderRequest,
    CreateOrderCreateOrderRequest,
    HotelDetailHotelDetailRequest,
    HotelstaticHotelStaticListRequest,
    RegionListRegionListRequest,
    RoomAvailRoomAvailRequest,
    RoomStaticModelRoomStaticRequest,
    SearchOrderQueryBookingsRequest,
    SearchOrderQueryOrderRequest,
)
from tmsx.exceptions import TMSXError
from tmsx.hotel import Client
from tmsx_test_runner.path import get as path_get
from tmsx_test_runner.path import is_missing

DEFAULT_CASES_FILE = Path(__file__).resolve().parents[3] / "test-cases" / "tmsx-hotel-cases.yaml"

# Op name → (SDK method name, generated request class).
OP_DISPATCH: dict[str, tuple[str, type]] = {
    "list_regions":     ("list_regions", RegionListRegionListRequest),
    "list_hotels":      ("list_hotels", HotelstaticHotelStaticListRequest),
    "list_room_types":  ("list_room_types", RoomStaticModelRoomStaticRequest),
    "search_hotel":     ("search_hotel", HotelDetailHotelDetailRequest),
    "check_room_rate":  ("check_room_rate", RoomAvailRoomAvailRequest),
    "create_order":     ("create_order", CreateOrderCreateOrderRequest),
    "search_order":     ("search_order", SearchOrderQueryOrderRequest),
    "query_bookings":   ("query_bookings", SearchOrderQueryBookingsRequest),
    "cancel_order":     ("cancel_order", CancelOrderCancelOrderRequest),
}


# ---------- variable interpolation -----------------------------------------

_VAR = re.compile(r"\$\{([A-Za-z_][\w.+\-]*)\}")
_DATE_OFFSET = re.compile(r"^today([+\-]\d+)?d?$")


def _builtin_date_vars(offset_days: int = 0) -> dict[str, str]:
    """Date variables every case can use without declaring them."""
    today = date.today() + timedelta(days=offset_days)
    return {
        "today":              today.isoformat(),
        "tomorrow":           (today + timedelta(days=1)).isoformat(),
        "day_after_tomorrow": (today + timedelta(days=2)).isoformat(),
        "next_week":          (today + timedelta(days=7)).isoformat(),
        "next_month":         (today + timedelta(days=30)).isoformat(),
    }


def _resolve_var(expr: str, scope: dict[str, Any]) -> Any:
    """Resolve `name` or `name.sub.path` or `today+Nd` from scope."""
    # `today+Nd` / `today-Nd` shortcut, evaluated at call time.
    offset_match = _DATE_OFFSET.match(expr)
    if offset_match:
        offset = int(offset_match.group(1) or 0)
        return (date.today() + timedelta(days=offset)).isoformat()
    head, _, tail = expr.partition(".")
    if head not in scope:
        raise KeyError(f"unresolved variable: ${{{expr}}}")
    value = scope[head]
    if not tail:
        return value
    rest = path_get(value, tail)
    if is_missing(rest):
        raise KeyError(f"unresolved variable subpath: ${{{expr}}}")
    return rest


def interpolate(value: Any, scope: dict[str, Any]) -> Any:
    if isinstance(value, str):
        match = _VAR.fullmatch(value.strip())
        if match:
            # Whole-string is a variable — preserve the original type.
            return _resolve_var(match.group(1), scope)
        # Embedded variables — string-substitute.
        return _VAR.sub(lambda m: str(_resolve_var(m.group(1), scope)), value)
    if isinstance(value, list):
        return [interpolate(item, scope) for item in value]
    if isinstance(value, dict):
        return {k: interpolate(v, scope) for k, v in value.items()}
    return value


# ---------- response → dict -------------------------------------------------


def response_to_dict(parsed: Any) -> dict[str, Any]:
    if parsed is None:
        return {}
    if hasattr(parsed, "to_dict"):
        return parsed.to_dict()  # type: ignore[no-any-return]
    if isinstance(parsed, dict):
        return parsed
    return {"__raw__": str(parsed)}


# ---------- assertions ------------------------------------------------------


def evaluate_assertions(response_dict: dict[str, Any], assertions: list[dict[str, Any]]) -> list[str]:
    failures: list[str] = []
    for assertion in assertions or []:
        path = assertion["path"]
        actual = path_get(response_dict, path)
        if "absent" in assertion:
            want_absent = assertion["absent"]
            if want_absent and not is_missing(actual) and actual not in (None, "", [], {}):
                failures.append(f"path '{path}' expected absent, got {actual!r}")
            continue
        if "present" in assertion:
            if assertion["present"] and (is_missing(actual) or actual in (None, "")):
                failures.append(f"path '{path}' expected present, got missing/empty")
            continue
        if "non_empty" in assertion:
            if assertion["non_empty"] and (is_missing(actual) or not actual):
                failures.append(f"path '{path}' expected non_empty, got {actual!r}")
            continue
        if "empty" in assertion:
            if assertion["empty"] and not (is_missing(actual) or not actual):
                failures.append(f"path '{path}' expected empty, got {actual!r}")
            continue
        if "equals" in assertion:
            expected = assertion["equals"]
            if actual != expected:
                failures.append(f"path '{path}' expected {expected!r}, got {actual!r}")
            continue
        if "not_equals" in assertion:
            if actual == assertion["not_equals"]:
                failures.append(f"path '{path}' expected not {assertion['not_equals']!r}, got {actual!r}")
            continue
        if "in" in assertion:
            if actual not in assertion["in"]:
                failures.append(f"path '{path}' expected in {assertion['in']!r}, got {actual!r}")
            continue
        failures.append(f"unknown assertion shape: {assertion!r}")
    return failures


# ---------- step + case execution ------------------------------------------


def execute_step(sdk_client: Client, step: dict[str, Any], scope: dict[str, Any]) -> dict[str, Any]:
    op_key = step["op"]
    method_name, request_cls = OP_DISPATCH[op_key]
    raw_input = interpolate(step.get("input") or {}, scope)
    request_obj = request_cls.from_dict(raw_input)
    method = getattr(sdk_client, method_name)
    response = method(request_obj)
    return response_to_dict(response)


def execute_case(
    sdk_client: Client,
    case: dict[str, Any],
    all_cases: dict[str, dict[str, Any]],
    cross_case_state: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Run one case. Returns a result dict the caller can pretty-print or aggregate."""
    case_id = case["id"]
    print(f"\n=== {case_id} · {case['name']}")

    # Ensure depends_on cases have run; pull their captures into our scope.
    dep_scope: dict[str, Any] = {}
    for dep_id in case.get("depends_on") or []:
        if dep_id not in cross_case_state:
            print(f"    → running dependency {dep_id} first")
            execute_case(sdk_client, all_cases[dep_id], all_cases, cross_case_state)
        dep_scope[dep_id] = cross_case_state[dep_id].get("captures", {})

    # Resolve case variables against builtins first, so a variable can reference ${today+Nd}.
    builtin_scope = _builtin_date_vars()
    case_vars = interpolate(deepcopy(case.get("variables") or {}), {**builtin_scope, **dep_scope})
    scope: dict[str, Any] = {**builtin_scope, **case_vars, **dep_scope}
    captures: dict[str, Any] = {}
    failures: list[str] = []

    for step_idx, step in enumerate(case["flow"], start=1):
        op_key = step["op"]
        try:
            response_dict = execute_step(sdk_client, step, scope)
        except TMSXError as exc:
            failures.append(f"step {step_idx} ({op_key}) raised TMSXError: {exc}")
            break
        except Exception as exc:  # noqa: BLE001 — runner is a backstop
            failures.append(f"step {step_idx} ({op_key}) raised {type(exc).__name__}: {exc}")
            break
        if _DEBUG:
            import json as _json
            print(f"    DEBUG response keys: {list(response_dict.keys())}")
            sample = _json.dumps(response_dict, default=str)[:600]
            print(f"    DEBUG response[:600]: {sample}")
        # Assertions
        step_failures = evaluate_assertions(response_dict, step.get("assert") or [])
        if step_failures:
            for failure in step_failures:
                failures.append(f"step {step_idx} ({op_key}): {failure}")
            break
        # Captures
        for capture in step.get("capture") or []:
            value = path_get(response_dict, capture["path"])
            if is_missing(value):
                failures.append(
                    f"step {step_idx} ({op_key}): capture '{capture['name']}' at '{capture['path']}' resolved to missing"
                )
                break
            captures[capture["name"]] = value
            scope[capture["name"]] = value
        if failures:
            break
        print(f"    ✓ step {step_idx}: {op_key}")

    cross_case_state[case_id] = {"captures": captures, "failures": failures}
    if failures:
        print(f"    ✗ FAIL")
        for failure in failures:
            print(f"        {failure}")
    else:
        print(f"    ✓ PASS")
    return cross_case_state[case_id]


def main() -> int:
    parser = argparse.ArgumentParser(prog="tmsx-test-runner", description="Run TMSX hotel integration test cases.")
    parser.add_argument("--cases-file", type=Path, default=DEFAULT_CASES_FILE)
    parser.add_argument("--case", action="append", default=[], help="run a single case by ID; repeatable")
    parser.add_argument("--all", action="store_true", help="run all cases")
    parser.add_argument("--list", action="store_true", help="list all case IDs and exit")
    parser.add_argument("--base-url", default="http://developers.tourmind.cn")
    parser.add_argument("--agent-code", default="tms_test")
    parser.add_argument("--username", default="tms_test")
    parser.add_argument("--password", default="tms_test")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON summary")
    args = parser.parse_args()

    if not args.cases_file.exists():
        print(f"cases file not found: {args.cases_file}", file=sys.stderr)
        return 2
    doc = yaml.safe_load(args.cases_file.read_text())
    all_cases: dict[str, dict[str, Any]] = {case["id"]: case for case in doc.get("cases", [])}

    if args.list:
        for case_id, case in all_cases.items():
            tags = case.get("tags") or []
            print(f"{case_id:14s}  {case['name']}  {tags}")
        return 0

    if args.all:
        targets = list(all_cases.keys())
    else:
        targets = args.case
    if not targets:
        parser.error("provide --case, --all, or --list")

    for case_id in targets:
        if case_id not in all_cases:
            print(f"unknown case ID: {case_id}", file=sys.stderr)
            return 2

    with Client(
        agent_code=args.agent_code,
        username=args.username,
        password=args.password,
        base_url=args.base_url,
    ) as sdk_client:
        cross_case_state: dict[str, dict[str, Any]] = {}
        for case_id in targets:
            if case_id not in cross_case_state:
                execute_case(sdk_client, all_cases[case_id], all_cases, cross_case_state)

    # Summary
    passed = [cid for cid, state in cross_case_state.items() if not state["failures"]]
    failed = [cid for cid, state in cross_case_state.items() if state["failures"]]
    print(f"\n=== summary: {len(passed)} passed, {len(failed)} failed of {len(cross_case_state)} cases run")
    if args.json:
        json.dump({"passed": passed, "failed": failed, "state": cross_case_state}, sys.stdout, default=str, indent=2)
        print()
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
