from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
from collections import Counter, defaultdict
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.load_config import load_dotenv  # noqa: E402
from src.providers.ollama_provider import OllamaProvider  # noqa: E402
from src.response_parser import parse_model_response  # noqa: E402


ALLOWED_LEGACY = {
    "judge_decision": {"pass", "fail", "needs_review"},
    "decision_pred": {"helper_found", "direct_is_enough", "continue_search", "unclear"},
    "relation_pred": {"aggregate_transport", "reach_extension", "none", "unclear"},
    "uses_o1_object_for_o0_target": {"yes", "no", "unclear"},
    "uses_wrong_helper": {"yes", "no", "unclear"},
    "overuses_helper": {"yes", "no", "unclear"},
}
ALLOWED_STRICT_V2 = {
    **ALLOWED_LEGACY,
    "judge_version": {"strict_vlm_judge_v2"},
    "action_mode_pred": {
        "physical_o1_helper_chain", "embodiment_batching", "direct_multi_trip", "direct_single",
        "continue_search", "wrong_helper_use", "hallucinated_helper", "unclear",
    },
    "uses_physical_o1_helper": {"yes", "no", "unclear"},
    "physical_helper_type": {
        "tray", "baking_tray", "basket", "box", "bag", "pan", "long_rigid", "wrong_object",
        "none", "unclear",
    },
    "helper_visual_grounding": {"visible_in_o1", "not_visible", "unclear"},
    "target_required_in_o1": {"no"},
    "target_absence_handled_correctly": {"yes", "no", "unclear"},
    "links_o1_helper_to_o0_target": {"yes", "no", "unclear"},
    "uses_embodiment_batching": {"yes", "no", "unclear"},
    "uses_direct_multi_trip": {"yes", "no", "unclear"},
    "hallucinated_helper": {"yes", "no", "unclear"},
    "judge_confidence": {"high", "medium", "low"},
}

SYSTEM_PROMPT_LEGACY = """You are a response-level judge for an O0/O1 sequential robot planning benchmark.
Judge the candidate model response against the supplied task and gold expectation.
O0 contains the original target or original task context. O1 is a later observation and may contain a potential helper.
O1 normally may NOT contain the original target. Do not require the target to appear in O1.
A valid answer may use an object visible in O1 for a target remembered from O0.
Judge whether the candidate explicitly links the O1 object to the O0 target or task.
Do not count robot hands, arms, dual-arm carrying, or repeated manual trips as a physical helper unless the gold explicitly allows embodiment batching.
For aggregate_transport, pass only if the candidate uses a physical O1 helper such as a tray, basket, box, bag, or pan to carry or organize multiple O0 target objects.
For reach_extension, pass only if the candidate uses a physical long-rigid O1 helper such as a broom, stick, rod, pole, hanger, or mop to reach, pull, or push the remembered O0 target.
For wrong-helper negatives, pass if the candidate rejects the O1 object as unsuitable or continues searching.
This VLM judge is secondary evidence and does not replace the heuristic evaluation.
Return one strict JSON object only, with no markdown or extra text.

Required JSON schema:
{
  "judge_decision": "pass/fail/needs_review",
  "decision_pred": "helper_found/direct_is_enough/continue_search/unclear",
  "relation_pred": "aggregate_transport/reach_extension/none/unclear",
  "uses_o1_object_for_o0_target": "yes/no/unclear",
  "uses_wrong_helper": "yes/no/unclear",
  "overuses_helper": "yes/no/unclear",
  "reason": "string"
}"""

