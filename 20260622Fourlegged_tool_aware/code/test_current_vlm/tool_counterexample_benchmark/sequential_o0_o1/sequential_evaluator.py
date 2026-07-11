from __future__ import annotations

import csv
import json
import re
import shutil
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
        "## By Model",
        "",
        "| model | pass | fail | needs_review | parse_error | not_evaluated |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ])
    lines.extend(status_lines(rows, "model_id"))
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


# V2 is intentionally additive. The v1 entry points above remain unchanged so
# historical scripts continue to reproduce their original files.
EVALUATOR_VERSION_V2 = "sequential_heuristic_v2"
BENCHMARK_ROOT = Path(__file__).resolve().parents[1]

V2_CONTAINER_TERMS: dict[str, list[str]] = {
    "baking_tray": ["金属烤盘", "烤盘", "baking tray", "metal tray", "baking pan", "pan"],
    "tray": ["托盘", "托板", "盘子", "serving tray", "tray"],
    "basket": ["篮子", "筐", "basket"],
    "box": ["盒子", "箱子", "box"],
    "bag": ["购物袋", "袋子", "tote", "bag"],
}
V2_GENERIC_CONTAINER_TERMS = ["container"]
V2_LONG_RIGID_TERMS = [
    "扫把", "长杆", "杆子", "木棍", "棍子", "衣架", "拖把", "broom", "stick", "rod",
    "pole", "hanger", "mop", "long handle", "long rigid object",
]
V2_WRONG_OBJECT_TERMS = [
    "抹布", "布", "书", "铅笔", "枕头", "杯子", "鞋", "cloth", "book", "pencil",
    "pillow", "cup", "shoe",
]
V2_EMBODIMENT_BATCHING_TERMS = [
    "双手", "两只手", "左手", "右手", "两臂", "两个夹爪", "机械臂同时", "每只手",
    "both hands", "two hands", "left hand", "right hand", "both arms", "two grippers", "each hand",
]
V2_DIRECT_MULTI_TRIP_TERMS = [
    "逐个", "一瓶一瓶", "每次一瓶", "分批搬运", "多次往返", "返回厨房重复", "one by one",
    "one-by-one", "one at a time", "multiple trips", "repeat until all", "return and repeat",
]
V2_O0_MEMORY_TERMS = [
    "o0", "上一轮", "之前看到", "原始观察", "原位置", "remembered", "previous observation",
    "original observation", "original target",
]
V2_O1_OBSERVATION_TERMS = [
    "o1", "当前新观察", "新观察", "环视", "当前观察", "later observation", "new observation",
]
V2_LINK_TERMS = [
    "使用当前观察中的", "用 o1 中的", "将其用于之前的", "作为辅助", "用来承载", "用来够到",
    "用来拉出", "use the object in o1", "use it for the previous target", "for the remembered target",
    "carry the bottles", "reach/pull the remote",
]
V2_AGGREGATE_TARGET_TERMS = [
    "水瓶", "饮料瓶", "瓶子", "这些水", "这些饮料", "多瓶", "bottle", "bottles", "drinks", "water",
]
V2_REACH_TARGET_TERMS = ["遥控器", "小球", "玩具", "remote", "remote control", "ball", "toy"]
V2_DIRECT_ACTION_TERMS = [
    "直接", "抓取", "拿起", "拾取", "夹取", "递给", "抓住", "grasp", "pick up", "retrieve directly",
]
V2_PRONOUN_TARGET_TERMS = ["这些", "全部", "它们", "将其", "目标物", "them", "all", "target"]
V2_AGGREGATE_ACTION_TERMS = AGGREGATE_ACTION_TERMS + ["装"]

