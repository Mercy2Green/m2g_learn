from __future__ import annotations

import json
from typing import Any
from urllib import request
from urllib.error import HTTPError, URLError

try:
    import requests  # type: ignore
except ImportError:  # pragma: no cover
    requests = None


class OllamaClientError(RuntimeError):
    """Raised when the local Ollama endpoint cannot return a usable response."""


class OllamaClient:
    def __init__(self, base_url: str, timeout_seconds: int = 300) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    def chat(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        options: dict[str, Any] | None = None,
    ) -> str:
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "format": "json",
            "options": options or {},
        }
        data = self._post_json("/api/chat", payload)
        message = data.get("message", {})
        content = message.get("content")
        if not isinstance(content, str):
            raise OllamaClientError("Ollama /api/chat response did not include message.content")
        return content

    def generate(
        self,
        *,
        model: str,
        prompt: str,
        options: dict[str, Any] | None = None,
    ) -> str:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": options or {},
        }
        data = self._post_json("/api/generate", payload)
        content = data.get("response")
        if not isinstance(content, str):
            raise OllamaClientError("Ollama /api/generate response did not include response")
        return content

    def _post_json(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        if requests is not None:
            try:
                response = requests.post(url, json=payload, timeout=self.timeout_seconds)
                response.raise_for_status()
                data = response.json()
            except Exception as exc:  # pragma: no cover - depends on local service
                raise OllamaClientError(f"Ollama request failed: {exc}") from exc
        else:
            encoded = json.dumps(payload).encode("utf-8")
            req = request.Request(url, data=encoded, headers={"Content-Type": "application/json"}, method="POST")
            try:
                with request.urlopen(req, timeout=self.timeout_seconds) as response:  # noqa: S310 local endpoint
                    data = json.loads(response.read().decode("utf-8"))
            except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:  # pragma: no cover
                raise OllamaClientError(f"Ollama request failed: {exc}") from exc
        if not isinstance(data, dict):
            raise OllamaClientError("Ollama response root was not a JSON object")
        return data
