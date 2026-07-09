from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl  # noqa: E402
from src.load_config import load_dotenv, load_yaml  # noqa: E402
from src.vlm_image_judge import (  # noqa: E402
    CSV_FIELDS,
    build_ahd_image_quality_prompt,
    image_to_base64,
    normalize_judge_output,
    probe_image,
    resolve_image_path,
    run_judge_with_retries,
    write_csv,
    write_jsonl,
)


def main() -> None:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    config = load_yaml(ROOT / "configs" / "vlm_image_judge.yaml")
    default_judge = config["default_judge"]

    results_path = _resolve_path(args.results)
    manifest_path = _resolve_path(args.manifest)
    output_dir = _resolve_path(args.output_dir)
    output_jsonl = output_dir / "vlm_image_judge.jsonl"
    if output_jsonl.exists() and not args.overwrite:
        raise SystemExit(f"Output exists: {output_jsonl}. Use --overwrite to replace it.")

    result_rows = read_jsonl(results_path)
    manifest_rows = read_jsonl(manifest_path)
    if not result_rows:
        raise SystemExit(f"Results file not found or empty: {results_path}")
    if not manifest_rows:
        raise SystemExit(f"Manifest file not found or empty: {manifest_path}")
    if args.limit is not None:
        result_rows = result_rows[: args.limit]

    manifest_by_spec_id = {str(row["spec_id"]): row for row in manifest_rows}
    judge_model = args.judge_model or str(default_judge["model"])
    ollama_url = args.ollama_url or str(default_judge["ollama_url"])
    max_retries = args.max_retries if args.max_retries is not None else int(default_judge["max_retries"])
    temperature = args.temperature if args.temperature is not None else float(default_judge["temperature"])

    output_dir.mkdir(parents=True, exist_ok=True)
    started_at = time.time()
    rows: list[dict[str, Any]] = []
    print(
        f"[PROGRESS] starting AHD VLM image judge rows={len(result_rows)} "
        f"model={judge_model} output_dir={output_dir}",
        file=sys.stderr,
        flush=True,
    )
    for index, result_row in enumerate(result_rows, start=1):
        row = judge_one_row(
            result_row,
            manifest_by_spec_id,
            judge_model=judge_model,
            ollama_url=ollama_url,
            max_retries=max_retries,
            temperature=temperature,
        )
        rows.append(row)
        if should_print_progress(index, len(result_rows), args.progress_every):
            print(progress_message(index, len(result_rows), started_at, row), file=sys.stderr, flush=True)

    keep_rows = [row for row in rows if row["keep"] is True]
    reject_rows = [row for row in rows if row["keep"] is False]
    write_jsonl(output_jsonl, rows)
    write_csv(output_dir / "vlm_image_judge.csv", rows, CSV_FIELDS)
    write_jsonl(output_dir / "vlm_image_judge_keep_list.jsonl", keep_rows)
    write_jsonl(output_dir / "vlm_image_judge_reject_list.jsonl", reject_rows)
    write_failures(output_dir / "vlm_image_judge_failures.md", reject_rows)
    print(f"Wrote {len(rows)} judge rows to {output_jsonl}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run local Ollama VLM image-quality judge on generated AHD images.")
    parser.add_argument("--results", default="data/runs/ahd_cosmos3_smoke12_results.jsonl")
    parser.add_argument("--manifest", default="prompts/manifests/cosmos3_smoke12_manifest.jsonl")
    parser.add_argument("--output_dir", default="data/judges/ahd_cosmos3_smoke12_qwen32")
    parser.add_argument("--judge_model", default="qwen3-vl:32b-instruct-q4_K_M")
    parser.add_argument("--ollama_url", default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--progress_every", type=int, default=1)
    parser.add_argument("--max_retries", type=int, default=None)
    parser.add_argument("--temperature", type=float, default=None)
    return parser.parse_args()


def judge_one_row(
    result_row: dict[str, Any],
    manifest_by_spec_id: dict[str, dict[str, Any]],
    *,
    judge_model: str,
    ollama_url: str,
    max_retries: int,
    temperature: float,
) -> dict[str, Any]:
    spec_id = str(result_row.get("spec_id", ""))
    manifest_row = manifest_by_spec_id.get(spec_id, {"spec_id": spec_id})
    image_path = resolve_image_path(result_row, ROOT)
    probe = probe_image(image_path)
    if not probe["exists"] or not probe["valid_image"]:
        row = normalize_judge_output(
            None,
            result_row,
            manifest_row,
            "",
            judge_model,
            image_path=image_path,
        )
        row["main_failure_reason"] = str(probe.get("error") or "invalid_image")
        row["one_prompt_fix"] = "Regenerate this image after confirming the expected output path exists."
        return row

    prompt = build_ahd_image_quality_prompt(result_row, manifest_row)
    parsed, raw_response, parse_error = run_judge_with_retries(
        base_url=ollama_url,
        model=judge_model,
        prompt=prompt,
        images=[image_to_base64(image_path)],
        temperature=temperature,
        max_retries=max_retries,
    )
    return normalize_judge_output(
        parsed,
        result_row,
        manifest_row,
        raw_response,
        judge_model,
        parse_error=parse_error,
        image_path=image_path,
    )


def should_print_progress(index: int, total: int, every: int) -> bool:
    every = max(1, every)
    return index == 1 or index == total or index % every == 0


def progress_message(index: int, total: int, started_at: float, row: dict[str, Any]) -> str:
    elapsed = time.time() - started_at
    avg = elapsed / index if index else 0.0
    remaining = max(0, total - index) * avg
    return (
        f"[PROGRESS] {index}/{total} keep={row.get('keep')} "
        f"spec_id={row.get('spec_id')} spec_type={row.get('spec_type')} "
        f"reason={row.get('main_failure_reason')} elapsed={_format_seconds(elapsed)} "
        f"eta={_format_seconds(remaining)}"
    )


def write_failures(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = ["# AHD VLM Image Judge Failures", ""]
    if not rows:
        lines.append("No rejected rows.")
    for row in rows:
        lines.append(
            f"- {row.get('spec_id')} ({row.get('spec_type')}): "
            f"{row.get('main_failure_reason')}. Fix: {row.get('one_prompt_fix')}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def _format_seconds(seconds: float) -> str:
    seconds = max(0, int(seconds))
    minutes, secs = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}" if hours else f"{minutes:02d}:{secs:02d}"


if __name__ == "__main__":
    main()
