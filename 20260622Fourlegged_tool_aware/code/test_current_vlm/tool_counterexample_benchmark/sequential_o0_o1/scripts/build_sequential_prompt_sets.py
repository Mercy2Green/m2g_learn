from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.load_config import load_yaml  # noqa: E402


MULTI_IMAGE_WRAPPER = """观察 O0 是机器人最初看到的场景。
观察 O1 是机器人短程环视后看到的新场景。
请基于两个观察为同一个原始任务更新高层计划。"""

TURN2_UPDATE = (
    "机器人现在获得了一个新的观察 O1。请结合上一轮看到的 O0 和当前 O1，为同一个原始任务更新高层计划。"
    "如果当前新观察中存在对原任务有用的物体，请说明如何使用；如果不适合，请说明是否继续检查附近区域或直接执行。"
    "仍然只输出同一 JSON schema。"
)

CLEAN_CATEGORIES = {"generic_clean", "embodiment_clean"}
CLEAN_FORBIDDEN_TERMS = [
    "工具", "容器", "托盘", "篮子", "箱子", "盒子", "袋子", "扫把", "长杆", "杆子",
    "tool", "helper", "container", "tray", "basket", "box", "broom", "stick", "rod",
]


def main() -> None:
    args = parse_args()
    old_path = root_path(args.old_prompts)
    output_path = root_path(args.output)
    report_path = output_path.with_name(f"{output_path.stem}_report.md")
    if (output_path.exists() or report_path.exists()) and not args.overwrite:
        raise SystemExit(f"Output exists. Use --overwrite: {output_path}")

    old_prompts = load_yaml(old_path).get("prompts", [])
    if not isinstance(old_prompts, list):
        raise ValueError("Old prompts config must contain a prompts list")
    if len(old_prompts) != 18:
        raise ValueError(f"Expected 18 old prompts, found {len(old_prompts)}")

    generated: list[dict[str, Any]] = []
    for old in old_prompts:
        generated.extend(generate_pair(old))
    validate_generated(old_prompts, generated)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(dump_prompt_yaml(generated), encoding="utf-8")
    report_path.write_text(build_report(old_prompts, generated), encoding="utf-8")
    print(f"old prompts: {len(old_prompts)}")
    print(f"generated sequential prompts: {len(generated)}")
    print(f"Wrote: {output_path}")
    print(f"Wrote: {report_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate O0/O1 sequential mappings for every old prompt.")
    parser.add_argument("--old_prompts", default="config/prompt_sets.yaml")
    parser.add_argument("--output", default="sequential_o0_o1/prompts/sequential_prompt_sets_full.yaml")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def root_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (ROOT / path).resolve()


def generate_pair(old: dict[str, Any]) -> list[dict[str, Any]]:
    old_id = str(old["prompt_id"])
    category = str(old.get("prompt_category", "uncategorized"))
    common = {
        "prompt_category": f"sequential_{category}",
        "old_prompt_category": category,
        "primary_for_sequential": bool(old.get("primary_for_counterexample", False)),
        "embodiment_profile": old.get("embodiment_profile", "generic"),
        "system_prompt": old.get("system_prompt", ""),
        "response_schema_text": old.get("response_schema_text", ""),
        "clean_evidence": category in CLEAN_CATEGORIES,
    }
    for optional in ("diagnostic_type", "intervention_type"):
        if optional in old:
            common[optional] = old[optional]
    if category not in CLEAN_CATEGORIES:
        common["evidence_note"] = "Intervention or diagnostic prompt; not clean sequential evidence."

    multi = {
        "prompt_id": f"multi_image__{old_id}",
        "protocol": "single_turn_multi_image",
        "base_prompt_id": old_id,
        **common,
        "user_prompt_template": f"{str(old.get('user_prompt_template', '')).rstrip()}\n\n{MULTI_IMAGE_WRAPPER}",
    }
    two_turn = {
        "prompt_id": f"two_turn__{old_id}",
        "protocol": "two_turn_sequential",
        "turn1_base_prompt_id": old_id,
        **common,
        "turn1_user_prompt_template": old.get("user_prompt_template", ""),
        "turn2_user_prompt": TURN2_UPDATE,
    }
    return [multi, two_turn]


def validate_generated(old_prompts: list[dict[str, Any]], generated: list[dict[str, Any]]) -> None:
    if len(generated) != 36:
        raise ValueError(f"Expected 36 generated prompts, found {len(generated)}")
    old_by_id = {str(row["prompt_id"]): row for row in old_prompts}
    ids: set[str] = set()
    for prompt in generated:
        prompt_id = str(prompt["prompt_id"])
        if prompt_id in ids:
            raise ValueError(f"Duplicate generated prompt id: {prompt_id}")
        ids.add(prompt_id)
        base_id = str(prompt.get("base_prompt_id") or prompt.get("turn1_base_prompt_id"))
        old = old_by_id[base_id]
        if prompt["system_prompt"] != old["system_prompt"]:
            raise ValueError(f"{prompt_id}: system prompt drift")
        if prompt["response_schema_text"] != old["response_schema_text"]:
            raise ValueError(f"{prompt_id}: response schema drift")
        if prompt["protocol"] == "two_turn_sequential":
            if prompt["turn1_user_prompt_template"] != old["user_prompt_template"]:
                raise ValueError(f"{prompt_id}: turn1 user prompt drift")
        if prompt["old_prompt_category"] in CLEAN_CATEGORIES:
            user_text = " ".join(
                str(prompt.get(key, ""))
                for key in ("user_prompt_template", "turn1_user_prompt_template", "turn2_user_prompt")
            ).lower()
            leaked = sorted(term for term in CLEAN_FORBIDDEN_TERMS if term.lower() in user_text)
            if leaked:
                raise ValueError(f"{prompt_id}: clean wrapper leakage: {leaked}")


def build_report(old_prompts: list[dict[str, Any]], generated: list[dict[str, Any]]) -> str:
    protocols = Counter(str(row["protocol"]) for row in generated)
    categories = Counter(str(row["old_prompt_category"]) for row in generated)
    primary = Counter(str(bool(row["primary_for_sequential"])).lower() for row in generated)
    embodiments = Counter(str(row["embodiment_profile"]) for row in generated)
    lines = [
        "# Full Sequential Prompt Mapping Report",
        "",
        f"- old prompt count: {len(old_prompts)}",
        f"- generated sequential prompt count: {len(generated)}",
        "- inheritance validation: PASS",
        "- clean wrapper leakage validation: PASS",
        "",
        "## By Protocol",
        "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in sorted(protocols.items()))
    lines.extend(["", "## By Old Prompt Category", ""])
    lines.extend(f"- {key}: {value}" for key, value in sorted(categories.items()))
    lines.extend(["", "## By Primary For Sequential", ""])
    lines.extend(f"- {key}: {value}" for key, value in sorted(primary.items()))
    lines.extend(["", "## By Embodiment Profile", ""])
    lines.extend(f"- {key}: {value}" for key, value in sorted(embodiments.items()))
    return "\n".join(lines) + "\n"


def dump_prompt_yaml(prompts: list[dict[str, Any]]) -> str:
    lines = ["prompts:"]
    for prompt in prompts:
        first = True
        for key, value in prompt.items():
            prefix = "  - " if first else "    "
            first = False
            if isinstance(value, str) and "\n" in value:
                lines.append(f"{prefix}{key}: |")
                lines.extend(f"      {line}" for line in value.splitlines())
            else:
                lines.append(f"{prefix}{key}: {yaml_scalar(value)}")
    return "\n".join(lines) + "\n"


def yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


if __name__ == "__main__":
    main()
