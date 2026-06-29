from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.load_config import load_dotenv, load_yaml  # noqa: E402


def main() -> int:
    load_dotenv(ROOT / ".env")
    models = load_yaml(ROOT / "config/models.yaml").get("models", [])
    ollama_models = [model for model in models if model.get("provider") == "ollama"]
    if not ollama_models:
        print("No Ollama models found in config/models.yaml.")
        return 1

    base_urls = sorted({str(model.get("base_url") or "http://localhost:11434").rstrip("/") for model in ollama_models})
    had_error = False
    for base_url in base_urls:
        available = fetch_ollama_tags(base_url)
        if available is None:
            had_error = True
            continue
        print(f"Ollama reachable at {base_url}. Local models: {len(available)}")
        for model in ollama_models:
            if str(model.get("base_url") or "http://localhost:11434").rstrip("/") != base_url:
                continue
            model_id = str(model.get("model_id", ""))
            model_name = str(model.get("model_name", ""))
            enabled = bool(model.get("enabled", False))
            supports_vision = str(model.get("supports_vision", "unknown")).lower()
            is_available = model_name in available
            print(
                f"model_id={model_id} | model_name={model_name} | enabled={enabled} | "
                f"supports_vision={supports_vision} | available_locally={is_available}"
            )
            if supports_vision in {"false", "unknown"}:
                print(
                    f"  WARNING: {model_id} should not be used as VLM evidence until an image smoke test passes."
                )
            if is_available:
                print(f"  OK: local model is available.")
            else:
                print(f"  MISSING: Run: ollama pull {model_name}")
                if enabled:
                    had_error = True
    return 1 if had_error else 0


def fetch_ollama_tags(base_url: str) -> set[str] | None:
    url = f"{base_url}/api/tags"
    request = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"Ollama is not reachable at {base_url}. Start it with: ollama serve")
        print(f"Details: {exc}")
        return None

    models = payload.get("models", [])
    names: set[str] = set()
    for item in models:
        if isinstance(item, dict):
            name = item.get("name") or item.get("model")
            if name:
                names.add(str(name))
    return names


if __name__ == "__main__":
    raise SystemExit(main())
