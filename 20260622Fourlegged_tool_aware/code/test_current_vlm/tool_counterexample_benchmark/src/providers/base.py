from __future__ import annotations

import time
from abc import ABC, abstractmethod
from typing import Any


class ProviderError(RuntimeError):
    pass


class VLMProvider(ABC):
    name: str

    def __init__(self, model_config: dict[str, Any]) -> None:
        self.model_config = model_config
        self.model_id = str(model_config.get("model_id", self.name))
        self.model_name = str(model_config.get("model_name") or "")
        self.temperature = float(model_config.get("temperature", 0.0))
        self.max_tokens = int(model_config.get("max_tokens", 1024))
        self.timeout_seconds = int(model_config.get("timeout_seconds", 60))
        self.retries = int(model_config.get("retries", 2))

    def run_with_retry(
        self,
        image_path: str,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                return self.run(image_path, system_prompt, user_prompt, response_schema)
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                if attempt >= self.retries:
                    break
                time.sleep(min(2**attempt, 8))
        raise ProviderError(f"{self.model_id} failed after {self.retries + 1} attempt(s): {last_error}") from last_error

    @abstractmethod
    def run(
        self,
        image_path: str,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        raise NotImplementedError


def provider_result(raw_text: str, provider: str, model_id: str, model_name: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "provider": provider,
        "model_id": model_id,
        "model_name": model_name,
        "raw_response": raw_text,
        "metadata": metadata or {},
    }
