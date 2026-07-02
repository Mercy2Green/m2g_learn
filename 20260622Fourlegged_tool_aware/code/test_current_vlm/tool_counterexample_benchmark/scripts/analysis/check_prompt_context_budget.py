from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import safe_load_yaml  # noqa: E402
from src.prompt_builder import build_prompt  # noqa: E402


CSV_FIELDNAMES = [
    "model_id",
    "model_name",
    "provider",
    "prompt_id",
    "prompt_category",
    "embodiment_profile",
    "task_id",
    "task_name",
    "system_prompt_chars",
    "user_prompt_chars",
    "total_prompt_chars",
    "approx_input_tokens",
    "reserve_generation_tokens",
    "num_ctx",
    "estimated_total_tokens",
    "estimated_headroom",
    "approximate_risk",
    "recommendation",
]


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    models = filter_by_ids(load_items(args.models, "models"), "model_id", args.model_ids)
    prompts = filter_by_ids(load_items(args.prompts, "prompts"), "prompt_id", args.prompt_ids)
    tasks = filter_by_ids(load_items(args.tasks, "tasks"), "task_id", args.task_ids)

    rows = build_rows(models, prompts, tasks)
    write_csv(output_dir / "context_preflight_prompt_budget.csv", rows)
    write_markdown(output_dir / "context_preflight_prompt_budget.md", rows)
    print({"output_dir": str(output_dir), "rows": len(rows), "risk_counts": dict(Counter(row["approximate_risk"] for row in rows))})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preflight approximate prompt/context budget risk without calling any model.")
    parser.add_argument("--models", default="config/models.yaml")
    parser.add_argument("--prompts", default="config/prompt_sets.yaml")
    parser.add_argument("--tasks", default="config/tasks.yaml")
    parser.add_argument("--model_ids", nargs="*", default=None)
    parser.add_argument("--prompt_ids", nargs="*", default=None)
    parser.add_argument("--task_ids", nargs="*", default=None)
    parser.add_argument("--output_dir", default="analysis_review/context_preflight_prompt_budget")
    return parser.parse_args()


def load_items(path: str, key: str) -> list[dict[str, Any]]:
    data = safe_load_yaml(path)
    items = data.get(key, [])
    if not isinstance(items, list):
        raise ValueError(f"{path}: expected `{key}` to be a list.")
    return [item for item in items if isinstance(item, dict)]


def filter_by_ids(items: list[dict[str, Any]], key: str, selected: list[str] | None) -> list[dict[str, Any]]:
    if not selected:
        return items
    allowed = set(selected)
    return [item for item in items if str(item.get(key, "")) in allowed]


def build_rows(models: list[dict[str, Any]], prompts: list[dict[str, Any]], tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for model in models:
        for prompt in prompts:
            for task in tasks:
                system_prompt, user_prompt, _leakage = build_prompt(task, prompt)
                rows.append(row_for(model, prompt, task, system_prompt, user_prompt))
    return rows


def row_for(
    model: dict[str, Any],
    prompt: dict[str, Any],
    task: dict[str, Any],
    system_prompt: str,
    user_prompt: str,
) -> dict[str, Any]:
    system_chars = len(system_prompt)
    user_chars = len(user_prompt)
    total_chars = system_chars + user_chars
    approx_input = math.ceil(total_chars / 2)
    max_tokens = optional_int(model.get("max_tokens"))
    num_ctx = optional_int(model.get("num_ctx"))
    risk = approximate_risk(approx_input, max_tokens, num_ctx)
    estimated_total = "" if max_tokens is None else approx_input + max_tokens
    headroom = "" if max_tokens is None or num_ctx is None else num_ctx - approx_input - max_tokens
    return {
        "model_id": model.get("model_id", ""),
        "model_name": model.get("model_name", ""),
        "provider": model.get("provider", ""),
        "prompt_id": prompt.get("prompt_id", ""),
        "prompt_category": prompt.get("prompt_category", ""),
        "embodiment_profile": prompt.get("embodiment_profile", ""),
        "task_id": task.get("task_id", ""),
        "task_name": task.get("name", ""),
        "system_prompt_chars": system_chars,
        "user_prompt_chars": user_chars,
        "total_prompt_chars": total_chars,
        "approx_input_tokens": approx_input,
        "reserve_generation_tokens": max_tokens if max_tokens is not None else "",
        "num_ctx": num_ctx if num_ctx is not None else "",
        "estimated_total_tokens": estimated_total,
        "estimated_headroom": headroom,
        "approximate_risk": risk,
        "recommendation": recommendation(model, risk),
    }


def optional_int(value: Any) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def approximate_risk(approx_input_tokens: int, max_tokens: int | None, num_ctx: int | None) -> str:
    if max_tokens is None or num_ctx is None:
        return "unknown"
    projected = approx_input_tokens + max_tokens
    if projected > num_ctx:
        return "high"
    if projected > 0.75 * num_ctx:
        return "medium"
    return "low"


def recommendation(model: dict[str, Any], risk: str) -> str:
    model_id = str(model.get("model_id", ""))
    num_ctx = optional_int(model.get("num_ctx"))
    max_tokens = optional_int(model.get("max_tokens"))
    if risk == "low":
        return ""
    if num_ctx == 4096 and max_tokens == 1536:
        return "Consider num_ctx 8192 or max_tokens 1024 before long-prompt VLM runs."
    if model_id in {"ollama_minicpm_v4_5_q8_0", "ollama_llama3_2_vision_11b_instruct_q8_0"}:
        return "Watch closely: this round's 4096 context and 1536 max_tokens leave less room for image tokens."
    if num_ctx is not None and num_ctx < 8192:
        return "Consider increasing num_ctx to 8192 if the model supports it."
    return "Review prompt/image context usage before full run."


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in CSV_FIELDNAMES})