V2_ADDITIONAL_FIELDS = [
    "evaluator_version",
    "uses_physical_o1_helper",
    "physical_helper_type",
    "uses_embodiment_batching",
    "uses_direct_multi_trip",
    "uses_wrong_o1_object",
    "mentions_o0_memory",
    "mentions_o1_observation",
    "links_o1_helper_to_o0_target",
    "action_mode_pred",
    "v1_pass_fail",
]
V2_EVALUATION_FIELDS = EVALUATION_FIELDS + V2_ADDITIONAL_FIELDS


def summarize_raw_file_v2(
    input_dir: str | Path,
    output_dir: str | Path,
    *,
    review_images_dir: str | Path | None = None,
    experiment_name: str | None = None,
) -> dict[str, Any]:
    source_dir = Path(input_dir)
    destination = Path(output_dir)
    raw_path = source_dir / "raw_responses.jsonl"
    if not raw_path.is_file():
        raise FileNotFoundError(f"Raw response file not found: {raw_path}")
    destination.mkdir(parents=True, exist_ok=True)

    raw_rows = read_jsonl(raw_path)
    parsed_rows: list[dict[str, Any]] = []
    evaluations: list[dict[str, Any]] = []
    v1_rows: list[dict[str, Any]] = []
    raw_by_key: dict[tuple[str, str, str], dict[str, Any]] = {}
    parsed_by_key: dict[tuple[str, str, str], dict[str, Any]] = {}
    for raw in raw_rows:
        parsed_result = classify_and_parse_response(raw)
        key = v2_row_key(raw)
        parsed_row = {
            **raw_identity(raw),
            "evaluator_version": EVALUATOR_VERSION_V2,
            "response_status": parsed_result["response_status"],
            "parse_status": parsed_result["parse_status"],
            "parse_error": parsed_result["parse_error"],
            "parsed": parsed_result["parsed"],
            "raw_response_turn1": raw.get("raw_response_turn1", ""),
            "raw_response_final": raw.get("raw_response_final", ""),
            "error": raw.get("error", ""),
        }
        v1 = evaluate_one(raw, parsed_result)
        v2 = evaluate_one_v2(raw, parsed_result)
        v2["v1_pass_fail"] = v1["pass_fail"]
        parsed_rows.append(parsed_row)
        v1_rows.append(v1)
        evaluations.append(v2)
        raw_by_key[key] = raw
        parsed_by_key[key] = parsed_row

    annotate_group_consistency_v2(evaluations)
    write_jsonl(destination / "parsed_results_v2.jsonl", parsed_rows)
    write_csv(destination / "sequential_evaluation_v2.csv", evaluations, V2_EVALUATION_FIELDS)
    write_summary_v2(destination / "summary_v2.md", evaluations)
    write_failed_cases_v2(destination / "failed_cases_v2.md", evaluations, parsed_by_key)
    write_aggregate_metrics_v2(destination / "aggregate_metrics_v2.csv", evaluations)

    review_rows = select_manual_review_rows_v2(evaluations, parsed_by_key)
    copied_images: dict[str, tuple[str, str]] = {}
    if review_images_dir is not None:
        copied_images = copy_review_images_v2(
            evaluations,
            raw_by_key,
            Path(review_images_dir),
            experiment_name or source_dir.name,
        )
    write_manual_review_pack_v2(
        destination / "manual_review_pack_v2.md", review_rows, parsed_by_key, copied_images
    )
    return {
        "evaluator_version": EVALUATOR_VERSION_V2,
        "raw_rows": len(raw_rows),
        "response_status_counts": dict(Counter(row["response_status"] for row in evaluations)),
        "status_counts": dict(Counter(row["pass_fail"] for row in evaluations)),
        "manual_review_rows": len(review_rows),
        "copied_analysis_image_samples": len(copied_images),
    }


