from __future__ import annotations

from typing import Any


RESPONSE_SCHEMA_TEXT = """
请只输出一个 JSON 对象，不要输出 markdown 或额外解释。JSON schema:
{
  "task_understanding": "string",
  "plan": ["step1", "step2", "step3"],
  "uses_tool_or_container": "yes/no",
  "tool_or_container": "string or none",
  "will_search_for_tool_if_not_visible": "yes/no",
  "estimated_number_of_trips": "single/few/multiple/unknown",
  "efficiency_consideration": "string",
  "safety_or_stability_consideration": "string",
  "reason": "string",
  "failure_risk": "string"
}
"""


def build_prompt(task: dict[str, Any], prompt_set: dict[str, Any]) -> tuple[str, str, list[str]]:
    system_prompt = f"{prompt_set['system_prompt'].strip()}\n\n{RESPONSE_SCHEMA_TEXT.strip()}"
    user_template = prompt_set["user_prompt_template"]
    user_prompt = user_template.format(
        instruction=task.get("instruction", ""),
        scene_note=task.get("scene_note", ""),
        task_id=task.get("task_id", ""),
        task_name=task.get("name", ""),
    ).strip()
    leakage_terms = find_prompt_leakage(task, user_prompt)
    return system_prompt, user_prompt, leakage_terms


def find_prompt_leakage(task: dict[str, Any], user_prompt: str) -> list[str]:
    """Check task-specific answer terms in the task/user text only.

    The required output schema contains tool-related field names, so schema text is
    intentionally excluded from this check.
    """
    terms = task.get("invalid_prompt_leakage_terms") or []
    return sorted({term for term in terms if term and term in user_prompt})
