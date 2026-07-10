from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from src.response_parser import parse_model_response


CONTAINER_TERMS = {
    "托盘": "tray", "盘子": "tray", "篮子": "basket", "筐": "basket", "箱子": "box",
    "盒子": "box", "袋子": "bag", "包": "bag", "container": "container", "tray": "tray",
    "basket": "basket", "box": "box", "bag": "bag", "tote": "tote bag",
}
LONG_RIGID_TERMS = {
    "扫把": "broom", "长杆": "rod", "杆子": "rod", "棍": "stick", "衣架": "hanger",
    "broom": "broom", "stick": "stick", "rod": "rod", "hanger": "hanger",
}
WRONG_OBJECT_TERMS = {
    "布": "cloth", "书": "book", "铅笔": "pencil", "枕头": "pillow", "杯子": "cup",
    "鞋": "shoe", "cloth": "cloth", "book": "book", "pencil": "pencil", "pillow": "pillow",
    "cup": "cup", "shoe": "shoe",
}
SEARCH_TERMS = [
    "寻找合适", "寻找可用", "查找合适", "检查附近区域", "查看附近区域", "搜索附近",
    "继续检查附近", "look for a suitable", "look for a useful", "search nearby", "check nearby",
    "inspect nearby", "continue checking nearby",
]
REJECT_TERMS = [
    "不适合", "不合适", "无关", "不能用于", "无法帮助", "不使用当前", "not suitable",
    "unsuitable", "irrelevant", "cannot help", "reject",
]
DIRECT_TERMS = [
    "直接拿", "直接抓", "直接夹", "直接拾取", "直接执行", "拿起水瓶", "抓取水瓶",
    "directly", "direct grasp", "pick up the bottle", "grasp the bottle",
]
ONE_BY_ONE_TERMS = ["逐个", "一个个", "一瓶一瓶", "每次一个", "one by one", "one-by-one"]
AGGREGATE_ACTION_TERMS = [
    "放入", "放进", "装入", "装进", "装载", "收集", "集中", "承载", "运送", "搬运",
    "put", "place", "load", "collect", "gather", "carry", "transport", "deliver",
]
REACH_ACTION_TERMS = [
    "拨出", "拉出", "推出来", "勾出", "扫出", "伸到", "够到", "pull", "push", "hook",
    "sweep", "reach", "retrieve",
]
USE_ACTION_TERMS = AGGREGATE_ACTION_TERMS + REACH_ACTION_TERMS + ["使用", "利用", "use"]


EVALUATION_FIELDS = [
    "sample_id", "sample_type", "group_id", "protocol", "prompt_id", "model_id", "o0_spec_id",
    "o1_spec_id", "response_status", "parse_status", "inferred_helper_mentioned", "inferred_valid_helper_action_chain",
    "inferred_searches_helper", "inferred_selected_helper", "decision_pred", "relation_pred", "pass_fail",
    "failure_reason", "same_o1_different_o0_consistency",
]


def summarize_raw_file(input_dir: str | Path) -> dict[str, Any]:
    output_dir = Path(input_dir)
    raw_path = output_dir / "raw_responses.jsonl"
    if not raw_path.is_file():
        raise FileNotFoundError(f"Raw response file not found: {raw_path}")
    raw_rows = read_jsonl(raw_path)
    parsed_rows: list[dict[str, Any]] = []
    evaluations: list[dict[str, Any]] = []
    for raw in raw_rows:
        parsed_result = classify_and_parse_response(raw)
        parsed_row = {
            **raw_identity(raw),
            "response_status": parsed_result["response_status"],
            "parse_status": parsed_result["parse_status"],
            "parse_error": parsed_result["parse_error"],
            "parsed": parsed_result["parsed"],
            "raw_response_turn1": raw.get("raw_response_turn1", ""),
            "raw_response_final": raw.get("raw_response_final", ""),
            "error": raw.get("error", ""),
        }
        parsed_rows.append(parsed_row)
        evaluations.append(evaluate_one(raw, parsed_result))

    annotate_group_consistency(evaluations)
    write_jsonl(output_dir / "parsed_results.jsonl", parsed_rows)
    write_csv(output_dir / "sequential_evaluation.csv", evaluations, EVALUATION_FIELDS)
    write_summary(output_dir / "summary.md", evaluations)
    write_failed_cases(output_dir / "failed_cases.md", evaluations, parsed_rows)
    return {
        "raw_rows": len(raw_rows),
        "parse_success": sum(row["response_status"] == "ok_eval" for row in evaluations),
        "response_status_counts": dict(Counter(row["response_status"] for row in evaluations)),
        "status_counts": dict(Counter(row["pass_fail"] for row in evaluations)),
    }