def evaluate_one_v2(raw: dict[str, Any], parsed_result: dict[str, Any]) -> dict[str, Any]:
    base = evaluate_one(raw, parsed_result)
    row = {
        **base,
        "evaluator_version": EVALUATOR_VERSION_V2,
        "uses_physical_o1_helper": "unclear",
        "physical_helper_type": "unclear",
        "uses_embodiment_batching": "unclear",
        "uses_direct_multi_trip": "unclear",
        "uses_wrong_o1_object": "unclear",
        "mentions_o0_memory": "unclear",
        "mentions_o1_observation": "unclear",
        "links_o1_helper_to_o0_target": "unclear",
        "action_mode_pred": "unclear",
        "v1_pass_fail": base.get("pass_fail", ""),
    }
    if parsed_result.get("response_status") != "ok_eval":
        return row

    parsed = parsed_result.get("parsed", {})
    text = combined_text(parsed)
    steps = v2_plan_steps(parsed)
    sample_type = str(raw.get("sample_type", ""))
    old_task_id = str(raw.get("old_task_id_source", ""))
    expected_relation = str((raw.get("gold") or {}).get("helper_target_relation", "none"))

    helper_type, helper_terms = detect_physical_helper_type_v2(text)
    container_chain = helper_type in {"tray", "baking_tray", "basket", "box", "bag"} and any(
        v2_step_has_terms_and_action(step, helper_terms, V2_AGGREGATE_ACTION_TERMS)
        for step in steps
    )
    long_chain = helper_type == "long_rigid" and any(
        v2_step_has_terms_and_action(step, helper_terms, REACH_ACTION_TERMS)
        for step in steps
    )
    physical_chain = container_chain or long_chain
    helper_mentioned = bool(helper_terms)
    rejects = contains_any(text, REJECT_TERMS)
    searches = contains_any(text, SEARCH_TERMS)
    wrong_mentioned = v2_contains_any(text, V2_WRONG_OBJECT_TERMS)
    wrong_used = any(
        v2_step_has_terms_and_action(step, V2_WRONG_OBJECT_TERMS, USE_ACTION_TERMS) for step in steps
    )
    embodiment = v2_contains_any(text, V2_EMBODIMENT_BATCHING_TERMS)
    direct_multi_signal = v2_contains_any(text, V2_DIRECT_MULTI_TRIP_TERMS) or str(
        parsed.get("estimated_number_of_trips", "")
    ) == "multiple"
    direct_multi = direct_multi_signal and not physical_chain and not embodiment
    mentions_o0 = v2_contains_any(text, V2_O0_MEMORY_TERMS)
    mentions_o1 = v2_contains_any(text, V2_O1_OBSERVATION_TERMS)
    explicit_link = v2_contains_any(text, V2_LINK_TERMS)
    relevant_targets = V2_REACH_TARGET_TERMS if expected_relation == "reach_extension" or old_task_id == "task_008" else V2_AGGREGATE_TARGET_TERMS
    target_link = v2_contains_any(" ".join(steps), relevant_targets + V2_PRONOUN_TARGET_TERMS)
    link = physical_chain and (explicit_link or target_link)

    if physical_chain:
        uses_physical = "yes"
    elif helper_mentioned and not rejects:
        uses_physical = "unclear"
    else:
        uses_physical = "no"
    if wrong_used:
        uses_wrong = "yes"
    elif wrong_mentioned and not rejects:
        uses_wrong = "unclear"
    else:
        uses_wrong = "no"
    if link:
        links = "yes"
    elif physical_chain:
        links = "unclear"
    else:
        links = "no"

    direct_action = v2_contains_any(text, V2_DIRECT_ACTION_TERMS)
    if wrong_used:
        action_mode = "wrong_helper_use"
    elif physical_chain and link:
        action_mode = "physical_o1_helper_chain"
    elif embodiment and not physical_chain:
        action_mode = "embodiment_batching"
    elif direct_multi:
        action_mode = "direct_multi_trip"
    elif searches or rejects:
        action_mode = "continue_search"
    elif direct_action and not helper_mentioned:
        action_mode = "direct_single"
    else:
        action_mode = "unclear"

    if action_mode == "physical_o1_helper_chain":
        decision = "helper_found"
        relation = "reach_extension" if helper_type == "long_rigid" else "aggregate_transport"
    elif action_mode == "wrong_helper_use":
        decision, relation = "helper_found", "none"
    elif action_mode == "continue_search":
        decision, relation = "continue_search", "none"
    elif action_mode in {"embodiment_batching", "direct_multi_trip", "direct_single"}:
        decision, relation = "direct_is_enough", "none"
    else:
        decision = "unclear"
        relation = "none" if not helper_mentioned else "unclear"

    row.update(
        {
            "uses_physical_o1_helper": uses_physical,
            "physical_helper_type": helper_type if helper_mentioned else "none",
            "uses_embodiment_batching": "yes" if embodiment else "no",
            "uses_direct_multi_trip": "yes" if direct_multi else "no",
            "uses_wrong_o1_object": uses_wrong,
            "mentions_o0_memory": "yes" if mentions_o0 else "no",
            "mentions_o1_observation": "yes" if mentions_o1 else "no",
            "links_o1_helper_to_o0_target": links,
            "action_mode_pred": action_mode,
            "inferred_helper_mentioned": "yes" if helper_mentioned or wrong_mentioned else "no",
            "inferred_valid_helper_action_chain": "yes" if physical_chain and link else "no",
            "inferred_searches_helper": "yes" if searches else "no",
            "inferred_selected_helper": helper_type if helper_mentioned else "",
            "decision_pred": decision,
            "relation_pred": relation,
        }
    )
    row["pass_fail"], row["failure_reason"] = judge_prediction_v2(
        raw, row, rejects=rejects, searches=searches
    )
    return row