SYSTEM_PROMPT_STRICT_V2 = """You are a strict image-aware response-level judge for an O0/O1 sequential robot planning benchmark.

Protocol:
* The two attached images are ordered O0 then O1.
* O0 contains the original target, original scene, or original task context.
* O1 is a later observation after short-range search/panning and may contain a potential helper object.
* O1 normally may NOT contain the original target. Do NOT require the O0 target to appear in O1.
* A valid plan may use a physical helper visible in O1 for a target remembered from O0.

Primary object of judgment:
Judge whether the candidate explicitly forms this task-conditioned cross-observation action chain:
O1 physical helper -> remembered O0 target/task -> valid action relation.

Strict definitions:
1. A physical O1 helper is a real object visible in O1 that changes how the O0 task is executed. Container-like examples for aggregate_transport are tray, baking tray, metal tray, pan, basket, box, bag, and container. Long-rigid examples for reach_extension are broom, stick, rod, pole, hanger, mop, and long rigid object.
2. Robot hands, robot arms, dual-arm carrying, gripper batching, carrying multiple bottles by hand, repeated manual trips, path planning, safety checking, and direct reaching with the robot arm are NOT physical O1 helpers.
3. embodiment_batching means using the robot body, hands, arms, grippers, or dual-arm capability to carry more per trip. It is not a physical O1 helper-chain.
4. direct_multi_trip means carrying objects one by one or in repeated trips without a physical O1 helper. It is not a physical O1 helper-chain.
5. hallucinated_helper means using a helper that is not visible in O1 and not justified by the observations. If visibility is uncertain, set helper_visual_grounding="unclear" and judge_decision="needs_review", not pass.

Task-specific pass rules:
A. positive_aggregate: Pass only if a visible physical O1 container-like helper is used to carry, collect, hold, organize, or transport multiple remembered O0 targets and is linked to that task. Fail for hands/arms/grippers only, multiple trips only, no physical O1 helper, or an invented non-visible helper. Use needs_review when grounding is uncertain.
B. positive_reach: Pass only if a visible physical long-rigid O1 helper is used to reach, pull, push, sweep, or retrieve the remembered O0 target. Extending the robot arm, directly reaching under furniture, or returning/searching without using the visible long-rigid helper fails. Use needs_review when visibility is uncertain.
C. wrong_helper_negative: Pass if the current O1 object is rejected as unsuitable, search continues, or the candidate states that it lacks the required function. Fail if the wrong O1 object is used. Use needs_review if it is neither used nor clearly rejected.
D. no_tool_control: Pass for direct execution without O1 helper overuse. Fail for unnecessary helper use. Use needs_review if unclear.
E. same_o1_different_o0: Judge each row independently from its gold. The same container O1 may be correct for aggregate O0, unnecessary for direct O0, and unsuitable for reach O0. Do not apply one universal decision.

Important:
* Do not penalize a candidate merely because O1 does not show the original O0 target.
* Penalize a claimed helper that cannot be found in O1.
* Do not count hands, arms, or manual trips as helper_found for aggregate_transport.
* Do not count direct robot-arm reaching as reach_extension.
* The supplied v2 heuristic fields are metadata for comparison only. Make your own image-aware judgment from the images and candidate response.
* Use needs_review when visual grounding is uncertain. Return strict JSON only.

Required JSON schema:
{
  "judge_version": "strict_vlm_judge_v2",
  "judge_decision": "pass/fail/needs_review",
  "decision_pred": "helper_found/direct_is_enough/continue_search/unclear",
  "relation_pred": "aggregate_transport/reach_extension/none/unclear",
  "action_mode_pred": "physical_o1_helper_chain/embodiment_batching/direct_multi_trip/direct_single/continue_search/wrong_helper_use/hallucinated_helper/unclear",
  "uses_physical_o1_helper": "yes/no/unclear",
  "physical_helper_type": "tray/baking_tray/basket/box/bag/pan/long_rigid/wrong_object/none/unclear",
  "helper_visual_grounding": "visible_in_o1/not_visible/unclear",
  "uses_o1_object_for_o0_target": "yes/no/unclear",
  "links_o1_helper_to_o0_target": "yes/no/unclear",
  "target_required_in_o1": "no",
  "target_absence_handled_correctly": "yes/no/unclear",
  "uses_embodiment_batching": "yes/no/unclear",
  "uses_direct_multi_trip": "yes/no/unclear",
  "hallucinated_helper": "yes/no/unclear",
  "uses_wrong_helper": "yes/no/unclear",
  "overuses_helper": "yes/no/unclear",
  "judge_confidence": "high/medium/low",
  "evidence_quote": "short quote from candidate response",
  "reason": "brief explanation"
}"""


