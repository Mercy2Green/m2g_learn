from __future__ import annotations

import re
from typing import Any


REQUIRED_FIELDS = {
    "spec_id",
    "model_id",
    "instruction_en_variant",
    "instruction_zh_variant",
    "cosmos_prompt_variant",
    "negative_prompt_variant",
    "notes",
}

FORBIDDEN_FIELDS = {
    "gold",
    "mode",
    "needed_helper_function",
    "helper_found",
    "selected_helper",
    "helper_target_relation",
    "continue_search",
    "direct_fallback_allowed",
    "target_memory",
    "helper_candidates_gold",
    "pairing_role",
}

FORBIDDEN_LEAKAGE_TERMS = [
    "mode",
    "search_helper",
    "direct",
    "needed_helper_function",
    "helper_found",
    "selected_helper",
    "helper_target_relation",
    "continue_search",
    "direct_fallback_allowed",
    "target_memory",
    "helper_candidates_gold",
    "pairing_role",
    "correct helper",
    "wrong helper",
    "should use",
    "task-relevant",
]


def validate_enrichment_row(row: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - set(row))
    extra = sorted(set(row) - REQUIRED_FIELDS)
    forbidden = sorted(set(row) & FORBIDDEN_FIELDS)
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
    if extra:
        errors.append(f"unexpected fields: {', '.join(extra)}")
    if forbidden:
        errors.append(f"forbidden label fields present: {', '.join(forbidden)}")
    for field in REQUIRED_FIELDS - {"notes"}:
        if field in row and not isinstance(row[field], str):
            errors.append(f"{field} must be a string")
    if "notes" in row and not isinstance(row["notes"], list):
        errors.append("notes must be a list")
    return errors


def check_forbidden_label_leakage(row: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key, value in row.items():
        if key in FORBIDDEN_FIELDS:
            errors.append(f"forbidden label field present: {key}")
        if isinstance(value, str):
            for term in FORBIDDEN_LEAKAGE_TERMS:
                if _contains_term(value, term):
                    errors.append(f"{key} contains forbidden label term: {term}")
        elif isinstance(value, list):
            joined = " ".join(str(item) for item in value)
            for term in FORBIDDEN_LEAKAGE_TERMS:
                if _contains_term(joined, term):
                    errors.append(f"{key} contains forbidden label term: {term}")
    return errors


def _contains_term(text: str, term: str) -> bool:
    pattern = r"(?<![a-z0-9_])" + re.escape(term.lower()) + r"(?![a-z0-9_])"
    return re.search(pattern, text.lower()) is not None