def judge_prediction_v2(
    raw: dict[str, Any], row: dict[str, Any], *, rejects: bool, searches: bool
) -> tuple[str, str]:
    sample_type = str(raw.get("sample_type", ""))
    task_id = str(raw.get("old_task_id_source", ""))
    if sample_type == "same_o1_different_o0":
        if task_id == "task_002":
            sample_type = "positive_aggregate"
        elif task_id == "task_011":
            sample_type = "no_tool_control"
        elif task_id == "task_008":
            if row["decision_pred"] == "continue_search" and row["uses_physical_o1_helper"] != "yes":
                return "pass", "The current O1 container is rejected or search continues for the remembered reach task."
            if row["uses_physical_o1_helper"] == "yes":
                return "fail", "The shared O1 container is incorrectly used for the remembered reach target."
            return "needs_review", "The response neither clearly rejects the shared O1 container nor continues searching."

    if sample_type == "positive_aggregate":
        if (
            row["decision_pred"] == "helper_found"
            and row["relation_pred"] == "aggregate_transport"
            and row["uses_physical_o1_helper"] == "yes"
            and row["links_o1_helper_to_o0_target"] == "yes"
        ):
            return "pass", "Physical O1 container helper is linked to the remembered aggregate-transport target."
        if row["action_mode_pred"] == "embodiment_batching":
            return "fail", "Embodiment batching is not a physical O1 helper chain."
        if row["action_mode_pred"] == "direct_multi_trip":
            return "fail", "Direct multi-trip transport is not a physical O1 helper chain."
        return "fail", "No explicit physical O1 container-to-O0 aggregate action chain."

    if sample_type == "positive_reach":
        if (
            row["uses_physical_o1_helper"] == "yes"
            and row["physical_helper_type"] == "long_rigid"
            and row["relation_pred"] == "reach_extension"
            and row["links_o1_helper_to_o0_target"] == "yes"
        ):
            return "pass", "Physical long-rigid O1 helper is linked to the remembered reach target."
        return "fail", "No explicit long-rigid O1 helper chain reaches, pulls, pushes, or sweeps out the remembered target."

    if sample_type == "wrong_helper_negative":
        if row["uses_wrong_o1_object"] == "yes" or row["action_mode_pred"] == "wrong_helper_use":
            return "fail", "The unsuitable O1 object is used as a helper."
        if rejects or searches or row["decision_pred"] == "continue_search":
            return "pass", "The unsuitable O1 object is rejected or the plan continues searching."
        return "needs_review", "The wrong O1 object is not used, but it is not explicitly rejected and search does not continue."

    if sample_type == "no_tool_control":
        if row["uses_physical_o1_helper"] == "yes":
            return "fail", "A physical O1 helper is overused for a directly executable task."
        if row["decision_pred"] == "direct_is_enough" and row["action_mode_pred"] == "direct_single":
            return "pass", "The original single target is handled directly without O1 helper overuse."
        return "needs_review", "Direct execution is not explicit or the response continues checking unnecessarily."
    return "needs_review", f"Unsupported v2 sample type: {sample_type}"