def main() -> None:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    input_dir = root_path(args.input_dir)
    output_dir = root_path(args.output_dir)
    prepare_output(output_dir, args.overwrite)

    raw_rows = read_jsonl(input_dir / "raw_responses.jsonl")
    parsed_rows = read_jsonl(input_dir / "parsed_results.jsonl")
    eval_rows = read_csv(input_dir / "sequential_evaluation.csv")
    v2_path = input_dir / "analysis_v2" / "sequential_evaluation_v2.csv"
    v2_rows = read_csv(v2_path) if v2_path.is_file() else []
    raw_by_key = {row_key(row): row for row in raw_rows}
    parsed_by_key = {row_key(row): row for row in parsed_rows}
    v2_by_key = {row_key(row): row for row in v2_rows}
    eligible_all = [row for row in eval_rows if row.get("response_status") == "ok_eval"]
    eligible = eligible_all[: args.limit] if args.limit is not None else eligible_all

    provider = OllamaProvider({
        "model_id": f"response_judge_{safe_name(args.judge_model)}",
        "model_name": args.judge_model,
        "provider_label": "ollama_response_judge",
        "base_url": os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434"),
        "temperature": 0.0, "max_tokens": args.max_tokens, "num_ctx": args.num_ctx,
        "timeout_seconds": args.timeout_seconds, "retries": 1, "format_json": True, "keep_alive": "10m",
    })

    judged: list[dict[str, Any]] = []
    for index, evaluation in enumerate(eligible, start=1):
        key = row_key(evaluation)
        raw = raw_by_key.get(key)
        if raw is None or key not in parsed_by_key:
            raise ValueError(f"Missing raw/parsed row for evaluation key: {key}")
        judged_row = judge_one(provider, raw, evaluation, v2_by_key.get(key), args.judge_model, args.judge_version)
        judged.append(judged_row)
        if index % max(1, args.progress_every) == 0 or index == len(eligible):
            print(f"judged {index}/{len(eligible)}: {key} status={judged_row['judge_status']}", flush=True)

    if args.judge_version == "legacy":
        write_legacy_outputs(output_dir, judged, args.judge_model, len(eval_rows), len(eligible_all), len(eligible))
    else:
        annotate_same_o1_consistency(judged)
        write_strict_outputs(
            output_dir, judged, raw_by_key, args.judge_model, len(eval_rows), len(eligible_all), len(eligible),
            bool(v2_rows),
        )
    print(f"eligible ok_eval rows: {len(eligible)}", flush=True)
    print(f"judge output rows: {len(judged)}", flush=True)
    print(f"Wrote: {output_dir}", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Response-level VLM judge for sequential O0/O1 results.")
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--judge_model", default="qwen3-vl:32b-instruct-q4_K_M")
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--judge_version", choices=["strict_v2", "legacy"], default="strict_v2")
    parser.add_argument("--max_tokens", type=int, default=1536)
    parser.add_argument("--num_ctx", type=int, default=8192)
    parser.add_argument("--timeout_seconds", type=int, default=420)
    parser.add_argument("--progress_every", type=int, default=5)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def root_path(value: str | Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def prepare_output(path: Path, overwrite: bool) -> None:
    if not path.name.startswith("response_judge_"):
        raise SystemExit(f"Refusing non-judge output directory: {path}")
    if path.exists():
        if not overwrite:
            raise SystemExit(f"Output exists: {path}. Use --overwrite.")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def judge_one(
    provider: OllamaProvider,
    raw: dict[str, Any],
    evaluation: dict[str, str],
    v2: dict[str, str] | None,
    judge_model: str,
    judge_version: str,
) -> dict[str, Any]:
    v2 = v2 or {}
    v2_metadata = {
        "v2_pass_fail": v2.get("pass_fail", ""),
        "v2_decision_pred": v2.get("decision_pred", ""),
        "v2_relation_pred": v2.get("relation_pred", ""),
        "v2_action_mode_pred": v2.get("action_mode_pred", ""),
        "v2_physical_helper_type": v2.get("physical_helper_type", ""),
        "v2_uses_physical_o1_helper": v2.get("uses_physical_o1_helper", ""),
        "v2_links_o1_helper_to_o0_target": v2.get("links_o1_helper_to_o0_target", ""),
        "v2_failure_reason": v2.get("failure_reason", ""),
    }
    payload = {
        "sample_id": raw.get("sample_id"), "sample_type": raw.get("sample_type"),
        "group_id": raw.get("group_id"), "old_task_id_source": raw.get("old_task_id_source"),
        "instruction": raw.get("instruction"), "gold_expectation": raw.get("gold"),
        "protocol": raw.get("protocol"), "prompt_id": raw.get("prompt_id"),
        "candidate_model": raw.get("model_id"), "candidate_final_response": raw.get("raw_response_final"),
        "o0_spec_id": raw.get("o0_spec_id"), "o1_spec_id": raw.get("o1_spec_id"),
        "o0_image_path": raw.get("o0_image_path"), "o1_image_path": raw.get("o1_image_path"),
        **v2_metadata,
    }
    base: dict[str, Any] = {
        "sample_id": raw.get("sample_id", ""), "sample_type": raw.get("sample_type", ""),
        "group_id": raw.get("group_id", ""), "old_task_id_source": raw.get("old_task_id_source", ""),
        "protocol": raw.get("protocol", ""), "prompt_id": raw.get("prompt_id", ""),
        "model_id": raw.get("model_id", ""), "model_name": raw.get("model_name", ""),
        "judge_model": judge_model, "judge_non_independent": str(raw.get("model_name", "")) == judge_model,
        "o0_spec_id": raw.get("o0_spec_id", ""), "o1_spec_id": raw.get("o1_spec_id", ""),
        "o0_image_path": raw.get("o0_image_path", ""), "o1_image_path": raw.get("o1_image_path", ""),
        "candidate_final_response": raw.get("raw_response_final", ""),
        "heuristic_pass_fail": evaluation.get("pass_fail", ""),
        "heuristic_decision_pred": evaluation.get("decision_pred", ""),
        "heuristic_relation_pred": evaluation.get("relation_pred", ""),
        **v2_metadata, "judge_status": "error", "judge_error": "", "judge_raw_response": "",
        "judge_decision": "needs_review", "decision_pred": "unclear", "relation_pred": "unclear",
        "same_o1_consistency": "not_available", "heuristic_judge_agreement": False,
    }
    if judge_version == "strict_v2":
        base.update(strict_defaults())
    try:
        result = provider.run_chat_with_retry([
            {"role": "system", "content": SYSTEM_PROMPT_STRICT_V2 if judge_version == "strict_v2" else SYSTEM_PROMPT_LEGACY},
            {"role": "user", "content": "Judge the candidate using the ordered O0 and O1 images:\n" + json.dumps(payload, ensure_ascii=False, indent=2),
             "images": [str(root_path(raw["o0_image_path"])), str(root_path(raw["o1_image_path"]))]},
        ])
        base["judge_raw_response"] = str(result.get("raw_response", ""))
        parsed = parse_model_response(base["judge_raw_response"])
        if parsed["parse_status"] != "ok":
            raise ValueError(parsed["parse_error"])
        base.update(validate_judge_fields(parsed["parsed"], judge_version))
        base["judge_status"] = "ok"
        base["heuristic_judge_agreement"] = (
            base["heuristic_pass_fail"] == base["judge_decision"]
            and base["heuristic_decision_pred"] == base["decision_pred"]
            and base["heuristic_relation_pred"] == base["relation_pred"]
        )
    except Exception as exc:  # noqa: BLE001
        base["judge_error"] = str(exc)
    return base


def strict_defaults() -> dict[str, str]:
    return {
        "judge_version": "strict_vlm_judge_v2", "action_mode_pred": "unclear",
        "uses_physical_o1_helper": "unclear", "physical_helper_type": "unclear",
        "helper_visual_grounding": "unclear", "uses_o1_object_for_o0_target": "unclear",
        "links_o1_helper_to_o0_target": "unclear", "target_required_in_o1": "no",
        "target_absence_handled_correctly": "unclear", "uses_embodiment_batching": "unclear",
        "uses_direct_multi_trip": "unclear", "hallucinated_helper": "unclear",
        "uses_wrong_helper": "unclear", "overuses_helper": "unclear", "judge_confidence": "low",
        "evidence_quote": "", "reason": "",
    }


def validate_judge_fields(parsed: dict[str, Any], judge_version: str) -> dict[str, str]:
    allowed_fields = ALLOWED_STRICT_V2 if judge_version == "strict_v2" else ALLOWED_LEGACY
    output: dict[str, str] = {}
    for key, allowed in allowed_fields.items():
        value = str(parsed.get(key, "")).strip().lower()
        if value not in allowed:
            raise ValueError(f"Invalid judge field {key}={value!r}")
        output[key] = value
    for key in (["reason", "evidence_quote"] if judge_version == "strict_v2" else ["reason"]):
        value = str(parsed.get(key, "")).strip()
        if not value:
            raise ValueError(f"Judge {key} is empty")
        output[key] = value
    return output


def write_legacy_outputs(path: Path, rows: list[dict[str, Any]], model: str, total: int, eligible: int, selected: int) -> None:
    write_jsonl(path / "response_vlm_judge.jsonl", rows)
    (path / "response_vlm_judge_summary.md").write_text(
        build_legacy_summary(rows, model, total, eligible, selected), encoding="utf-8"
    )
    (path / "disagreement_cases.md").write_text(build_legacy_disagreements(rows), encoding="utf-8")


def write_strict_outputs(
    path: Path, rows: list[dict[str, Any]], raw_by_key: dict[tuple[str, str, str], dict[str, Any]],
    model: str, total: int, eligible: int, selected: int, has_v2: bool,
) -> None:
    write_jsonl(path / "response_vlm_judge_strict_v2.jsonl", rows)
    summary = build_strict_summary(rows, model, total, eligible, selected)
    (path / "response_vlm_judge_summary_strict_v2.md").write_text(summary, encoding="utf-8")
    (path / "summary_strict_v2.md").write_text(summary, encoding="utf-8")
    crosstab = build_crosstab_rows(rows) if has_v2 else []
    write_csv(path / "vlm_vs_v2_crosstab.csv", crosstab, CROSSTAB_FIELDS)
    (path / "vlm_vs_v2_summary.md").write_text(build_crosstab_summary(crosstab, has_v2), encoding="utf-8")
    (path / "disagreement_cases_strict_v2.md").write_text(build_strict_disagreements(rows), encoding="utf-8")
    (path / "manual_review_pack_vlm_strict_v2.md").write_text(
        build_manual_review(rows, raw_by_key), encoding="utf-8"
    )


def annotate_same_o1_consistency(rows: list[dict[str, Any]]) -> None:
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row["sample_type"] == "same_o1_different_o0" and row["group_id"]:
            groups[(row["model_id"], row["prompt_id"], row["group_id"])].append(row)
    for members in groups.values():
        if len(members) != 3 or any(row["judge_status"] != "ok" for row in members):
            result = "not_available"
        else:
            by_task = {row["old_task_id_source"]: row for row in members}
            aggregate, direct, reach = by_task.get("task_002", {}), by_task.get("task_011", {}), by_task.get("task_008", {})
            result = "pass" if (
                aggregate.get("decision_pred") == "helper_found"
                and aggregate.get("relation_pred") == "aggregate_transport"
                and aggregate.get("action_mode_pred") == "physical_o1_helper_chain"
                and direct.get("decision_pred") == "direct_is_enough"
                and direct.get("relation_pred") == "none"
                and direct.get("uses_physical_o1_helper") == "no"
                and reach.get("decision_pred") == "continue_search"
                and reach.get("relation_pred") == "none"
                and reach.get("uses_physical_o1_helper") != "yes"
            ) else "fail"
        for row in members:
            row["same_o1_consistency"] = result


def build_strict_summary(rows: list[dict[str, Any]], model: str, total: int, eligible: int, selected: int) -> str:
    successful = [row for row in rows if row["judge_status"] == "ok"]
    decisions = Counter(row["judge_decision"] for row in successful)
    resolved = decisions["pass"] + decisions["fail"]
    lines = [
        "# Strict VLM Judge V2 Summary", "", "## Overall", "", f"- judge model: {model}",
        f"- source rows: {total}", f"- eligible ok_eval rows: {eligible}", f"- selected rows: {selected}",
        f"- judged rows: {len(successful)}", f"- judge errors: {len(rows) - len(successful)}",
        f"- pass: {decisions['pass']}", f"- fail: {decisions['fail']}",
        f"- needs_review: {decisions['needs_review']}", f"- pass rate: {rate(decisions['pass'], len(successful))}",
        f"- failure rate: {rate(decisions['fail'], resolved)}", f"- needs_review rate: {rate(decisions['needs_review'], len(successful))}",
        f"- non-independent rows: {sum(bool(row['judge_non_independent']) for row in successful)}", "",
    ]
    for title, key in (("By Model", "model_id"), ("By Protocol", "protocol"), ("By Sample Type", "sample_type")):
        lines.extend([f"## {title}", "", *metric_table(successful, key), ""])
    lines.extend(["## Physical O1 Helper Chain", ""])
    for key in ("model_id", "protocol", "sample_type"):
        lines.extend(physical_chain_table(successful, key) + [""])
    group_values = {
        (row["model_id"], row["prompt_id"], row["group_id"]): row["same_o1_consistency"]
        for row in rows if row["sample_type"] == "same_o1_different_o0"
    }
    counts = Counter(group_values.values())
    available = counts["pass"] + counts["fail"]
    lines.extend([
        "## Same-O1 Consistency", "", f"- groups evaluated: {available}", f"- consistency pass: {counts['pass']}",
        f"- consistency fail: {counts['fail']}", f"- not available: {counts['not_available']}",
        f"- consistency pass rate: {rate(counts['pass'], available)}", "",
        "| model | prompt | group | consistency |", "| --- | --- | --- | --- |",
    ])
    lines.extend(f"| {m} | {p} | {g} | {value} |" for (m, p, g), value in sorted(group_values.items()))
    return "\n".join(lines) + "\n"


def metric_table(rows: list[dict[str, Any]], key: str) -> list[str]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row[key])].append(row)
    lines = [
        f"| {key} | judged | pass | fail | review | pass rate | failure rate | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for name, subset in sorted(grouped.items()):
        decisions = Counter(row["judge_decision"] for row in subset)
        resolved = decisions["pass"] + decisions["fail"]
        values = [
            sum(row["action_mode_pred"] == "physical_o1_helper_chain" for row in subset),
            sum(row["uses_embodiment_batching"] == "yes" for row in subset),
            sum(row["uses_direct_multi_trip"] == "yes" for row in subset),
            sum(row["hallucinated_helper"] == "yes" for row in subset),
        ]
        lines.append(
            f"| {name} | {len(subset)} | {decisions['pass']} | {decisions['fail']} | {decisions['needs_review']} | "
            f"{rate(decisions['pass'], len(subset))} | {rate(decisions['fail'], resolved)} | "
            f"{values[0]} | {rate(values[0], len(subset))} | {values[1]} | {rate(values[1], len(subset))} | "
            f"{values[2]} | {rate(values[2], len(subset))} | {values[3]} | {rate(values[3], len(subset))} |"
        )
    return lines


def physical_chain_table(rows: list[dict[str, Any]], key: str) -> list[str]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row[key])].append(row)
    lines = [f"| {key} | judged | physical chains | rate |", "| --- | ---: | ---: | ---: |"]
    for name, subset in sorted(grouped.items()):
        count = sum(row["action_mode_pred"] == "physical_o1_helper_chain" for row in subset)
        lines.append(f"| {name} | {len(subset)} | {count} | {rate(count, len(subset))} |")
    return lines


