from __future__ import annotations

import os
from typing import Any
from urllib.parse import urlparse

from ..image_utils import image_to_data_url
from .base import ProviderError, VLMProvider, provider_result


class OpenAICompatibleProvider(VLMProvider):
    name = "openai_compatible"

    def __init__(self, model_config: dict[str, Any]) -> None:
        super().__init__(model_config)
        self.provider_label = str(model_config.get("provider_label", self.name))
        self.api_key_env = str(model_config.get("api_key_env", ""))
        self.base_url = str(model_config.get("base_url", ""))
        self.response_format_json = bool(model_config.get("response_format_json", False))
        self.image_transport = str(model_config.get("image_transport", "data_url"))
        self.extra_body = model_config.get("extra_body") or {}

        if not self.api_key_env:
            raise ProviderError(f"{self.model_id}: api_key_env is required for openai_compatible provider.")
        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise ProviderError(f"{self.model_id}: {self.api_key_env} is not set. Add it to .env or disable this model.")
        if not self.base_url:
            raise ProviderError(f"{self.model_id}: base_url is empty.")
        if not self.model_name:
            raise ProviderError(f"{self.model_id}: model_name is empty.")
        if self.image_transport != "data_url":
            raise ProviderError(f"{self.model_id}: unsupported image_transport '{self.image_transport}'. Use 'data_url'.")
        if not isinstance(self.extra_body, dict):
            raise ProviderError(f"{self.model_id}: extra_body must be a mapping.")

        try:
            from openai import OpenAI
        except ImportError as exc:  # pragma: no cover
            raise ProviderError("OpenAI SDK is required. Run: pip install -r requirements.txt") from exc

        self.client = OpenAI(api_key=api_key, base_url=self.base_url, timeout=self.timeout_seconds)

    def run(
        self,
        image_path: str,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        image_url = image_to_data_url(image_path)
        request: dict[str, Any] = {
            "model": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "messages": [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_prompt},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                },
            ],
        }
        if self.response_format_json:
            request["response_format"] = {"type": "json_object"}
        if self.extra_body:
            request["extra_body"] = self.extra_body

        response = self.client.chat.completions.create(**request)
        raw_text = response.choices[0].message.content or ""
        metadata = {
            "usage": _to_dict(response.usage),
            "provider_label": self.provider_label,
            "base_url_host": urlparse(self.base_url).netloc,
            "response_format_json": self.response_format_json,
            "image_transport": self.image_transport,
        }
        result = provider_result(raw_text, self.name, self.model_id, self.model_name, metadata)
        result["provider_label"] = self.provider_label
        return result


def _to_dict(value: Any) -> dict[str, Any]:
    if value is None:
        return {}
    if hasattr(value, "model_dump"):
        return value.model_dump()
    return dict(value)