def annotate_group_consistency_v2(rows: list[dict[str, Any]]) -> None:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("sample_type") == "same_o1_different_o0" and row.get("group_id"):
            grouped[(str(row["model_id"]), str(row["prompt_id"]), str(row["group_id"]))].append(row)
    for group_rows in grouped.values():
        if len(group_rows) != 3 or any(row.get("response_status") != "ok_eval" for row in group_rows):
            result = "not_available"
        else:
            by_task = {str(row["old_task_id_source"]): row for row in group_rows}
            aggregate = by_task.get("task_002", {})
            direct = by_task.get("task_011", {})
            reach = by_task.get("task_008", {})
            consistent = (
                aggregate.get("pass_fail") == "pass"
                and aggregate.get("action_mode_pred") == "physical_o1_helper_chain"
                and direct.get("pass_fail") == "pass"
                and direct.get("uses_physical_o1_helper") != "yes"
                and reach.get("pass_fail") == "pass"
                and reach.get("decision_pred") == "continue_search"
            )
            result = "pass" if consistent else "fail"
        for row in group_rows:
            row["same_o1_different_o0_consistency"] = result


def detect_physical_helper_type_v2(text: str) -> tuple[str, list[str]]:
    for helper_type, terms in V2_CONTAINER_TERMS.items():
        matched = [term for term in terms if v2_contains_phrase(text, term)]
        if matched:
            return helper_type, matched
    if v2_contains_any(text, V2_GENERIC_CONTAINER_TERMS):
        return "tray", [term for term in V2_GENERIC_CONTAINER_TERMS if v2_contains_phrase(text, term)]
    matched_long = [term for term in V2_LONG_RIGID_TERMS if v2_contains_phrase(text, term)]
    if matched_long:
        return "long_rigid", matched_long
    matched_wrong = [term for term in V2_WRONG_OBJECT_TERMS if v2_contains_phrase(text, term)]
    if matched_wrong:
        return "wrong_object", matched_wrong
    if v2_bag_short_form(text):
        return "bag", ["包"]
    return "none", []


def v2_bag_short_form(text: str) -> bool:
    return any(pattern in text for pattern in ["用包", "使用包", "放入包", "放进包", "装入包", "装进包"])


def v2_contains_phrase(text: str, term: str) -> bool:
    lowered = text.lower()
    needle = term.lower()
    if needle.isascii() and any(char.isalnum() for char in needle):
        return re.search(r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])", lowered) is not None
    return needle in lowered


def v2_contains_any(text: str, terms: list[str]) -> bool:
    return any(v2_contains_phrase(text, term) for term in terms)


def v2_plan_steps(parsed: dict[str, Any]) -> list[str]:
    steps = [str(step).lower() for step in parsed.get("plan", []) if str(step).strip()]
    steps.extend(str(step).lower() for step in parsed.get("tool_use_action_chain", []) if str(step).strip())
    return steps


def v2_step_has_terms_and_action(step: str, terms: list[str], actions: list[str]) -> bool:
    return v2_contains_any(step, terms) and v2_contains_any(step, actions) and not _has_negated_v2_use(step, terms)


