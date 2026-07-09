from __future__ import annotations

from pathlib import Path
from typing import Any


def ahd_root() -> Path:
    return Path(__file__).resolve().parents[1]


def storage_config(config: dict[str, Any]) -> dict[str, Any]:
    return {
        "raw_runs_root": "data/generated_runs",
        "curated_pools_root": "data/curated_pools",
        "paired_datasets_root": "data/paired_datasets",
        "write_legacy_data_images": False,
        "curated_copy_mode": "copy",
        **dict(config.get("storage") or {}),
    }


def raw_runs_root(config: dict[str, Any], root: Path | None = None) -> Path:
    base = root or ahd_root()
    return base / str(storage_config(config)["raw_runs_root"])


def raw_run_dir(run_name: str, config: dict[str, Any], root: Path | None = None) -> Path:
    return raw_runs_root(config, root) / safe_name(run_name)


def raw_run_image_dir(run_name: str, view_stage: str, config: dict[str, Any], root: Path | None = None) -> Path:
    return raw_run_dir(run_name, config, root) / "images" / view_stage_dir(view_stage)


def raw_run_image_path(
    run_name: str,
    spec_id: str,
    view_stage: str,
    config: dict[str, Any],
    root: Path | None = None,
) -> Path:
    return raw_run_image_dir(run_name, view_stage, config, root) / f"{safe_name(spec_id)}.jpg"


def curated_pools_root(config: dict[str, Any], root: Path | None = None) -> Path:
    base = root or ahd_root()
    return base / str(storage_config(config)["curated_pools_root"])


def curated_pool_dir(pool_name: str, config: dict[str, Any], root: Path | None = None) -> Path:
    return curated_pools_root(config, root) / safe_name(pool_name)


def curated_pool_image_dir(pool_name: str, view_stage: str, config: dict[str, Any], root: Path | None = None) -> Path:
    return curated_pool_dir(pool_name, config, root) / "images" / view_stage_dir(view_stage)


def curated_pool_image_path(
    pool_name: str,
    spec_id: str,
    view_stage: str,
    config: dict[str, Any],
    root: Path | None = None,
) -> Path:
    return curated_pool_image_dir(pool_name, view_stage, config, root) / f"{safe_name(spec_id)}.jpg"


def paired_datasets_root(config: dict[str, Any], root: Path | None = None) -> Path:
    base = root or ahd_root()
    return base / str(storage_config(config)["paired_datasets_root"])


def view_stage_dir(view_stage: str) -> str:
    return "o0" if str(view_stage).upper() == "O0" else "o1"


def relative_to_root(path: Path, root: Path | None = None) -> str:
    base = root or ahd_root()
    resolved = path if path.is_absolute() else base / path
    try:
        return str(resolved.relative_to(base))
    except ValueError:
        return str(resolved)


def safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in value)
