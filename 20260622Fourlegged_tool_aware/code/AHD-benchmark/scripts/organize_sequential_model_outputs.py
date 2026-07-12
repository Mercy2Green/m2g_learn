from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


AHD_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPERIMENTS = {
    "core_clean_4models": AHD_ROOT / "outputs/test_o0o1_v2/sequential_o0_o1_core_clean_4models_v2",
    "prompt_sensitivity_3models": AHD_ROOT / "outputs/test_o0o1_v2/sequential_o0_o1_prompt_sensitivity_3models_v2",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize raw sequential candidate-model outputs for review.")
    parser.add_argument("--output_dir", default=str(AHD_ROOT / "outputs/model_outputs_review"))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    output_dir = Path(args.output_dir).resolve()
    prepare_output(output_dir, args.overwrite)

    experiment_summaries: list[tuple[str, int, int]] = []
    for experiment_name, experiment_dir in DEFAULT_EXPERIMENTS.items():
        rows = read_jsonl(experiment_dir / "raw_responses.jsonl")
        build_experiment(output_dir / experiment_name, experiment_name, experiment_dir, rows)
        experiment_summaries.append((experiment_name, len(rows), len({row["model_id"] for row in rows})))
    write_root_index(output_dir, experiment_summaries)
    print(f"Wrote organized model outputs: {output_dir}")


def build_experiment(
    destination: Path,
    experiment_name: str,
    experiment_dir: Path,
    rows: list[dict[str, Any]],
) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["model_id"])].append(row)

    model_links: list[str] = []
    for model_id, model_rows in sorted(grouped.items()):
        model_dir = destination / safe_name(model_id)
        build_model(model_dir, model_id, model_rows)
        model_links.append(f"- [{model_id}](./{model_dir.name}/README.md): {len(model_rows)} outputs")

    sample_counts = Counter(str(row["sample_type"]) for row in rows)
    lines = [
        f"# {experiment_name}", "",
        "Candidate model outputs only. No heuristic or VLM-judge labels are included.", "",
        f"- source: `{experiment_dir / 'raw_responses.jsonl'}`",
        f"- outputs: {len(rows)}", f"- models: {len(grouped)}", "",
        "## Models", "", *model_links, "", "## Task Counts", "",
    ]
    lines.extend(f"- `{name}`: {count}" for name, count in sorted(sample_counts.items()))
    (destination / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_model(destination: Path, model_id: str, rows: list[dict[str, Any]]) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    by_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_task[str(row["sample_type"])].append(row)

    task_links: list[str] = []
    for task_type, task_rows in sorted(by_task.items()):
        task_dir = destination / safe_name(task_type)
        build_task(task_dir, task_type, task_rows)
        task_links.append(f"- [{task_type}](./{task_dir.name}/README.md): {len(task_rows)} outputs")
    lines = [
        f"# {model_id}", "", f"- model outputs: {len(rows)}", f"- task types: {len(by_task)}", "",
        "## Tasks", "", *task_links,
    ]
    (destination / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_task(destination: Path, task_type: str, rows: list[dict[str, Any]]) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    by_sample: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_sample[str(row["sample_id"])].append(row)
    sample_links: list[str] = []
    for sample_id, sample_rows in sorted(by_sample.items()):
        sample_dir = destination / safe_name(sample_id)
        build_sample(sample_dir, sample_id, sample_rows)
        sample_links.append(f"- [{sample_id}](./{sample_dir.name}/ALL_OUTPUTS.md): {len(sample_rows)} outputs")
    lines = [f"# {task_type}", "", f"- outputs: {len(rows)}", f"- samples: {len(by_sample)}", "", *sample_links]
    (destination / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_sample(destination: Path, sample_id: str, rows: list[dict[str, Any]]) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    ordered = sorted(rows, key=lambda row: (str(row["protocol"]), str(row["prompt_id"])))
    combined = [f"# {sample_id}: All Candidate Outputs", "", "This page contains raw candidate-model responses only.", ""]
    for row in ordered:
        protocol_dir = destination / safe_name(str(row["protocol"]))
        protocol_dir.mkdir(parents=True, exist_ok=True)
        filename = safe_name(str(row["prompt_id"])) + ".md"
        content = render_output(row)
        (protocol_dir / filename).write_text(content, encoding="utf-8")
        combined.extend([
            f"## {row['protocol']} | {row['prompt_id']}", "",
            f"Detailed file: [`{protocol_dir.name}/{filename}`](./{protocol_dir.name}/{filename})", "",
            render_prompt_sections(row), "",
            render_response_sections(row), "",
        ])
    (destination / "ALL_OUTPUTS.md").write_text("\n".join(combined) + "\n", encoding="utf-8")


def render_output(row: dict[str, Any]) -> str:
    resolved_o0 = resolve_image(str(row.get("o0_image_path", "")))
    resolved_o1 = resolve_image(str(row.get("o1_image_path", "")))
    lines = [
        f"# {row['sample_id']} | {row['prompt_id']}", "",
        "Raw candidate-model output. No evaluator or judge result is included.", "",
        "## Metadata", "",
        f"- model: `{row['model_id']}`", f"- model name: `{row.get('model_name', '')}`",
        f"- task/sample type: `{row['sample_type']}`", f"- old task source: `{row.get('old_task_id_source', '')}`",
        f"- protocol: `{row['protocol']}`", f"- prompt: `{row['prompt_id']}`",
        f"- group: `{row.get('group_id', '')}`", f"- provider error: `{row.get('error', '')}`", "",
        "## Task", "", str(row.get("instruction", "")), "",
        "## Images", "",
        f"- O0: `{row.get('o0_image_path', '')}`", f"- O0 absolute: `{resolved_o0}`",
        f"- O1: `{row.get('o1_image_path', '')}`", f"- O1 absolute: `{resolved_o1}`", "",
        render_prompt_sections(row), "",
        render_response_sections(row),
    ]
    return "\n".join(lines) + "\n"


def render_prompt_sections(row: dict[str, Any]) -> str:
    protocol = str(row.get("protocol", ""))
    descriptions = {
        "single_turn_multi_image": "O0 and O1 are provided together in one user message; the displayed final response is produced in that single call.",
        "two_turn_sequential": "Turn 1 provides O0 for an initial plan. Turn 2 keeps that assistant response in conversation history and provides O1 for the final updated plan.",
    }
    system_prompt = str(row.get("system_prompt", ""))
    turn1_prompt = str(row.get("user_prompt_turn1", ""))
    turn2_prompt = str(row.get("user_prompt_turn2", ""))
    return "\n".join([
        "## Protocol And Prompt Content", "",
        f"- protocol id: `{protocol}`", f"- prompt id: `{row.get('prompt_id', '')}`",
        f"- protocol behavior: {descriptions.get(protocol, 'See the raw message sequence below.')}", "",
        "### System Prompt", "", fenced_text(system_prompt or "(empty)"), "",
        "### User Prompt Turn 1", "", fenced_text(turn1_prompt or "(empty)"), "",
        "### User Prompt Turn 2", "", fenced_text(turn2_prompt or "(not applicable)"),
    ])


def render_response_sections(row: dict[str, Any]) -> str:
    turn1 = str(row.get("raw_response_turn1", ""))
    final = str(row.get("raw_response_final", ""))
    return "\n".join([
        "### Turn 1 Raw Response", "", fenced(turn1 or "(empty)"), "",
        "### Final Raw Response", "", fenced(final or "(empty)"),
    ])


def fenced(value: str) -> str:
    fence = "````" if "```" in value else "```"
    return f"{fence}json\n{value}\n{fence}"


def fenced_text(value: str) -> str:
    fence = "````" if "```" in value else "```"
    return f"{fence}text\n{value}\n{fence}"


def resolve_image(value: str) -> Path:
    path = Path(value)
    benchmark_root = AHD_ROOT.parent / "test_current_vlm/tool_counterexample_benchmark"
    return path.resolve() if path.is_absolute() else (benchmark_root / path).resolve()


def write_root_index(destination: Path, summaries: list[tuple[str, int, int]]) -> None:
    lines = [
        "# Sequential O0/O1 Candidate Model Outputs", "",
        "This directory contains only original candidate-model responses reorganized for manual reading.",
        "It does not contain heuristic evaluation or VLM-judge decisions.", "", "## Experiments", "",
    ]
    lines.extend(f"- [{name}](./{name}/README.md): {rows} outputs, {models} models" for name, rows, models in summaries)
    (destination / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def prepare_output(path: Path, overwrite: bool) -> None:
    if path.exists():
        if not overwrite:
            raise SystemExit(f"Output exists: {path}. Use --overwrite.")
        shutil.rmtree(path)
    path.mkdir(parents=True)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def safe_name(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    return normalized.strip("._") or "unnamed"


if __name__ == "__main__":
    main()