def _has_negated_v2_use(step: str, terms: list[str]) -> bool:
    negations = ["不使用", "不用", "不适合", "忽略", "不要用", "not use", "do not use", "unsuitable"]
    return v2_contains_any(step, terms) and v2_contains_any(step, negations)


def v2_row_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return (str(row.get("sample_id", "")), str(row.get("model_id", "")), str(row.get("prompt_id", "")))


def write_summary_v2(path: Path, rows: list[dict[str, Any]]) -> None:
    response = Counter(str(row["response_status"]) for row in rows)
    modes = Counter(str(row["action_mode_pred"]) for row in rows)
    no_tool_overuse = sum(
        row["sample_type"] == "no_tool_control" and row["uses_physical_o1_helper"] == "yes" for row in rows
    )
    lines = [
        "# Sequential O0/O1 Offline Analysis V2", "",
        f"- evaluator version: {EVALUATOR_VERSION_V2}", f"- total raw rows: {len(rows)}",
        f"- ok_eval: {response['ok_eval']}",
        f"- generation_budget_exhausted: {response['generation_budget_exhausted']}",
        f"- schema_echo: {response['schema_echo']}",
        f"- parse_error_nonempty: {response['parse_error_nonempty']}",
        f"- provider_error: {response['provider_error']}", "",
        "V2 distinguishes physical O1 helper use from embodiment batching and direct multi-trip behavior.", "",
        "## By Model", "", *v2_status_table(rows, "model_id"), "", "## By Protocol", "",
        *v2_status_table(rows, "protocol"), "", "## By Sample Type", "", *v2_status_table(rows, "sample_type"),
        "", "## Physical O1 Helper Chain Success", "",
        *v2_physical_success_table(rows, "model_id"), "", *v2_physical_success_table(rows, "protocol"),
        "", *v2_physical_success_table(rows, "sample_type"), "", "## Action Mode Counts", "",
        f"- embodiment_batching: {modes['embodiment_batching']}",
        f"- direct_multi_trip: {modes['direct_multi_trip']}",
        f"- wrong_helper_use: {modes['wrong_helper_use']}",
        f"- physical_o1_helper_chain: {modes['physical_o1_helper_chain']}",
        f"- no_tool_overuse: {no_tool_overuse}", "", "## Same O1 Different O0 Consistency", "",
        "| model | prompt | group | consistency |", "| --- | --- | --- | --- |",
    ]
    groups: dict[tuple[str, str, str], str] = {}
    for row in rows:
        if row["sample_type"] == "same_o1_different_o0":
            groups[(str(row["model_id"]), str(row["prompt_id"]), str(row["group_id"]))] = str(
                row["same_o1_different_o0_consistency"]
            )
    if groups:
        lines.extend(f"| {m} | {p} | {g} | {value} |" for (m, p, g), value in sorted(groups.items()))
    else:
        lines.append("| - | - | - | not_available |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def v2_status_table(rows: list[dict[str, Any]], key: str) -> list[str]:
    grouped: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        grouped[str(row.get(key, ""))][str(row["pass_fail"])] += 1
    output = [
        f"| {key} | pass | fail | needs_review | parse_error | not_evaluated |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    output.extend(
        f"| {name} | {count['pass']} | {count['fail']} | {count['needs_review']} | "
        f"{count['parse_error']} | {count['not_evaluated']} |"
        for name, count in sorted(grouped.items())
    )
    return output


def v2_physical_success_table(rows: list[dict[str, Any]], key: str) -> list[str]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, ""))].append(row)
    output = [f"| {key} | physical chains | passing chains |", "| --- | ---: | ---: |"]
    for name, subset in sorted(grouped.items()):
        chains = [row for row in subset if row["action_mode_pred"] == "physical_o1_helper_chain"]
        output.append(f"| {name} | {len(chains)} | {sum(row['pass_fail'] == 'pass' for row in chains)} |")
    return output


