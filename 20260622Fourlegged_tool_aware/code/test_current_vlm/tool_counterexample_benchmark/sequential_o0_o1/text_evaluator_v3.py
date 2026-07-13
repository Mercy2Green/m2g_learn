from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from src.load_config import load_yaml
from src.response_parser import parse_model_response

ROOT = Path(__file__).resolve().parents[1]
VERSION = "sequential_text_evaluator_v3"
EVIDENCE_FIELDS = ("task_understanding", "plan", "tool_use_action_chain", "selected_helper", "helper_needed", "uncertainty_or_missing_information", "reason")


def _texts(parsed: dict[str, Any]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for field in EVIDENCE_FIELDS:
        value = parsed.get(field, "")
        out[field] = [str(x).strip().lower() for x in value] if isinstance(value, list) else ([str(value).strip().lower()] if value else [])
    return out


def _hits(fields: dict[str, list[str]], terms: list[str], selected: tuple[str, ...] | None = None) -> list[dict[str, str]]:
    spans = []
    for field in selected or tuple(fields):
        for text in fields.get(field, []):
            if any(term.lower() in text for term in terms):
                spans.append({"field": field, "text": text})
    return spans


def protocol_validity(model: str, protocol: str, config: dict[str, Any]) -> dict[str, str]:
    default = config.get("default", {"validity": "requires_ingestion_diagnostic"})
    return dict(config.get("models", {}).get(model, {}).get(protocol, default))


def evaluate_raw(raw: dict[str, Any], evaluator_cfg: dict[str, Any], validity_cfg: dict[str, Any], audit: dict[str, Any] | None = None) -> dict[str, Any]:
    base = {key: raw.get(key, "") for key in ("sample_id", "sample_type", "group_id", "protocol", "prompt_id", "prompt_category", "model_id", "old_task_id_source", "instruction", "o0_spec_id", "o1_spec_id")}
    base["evaluator_version"] = VERSION
    pv = protocol_validity(str(raw.get("model_id", "")), str(raw.get("protocol", "")), validity_cfg)
    validity = str(pv.get("validity", "requires_ingestion_diagnostic"))
    sample_type = str(raw.get("sample_type", ""))
    if sample_type == "positive_reach" or (sample_type == "same_o1_different_o0" and str(raw.get("old_task_id_source")) == "task_008"):
        validity = "excluded_untrusted_image"
    result = {**base, "evaluation_validity": validity, "parse_status": "error", "task_state_update": "unclear", "helper_commitment": "none", "helper_role": "none", "selected_helper": "", "uses_physical_o1_helper": "no", "links_o1_helper_to_o0_target": "unclear", "target_set_preserved": "unclear", "action_mode_pred": "unclear", "decision_pred": "unclear", "relation_pred": "unclear", "pass_fail": "needs_review", "failure_type": "", "evidence_spans": []}
    if validity != "valid":
        result.update(pass_fail="excluded", failure_type=validity)
        return result
    final = str(raw.get("raw_response_final", ""))
    if raw.get("error") or not final.strip():
        result.update(parse_status="error", pass_fail="fail", failure_type="empty_or_error_response")
        return result
    parsed_result = parse_model_response(final)
    if parsed_result.get("parse_status") != "ok":
        result.update(failure_type="parse_error", evidence_spans=[{"field": "raw_response_final", "text": final[:300]}])
        return result
    result["parse_status"] = "ok"
    fields = _texts(parsed_result["parsed"])
    cfg = evaluator_cfg
    containers = cfg["container_helpers"]
    wrong = cfg["wrong_objects"]
    conditionals = cfg["conditional_markers"]
    load = cfg["load_actions"]
    transport = cfg["transport_actions"]
    physical_fields = ("plan", "tool_use_action_chain")
    container_spans = _hits(fields, containers)
    wrong_spans = _hits(fields, wrong)
    conditional_spans = _hits(fields, conditionals)
    load_spans = _hits(fields, load, physical_fields)
    transport_spans = _hits(fields, transport, physical_fields)
    selected_text = " ".join(fields["selected_helper"])
    selected = next((t for t in containers + wrong if t.lower() in selected_text), selected_text)
    chain_text = " ".join(sum((fields[f] for f in physical_fields), []))
    helper_in_chain = any(t.lower() in chain_text for t in containers + wrong)
    committed = helper_in_chain and bool(load_spans) and bool(transport_spans) and not conditional_spans
    conditional = bool(container_spans) and bool(conditional_spans)
    mentioned = bool(container_spans or wrong_spans)
    batching = bool(re.search(r"双臂|双手|两[只个]手|每次.{0,8}[两二三四多]瓶|dual.arm|both hands|multiple bottles.*hand", chain_text))
    multi_trip = bool(re.search(r"逐个|一个个|一瓶一瓶|分批|多次往返|one.by.one|multiple trips|repeated trips", chain_text))
    direct = bool(re.search(r"直接(拿|抓|取|搬|运|送|执行)|返回.{0,20}(水瓶|目标|原位置)|directly|return.{0,30}(target|bottle)", chain_text))
    search = bool(re.search(r"寻找|搜索|查找|检查.{0,12}(是否|目标|水瓶)|look for|search|find", chain_text))
    overwrite = bool(re.search(r"(目标|水瓶).{0,12}(移动|消失|不见|不存在)|(moved|disappeared|missing).{0,20}(target|bottle)", " ".join(sum(fields.values(), []))))
    premature = bool(re.search(r"任务(已经|已)完成|已经送达|task (is )?(already )?complete", " ".join(sum(fields.values(), []))))
    contamination = bool(re.search(r"(手机|phone).{0,16}(一起|也|加入|搬|运|送|目标)|(目标|objects?).{0,20}(手机|phone)", chain_text))
    pencil_bookkeeping = bool(re.search(r"(铅笔|pencil).{0,20}(标记|记录|计数|完成)|(标记|记录|计数).{0,20}(铅笔|pencil)", chain_text))
    wrong_physical = bool(wrong_spans) and helper_in_chain and not pencil_bookkeeping
    if premature: state = "premature_complete"
    elif contamination: state = "contaminated"
    elif overwrite or (search and sample_type in {"no_tool_control", "same_o1_different_o0"}): state = "overwritten"
    else: state = "preserved"
    if committed: commitment = "committed"
    elif conditional: commitment = "conditional"
    elif mentioned: commitment = "mentioned_only"
    else: commitment = "none"
    role = "incidental_bookkeeping" if pencil_bookkeeping else ("task_helper" if (committed or wrong_physical) else ("irrelevant" if mentioned else "none"))
    if premature: mode = "premature_task_completion"
    elif contamination: mode = "target_set_contamination"
    elif state == "overwritten": mode = "o1_target_overwrite"
    elif wrong_physical: mode = "wrong_helper_use"
    elif committed: mode = "physical_o1_helper_chain"
    elif conditional: mode = "conditional_helper_only"
    elif mentioned: mode = "helper_mention_without_chain"
    elif batching: mode = "embodiment_batching"
    elif multi_trip: mode = "direct_multi_trip"
    elif search: mode = "continue_search"
    elif direct or sample_type in {"no_tool_control", "wrong_helper_negative"}: mode = "direct_single"
    else: mode = "unclear"
    result.update(task_state_update=state, helper_commitment=commitment, helper_role=role, selected_helper=selected, uses_physical_o1_helper="yes" if committed or wrong_physical else "no", links_o1_helper_to_o0_target="yes" if committed else ("no" if mentioned else "unclear"), target_set_preserved="yes" if state == "preserved" else "no", action_mode_pred=mode, evidence_spans=(container_spans + wrong_spans + conditional_spans + load_spans + transport_spans)[:12])
    _judge(result, raw, audit)
    return result


def _judge(row: dict[str, Any], raw: dict[str, Any], audit: dict[str, Any] | None) -> None:
    typ, mode = str(raw.get("sample_type")), row["action_mode_pred"]
    source = str(raw.get("old_task_id_source", ""))
    aggregate = typ == "positive_aggregate" or (typ == "same_o1_different_o0" and source == "task_002")
    direct = typ == "no_tool_control" or (typ == "same_o1_different_o0" and source == "task_011")
    audited_helper = not audit or (audit.get("candidate_helper_present") == "yes" and audit.get("candidate_helper_function") == "container_for_multiple_objects")
    if aggregate:
        ok = mode == "physical_o1_helper_chain" and audited_helper
        row.update(decision_pred="helper_found" if ok else ("continue_search" if mode == "continue_search" else "direct_is_enough"), relation_pred="aggregate_transport" if ok else "none", pass_fail="pass" if ok else "fail", failure_type="" if ok else mode or "helper_ignored")
    elif direct:
        ok = row["task_state_update"] == "preserved" and mode == "direct_single"
        row.update(decision_pred="direct_is_enough" if ok else ("continue_search" if mode in {"continue_search", "o1_target_overwrite"} else "unclear"), relation_pred="none", pass_fail="pass" if ok else "fail", failure_type="" if ok else mode)
    elif typ == "wrong_helper_negative":
        ok = mode not in {"wrong_helper_use", "target_set_contamination", "o1_target_overwrite"} and row["target_set_preserved"] == "yes"
        row.update(decision_pred="continue_search" if mode == "continue_search" else "direct_is_enough", relation_pred="none", pass_fail="pass" if ok else "fail", failure_type="" if ok else mode)
    else:
        row.update(pass_fail="needs_review", failure_type="unknown_sample_type")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    path.mkdir(parents=True, exist_ok=True)
    with (path / "text_evaluation_v3.jsonl").open("w", encoding="utf-8") as f:
        for row in rows: f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    fields = list(rows[0]) if rows else []
    with (path / "text_evaluation_v3.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    counts = Counter(r["pass_fail"] for r in rows)
    (path / "summary_v3.md").write_text(f"# Text Evaluator V3\n\n- rows: {len(rows)}\n- pass: {counts['pass']}\n- fail: {counts['fail']}\n- needs_review: {counts['needs_review']}\n- excluded: {counts['excluded']}\n", encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--input_dir", required=True); p.add_argument("--output_dir"); p.add_argument("--audit_path"); args = p.parse_args()
    input_dir = Path(args.input_dir).resolve(); output = Path(args.output_dir).resolve() if args.output_dir else input_dir / "analysis_text_v3"
    cfg = load_yaml(ROOT / "sequential_o0_o1/configs/evaluator_v3.yaml"); validity = load_yaml(ROOT / "sequential_o0_o1/configs/model_protocol_validity.yaml")
    audits = {str(r.get("image_path")): r for r in read_jsonl(Path(args.audit_path))} if args.audit_path else {}
    rows = [evaluate_raw(r, cfg, validity, audits.get(str(r.get("o1_image_path")))) for r in read_jsonl(input_dir / "raw_responses.jsonl")]
    write_rows(output, rows); print(json.dumps({"rows": len(rows), "output_dir": str(output)}, ensure_ascii=False))


if __name__ == "__main__": main()