def classify_and_parse_response(raw: dict[str, Any]) -> dict[str, Any]:
    if raw.get("dry_run") is True:
        return {
            "response_status": "dry_run",
            "parse_status": "skipped",
            "parsed": {},
            "parse_error": "dry_run",
        }
    if raw.get("error"):
        return {
            "response_status": "provider_error",
            "parse_status": "provider_error",
            "parsed": {},
            "parse_error": str(raw.get("error")),
        }

    final = str(raw.get("raw_response_final", ""))
    if not final.strip():
        if is_generation_budget_exhausted(raw):
            return {
                "response_status": "generation_budget_exhausted",
                "parse_status": "generation_budget_exhausted",
                "parsed": {},
                "parse_error": "Model exhausted its generation budget before producing final content.",
            }
        return {
            "response_status": "parse_error_empty",
            "parse_status": "parse_error_empty",
            "parsed": {},
            "parse_error": "Model returned empty final content without confirmed budget exhaustion.",
        }

    parsed_result = parse_model_response(final)
    if parsed_result["parse_status"] != "ok":
        return {
            **parsed_result,
            "response_status": "parse_error_nonempty",
            "parse_status": "parse_error_nonempty",
        }
    if is_schema_echo(parsed_result["parsed"]):
        return {
            **parsed_result,
            "response_status": "schema_echo",
            "parse_status": "schema_echo",
            "parse_error": "Model echoed the response schema instead of producing a task-grounded plan.",
        }
    return {**parsed_result, "response_status": "ok_eval"}


def is_generation_budget_exhausted(raw: dict[str, Any]) -> bool:
    metadata = raw.get("metadata_final")
    if not isinstance(metadata, dict) or metadata.get("ollama_done") is not True:
        return False
    eval_count = optional_int(metadata.get("eval_count"))
    configured_max = optional_int(
        metadata.get("configured_max_tokens", raw.get("configured_max_tokens"))
    )
    return eval_count is not None and configured_max is not None and eval_count >= configured_max


def optional_int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def evaluate_one(raw: dict[str, Any], parsed_result: dict[str, Any]) -> dict[str, Any]:
    row = {
        **raw_identity(raw),
        "response_status": parsed_result.get("response_status", "parse_error_nonempty"),
        "parse_status": parsed_result.get("parse_status", "parse_error"),
        "inferred_helper_mentioned": "no",
        "inferred_valid_helper_action_chain": "no",
        "inferred_searches_helper": "no",
        "inferred_selected_helper": "",
        "decision_pred": "unclear",
        "relation_pred": "unclear",
        "pass_fail": "needs_review",
        "failure_reason": "",
        "same_o1_different_o0_consistency": "not_available",
    }
    response_status = str(parsed_result.get("response_status", ""))
    if response_status == "dry_run":
        row.update({"pass_fail": "needs_review", "failure_reason": "dry_run"})
        return row
    if response_status in {"generation_budget_exhausted", "provider_error"}:
        row.update(
            {
                "pass_fail": "not_evaluated",
                "failure_reason": parsed_result.get("parse_error", response_status),
            }
        )
        return row
    if response_status in {"parse_error_empty", "parse_error_nonempty"}:
        row.update({"pass_fail": "parse_error", "failure_reason": parsed_result.get("parse_error", "parse_error")})
        return row
    if response_status == "schema_echo":
        row.update(
            {
                "pass_fail": "needs_review",
                "failure_reason": "Model echoed the response schema instead of producing a task-grounded plan.",
            }
        )
        return row

    parsed = parsed_result.get("parsed", {})
    text = combined_text(parsed)
    container = first_term(text, CONTAINER_TERMS)
    long_rigid = first_term(text, LONG_RIGID_TERMS)
    wrong_object = first_term(text, WRONG_OBJECT_TERMS)
    selected = str(parsed.get("selected_helper") or parsed.get("tool_or_container") or "").strip()
    if not selected:
        selected = container or long_rigid or wrong_object

    searches = contains_any(text, SEARCH_TERMS)
    rejects = contains_any(text, REJECT_TERMS)
    container_chain = bool(container) and has_term_action_chain(parsed, CONTAINER_TERMS, AGGREGATE_ACTION_TERMS)
    reach_chain = bool(long_rigid) and has_term_action_chain(parsed, LONG_RIGID_TERMS, REACH_ACTION_TERMS)
    wrong_chain = bool(wrong_object) and has_term_action_chain(parsed, WRONG_OBJECT_TERMS, USE_ACTION_TERMS)
    valid_chain = container_chain or reach_chain or wrong_chain
    helper_mentioned = bool(container or long_rigid or wrong_object or selected)

    if container_chain:
        relation = "aggregate_transport"
    elif reach_chain:
        relation = "reach_extension"
    elif valid_chain:
        relation = "none"
    elif not helper_mentioned:
        relation = "none"
    else:
        relation = "unclear"

    sample_type = str(raw.get("sample_type", ""))
    if valid_chain:
        decision = "helper_found"
    elif searches or rejects:
        decision = "continue_search"
    elif contains_any(text, DIRECT_TERMS) or contains_any(text, ONE_BY_ONE_TERMS):
        decision = "direct_is_enough"
    elif sample_type == "no_tool_control" and not helper_mentioned:
        decision = "direct_is_enough"
    elif sample_type in {"positive_aggregate", "positive_reach"} and not helper_mentioned:
        decision = "direct_is_enough"
    else:
        decision = "unclear"

    row.update(
        {
            "inferred_helper_mentioned": "yes" if helper_mentioned else "no",
            "inferred_valid_helper_action_chain": "yes" if valid_chain else "no",
            "inferred_searches_helper": "yes" if searches else "no",
            "inferred_selected_helper": selected,
            "decision_pred": decision,
            "relation_pred": relation,
        }
    )
    pass_fail, reason = judge_prediction(raw, row, rejects=rejects, wrong_chain=wrong_chain)
    row["pass_fail"] = pass_fail
    row["failure_reason"] = reason
    return row