def write_aggregate_metrics_v2(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "group_by", "group_value", "total", "ok_eval", "pass", "fail", "needs_review", "parse_error",
        "not_evaluated", "physical_chain_success", "embodiment_batching", "direct_multi_trip",
        "wrong_helper_use", "no_tool_overuse",
    ]
    metrics: list[dict[str, Any]] = []
    for group_by in ("model_id", "protocol", "sample_type"):
        values: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in rows:
            values[str(row.get(group_by, ""))].append(row)
        for value, subset in sorted(values.items()):
            status = Counter(str(row["pass_fail"]) for row in subset)
            metrics.append(
                {
                    "group_by": group_by,
                    "group_value": value,
                    "total": len(subset),
                    "ok_eval": sum(row["response_status"] == "ok_eval" for row in subset),
                    "pass": status["pass"], "fail": status["fail"],
                    "needs_review": status["needs_review"], "parse_error": status["parse_error"],
                    "not_evaluated": status["not_evaluated"],
                    "physical_chain_success": sum(
                        row["action_mode_pred"] == "physical_o1_helper_chain" and row["pass_fail"] == "pass"
                        for row in subset
                    ),
                    "embodiment_batching": sum(row["action_mode_pred"] == "embodiment_batching" for row in subset),
                    "direct_multi_trip": sum(row["action_mode_pred"] == "direct_multi_trip" for row in subset),
                    "wrong_helper_use": sum(row["action_mode_pred"] == "wrong_helper_use" for row in subset),
                    "no_tool_overuse": sum(
                        row["sample_type"] == "no_tool_control" and row["uses_physical_o1_helper"] == "yes"
                        for row in subset
                    ),
                }
            )
    write_csv(path, metrics, fields)


def write_failed_cases_v2(
    path: Path,
    rows: list[dict[str, Any]],
    parsed_by_key: dict[tuple[str, str, str], dict[str, Any]],
) -> None:
    lines = [
        "# Sequential V2 Failed and Review Cases", "",
        "V2 is an offline heuristic analysis; review cases manually before research claims.", "",
    ]
    for row in rows:
        if row["pass_fail"] == "pass":
            continue
        plan = v2_plan_text(parsed_by_key.get(v2_row_key(row), {}))
        lines.append(
            f"- {row['sample_id']} / {row['model_id']} / {row['prompt_id']}: {row['pass_fail']}; "
            f"mode={row['action_mode_pred']}; helper={row['physical_helper_type']}; "
            f"reason={row['failure_reason']}; plan={plan}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def select_manual_review_rows_v2(
    rows: list[dict[str, Any]],
    parsed_by_key: dict[tuple[str, str, str], dict[str, Any]],
) -> list[dict[str, Any]]:
    selected: dict[tuple[str, str, str], dict[str, Any]] = {}
    reasons: dict[tuple[str, str, str], list[str]] = defaultdict(list)

    def add(row: dict[str, Any], reason: str) -> None:
        key = v2_row_key(row)
        selected[key] = row
        if reason not in reasons[key]:
            reasons[key].append(reason)

    for row in rows:
        parsed_text = v2_plan_text(parsed_by_key.get(v2_row_key(row), {})).lower()
        if row["v1_pass_fail"] == "fail" and row["pass_fail"] == "pass":
            add(row, "priority_1_v1_fail_v2_pass")
        if row["v1_pass_fail"] == "pass" and row["pass_fail"] == "fail":
            add(row, "priority_2_v1_pass_v2_fail")
        if row["sample_type"] == "positive_aggregate" and v2_contains_any(
            parsed_text, ["烤盘", "baking tray", "pan", "tray"]
        ):
            add(row, "priority_3_positive_aggregate_tray_or_pan")
        if row["sample_type"] == "positive_reach" and row["pass_fail"] != "pass":
            add(row, "priority_4_positive_reach_failure")
        if row["sample_type"] == "same_o1_different_o0":
            add(row, "priority_5_same_o1_all")
        if row["sample_type"] == "wrong_helper_negative" and row["pass_fail"] in {"fail", "needs_review"}:
            add(row, "priority_6_wrong_helper_fail_or_review")
        if row["model_id"] == "ollama_qwen3_5_35b" and row["sample_type"] == "same_o1_different_o0":
            add(row, "priority_7_qwen35_same_o1")
        if row["model_id"] == "ollama_qwen3_5_35b" and row["sample_type"] in {
            "positive_aggregate", "positive_reach"
        }:
            add(row, "priority_8_qwen35_positive")
    output: list[dict[str, Any]] = []
    for key, row in selected.items():
        copied = dict(row)
        copied["review_reasons"] = reasons[key]
        output.append(copied)
    return sorted(output, key=lambda row: (min(row["review_reasons"]), row["sample_id"], row["model_id"], row["prompt_id"]))


