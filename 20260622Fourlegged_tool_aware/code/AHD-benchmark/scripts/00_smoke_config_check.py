from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.load_config import load_dotenv, load_yaml
from src.spec_checks import check_generation_plan_totals


def main() -> None:
    load_dotenv(ROOT / ".env")
    config_paths = sorted((ROOT / "configs").glob("*.yaml"))
    configs = {path.name: load_yaml(path) for path in config_paths}
    models = configs.get("models.yaml", {})
    if "models" not in models:
        raise SystemExit("configs/models.yaml parsed but does not contain models")
    errors = check_generation_plan_totals(configs["generation_plan_v01.yaml"])
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Loaded {len(config_paths)} config files.")
    print(f"models.yaml models: {len(models['models'])}")
    print("generation_plan_v01.yaml raw_scene_specs total: 2000")
    print("No model API calls were made.")


if __name__ == "__main__":
    main()
