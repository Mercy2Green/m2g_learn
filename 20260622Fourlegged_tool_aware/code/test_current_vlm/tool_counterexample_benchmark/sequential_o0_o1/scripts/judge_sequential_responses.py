from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
from collections import Counter
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.load_config import load_dotenv  # noqa: E402
from src.providers.ollama_provider import OllamaProvider  # noqa: E402
from src.response_parser import parse_model_response  # noqa: E402


ALLOWED = {
    "judge_decision": {"pass", "fail", "needs_review"},
    "decision_pred": {"helper_found", "direct_is_enough", "continue_search", "unclear"},
    "relation_pred": {"aggregate_transport", "reach_extension", "none", "unclear"},
    "uses_o1_object_for_o0_target": {"yes", "no", "unclear"},
    "uses_wrong_helper": {"yes", "no", "unclear"},
    "overuses_helper": {"yes", "no", "unclear"},
}

SYSTEM_PROMPT = """You are a response-level judge for an O0/O1 sequential robot planning benchmark.
Judge the candidate model response against the supplied task and gold expectation.
O0 shows the original task target. O1 is a later observation. Decide whether the final plan correctly relates the O1 object to the remembered O0 target.
Do not judge image generation quality. Do not rewrite the candidate answer. Return one strict JSON object only, with no markdown or extra text.

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


def main() -> None:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    input_dir = root_path(args.input_dir)
    output_dir = root_path(args.output_dir)
    prepare_output(output_dir, args.overwrite)

    raw_rows = read_jsonl(input_dir / "raw_responses.jsonl")
    parsed_rows = read_jsonl(input_dir / "parsed_results.jsonl")
    eval_rows = read_csv(input_dir / "sequential_evaluation.csv")
    raw_by_key = {row_key(row): row for row in raw_rows}
    parsed_by_key = {row_key(row): row for row in parsed_rows}
    eligible_all = [row for row in eval_rows if row.get("response_status") == "ok_eval"]
    eligible = eligible_all
    if args.limit is not None:
        eligible = eligible[: args.limit]

    provider = OllamaProvider(
        {
            "model_id": f"response_judge_{safe_name(args.judge_model)}",
            "model_name": args.judge_model,
            "provider_label": "ollama_response_judge",
            "base_url": os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434"),
            "temperature": 0.0,
            "max_tokens": args.max_tokens,
            "num_ctx": args.num_ctx,
            "timeout_seconds": args.timeout_seconds,
            "retries": 1,
            "format_json": True,
            "keep_alive": "10m",
        }
    )

    judged: list[dict[str, Any]] = []
    for index, evaluation in enumerate(eligible, start=1):
        key = row_key(evaluation)
        raw = raw_by_key.get(key)
        parsed = parsed_by_key.get(key)
        if raw is None or parsed is None:
            raise ValueError(f"Missing raw/parsed row for evaluation key: {key}")
        judged_row = judge_one(provider, raw, evaluation, args.judge_model)
        judged.append(judged_row)
        if index % max(1, args.progress_every) == 0 or index == len(eligible):
            print(f"judged {index}/{len(eligible)}: {key} status={judged_row['judge_status']}")

    write_jsonl(output_dir / "response_vlm_judge.jsonl", judged)
    (output_dir / "response_vlm_judge_summary.md").write_text(
        build_summary(judged, args.judge_model, len(eval_rows), len(eligible_all), len(eligible)), encoding="utf-8"
    )
    (output_dir / "disagreement_cases.md").write_text(build_disagreements(judged), encoding="utf-8")
    print(f"eligible ok_eval rows: {len(eligible)}")
    print(f"judge output rows: {len(judged)}")
    print(f"Wrote: {output_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Second-pass VLM judge for sequential model responses.")
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--judge_model", default="qwen3-vl:32b-instruct-q4_K_M")
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--max_tokens", type=int, default=1024)
    parser.add_argument("--num_ctx", type=int, default=8192)
    parser.add_argument("--timeout_seconds", type=int, default=420)
    parser.add_argument("--progress_every", type=int, default=5)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def root_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (ROOT / path).resolve()


def prepare_output(path: Path, overwrite: bool) -> None:
    if path == ROOT or ROOT not in path.parents:
        raise SystemExit(f"Output directory must be below benchmark root: {path}")
    if path.exists():
        if not overwrite:
            raise SystemExit(f"Output exists: {path}. Use --overwrite.")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def judge_one(
    provider: OllamaProvider,
    raw: dict[str, Any],
    evaluation: dict[str, str],
    judge_model: str,
) -> dict[str, Any]:
    payload = {
        "sample_id": raw.get("sample_id"),
        "sample_type": raw.get("sample_type"),
        "instruction": raw.get("instruction"),
        "gold_expectation": raw.get("gold"),
        "protocol": raw.get("protocol"),
        "prompt_id": raw.get("prompt_id"),
        "candidate_model": raw.get("model_id"),
        "candidate_final_response": raw.get("raw_response_final"),
    }
    user_prompt = (
        "The two attached images are ordered O0 then O1. Judge this candidate response:\n"
        + json.dumps(payload, ensure_ascii=False, indent=2)
    )
    base = {
        "sample_id": raw.get("sample_id", ""),
        "sample_type": raw.get("sample_type", ""),
        "group_id": raw.get("group_id", ""),
        "protocol": raw.get("protocol", ""),
        "prompt_id": raw.get("prompt_id", ""),
        "model_id": raw.get("model_id", ""),
        "model_name": raw.get("model_name", ""),
        "judge_model": judge_model,
        "judge_non_independent": str(raw.get("model_name", "")) == judge_model,
        "heuristic_pass_fail": evaluation.get("pass_fail", ""),
        "heuristic_decision_pred": evaluation.get("decision_pred", ""),
        "heuristic_relation_pred": evaluation.get("relation_pred", ""),
        "judge_status": "error",
        "judge_error": "",
        "judge_raw_response": "",
        "judge_decision": "needs_review",
        "decision_pred": "unclear",
        "relation_pred": "unclear",
        "uses_o1_object_for_o0_target": "unclear",
        "uses_wrong_helper": "unclear",
        "overuses_helper": "unclear",
        "reason": "",
        "heuristic_judge_agreement": False,
    }
    try:
        result = provider.run_chat_with_retry(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": user_prompt,
                    "images": [str(root_path(raw["o0_image_path"])), str(root_path(raw["o1_image_path"]))],
                },
            ]
        )
        raw_response = str(result.get("raw_response", ""))
        base["judge_raw_response"] = raw_response
        parsed = parse_model_response(raw_response)
        if parsed["parse_status"] != "ok":
            raise ValueError(parsed["parse_error"])
        normalized = validate_judge_fields(parsed["parsed"])
        base.update(normalized)
        base["judge_status"] = "ok"
        base["heuristic_judge_agreement"] = (
            base["heuristic_pass_fail"] == base["judge_decision"]
            and base["heuristic_decision_pred"] == base["decision_pred"]
            and base["heuristic_relation_pred"] == base["relation_pred"]
        )
    except Exception as exc:  # noqa: BLE001
        base["judge_error"] = str(exc)
    return base


def validate_judge_fields(parsed: dict[str, Any]) -> dict[str, str]:
    output: dict[str, str] = {}
    for key, allowed in ALLOWED.items():
        value = str(parsed.get(key, "")).strip().lower()
        if value not in allowed:
            raise ValueError(f"Invalid judge field {key}={value!r}")
        output[key] = value
    reason = str(parsed.get("reason", "")).strip()
    if not reason:
        raise ValueError("Judge reason is empty")
    output["reason"] = reason
    return output


def build_summary(
    rows: list[dict[str, Any]],
    judge_model: str,
    total_rows: int,
    eligible_rows: int,
    selected_rows: int,
) -> str:
    successful = [row for row in rows if row["judge_status"] == "ok"]
    decisions = Counter(row["judge_decision"] for row in successful)
    agreement = sum(bool(row["heuristic_judge_agreement"]) for row in successful)
    non_independent = sum(bool(row["judge_non_independent"]) for row in successful)
    return "\n".join(
        [
            "# Sequential Response VLM Judge Summary", "",
            f"- judge model: {judge_model}", f"- source evaluation rows: {total_rows}",
            f"- eligible ok_eval rows: {eligible_rows}", f"- selected judge rows: {selected_rows}",
            f"- successfully judged rows: {len(successful)}",
            f"- judge errors: {len(rows) - len(successful)}", f"- pass: {decisions['pass']}",
            f"- fail: {decisions['fail']}", f"- needs_review: {decisions['needs_review']}",
            f"- full heuristic agreement: {agreement}",
            f"- heuristic disagreement: {len(successful) - agreement}",
            f"- non-independent judge rows: {non_independent}", "",
            "The response VLM judge is a secondary metric and does not replace the heuristic evaluator.",
            "Rows judged by the same model family/checkpoint are explicitly marked non-independent.",
        ]
    ) + "\n"


def build_disagreements(rows: list[dict[str, Any]]) -> str:
    disagreements = [
        row for row in rows if row["judge_status"] != "ok" or not row["heuristic_judge_agreement"]
    ]
    lines = [
        "# Sequential Heuristic / VLM Judge Disagreements", "",
        "The VLM judge is secondary evidence. Review these cases manually before drawing conclusions.", "",
    ]
    if not disagreements:
        lines.append("No disagreements.")
    for row in disagreements[:50]:
        lines.append(
            f"- {row['sample_id']} / {row['model_id']} / {row['prompt_id']}: "
            f"heuristic={row['heuristic_pass_fail']}/{row['heuristic_decision_pred']}/{row['heuristic_relation_pred']}; "
            f"judge={row['judge_decision']}/{row['decision_pred']}/{row['relation_pred']}; "
            f"status={row['judge_status']}; reason={row['reason'] or row['judge_error']}"
        )
    return "\n".join(lines) + "\n"


def row_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return (str(row.get("sample_id", "")), str(row.get("model_id", "")), str(row.get("prompt_id", "")))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def safe_name(value: str) -> str:
    return "".join(char if char.isalnum() else "_" for char in value)


if __name__ == "__main__":
    main()