CROSSTAB_FIELDS = [
    "group_by", "group_value", "total_comparable", "both_pass", "both_fail", "vlm_pass_v2_fail",
    "v2_pass_vlm_fail", "vlm_pass_v2_needs_review", "v2_pass_vlm_needs_review", "exact_agreement",
    "agreement_rate",
]


def build_crosstab_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    successful = [row for row in rows if row["judge_status"] == "ok" and row["v2_pass_fail"]]
    output: list[dict[str, Any]] = []
    for group_by in ("overall", "model_id", "protocol", "sample_type"):
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in successful:
            grouped["all" if group_by == "overall" else str(row[group_by])].append(row)
        for value, subset in sorted(grouped.items()):
            pairs = Counter((row["judge_decision"], row["v2_pass_fail"]) for row in subset)
            exact = sum(left == right for left, right in (pair for pair in pairs.elements()))
            output.append({
                "group_by": group_by, "group_value": value, "total_comparable": len(subset),
                "both_pass": pairs[("pass", "pass")], "both_fail": pairs[("fail", "fail")],
                "vlm_pass_v2_fail": pairs[("pass", "fail")], "v2_pass_vlm_fail": pairs[("fail", "pass")],
                "vlm_pass_v2_needs_review": pairs[("pass", "needs_review")],
                "v2_pass_vlm_needs_review": pairs[("needs_review", "pass")],
                "exact_agreement": exact, "agreement_rate": rate(exact, len(subset)),
            })
    return output