def write_markdown(path: Path, rows: list[dict[str, Any]]) -> None:
    risk_counts = Counter(row["approximate_risk"] for row in rows)
    top = sorted(rows, key=lambda row: sort_key(row), reverse=True)[:20]
    by_model = grouped_stats(rows, "model_id")
    by_prompt = grouped_stats(rows, "prompt_id")
    lines = [
        "# Context Preflight Prompt Budget",
        "",
        "This is a text-only preflight estimate. It does not include image tokens, so actual VLM context use may be higher.",
        "",
        "## Risk Counts",
        "",
        f"- high: {risk_counts.get('high', 0)}",
        f"- medium: {risk_counts.get('medium', 0)}",
        f"- low: {risk_counts.get('low', 0)}",
        f"- unknown: {risk_counts.get('unknown', 0)}",
        "",
        "## Highest Estimated Usage",
        "",
        "| Model | Prompt | Task | Approx input | Max tokens | Num ctx | Estimated total | Headroom | Risk |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in top:
        lines.append(
            f"| {row['model_id']} | {row['prompt_id']} | {row['task_id']} | {row['approx_input_tokens']} | "
            f"{row['reserve_generation_tokens']} | {row['num_ctx']} | {row['estimated_total_tokens']} | "
            f"{row['estimated_headroom']} | {row['approximate_risk']} |"
        )
    lines.extend(["", "## By Model", "", stats_table(by_model), "", "## By Prompt", "", stats_table(by_prompt), ""])
    lines.extend(
        [
            "## Recommendations",
            "",
            "- If a row is already medium/high in this text-only preflight, actual VLM calls are riskier because image tokens are not counted here.",
            "- For the six-model round05 run, prefer `num_ctx >= 8192` where the model supports it.",
            "- Pay particular attention to `ollama_minicpm_v4_5_q8_0` and `ollama_llama3_2_vision_11b_instruct_q8_0` when they use `num_ctx=4096` and `max_tokens=1536`.",
            "- If context risk appears in real run metadata, consider raising `num_ctx`, lowering `max_tokens` to 1024, or both.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def sort_key(row: dict[str, Any]) -> tuple[int, int]:
    risk_order = {"unknown": 0, "low": 1, "medium": 2, "high": 3}
    return (risk_order.get(str(row.get("approximate_risk", "")), 0), int(row.get("estimated_total_tokens") or 0))


def grouped_stats(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, ""))].append(row)
    output = []
    for name, group in sorted(grouped.items()):
        approx_values = [int(row["approx_input_tokens"]) for row in group]
        risks = Counter(row["approximate_risk"] for row in group)
        output.append(
            {
                "name": name,
                "rows": len(group),
                "max_approx_input": max(approx_values) if approx_values else 0,
                "avg_approx_input": round(sum(approx_values) / len(approx_values), 2) if approx_values else 0,
                "high": risks.get("high", 0),
                "medium": risks.get("medium", 0),
                "low": risks.get("low", 0),
                "unknown": risks.get("unknown", 0),
            }
        )
    return output


def stats_table(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| Name | Rows | Avg approx input | Max approx input | High | Medium | Low | Unknown |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['name']} | {row['rows']} | {row['avg_approx_input']} | {row['max_approx_input']} | "
            f"{row['high']} | {row['medium']} | {row['low']} | {row['unknown']} |"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