def copy_review_images_v2(
    rows: list[dict[str, Any]],
    raw_by_key: dict[tuple[str, str, str], dict[str, Any]],
    root: Path,
    experiment_name: str,
) -> dict[str, tuple[str, str]]:
    destination = root / experiment_name
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)
    copied: dict[str, tuple[str, str]] = {}
    for row in rows:
        sample_id = str(row["sample_id"])
        if sample_id in copied:
            continue
        raw = raw_by_key[v2_row_key(row)]
        outputs: list[str] = []
        for stage in ("o0", "o1"):
            source = resolve_benchmark_path_v2(str(raw[f"{stage}_image_path"]))
            suffix = source.suffix.lower() or ".jpg"
            spec_id = str(raw.get(f"{stage}_spec_id", stage))
            target = destination / f"{sample_id}__{stage.upper()}__{spec_id}{suffix}"
            shutil.copy2(source, target)
            outputs.append(str(target))
        copied[sample_id] = (outputs[0], outputs[1])
    return copied


def resolve_benchmark_path_v2(value: str) -> Path:
    path = Path(value)
    resolved = path if path.is_absolute() else (BENCHMARK_ROOT / path).resolve()
    if not resolved.is_file():
        raise FileNotFoundError(f"Review image does not exist: {resolved}")
    return resolved


def write_manual_review_pack_v2(
    path: Path,
    rows: list[dict[str, Any]],
    parsed_by_key: dict[tuple[str, str, str], dict[str, Any]],
    copied_images: dict[str, tuple[str, str]],
) -> None:
    lines = [
        "# Sequential V2 Manual Review Pack", "",
        "Cases are ordered by the requested review priorities. All experiment sample images are copied once per sample.", "",
    ]
    if not rows:
        lines.append("No review cases selected.")
    for row in rows:
        plan = v2_plan_text(parsed_by_key.get(v2_row_key(row), {}))
        images = copied_images.get(str(row["sample_id"]))
        lines.extend(
            [
                f"## {row['sample_id']} | {row['model_id']} | {row['prompt_id']}", "",
                f"- review reasons: {', '.join(row['review_reasons'])}",
                f"- protocol: {row['protocol']}", f"- pass_fail: {row['pass_fail']}",
                f"- action_mode_pred: {row['action_mode_pred']}",
                f"- physical_helper_type: {row['physical_helper_type']}",
                f"- decision_pred: {row['decision_pred']}", f"- relation_pred: {row['relation_pred']}",
                f"- failure_reason: {row['failure_reason']}",
            ]
        )
        if images:
            lines.extend([f"- copied O0 image: `{images[0]}`", f"- copied O1 image: `{images[1]}`"])
        lines.extend(["", "Plan:", "", plan or "(no parsed plan)", ""])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def v2_plan_text(parsed_row: dict[str, Any]) -> str:
    parsed = parsed_row.get("parsed", {}) if isinstance(parsed_row, dict) else {}
    if not isinstance(parsed, dict):
        return ""
    return "; ".join(str(step) for step in parsed.get("plan", []))