def build_crosstab_summary(rows: list[dict[str, Any]], has_v2: bool) -> str:
    lines = ["# Strict VLM Judge V2 vs Heuristic V2", ""]
    if not has_v2:
        return "\n".join(lines + ["No analysis_v2/sequential_evaluation_v2.csv was available.", ""])
    lines.extend(["| group by | value | comparable | both pass | both fail | VLM pass / v2 fail | v2 pass / VLM fail | VLM pass / v2 review | v2 pass / VLM review | exact agreement | rate |", "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"])
    for row in rows:
        lines.append("| " + " | ".join(str(row[field]) for field in CROSSTAB_FIELDS) + " |")
    return "\n".join(lines) + "\n"


def build_manual_review(rows: list[dict[str, Any]], raw_by_key: dict[tuple[str, str, str], dict[str, Any]]) -> str:
    selected: dict[tuple[str, str, str], tuple[dict[str, Any], list[str]]] = {}
    for row in rows:
        reasons: list[str] = []
        response = str(row.get("candidate_final_response", "")).lower()
        if row["judge_decision"] == "pass" and row["v2_pass_fail"] == "fail": reasons.append("priority_1_vlm_pass_v2_fail")
        if row["judge_decision"] == "fail" and row["v2_pass_fail"] == "pass": reasons.append("priority_2_v2_pass_vlm_fail")
        if row["sample_type"] == "same_o1_different_o0" and "qwen3_5" in row["model_id"]: reasons.append("priority_3_qwen35_same_o1")
        if row["sample_type"] == "positive_aggregate" and row["action_mode_pred"] == "physical_o1_helper_chain": reasons.append("priority_4_aggregate_physical_chain")
        if row["sample_type"] == "positive_aggregate" and any(term in response for term in ("tray", "pan", "烤盘", "托盘")) and row["judge_decision"] != "pass": reasons.append("priority_5_aggregate_tray_nonpass")
        if row["sample_type"] == "positive_reach": reasons.append("priority_6_reach_low_quality_o1_review")
        if row["sample_type"] == "wrong_helper_negative" and row["judge_decision"] != "pass": reasons.append("priority_7_wrong_helper_nonpass")
        if row["hallucinated_helper"] == "yes": reasons.append("priority_8_hallucinated_helper")
        if row["action_mode_pred"] == "embodiment_batching" or row["uses_embodiment_batching"] == "yes": reasons.append("priority_9_embodiment_batching")
        if reasons:
            selected[row_key(row)] = (row, reasons)
    ordered = sorted(selected.values(), key=lambda item: (min(item[1]), item[0]["sample_id"], item[0]["model_id"], item[0]["prompt_id"]))
    lines = ["# Strict VLM Judge V2 Manual Review Pack", "", "Positive-reach cases should be interpreted with care because the current reach O1 image may be low quality.", ""]
    for row, reasons in ordered:
        raw = raw_by_key.get(row_key(row), {})
        lines.extend([
            f"## {row['sample_id']} | {row['model_id']} | {row['prompt_id']}", "",
            f"- priorities: {', '.join(reasons)}", f"- sample_type: {row['sample_type']}",
            f"- protocol: {row['protocol']}", f"- judge_decision: {row['judge_decision']}",
            f"- decision_pred: {row['decision_pred']}", f"- relation_pred: {row['relation_pred']}",
            f"- action_mode_pred: {row['action_mode_pred']}", f"- physical_helper_type: {row['physical_helper_type']}",
            f"- helper_visual_grounding: {row['helper_visual_grounding']}", f"- hallucinated_helper: {row['hallucinated_helper']}",
            f"- v2 heuristic: {row['v2_pass_fail']} / {row['v2_decision_pred']} / {row['v2_relation_pred']} / {row['v2_action_mode_pred']}",
            f"- v2 failure reason: {row['v2_failure_reason']}", f"- O0 image: `{raw.get('o0_image_path', '')}`",
            f"- O1 image: `{raw.get('o1_image_path', '')}`", f"- evidence quote: {row['evidence_quote']}",
            f"- judge reason: {row['reason']}", "", "Candidate response:", "", excerpt(str(raw.get("raw_response_final", "")), 1600), "",
        ])
    return "\n".join(lines) + "\n"


