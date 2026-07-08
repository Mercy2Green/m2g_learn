from __future__ import annotations

from collections import Counter
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl


def _counter(specs: list[dict[str, Any]], key: str) -> Counter[str]:
    return Counter(str(spec.get(key)) for spec in specs)


def _visual_counter(specs: list[dict[str, Any]], key: str) -> Counter[str]:
    return Counter(str(spec.get("visual_scene", {}).get(key, "n/a")) for spec in specs)


def _section(title: str, counts: Counter[str]) -> list[str]:
    lines = [f"## {title}", ""]
    for key, count in sorted(counts.items()):
        lines.append(f"- {key}: {count}")
    lines.append("")
    return lines


def main() -> None:
    specs = read_jsonl(ROOT / "specs" / "scene_specs_checked.jsonl")
    prompts = read_jsonl(ROOT / "prompts" / "cosmos3_prompts_raw.jsonl")
    lines = [
        "# AHD Data Distribution Preview",
        "",
        f"- Checked specs: {len(specs)}",
        f"- Prompt entries: {len(prompts)}",
        "",
    ]
    lines.extend(_section("By View Stage", _counter(specs, "view_stage")))
    lines.extend(_section("By Spec Type", _counter(specs, "spec_type")))
    lines.extend(_section("By Task Family", _counter(specs, "task_family")))
    lines.extend(_section("By Helper Type", _visual_counter(specs, "helper_type")))
    lines.extend(_section("By Target Type", _visual_counter(specs, "target_type")))
    content = "\n".join(lines) + "\n"
    (ROOT / "docs" / "DATA_DISTRIBUTION_PREVIEW.md").write_text(content, encoding="utf-8")
    print(content)
    print("Saved docs/DATA_DISTRIBUTION_PREVIEW.md")


if __name__ == "__main__":
    main()
