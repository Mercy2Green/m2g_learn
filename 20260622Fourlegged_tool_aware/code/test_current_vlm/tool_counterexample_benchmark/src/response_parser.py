from __future__ import annotations

import json
import re
from typing import Any


JSON_BLOCK_PATTERN = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL | re.IGNORECASE)


def parse_model_response(raw_response: str) -> dict[str, Any]:
    text = raw_response.strip()
    candidates = [text]
    match = JSON_BLOCK_PATTERN.search(text)
    if match:
        candidates.insert(0, match.group(1).strip())
    object_text = _extract_json_object(text)
    if object_text:
        candidates.append(object_text)

    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return {
                "parse_status": "ok",
                "parsed": normalize_response(parsed),
                "parse_error": "",
            }
    return {
        "parse_status": "parse_error",
        "parsed": {},
        "parse_error": "Could not parse response as a JSON object.",
    }


def _extract_json_object(text: str) -> str | None:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    return text[start : end + 1]


def normalize_response(parsed: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(parsed)
    normalized["plan"] = _normalize_plan(normalized.get("plan"))
    normalized["uses_tool_or_container"] = _normalize_yes_no(normalized.get("uses_tool_or_container"))
    normalized["will_search_for_tool_if_not_visible"] = _normalize_yes_no(normalized.get("will_search_for_tool_if_not_visible"))
    normalized["estimated_number_of_trips"] = _normalize_trip_count(normalized.get("estimated_number_of_trips"))
    for key in [
        "task_understanding",
        "tool_or_container",
        "efficiency_consideration",
        "safety_or_stability_consideration",
        "uncertainty_or_missing_information",
        "reason",
        "failure_risk",
    ]:
        normalized[key] = "" if normalized.get(key) is None else str(normalized.get(key))
    return normalized


def _normalize_plan(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if value is None:
        return []
    return [str(value)]


def _normalize_yes_no(value: Any) -> str:
    if isinstance(value, bool):
        return "yes" if value else "no"
    text = str(value).strip().lower()
    if text in {"yes", "y", "true", "1", "是", "会", "使用"}:
        return "yes"
    if text in {"no", "n", "false", "0", "否", "不会", "none", "null"}:
        return "no"
    return "unknown"


def _normalize_trip_count(value: Any) -> str:
    text = str(value).strip().lower()
    if text in {"single", "one", "1", "一次", "single_trip"}:
        return "single"
    if text in {"few", "2", "two", "少数", "few_trips", "single_or_few_trips"}:
        return "few"
    if text in {"multiple", "many", "多次", "逐个", "one_by_one"}:
        return "multiple"
    return "unknown"
