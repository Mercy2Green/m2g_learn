from __future__ import annotations

from typing import Any


GENERAL_LEAKAGE_TERMS = [
    "工具",
    "容器",
    "托盘",
    "袋子",
    "箱子",
    "盒子",
    "篮子",
    "背包",
    "洗衣篮",
    "扫把",
    "簸箕",
    "抹布",
    "纸巾",
    "长杆",
    "杆子",
    "tool",
    "container",
    "tray",
    "bag",
    "box",
    "basket",
    "backpack",
    "broom",
    "dustpan",
    "cloth",
    "tissue",
    "rod",
    "stick",
]


def build_prompt(task: dict[str, Any], prompt_set: dict[str, Any]) -> tuple[str, str, list[str]]:
    response_schema_text = str(prompt_set.get("response_schema_text", "")).strip()
    system_prompt = prompt_set["system_prompt"].strip()
    if response_schema_text:
        system_prompt = f"{system_prompt}\n\n{response_schema_text}"
    user_template = prompt_set["user_prompt_template"]
    scene_note = task.get("scene_note", "") if prompt_set.get("include_scene_note", False) else ""
    user_prompt = user_template.format(
        instruction=task.get("instruction", ""),
        scene_note=scene_note,
        task_id=task.get("task_id", ""),
        task_name=task.get("name", ""),
    ).strip()
    leakage_terms = find_prompt_leakage(task, user_prompt)
    return system_prompt, user_prompt, leakage_terms


def find_prompt_leakage(task: dict[str, Any], user_prompt: str) -> list[str]:
    """Check answer terms in the task/user text only.

    The system prompt may contain response schema fields for diagnostic probes, so
    leakage checks intentionally focus on the user-facing task prompt.
    """
    terms = list(task.get("invalid_prompt_leakage_terms") or []) + GENERAL_LEAKAGE_TERMS
    lowered = user_prompt.lower()
    return sorted({term for term in terms if term and term.lower() in lowered})
