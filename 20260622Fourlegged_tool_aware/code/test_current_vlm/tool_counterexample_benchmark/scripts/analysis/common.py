from __future__ import annotations

import ast
import csv
import json
import re
from pathlib import Path
from typing import Any, Iterable


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    file_path = Path(path)
    if not file_path.exists():
        return rows
    with file_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            rows.append(json.loads(stripped))
    return rows


def write_jsonl(path: str | Path, rows: Iterable[dict[str, Any]]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_csv_dicts(path: str | Path) -> list[dict[str, str]]:
    file_path = Path(path)
    if not file_path.exists():
        return []
    with file_path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv_dicts(path: str | Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: _csv_value(row.get(field, "")) for field in fieldnames})


def _csv_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list, tuple, bool)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def safe_load_yaml(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {}
    text = file_path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        try:
            from src.load_config import load_yaml

            data = load_yaml(file_path)
            if data:
                return data
        except Exception:
            pass
    try:
        from src.load_config import _load_yaml_subset  # type: ignore

        data = _load_yaml_subset(_indent_unindented_top_level_lists(text))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _indent_unindented_top_level_lists(text: str) -> str:
    lines = text.splitlines()
    if len(lines) < 2 or not lines[0].endswith(":") or not lines[1].startswith("- "):
        return text
    normalized = [lines[0]]
    in_top_list = False
    for line in lines[1:]:
        if line.startswith("- "):
            normalized.append("  " + line)
            in_top_list = True
        elif in_top_list and line.startswith("  ") and not line.startswith("    "):
            normalized.append("  " + line)
        else:
            normalized.append(line)
    return "\n".join(normalized)


def compact_text(value: Any, max_chars: int = 500) -> str:
    text = "" if value is None else str(value)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def normalize_list_field(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, tuple):
        return [str(item) for item in value]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        try:
            parsed = json.loads(stripped)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except json.JSONDecodeError:
            pass
        try:
            parsed = ast.literal_eval(stripped)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except (ValueError, SyntaxError):
            pass
        if ";" in stripped:
            return [part.strip() for part in stripped.split(";") if part.strip()]
        if "," in stripped:
            return [part.strip() for part in stripped.split(",") if part.strip()]
        return [stripped]
    return [str(value)]


def join_key(row: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(row.get("task_id", "")),
        str(row.get("image_path", "")),
        str(row.get("model_id", "")),
        str(row.get("prompt_id", "")),
    )


def output_dir_to_run_id(path: str | Path) -> str:
    return Path(path).name


def infer_run_category_from_dirname(dirname: str) -> str:
    if "tool_prior_intervention" in dirname:
        return "tool_prior_intervention"
    if "diagnostic_probes" in dirname:
        return "diagnostic_probes"
    if "generic_clean" in dirname:
        return "generic_clean"
    if "humanoid_dual_arm_clean" in dirname:
        return "humanoid_dual_arm_clean"
    if "quadruped_single_arm_clean" in dirname:
        return "quadruped_single_arm_clean"
    if "all_clean" in dirname:
        return "all_clean"
    return "unknown"


def infer_model_from_dirname(dirname: str) -> str:
    known_categories = [
        "tool_prior_intervention",
        "diagnostic_probes",
        "humanoid_dual_arm_clean",
        "quadruped_single_arm_clean",
        "generic_clean",
        "all_clean",
    ]
    for category in known_categories:
        token = f"_{category}_"
        if token in dirname:
            return dirname.split(token, 1)[1]
    return ""


def flatten_parsed_fields(parsed: dict[str, Any]) -> dict[str, Any]:
    return {
        "parsed_plan": "; ".join(normalize_list_field(parsed.get("plan"))),
        "parsed_reason": str(parsed.get("reason", "") or ""),
        "parsed_efficiency_consideration": str(parsed.get("efficiency_consideration", "") or ""),
        "parsed_safety_or_stability_consideration": str(parsed.get("safety_or_stability_consideration", "") or ""),
        "parsed_uncertainty_or_missing_information": str(parsed.get("uncertainty_or_missing_information", "") or ""),
        "parsed_selected_helper": str(parsed.get("selected_helper") or parsed.get("tool_or_container") or ""),
        "parsed_tool_use_action_chain": "; ".join(normalize_list_field(parsed.get("tool_use_action_chain"))),
        "parsed_target_objects": "; ".join(normalize_list_field(parsed.get("target_objects"))),
        "parsed_visible_helper_objects": "; ".join(normalize_list_field(parsed.get("visible_helper_objects"))),
        "parsed_helper_needed": str(parsed.get("helper_needed", "") or ""),
        "parsed_helper_purpose": str(parsed.get("helper_purpose", "") or ""),
        "parsed_search_for_helper_if_none_visible": str(parsed.get("search_for_helper_if_none_visible", "") or ""),
    }


def lower_join(values: Iterable[Any] | Any) -> str:
    if isinstance(values, (str, bytes)):
        items = [values]
    elif isinstance(values, Iterable):
        items = list(values)
    else:
        items = [values]
    return " ".join("" if item is None else str(item) for item in items).lower()


def contains_any(text: str, keywords: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(keyword and keyword.lower() in lowered for keyword in keywords)


def extract_plan_text(row: dict[str, Any]) -> str:
    pieces = [
        row.get("parsed_plan", ""),
        row.get("parsed_tool_use_action_chain", ""),
        row.get("parsed_reason", ""),
        row.get("parsed_efficiency_consideration", ""),
        row.get("parsed_safety_or_stability_consideration", ""),
        row.get("parsed_uncertainty_or_missing_information", ""),
        row.get("raw_response", ""),
    ]
    return compact_text(" ".join(str(piece) for piece in pieces if piece), max_chars=4000)


def extract_evidence_quote(text: str, max_chars: int = 240) -> str:
    return compact_text(text, max_chars=max_chars)
