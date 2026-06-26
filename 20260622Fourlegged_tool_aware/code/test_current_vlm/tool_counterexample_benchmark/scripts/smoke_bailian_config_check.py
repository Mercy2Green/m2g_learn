from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.image_utils import list_images  # noqa: E402
from src.load_config import enabled_items, load_dotenv, load_yaml  # noqa: E402


def main() -> int:
    load_dotenv(ROOT / ".env")
    models = enabled_items(load_yaml(ROOT / "config/models.yaml"), "models")
    tasks = load_yaml(ROOT / "config/tasks.yaml").get("tasks", [])

    errors: list[str] = []
    warnings: list[str] = []

    for model in models:
        model_id = model.get("model_id", "")
        if model.get("provider") == "openai_compatible":
            api_key_env = str(model.get("api_key_env", ""))
            if not api_key_env:
                errors.append(f"{model_id}: api_key_env is empty.")
            elif not os.environ.get(api_key_env):
                errors.append(f"{model_id}: environment variable {api_key_env} is not set.")
            base_url = str(model.get("base_url", ""))
            if not base_url:
                errors.append(f"{model_id}: base_url is empty.")
            elif "{WorkspaceId}" in base_url:
                errors.append(f"{model_id}: base_url still contains {{WorkspaceId}} placeholder.")
            if not model.get("model_name"):
                errors.append(f"{model_id}: model_name is empty.")
        elif model.get("provider") != "mock":
            warnings.append(f"{model_id}: config check only validates openai_compatible and mock providers.")

    for task in tasks:
        images = list_images(task.get("image_dir", ""), ROOT, allow_placeholder=False)
        if not images:
            warnings.append(f"{task.get('task_id')}: no images found in {task.get('image_dir')}.")

    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"- {warning}")
    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Config check passed. This script did not call any model API.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
