from __future__ import annotations

from typing import Any

from .base import VLMProvider
from .gemini_provider import GeminiProvider
from .mock_provider import MockProvider
from .openai_provider import OpenAIProvider
from .qwen_provider import QwenProvider


PROVIDERS: dict[str, type[VLMProvider]] = {
    "mock": MockProvider,
    "openai": OpenAIProvider,
    "qwen": QwenProvider,
    "gemini": GeminiProvider,
}


def create_provider(model_config: dict[str, Any]) -> VLMProvider:
    provider_name = str(model_config.get("provider", "")).lower()
    provider_cls = PROVIDERS.get(provider_name)
    if provider_cls is None:
        raise ValueError(f"Unknown provider '{provider_name}'. Known providers: {sorted(PROVIDERS)}")
    return provider_cls(model_config)
