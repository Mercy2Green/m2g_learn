from __future__ import annotations

import os
from typing import Any

from ..image_utils import image_to_data_url
from .base import ProviderError, VLMProvider, provider_result


class QwenProvider(VLMProvider):
    name = "qwen"

    def __init__(self, model_config: dict[str, Any]) -> None:
        super().__init__(model_config)
        api_key = os.environ.get("QWEN_API_KEY")
        base_url = os.environ.get("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
        if not api_key:
            raise ProviderError("QWEN_API_KEY is not set. Add it to .env or disable the Qwen model.")
        if not self.model_name:
            raise ProviderError("QWEN_MODEL/model_name is empty for Qwen provider.")
        try:
            from openai import OpenAI
        except ImportError as exc:  # pragma: no cover
            raise ProviderError("OpenAI SDK is required for Qwen compatible endpoint. Run: pip install -r requirements.txt") from exc
        self.client = OpenAI(api_key=api_key, base_url=base_url, timeout=self.timeout_seconds)

    def run(
        self,
        image_path: str,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        image_url = image_to_data_url(image_path)
        response = self.client.chat.completions.create(
            model=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_prompt},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                },
            ],
        )
        raw_text = response.choices[0].message.content or ""
        return provider_result(raw_text, self.name, self.model_id, self.model_name, {"usage": _to_dict(response.usage)})


def _to_dict(value: Any) -> dict[str, Any]:
    if value is None:
        return {}
    if hasattr(value, "model_dump"):
        return value.model_dump()
    return dict(value)