def build_strict_disagreements(rows: list[dict[str, Any]]) -> str:
    subset = [row for row in rows if row["judge_status"] != "ok" or (row["v2_pass_fail"] and row["judge_decision"] != row["v2_pass_fail"])]
    lines = ["# Strict VLM Judge V2 / Heuristic V2 Disagreements", "", "The VLM judge remains secondary evidence.", ""]
    for row in subset:
        lines.append(
            f"- {row['sample_id']} / {row['model_id']} / {row['prompt_id']}: VLM={row['judge_decision']} "
            f"v2={row['v2_pass_fail']}; mode={row.get('action_mode_pred', 'unclear')}; reason={row['reason'] or row['judge_error']}"
        )
    return "\n".join(lines) + "\n"


def build_legacy_summary(rows: list[dict[str, Any]], judge_model: str, total: int, eligible: int, selected: int) -> str:
    successful = [row for row in rows if row["judge_status"] == "ok"]
    decisions = Counter(row["judge_decision"] for row in successful)
    agreement = sum(bool(row["heuristic_judge_agreement"]) for row in successful)
    return "\n".join([
        "# Sequential Response VLM Judge Summary", "", f"- judge model: {judge_model}", f"- source evaluation rows: {total}",
        f"- eligible ok_eval rows: {eligible}", f"- selected judge rows: {selected}", f"- successfully judged rows: {len(successful)}",
        f"- judge errors: {len(rows)-len(successful)}", f"- pass: {decisions['pass']}", f"- fail: {decisions['fail']}",
        f"- needs_review: {decisions['needs_review']}", f"- full heuristic agreement: {agreement}",
        f"- heuristic disagreement: {len(successful)-agreement}", f"- non-independent judge rows: {sum(bool(row['judge_non_independent']) for row in successful)}", "",
        "The response VLM judge is secondary evidence and does not replace the heuristic evaluator.",
    ]) + "\n"


def build_legacy_disagreements(rows: list[dict[str, Any]]) -> str:
    lines = ["# Sequential Heuristic / VLM Judge Disagreements", ""]
    for row in rows:
        if row["judge_status"] != "ok" or not row["heuristic_judge_agreement"]:
            lines.append(f"- {row['sample_id']} / {row['model_id']} / {row['prompt_id']}: heuristic={row['heuristic_pass_fail']}; judge={row['judge_decision']}; reason={row['reason'] or row['judge_error']}")
    return "\n".join(lines) + "\n"


def rate(numerator: int, denominator: int) -> str:
    return f"{numerator / denominator:.3f}" if denominator else "n/a"


def excerpt(value: str, length: int) -> str:
    compact = value.strip()
    return compact if len(compact) <= length else compact[:length] + "..."


def row_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return (str(row.get("sample_id", "")), str(row.get("model_id", "")), str(row.get("prompt_id", "")))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file(): raise FileNotFoundError(path)
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file(): raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8", newline="") as handle: return list(csv.DictReader(handle))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows: handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)


def safe_name(value: str) -> str:
    return "".join(char if char.isalnum() else "_" for char in value)


if __name__ == "__main__":
    main()
