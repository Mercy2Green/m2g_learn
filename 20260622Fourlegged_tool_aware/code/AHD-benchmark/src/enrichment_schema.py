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

COSMOS_PROMPT_FORBIDDEN_ACTION_PATTERNS = [
    r"\btransport\s+(?:all|them|these|to|toward|into)\b",
    r"\btransport\b.{0,60}\bto\s+(?:the\s+)?bedroom\b",
    r"\befficiently\s+transport\b",
    r"\bbring\s+(?:all|them|these)\b",
    r"\bdeliver\s+to\b",
    r"\bmove\s+to\b",
    r"\bretrieve\b.{0,80}\busing\b",
    r"\busing\s+(?:its|the)\s+single\s+arm\b",
    r"\brobot\s+must\b",
    r"\bmust\s+grasp\b",
    r"\btask\s+is\b",
    r"\bgrasp\s+one\s+object\b",
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
    cosmos_prompt = row.get("cosmos_prompt_variant")
    if isinstance(cosmos_prompt, str):
        for phrase in check_cosmos_prompt_action_leakage(cosmos_prompt):
            errors.append(f"cosmos_prompt_variant contains forbidden action/task phrase: {phrase}")
    return errors


def check_cosmos_prompt_action_leakage(text: str) -> list[str]:
    matches: list[str] = []
    normalized = " ".join(str(text).lower().split())
    for pattern in COSMOS_PROMPT_FORBIDDEN_ACTION_PATTERNS:
        found = re.search(pattern, normalized)
        if found:
            matches.append(found.group(0))
    return matches


def _contains_term(text: str, term: str) -> bool:
    pattern = r"(?<![a-z0-9_])" + re.escape(term.lower()) + r"(?![a-z0-9_])"
    return re.search(pattern, text.lower()) is not None
