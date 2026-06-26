from __future__ import annotations

import json
from typing import Any

from .base import VLMProvider, provider_result


class MockProvider(VLMProvider):
    name = "mock"

    def run(
        self,
        image_path: str,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        lower_prompt = user_prompt.lower()
        if "这瓶水" in user_prompt:
            payload = {
                "task_understanding": "Move one directly reachable bottle to the user.",
                "plan": ["确认目标水瓶", "直接抓取水瓶", "送到用户面前"],
                "uses_tool_or_container": "no",
                "tool_or_container": "none",
                "will_search_for_tool_if_not_visible": "no",
                "estimated_number_of_trips": "single",
                "efficiency_consideration": "A direct grasp is shortest for one bottle.",
                "safety_or_stability_consideration": "保持瓶身直立。",
                "reason": "Only one object is requested.",
                "failure_risk": "low",
            }
        elif "当前视野没有" in lower_prompt or "does not show" in lower_prompt:
            payload = {
                "task_understanding": "Move several drinks quickly.",
                "plan": ["识别所有饮料", "逐个抓取并送往目标房间", "返回继续搬剩余饮料"],
                "uses_tool_or_container": "no",
                "tool_or_container": "none",
                "will_search_for_tool_if_not_visible": "no",
                "estimated_number_of_trips": "multiple",
                "efficiency_consideration": "Multiple trips may be required.",
                "safety_or_stability_consideration": "每次只拿稳一个物体。",
                "reason": "Mock response intentionally includes a common failure pattern.",
                "failure_risk": "inefficient",
            }
        else:
            payload = {
                "task_understanding": "Complete the household mobile manipulation task.",
                "plan": ["观察目标物体", "选择合适的辅助物或直接抓取", "完成搬运或操作"],
                "uses_tool_or_container": "yes",
                "tool_or_container": "appropriate visible household aid",
                "will_search_for_tool_if_not_visible": "no",
                "estimated_number_of_trips": "few",
                "efficiency_consideration": "Reduce unnecessary trips when multiple objects are involved.",
                "safety_or_stability_consideration": "Avoid unstable stacking or spilling.",
                "reason": "Mock response for pipeline testing.",
                "failure_risk": "needs real model validation",
            }
        return provider_result(json.dumps(payload, ensure_ascii=False), self.name, self.model_id, self.model_name)