def judge_prediction(
    raw: dict[str, Any], prediction: dict[str, Any], *, rejects: bool, wrong_chain: bool
) -> tuple[str, str]:
    sample_type = str(raw.get("sample_type", ""))
    decision = prediction["decision_pred"]
    relation = prediction["relation_pred"]
    valid_chain = prediction["inferred_valid_helper_action_chain"] == "yes"
    expected = str((raw.get("gold") or {}).get("expected_decision", ""))
    expected_relation = str((raw.get("gold") or {}).get("helper_target_relation", "none"))

    if sample_type == "positive_aggregate":
        if decision == "helper_found" and relation == "aggregate_transport":
            return "pass", ""
        return "fail", "No valid aggregate helper-target action chain; direct/one-by-one handling is insufficient."
    if sample_type == "positive_reach":
        if decision == "helper_found" and relation == "reach_extension":
            return "pass", ""
        return "fail", "No valid reach-extension action chain for the remembered O0 target."
    if sample_type == "wrong_helper_negative":
        if decision == "continue_search" or rejects:
            return "pass", ""
        if valid_chain or wrong_chain or decision == "helper_found":
            return "fail", "The unsuitable O1 object was used as a helper."
        return "needs_review", "The response neither uses nor clearly rejects the unsuitable O1 object."
    if sample_type == "no_tool_control":
        if decision == "direct_is_enough" and not valid_chain:
            return "pass", ""
        if valid_chain or decision == "helper_found":
            return "fail", "The response over-used an O1 object for a directly executable task."
        return "needs_review", "Direct execution is not clear."
    if sample_type == "same_o1_different_o0":
        if decision == expected and (expected != "helper_found" or relation == expected_relation):
            return "pass", ""
        if decision == "unclear":
            return "needs_review", "Decision is unclear for the shared-O1 control case."
        return "fail", f"Expected {expected}/{expected_relation}, predicted {decision}/{relation}."
    return "needs_review", f"Unknown sample_type: {sample_type}"


def annotate_group_consistency(rows: list[dict[str, Any]]) -> None:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("sample_type") == "same_o1_different_o0" and row.get("group_id"):
            grouped[(str(row["model_id"]), str(row["prompt_id"]), str(row["group_id"]))].append(row)
    for group_rows in grouped.values():
        if len(group_rows) != 3 or any(row.get("response_status") != "ok_eval" for row in group_rows):
            result = "not_available"
        else:
            by_source = {str(row["old_task_id_source"]): row["decision_pred"] for row in group_rows}
            result = "pass" if by_source == {
                "task_002": "helper_found",
                "task_011": "direct_is_enough",
                "task_008": "continue_search",
            } else "fail"
        for row in group_rows:
            row["same_o1_different_o0_consistency"] = result


def raw_identity(raw: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "sample_id", "sample_type", "group_id", "protocol", "prompt_id", "model_id", "o0_spec_id",
        "o1_spec_id", "old_task_id_source", "instruction", "o0_image_path", "o1_image_path", "gold",
    ]
    return {key: raw.get(key, "") for key in keys}


def combined_text(parsed: dict[str, Any]) -> str:
    values: list[str] = []
    for key in (
        "task_understanding", "efficiency_consideration", "safety_or_stability_consideration",
        "uncertainty_or_missing_information", "reason", "selected_helper", "tool_or_container",
    ):
        if parsed.get(key):
            values.append(str(parsed[key]))
    values.extend(str(step) for step in parsed.get("plan", []))
    values.extend(str(step) for step in parsed.get("tool_use_action_chain", []))
    return " ".join(values).lower()


