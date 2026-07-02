from __future__ import annotations

import argparse
import base64
import json
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    compact_text,
    normalize_list_field,
    read_csv_dicts,
    read_jsonl,
    safe_load_yaml,
    write_csv_dicts,
    write_jsonl,
)


DEFAULT_INPUT = "analysis_review/round04_strong_tools_v2/all_rows_merged.jsonl"
DEFAULT_OUTPUT_DIR = "analysis_review/round04_strong_tools_vlm_judge_qwen32_smoke"
DEFAULT_JUDGE_MODEL = "qwen3-vl:32b-instruct-q4_K_M"
DEFAULT_OLLAMA_URL = "http://localhost:11434"

SCHEMA_FIELDS = [
    "rereview_label",
    "confidence",
    "task_family",
    "target_objects",
    "target_visible",
    "helper_required",
    "visible_helper_objects",
    "selected_helper",
    "selected_helper_is_target",
    "helper_type_is_appropriate",
    "committed_helper_use",
    "valid_helper_action_chain",
    "conditional_helper_only",
    "direct_operation_when_helper_needed",
    "search_failure_when_helper_not_visible",
    "over_tool_use",
    "failure_modes",
    "evidence_quote",
    "rationale",
]

CSV_FIELDNAMES = [
    "run_id",
    "task_id",
    "task_name",
    "image_name",
    "image_path",
    "image_used",
    "image_missing",
    "model_id",
    "prompt_id",
    "prompt_category",
    "embodiment_profile",
    "auto_pass_fail",
    "rule_rereview_label",
    "vlm_rereview_label",
    "vlm_confidence",
    "task_family",
    "target_objects",
    "target_visible",
    "helper_required",
    "visible_helper_objects",
    "selected_helper",
    "selected_helper_is_target",
    "helper_type_is_appropriate",
    "committed_helper_use",
    "valid_helper_action_chain",
    "conditional_helper_only",
    "direct_operation_when_helper_needed",
    "search_failure_when_helper_not_visible",
    "over_tool_use",
    "failure_modes",
    "evidence_quote",
    "rationale",
    "judge_model",
    "judge_parse_error",
    "judge_raw_response_short",
    "parsed_plan",
    "parsed_reason",
]


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_jsonl = output_dir / "vlm_case_rereview.jsonl"
    if output_jsonl.exists() and not args.overwrite:
        raise SystemExit(f"Output exists: {output_jsonl}. Use --overwrite to replace it.")

    rows = filter_rows(read_jsonl(args.input), args)
    if args.limit:
        rows = rows[: args.limit]

    task_by_id = load_tasks_by_id()
    rule_by_key = load_rule_rows(args.rule_case_rereview)
    results: list[dict[str, Any]] = []
    started_at = time.time()
    if not args.quiet:
        print(
            f"[PROGRESS] starting VLM judge: rows={len(rows)} "
            f"judge_model={args.judge_model} output_dir={output_dir}",
            file=sys.stderr,
            flush=True,
        )
    for index, row in enumerate(rows, start=1):
        result = judge_or_skip_row(row, args, task_by_id, rule_by_key)
        results.append(result)
        if should_print_progress(index, len(rows), args.progress_every, args.quiet):
            print(progress_message(index, len(rows), started_at, row, result), file=sys.stderr, flush=True)

    write_csv_dicts(output_dir / "vlm_case_rereview.csv", results, CSV_FIELDNAMES)
    write_jsonl(output_jsonl, results)
    write_rule_comparison(output_dir / "vlm_rule_comparison.csv", results)
    write_rule_disagreements(output_dir / "vlm_rule_disagreements.md", results)
    write_high_risk(output_dir / "vlm_high_risk_cases_for_human.md", results)
    print(json.dumps({"output_dir": str(output_dir), "rows": len(results), "judge_model": args.judge_model}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Image-aware local Ollama VLM judge rereview for benchmark outputs.")
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output_dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--judge_model", default=DEFAULT_JUDGE_MODEL)
    parser.add_argument("--ollama_url", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--task_ids", nargs="*", default=None)
    parser.add_argument("--model_ids", nargs="*", default=None)
    parser.add_argument("--prompt_ids", nargs="*", default=None)
    parser.add_argument("--rule_case_rereview", default="")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--no_image", action="store_true")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max_retries", type=int, default=2)
    parser.add_argument("--progress_every", type=int, default=1, help="Print progress every N rows. Default: 1.")
    parser.add_argument("--quiet", action="store_true", help="Disable progress messages.")
    return parser.parse_args()


def should_print_progress(index: int, total: int, every: int, quiet: bool) -> bool:
    if quiet:
        return False
    if total == 0:
        return False
    every = max(1, every)
    return index == 1 or index == total or index % every == 0


def format_seconds(seconds: float) -> str:
    seconds = max(0, int(seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def progress_message(
    index: int,
    total: int,
    started_at: float,
    row: dict[str, Any],
    result: dict[str, Any],
) -> str:
    elapsed = time.time() - started_at
    avg = elapsed / index if index else 0.0
    remaining = max(0, total - index) * avg
    percent = (index / total * 100.0) if total else 100.0
    label = result.get("vlm_rereview_label", "")
    image_used = result.get("image_used", "")
    image_missing = result.get("image_missing", "")
    return (
        f"[PROGRESS] {index}/{total} ({percent:.1f}%) "
        f"elapsed={format_seconds(elapsed)} avg={avg:.1f}s/row eta={format_seconds(remaining)} "
        f"task={row.get('task_id', '')} model={row.get('model_id', '')} "
        f"prompt={row.get('prompt_id', '')} label={label} "
        f"image_used={image_used} image_missing={image_missing}"
    )


def filter_rows(rows: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    output = rows
    if args.task_ids:
        allowed = set(args.task_ids)
        output = [row for row in output if str(row.get("task_id", "")) in allowed]
    if args.model_ids:
        allowed = set(args.model_ids)
        output = [row for row in output if str(row.get("model_id", "")) in allowed]
    if args.prompt_ids:
        allowed = set(args.prompt_ids)
        output = [row for row in output if str(row.get("prompt_id", "")) in allowed]
    return output


def load_tasks_by_id() -> dict[str, dict[str, Any]]:
    data = safe_load_yaml(Path("config/tasks.yaml"))
    tasks = data.get("tasks", data if isinstance(data, list) else [])
    if isinstance(tasks, dict):
        tasks = tasks.get("tasks", [])
    return {str(task.get("task_id", "")): task for task in tasks if isinstance(task, dict)}


def load_rule_rows(path: str) -> dict[tuple[str, str, str, str], dict[str, str]]:
    if not path:
        return {}
    rows = read_csv_dicts(path)
    return {rule_key(row): row for row in rows}


def rule_key(row: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(row.get("task_id", "")),
        str(row.get("image_name", "")),
        str(row.get("model_id", "")),
        str(row.get("prompt_id", "")),
    )


def judge_or_skip_row(
    row: dict[str, Any],
    args: argparse.Namespace,
    task_by_id: dict[str, dict[str, Any]],
    rule_by_key: dict[tuple[str, str, str, str], dict[str, str]],
) -> dict[str, Any]:
    rule = rule_by_key.get(rule_key(row), {})
    image_path, image_missing = resolve_image_path(row, task_by_id)
    base = base_result(row, rule, args.judge_model, image_path, image_missing)
    parse_status = str(row.get("parse_status", ""))
    if parse_status != "ok":
        raw = str(row.get("raw_response", ""))
        if looks_parse_recoverable(raw):
            base.update(
                {
                    "vlm_rereview_label": "uncertain",
                    "vlm_confidence": "low",
                    "failure_modes": ["parse_recoverable"],
                    "rationale": "Tested model output was not parsed as JSON, but raw response appears recoverable. Judge was not called.",
                }
            )
        else:
            base.update(
                {
                    "vlm_rereview_label": "parse_error",
                    "vlm_confidence": "high",
                    "failure_modes": ["tested_model_parse_error"],
                    "rationale": "Tested model output parse_status is not ok. Judge was not called.",
                }
            )
        return base

    images: list[str] = []
    image_used = "no"
    if not args.no_image and image_path and Path(image_path).exists():
        images = [image_to_base64(image_path)]
        image_used = "yes"
    base["image_used"] = image_used
    if image_used == "no":
        base["needs_visual_check"] = "yes"

    prompt = build_judge_prompt(row, base)
    try:
        parsed, raw_response = run_judge_with_retries(args, prompt, images)
    except RuntimeError as exc:
        base.update(
            {
                "vlm_rereview_label": "judge_parse_error",
                "vlm_confidence": "low",
                "judge_parse_error": str(exc),
                "judge_raw_response_short": "",
                "failure_modes": ["judge_error"],
                "rationale": str(exc),
            }
        )
        return base

    return merge_judge_output(base, parsed, raw_response, image_used)


def base_result(
    row: dict[str, Any],
    rule: dict[str, str],
    judge_model: str,
    image_path: str,
    image_missing: bool,
) -> dict[str, Any]:
    return {
        "run_id": row.get("run_id", ""),
        "task_id": row.get("task_id", ""),
        "task_name": row.get("task_name", ""),
        "image_name": row.get("image_name", ""),
        "image_path": image_path,
        "image_used": "no",
        "image_missing": "yes" if image_missing else "no",
        "model_id": row.get("model_id", ""),
        "prompt_id": row.get("prompt_id", ""),
        "prompt_category": row.get("prompt_category", ""),
        "embodiment_profile": row.get("embodiment_profile", ""),
        "auto_pass_fail": row.get("auto_pass_fail", ""),
        "rule_rereview_label": rule.get("rereview_label", ""),
        "vlm_rereview_label": "",
        "vlm_confidence": "",
        "task_family": task_family_for(str(row.get("task_id", ""))),
        "target_objects": [],
        "target_visible": "uncertain",
        "helper_required": "uncertain",
        "visible_helper_objects": [],
        "selected_helper": "",
        "selected_helper_is_target": "uncertain",
        "helper_type_is_appropriate": "uncertain",
        "committed_helper_use": "uncertain",
        "valid_helper_action_chain": "uncertain",
        "conditional_helper_only": "uncertain",
        "direct_operation_when_helper_needed": "uncertain",
        "search_failure_when_helper_not_visible": "uncertain",
        "over_tool_use": "uncertain",
        "failure_modes": [],
        "evidence_quote": "",
        "rationale": "",
        "judge_model": judge_model,
        "judge_parse_error": "",
        "judge_raw_response_short": "",
        "parsed_plan": row.get("parsed_plan", ""),
        "parsed_reason": row.get("parsed_reason", ""),
        "raw_response_short": row.get("raw_response_short", ""),
        "needs_visual_check": "yes" if image_missing else "no",
    }


def resolve_image_path(row: dict[str, Any], task_by_id: dict[str, dict[str, Any]]) -> tuple[str, bool]:
    existing = str(row.get("image_path", "") or "")
    if existing and Path(existing).exists():
        return existing, False
    task = task_by_id.get(str(row.get("task_id", "")), {})
    image_dir = str(task.get("image_dir", "") or "")
    image_name = str(row.get("image_name", "") or "")
    if image_dir and image_name:
        candidate = Path(image_dir) / image_name
        if candidate.exists():
            return str(candidate), False
        absolute = Path.cwd() / candidate
        if absolute.exists():
            return str(absolute), False
        return str(candidate), True
    return existing, True


def image_to_base64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode("ascii")


def build_judge_prompt(row: dict[str, Any], base: dict[str, Any]) -> str:
    expected_behavior = row.get("expected_behavior", {})
    if not isinstance(expected_behavior, dict):
        expected_behavior = {}
    content = {
        "task_id": row.get("task_id", ""),
        "task_name": row.get("task_name", ""),
        "instruction": row.get("task_instruction", ""),
        "expected_should_use_tool_or_container": row.get("expected_should_use_tool_or_container", expected_behavior.get("should_use_tool_or_container", "")),
        "expected_tool_or_container_types": row.get("expected_tool_or_container_types", expected_behavior.get("expected_tool_or_container_types", [])),
        "expected_should_search_for_tool_if_not_visible": row.get("expected_should_search_for_tool_if_not_visible", expected_behavior.get("should_search_for_tool_if_not_visible", "")),
        "expected_should_avoid_over_tool_use": row.get("expected_should_avoid_over_tool_use", expected_behavior.get("should_avoid_over_tool_use", "")),
        "target_object_terms": row.get("target_object_terms", expected_behavior.get("target_object_terms", [])),
        "task_family": base["task_family"],
        "tested_model_id": row.get("model_id", ""),
        "prompt_id": row.get("prompt_id", ""),
        "parsed_plan": row.get("parsed_plan", ""),
        "parsed_reason": row.get("parsed_reason", ""),
        "raw_response_short": row.get("raw_response_short", ""),
        "image_status": "image attached" if base.get("image_used") == "yes" else "no image attached",
    }
    return f"""You are an image-aware judge for a robotics VLM planning benchmark.

You are judging the tested model's plan, not solving the task yourself.
Use the image if attached. If image evidence is unclear, use uncertain or medium/low confidence.
Do not reward a plan merely for mentioning helper objects.
A valid helper chain requires committed use in the plan.
The helper must be a non-target object. Do not count target objects as helpers.
Return only one valid JSON object. No markdown, no comments, no code fences.

Task-family rubric:

A. aggregation_transport: task_001, task_004, task_005, task_007, task_010.
Pass requires a non-target appropriate helper, target objects loaded/placed/collected into or onto it, and the helper with targets carried/moved/delivered to destination.
task_001: water bottles are targets. Bag/tray/basket/box can be helper. Direct hand carrying one by one or by hand is fail.
task_004: snacks/drinks/fruit are targets. Tray/box/container/plate can be helper only if clearly used as carrier.
task_005: cups/plates/bowls/dishes are targets. A used plate/盘子 must not count as helper. Tray/basin/basket is valid helper.
task_007: clothes/towels are targets. Direct carrying clothes by hand is not helper chain. Laundry basket/storage basket carried to laundry area is pass.
task_010: fragile objects are targets. Tray/box/padded box is valid if it actually carries/protects them.

B. helper_search: task_002.
Pass requires explicit nearby search/check for bag/tray/box/basket/container if no suitable container is visible, then using it to aggregate and transport bottles. Fail if no helper visible so direct/batched carry, or only conditional helper mention.

C. reach_extension: task_008.
Pass requires rod/stick/broom/mop/long object used to pull/push/hook/retrieve the remote from under sofa, then pick up remote. Direct arm/gripper reach is fail. Lifting sofa with a tool can be pass only with medium confidence and a safety caveat.

D. cleanup_collection: task_006, task_009.
task_006: Pass if visible basket/box/container/dustpan/broom collects scattered small objects and completes storage/cleanup. Do not automatically count trash can/bin as helper unless task wording or image clearly indicates objects are trash.
task_009: Pass if broom/dustpan/tissue/cloth/rag performs cleaning. Direct hand pickup/wiping without cleaning tool is fail or uncertain.

E. control_no_tool: task_011.
Directly picking up the single bottle and giving it to user is pass. Searching for tray/bag/container for one bottle is over_tool_use fail.

Input row:
{json.dumps(content, ensure_ascii=False, indent=2)}

Output JSON schema:
{{
  "rereview_label": "true_pass | true_fail | uncertain | parse_error",
  "confidence": "high | medium | low",
  "task_family": "aggregation_transport | helper_search | reach_extension | cleanup_collection | control_no_tool | other",
  "target_objects": ["string"],
  "target_visible": "yes | no | uncertain",
  "helper_required": "yes | no | uncertain",
  "visible_helper_objects": ["string"],
  "selected_helper": "string or none",
  "selected_helper_is_target": "yes | no | uncertain",
  "helper_type_is_appropriate": "yes | no | uncertain",
  "committed_helper_use": "yes | no | uncertain",
  "valid_helper_action_chain": "yes | no | uncertain",
  "conditional_helper_only": "yes | no | uncertain",
  "direct_operation_when_helper_needed": "yes | no | uncertain",
  "search_failure_when_helper_not_visible": "yes | no | not_applicable | uncertain",
  "over_tool_use": "yes | no | uncertain",
  "failure_modes": ["string"],
  "evidence_quote": "string",
  "rationale": "string"
}}"""


def run_judge_with_retries(args: argparse.Namespace, prompt: str, images: list[str]) -> tuple[dict[str, Any], str]:
    last_raw = ""
    attempts = max(1, int(args.max_retries) + 1)
    for attempt in range(attempts):
        retry_prompt = prompt
        if attempt:
            retry_prompt += "\n\nYour previous answer was not valid JSON. Return only one valid JSON object following the schema."
        raw = ollama_chat(args.ollama_url, args.judge_model, retry_prompt, images, args.temperature)
        last_raw = raw
        parsed = extract_json(raw)
        if parsed is not None:
            return parsed, raw
        time.sleep(0.5)
    raise RuntimeError(f"Judge JSON parse failed after {attempts} attempts. Last response: {compact_text(last_raw, 500)}")


def ollama_chat(base_url: str, model: str, prompt: str, images: list[str], temperature: float) -> str:
    payload: dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": temperature},
    }
    if images:
        payload["messages"][0]["images"] = images
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code == 404 or "not found" in body.lower() or "pull" in body.lower():
            raise RuntimeError(f"Ollama model '{model}' is not available. Run: ollama pull {model}") from exc
        raise RuntimeError(f"Ollama request failed with HTTP {exc.code}: {body}") from exc
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        raise RuntimeError(f"Could not connect to Ollama at {base_url}. Run: ollama serve") from exc
    if "error" in data:
        error = str(data.get("error", ""))
        if "not found" in error.lower() or "pull" in error.lower():
            raise RuntimeError(f"Ollama model '{model}' is not available. Run: ollama pull {model}")
        raise RuntimeError(f"Ollama error: {error}")
    return str(data.get("message", {}).get("content", ""))


def extract_json(text: str) -> dict[str, Any] | None:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`")
        if stripped.lower().startswith("json"):
            stripped = stripped[4:].strip()
    for candidate in [stripped, between_braces(stripped)]:
        if not candidate:
            continue
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    return None


def between_braces(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return ""
    return text[start : end + 1]


def merge_judge_output(base: dict[str, Any], parsed: dict[str, Any], raw_response: str, image_used: str) -> dict[str, Any]:
    for field in SCHEMA_FIELDS:
        if field in parsed:
            base[field] = parsed[field]
    base["vlm_rereview_label"] = str(parsed.get("rereview_label", "uncertain"))
    base["vlm_confidence"] = str(parsed.get("confidence", "low"))
    if image_used == "no" and base["vlm_confidence"] == "high":
        base["vlm_confidence"] = "medium"
    base["judge_raw_response_short"] = compact_text(raw_response, 800)
    base["judge_parse_error"] = ""
    return base


def task_family_for(task_id: str) -> str:
    if task_id in {"task_001", "task_004", "task_005", "task_007", "task_010"}:
        return "aggregation_transport"
    if task_id == "task_002":
        return "helper_search"
    if task_id == "task_008":
        return "reach_extension"
    if task_id in {"task_006", "task_009"}:
        return "cleanup_collection"
    if task_id == "task_011":
        return "control_no_tool"
    return "other"


def looks_parse_recoverable(raw_text: str) -> bool:
    lowered = raw_text.lower()
    return bool(raw_text.strip()) and any(token in lowered for token in ["plan", "step", "步骤", "计划", "抓取", "移动", "使用", "carry", "move"])


def write_rule_comparison(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "task_id",
        "image_name",
        "model_id",
        "prompt_id",
        "rule_rereview_label",
        "vlm_rereview_label",
        "comparison_type",
        "selected_helper_is_target",
        "conditional_helper_only",
        "committed_helper_use",
        "search_failure_when_helper_not_visible",
        "evidence_quote",
        "rationale",
    ]
    comparison_rows = []
    for row in rows:
        comparison_rows.append(
            {
                **{field: row.get(field, "") for field in fieldnames},
                "comparison_type": comparison_type(row),
            }
        )
    write_csv_dicts(path, comparison_rows, fieldnames)


def comparison_type(row: dict[str, Any]) -> str:
    rule = str(row.get("rule_rereview_label", ""))
    vlm = str(row.get("vlm_rereview_label", ""))
    if rule == "true_pass" and vlm == "true_fail":
        return "rule_pass_vlm_fail"
    if rule == "true_fail" and vlm == "true_pass":
        return "rule_fail_vlm_pass"
    if rule == "uncertain" and vlm in {"true_pass", "true_fail"}:
        return "rule_uncertain_vlm_resolved"
    if rule == "true_pass" and row.get("selected_helper_is_target") == "yes":
        return "rule_pass_vlm_selected_helper_is_target"
    if rule == "true_pass" and row.get("conditional_helper_only") == "yes":
        return "rule_pass_vlm_conditional_helper_only"
    if rule == "true_fail" and row.get("committed_helper_use") == "yes":
        return "rule_fail_vlm_committed_helper_use"
    if row.get("task_id") == "task_002":
        return "task002_search_agreement" if row.get("search_failure_when_helper_not_visible") else "task002_search_review"
    return "consistent_or_other"


def write_rule_disagreements(path: Path, rows: list[dict[str, Any]]) -> None:
    selected = [row for row in rows if comparison_type(row) not in {"consistent_or_other", "task002_search_agreement"}]
    lines = ["# VLM vs Rule Disagreements", ""]
    if not selected:
        lines.append("No high-signal VLM/rule disagreements found.")
    for row in selected:
        lines.append(
            f"- {row.get('task_id')} / {row.get('model_id')} / {row.get('prompt_id')} / {row.get('image_name')}: "
            f"rule={row.get('rule_rereview_label')} vlm={row.get('vlm_rereview_label')} type={comparison_type(row)}. "
            f"Evidence: {row.get('evidence_quote')} Rationale: {row.get('rationale')}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_high_risk(path: Path, rows: list[dict[str, Any]]) -> None:
    selected = [
        row for row in rows
        if row.get("vlm_rereview_label") in {"uncertain", "judge_parse_error"}
        or row.get("image_missing") == "yes"
        or comparison_type(row) in {"rule_pass_vlm_fail", "rule_fail_vlm_pass", "rule_pass_vlm_selected_helper_is_target", "rule_pass_vlm_conditional_helper_only"}
    ]
    lines = ["# VLM High Risk Cases For Human Review", ""]
    if not selected:
        lines.append("No high-risk cases in this subset.")
    for row in selected:
        lines.append(
            f"- {row.get('task_id')} / {row.get('model_id')} / {row.get('prompt_id')}: "
            f"vlm={row.get('vlm_rereview_label')} confidence={row.get('vlm_confidence')} "
            f"image_missing={row.get('image_missing')} comparison={comparison_type(row)}. "
            f"{row.get('rationale')}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
