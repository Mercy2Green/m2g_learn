from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .base import ProviderError, VLMProvider, provider_result


class GeminiProvider(VLMProvider):
    name = "gemini"

    def __init__(self, model_config: dict[str, Any]) -> None:
        super().__init__(model_config)
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ProviderError("GEMINI_API_KEY is not set. Add it to .env or disable the Gemini model.")
        if not self.model_name:
            raise ProviderError("GEMINI_MODEL/model_name is empty for Gemini provider.")
        try:
            import google.generativeai as genai
        except ImportError as exc:  # pragma: no cover
            raise ProviderError("Gemini SDK is not installed. Run: pip install -r requirements.txt") from exc
        genai.configure(api_key=api_key)
        self.genai = genai
        self.model = genai.GenerativeModel(self.model_name)

    def run(
        self,
        image_path: str,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image file not found: {path}")
        image_file = self.genai.upload_file(path=str(path))
        response = self.model.generate_content(
            [system_prompt, user_prompt, image_file],
            generation_config={
                "temperature": self.temperature,
                "max_output_tokens": self.max_tokens,
                "response_mime_type": "application/json",
            },
            request_options={"timeout": self.timeout_seconds},
        )
        raw_text = getattr(response, "text", "") or ""
        return provider_result(raw_text, self.name, self.model_id, self.model_name)
