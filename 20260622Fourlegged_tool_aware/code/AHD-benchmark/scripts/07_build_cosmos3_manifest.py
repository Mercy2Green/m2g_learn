from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.cosmos3_manifest import (  # noqa: E402
    build_mini36_selection,
    build_smoke12_selection,
    resolve_prompt_source,
    save_manifest,
)
from src.jsonl_utils import read_jsonl  # noqa: E402
from src.load_config import load_yaml  # noqa: E402


def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"Expected true/false, got: {value}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a deterministic Cosmos3 generation manifest.")
    parser.add_argument("--plan", choices=["smoke12", "mini36"], default="smoke12")
    parser.add_argument("--enrichment_file", default=None)
    parser.add_argument("--use_enrichment", type=parse_bool, default=True)
    parser.add_argument("--output_manifest", default=None)
    args = parser.parse_args()

    config = load_yaml(ROOT / "configs" / "cosmos3_batch_generation.yaml")
    specs_path = ROOT / "specs" / "scene_specs_checked.jsonl"
    prompts_path = ROOT / "prompts" / "cosmos3_prompts_raw.jsonl"
    specs = read_jsonl(specs_path)
    prompts = read_jsonl(prompts_path)
    if not specs:
        raise SystemExit(f"Checked specs not found or empty: {specs_path}")
    if not prompts:
        raise SystemExit(f"Deterministic prompts not found or empty: {prompts_path}")

    if args.plan == "smoke12":
        selected_specs = build_smoke12_selection(specs, config["smoke12_plan"])
        default_name = "cosmos3_smoke12_manifest.jsonl"
    else:
        selected_specs = build_mini36_selection(specs, int(config["mini36_plan"]["each_spec_type"]))
        default_name = "cosmos3_mini36_manifest.jsonl"

    prompt_by_spec_id = {str(row["spec_id"]): row for row in prompts}
    enriched_by_spec_id: dict[str, dict[str, Any]] = {}
    enrichment_path: Path | None = None
    if args.use_enrichment:
        if not args.enrichment_file:
            raise SystemExit("--enrichment_file is required when --use_enrichment true")
        enrichment_path = _resolve_path(args.enrichment_file)
        enriched_by_spec_id = {str(row["spec_id"]): row for row in read_jsonl(enrichment_path)}

    rows: list[dict[str, Any]] = []
    for spec in selected_specs:
        spec_id = str(spec["spec_id"])
        deterministic = prompt_by_spec_id.get(spec_id)
        if deterministic is None:
            raise SystemExit(f"Missing deterministic prompt for spec_id={spec_id}")
        prompt_fields = resolve_prompt_source(
            deterministic,
            enriched_by_spec_id,
            use_enrichment=args.use_enrichment,
            default_enrichment_model=str(config["default_enrichment_model"]),
        )
        stage_dir = "o0" if str(spec["view_stage"]).upper() == "O0" else "o1"
        rows.append({
            "spec_id": spec_id,
            "view_stage": spec["view_stage"],
            "spec_type": spec["spec_type"],
            "prompt_source": prompt_fields["prompt_source"],
            "enrichment_model": prompt_fields["enrichment_model"],
            "prompt": prompt_fields["prompt"],
            "negative_prompt": prompt_fields["negative_prompt"],
            "seed": int(spec["seed"]),
            "output_image_path": f"{config['default_output_root']}/{stage_dir}/{spec_id}.jpg",
            "source_spec_path": str(specs_path.relative_to(ROOT)),
            "source_prompt_path": str(
                enrichment_path.relative_to(ROOT)
                if prompt_fields["prompt_source"] == "llm_enriched" and enrichment_path is not None
                else prompts_path.relative_to(ROOT)
            ),
        })

    output_path = _resolve_path(args.output_manifest) if args.output_manifest else ROOT / str(config["manifest_dir"]) / default_name
    save_manifest(output_path, rows)
    report_path = output_path.with_name(f"{output_path.stem}_report.md")
    _write_manifest_report(report_path, rows)
    enriched_count = sum(1 for row in rows if row["prompt_source"] == "llm_enriched")
    fallback_ids = [str(row["spec_id"]) for row in rows if row["prompt_source"] == "deterministic"]
    print(f"Wrote {len(rows)} rows to {output_path}")
    print(f"Plan: {args.plan}; enrichment: {args.use_enrichment}")
    print(f"Total rows: {len(rows)}")
    print(f"LLM enriched rows: {enriched_count}")
    print(f"Deterministic fallback rows: {len(fallback_ids)}")
    print(f"Fallback spec_ids: {', '.join(fallback_ids) if fallback_ids else 'none'}")
    print(f"Wrote report: {report_path}")


def _resolve_path(path_text: str | None) -> Path:
    if not path_text:
        raise ValueError("Path is required")
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def _write_manifest_report(path: Path, rows: list[dict[str, Any]]) -> None:
    enriched = [row for row in rows if row["prompt_source"] == "llm_enriched"]
    fallback = [row for row in rows if row["prompt_source"] == "deterministic"]
    lines = [
        f"# Cosmos3 Manifest Report: {path.stem.removesuffix('_report')}",
        "",
        f"- total rows: {len(rows)}",
        f"- llm_enriched rows: {len(enriched)}",
        f"- deterministic fallback rows: {len(fallback)}",
        "",
        "## Fallback Spec IDs",
        "",
    ]
    if fallback:
        lines.extend(f"- {row['spec_id']}" for row in fallback)
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
