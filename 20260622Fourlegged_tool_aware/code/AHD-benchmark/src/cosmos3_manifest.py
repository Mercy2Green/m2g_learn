from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


def load_manifest(path: str | Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Manifest not found: {file_path}")
    with file_path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            value = json.loads(stripped)
            if not isinstance(value, dict):
                raise ValueError(f"Manifest row {line_no} is not an object: {file_path}")
            rows.append(value)
    return rows


def save_manifest(path: str | Path, rows: Iterable[dict[str, Any]]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def build_smoke12_selection(
    specs: list[dict[str, Any]],
    plan_counts: dict[str, int],
) -> list[dict[str, Any]]:
    return _select_by_spec_type_counts(specs, plan_counts)


def build_mini36_selection(
    specs: list[dict[str, Any]],
    per_spec_type: int,
) -> list[dict[str, Any]]:
    spec_types = sorted({str(spec["spec_type"]) for spec in specs})
    return _select_by_spec_type_counts(specs, {spec_type: per_spec_type for spec_type in spec_types})


def resolve_prompt_source(
    deterministic_prompt: dict[str, Any],
    enriched_by_spec_id: dict[str, dict[str, Any]],
    *,
    use_enrichment: bool,
    default_enrichment_model: str,
) -> dict[str, Any]:
    spec_id = str(deterministic_prompt["spec_id"])
    enriched = enriched_by_spec_id.get(spec_id) if use_enrichment else None
    enriched_prompt = str(enriched.get("cosmos_prompt_variant", "")).strip() if enriched else ""
    if enriched and enriched_prompt:
        negative_prompt = str(enriched.get("negative_prompt_variant", "")).strip()
        if not negative_prompt:
            negative_prompt = str(deterministic_prompt.get("negative_prompt", ""))
        return {
            "prompt_source": "llm_enriched",
            "enrichment_model": str(enriched.get("model_id") or default_enrichment_model),
            "prompt": enriched_prompt,
            "negative_prompt": negative_prompt,
        }

    return {
        "prompt_source": "deterministic",
        "enrichment_model": None,
        "prompt": str(deterministic_prompt.get("prompt", "")),
        "negative_prompt": str(deterministic_prompt.get("negative_prompt", "")),
    }


def _select_by_spec_type_counts(
    specs: list[dict[str, Any]],
    plan_counts: dict[str, int],
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for spec_type in sorted(plan_counts):
        count = int(plan_counts[spec_type])
        matches = sorted(
            (spec for spec in specs if str(spec.get("spec_type")) == spec_type),
            key=lambda spec: str(spec.get("spec_id", "")),
        )
        if len(matches) < count:
            raise ValueError(f"Need {count} specs for {spec_type}, found {len(matches)}")
        selected.extend(matches[:count])
    return selected
