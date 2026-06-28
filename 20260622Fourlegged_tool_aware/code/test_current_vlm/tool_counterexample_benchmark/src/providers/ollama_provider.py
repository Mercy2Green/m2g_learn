from __future__ import annotations

import json
import socket
import urllib.error
import urllib.request
from typing import Any

from ..image_utils import image_to_base64
from .base import ProviderError, VLMProvider, provider_result


class OllamaProvider(VLMProvider):
    name = "ollama"

    def __init__(self, model_config: dict[str, Any]) -> None:
        super().__init__(model_config)
        self.provider_label = str(model_config.get("provider_label", "ollama_local"))
        self.base_url = str(model_config.get("base_url") or "http://localhost:11434").rstrip("/")
        self.format_json = bool(model_config.get("format_json", False))
        self.num_ctx = _optional_int(model_config.get("num_ctx"))
        self.keep_alive = str(model_config.get("keep_alive", "") or "")

        if not self.model_name:
            raise ProviderError(f"{self.model_id}: model_name is required for Ollama provider. Run: ollama pull <model_name>")

    def run(
        self,
        image_path: str,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        base64_image = image_to_base64(image_path)
        options: dict[str, Any] = {
            "temperature": self.temperature,
            "num_predict": self.max_tokens,
        }
        if self.num_ctx is not None:
            options["num_ctx"] = self.num_ctx

        payload: dict[str, Any] = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": user_prompt,
                    "images": [base64_image],
                },
            ],
            "stream": False,
            "options": options,
        }
        if self.format_json:
            payload["format"] = "json"
        if self.keep_alive:
            payload["keep_alive"] = self.keep_alive

        response_json = self._post_chat(payload)
        raw_text = response_json.get("message", {}).get("content", "")
        metadata = {
            "provider_label": self.provider_label,
            "base_url": self.base_url,
            "format_json": self.format_json,
            "num_ctx": self.num_ctx,
            "keep_alive": self.keep_alive,
            "ollama_done": response_json.get("done"),
            "eval_count": response_json.get("eval_count"),
            "eval_duration": response_json.get("eval_duration"),
            "prompt_eval_count": response_json.get("prompt_eval_count"),
            "prompt_eval_duration": response_json.get("prompt_eval_duration"),
        }
        result = provider_result(raw_text, self.name, self.model_id, self.model_name, metadata)
        result["provider_label"] = self.provider_label
        return result

    def _post_chat(self, payload: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.base_url}/api/chat"
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                response_text = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code == 404 or "not found" in body.lower() or "pull" in body.lower():
                raise ProviderError(f"Ollama model '{self.model_name}' is not available. Run: ollama pull {self.model_name}") from exc
            raise ProviderError(f"Ollama request failed with HTTP {exc.code}: {body}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            raise ProviderError(f"Could not connect to Ollama at {self.base_url}. Run: ollama serve") from exc

        try:
            parsed = json.loads(response_text)
        except json.JSONDecodeError as exc:
            raise ProviderError(f"Ollama returned non-JSON response: {response_text[:500]}") from exc
        if not isinstance(parsed, dict):
            raise ProviderError("Ollama response root is not a JSON object.")
        if "error" in parsed:
            error = str(parsed.get("error", ""))
            if "not found" in error.lower() or "pull" in error.lower():
                raise ProviderError(f"Ollama model '{self.model_name}' is not available. Run: ollama pull {self.model_name}")
            raise ProviderError(f"Ollama error: {error}")
        return parsed


def _optional_int(value: Any) -> int | None:
    if value in (None, ""):
        return None
    return int(value)