def is_schema_echo(parsed: dict[str, Any]) -> bool:
    understanding = str(parsed.get("task_understanding", "")).strip().lower()
    plan = [str(step).strip().lower() for step in parsed.get("plan", [])]
    return understanding == "string" or plan == ["step1", "step2", "step3"]


def has_term_action_chain(
    parsed: dict[str, Any], term_map: dict[str, str], action_terms: list[str]
) -> bool:
    steps = [str(step).lower() for step in parsed.get("plan", [])]
    steps.extend(str(step).lower() for step in parsed.get("tool_use_action_chain", []))
    for step in steps:
        if any(term.lower() in step for term in term_map) and contains_any(step, action_terms):
            return True
    full = " ".join(steps)
    return any(term.lower() in full for term in term_map) and contains_any(full, action_terms)


def first_term(text: str, term_map: dict[str, str]) -> str:
    matches = [(text.find(term.lower()), canonical) for term, canonical in term_map.items() if term.lower() in text]
    return min(matches)[1] if matches else ""


def contains_any(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError(f"JSONL row is not an object: {path}")
                rows.append(value)
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_summary(path: Path, rows: list[dict[str, Any]]) -> None:
    response_counts = Counter(row["response_status"] for row in rows)
    lines = [
        "# Sequential O0/O1 Evaluation Summary",
        "",
        f"- evaluated rows: {len(rows)}",
        f"- ok evaluations: {response_counts['ok_eval']}",
        f"- generation budget exhausted: {response_counts['generation_budget_exhausted']}",
        f"- schema echoes: {response_counts['schema_echo']}",
        f"- non-empty parse errors: {response_counts['parse_error_nonempty']}",
        f"- provider errors: {response_counts['provider_error']}",
        "- clean protocols do not explicitly name task-specific helper types.",
        "- generation/provider failures are not counted as task-capability failures.",
        "",
        "## Response Execution Status",
        "",
        "| response_status | count |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {status} | {count} |" for status, count in sorted(response_counts.items()))
    lines.extend([
        "",
        "## By Protocol",
        "",
        "| protocol | pass | fail | needs_review | parse_error | not_evaluated |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ])
    lines.extend(status_lines(rows, "protocol"))
    lines.extend([
        "", "## By Sample Type", "", "| sample_type | pass | fail | needs_review | parse_error | not_evaluated |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ])
    lines.extend(status_lines(rows, "sample_type"))
    lines.extend([
        "", "## Same O1 Different O0 Consistency", "",
        "| model | prompt | group | consistency |", "| --- | --- | --- | --- |",
    ])
    group_rows: dict[tuple[str, str, str], str] = {}
    for row in rows:
        if row.get("sample_type") == "same_o1_different_o0":
            key = (str(row["model_id"]), str(row["prompt_id"]), str(row["group_id"]))
            group_rows[key] = str(row["same_o1_different_o0_consistency"])
    if group_rows:
        for (model, prompt, group), result in sorted(group_rows.items()):
            lines.append(f"| {model} | {prompt} | {group} | {result} |")
    else:
        lines.append("| - | - | - | not_available |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def status_lines(rows: list[dict[str, Any]], key: str) -> list[str]:
    grouped: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        grouped[str(row.get(key, ""))][str(row.get("pass_fail", ""))] += 1
    return [
        f"| {name} | {counts['pass']} | {counts['fail']} | {counts['needs_review']} | "
        f"{counts['parse_error']} | {counts['not_evaluated']} |"
        for name, counts in sorted(grouped.items())
    ]


def write_failed_cases(path: Path, rows: list[dict[str, Any]], parsed_rows: list[dict[str, Any]]) -> None:
    parsed_by_key = {
        (row["sample_id"], row["model_id"], row["prompt_id"]): row for row in parsed_rows
    }
    lines = [
        "# Sequential Failed and Review Cases", "",
        "Heuristic labels are a baseline first pass and require human review before research claims.", "",
    ]
    failures = [row for row in rows if row["pass_fail"] != "pass"]
    if not failures:
        lines.append("No failed or review cases.")
    for row in failures:
        parsed = parsed_by_key.get((row["sample_id"], row["model_id"], row["prompt_id"]), {}).get("parsed", {})
        plan = "; ".join(parsed.get("plan", [])) if isinstance(parsed, dict) else ""
        lines.append(
            f"- {row['sample_id']} / {row['model_id']} / {row['prompt_id']}: "
            f"{row['pass_fail']} - {row['failure_reason']} Plan: {plan}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
