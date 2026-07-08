from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Cosmos3Runtime:
    ahd_root: Path
    cosmos_root: Path
    conda_prefix: str = "/data0/yurunze/conda_envs/codex_cosmos"
    checkpoint_path: str = "/data0/yurunze/models/Cosmos3-Nano"
    hf_home: str = "/data0/yurunze/models/hf-cache"
    cuda_visible_devices: str = "1"
    extra_args: tuple[str, ...] = ("--no-use-torch-compile",)

    @property
    def framework_dir(self) -> Path:
        return self.cosmos_root / "framework"

    @property
    def python_bin(self) -> Path:
        return Path(self.conda_prefix) / "bin" / "python"


def ensure_output_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def build_cosmos3_command(
    row: dict[str, Any],
    runtime: Cosmos3Runtime,
    *,
    work_dir: Path,
) -> tuple[list[str], Path, Path]:
    sample_name = _safe_name(str(row["spec_id"]))
    input_path = work_dir / "inputs" / f"{sample_name}.json"
    output_dir = work_dir / "outputs" / sample_name
    input_path.parent.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    sample = {
        "name": sample_name,
        "model_mode": "text2image",
        "prompt": str(row["prompt"]),
        "negative_prompt": str(row.get("negative_prompt", "")),
        "seed": int(row.get("seed", 0)),
        "resolution": "720",
        "aspect_ratio": "1,1",
        "num_frames": 1,
        "num_steps": 35,
        "guidance": 6.0,
        "extra": {
            "spec_id": row.get("spec_id"),
            "spec_type": row.get("spec_type"),
            "prompt_source": row.get("prompt_source"),
        },
    }
    input_path.write_text(json.dumps(sample, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    command = [
        str(runtime.python_bin),
        "-m",
        "cosmos_framework.scripts.inference",
        "--parallelism-preset=latency",
        *runtime.extra_args,
        "-i",
        str(input_path),
        "-o",
        str(output_dir),
        "--checkpoint-path",
        runtime.checkpoint_path,
        "--seed",
        str(int(row.get("seed", 0))),
        "--no-guardrails",
    ]
    return command, input_path, output_dir


def command_preview(command: list[str], runtime: Cosmos3Runtime) -> str:
    env_prefix = (
        f"COSMOS_CONDA_PREFIX={runtime.conda_prefix} "
        f"CHECKPOINT_PATH={runtime.checkpoint_path} "
        f"HF_HOME={runtime.hf_home} "
        f"CUDA_VISIBLE_DEVICES={runtime.cuda_visible_devices} "
        "LD_LIBRARY_PATH= "
    )
    return env_prefix + " ".join(_shell_quote(part) for part in command)


def run_cosmos3_one(
    row: dict[str, Any],
    runtime: Cosmos3Runtime,
    *,
    work_dir: Path,
    timeout_seconds: int | None = None,
) -> dict[str, Any]:
    ensure_output_parent(row["output_image_path"])
    command, input_path, output_dir = build_cosmos3_command(row, runtime, work_dir=work_dir)
    env = os.environ.copy()
    env.update({
        "COSMOS_CONDA_PREFIX": runtime.conda_prefix,
        "CHECKPOINT_PATH": runtime.checkpoint_path,
        "HF_HOME": runtime.hf_home,
        "CUDA_VISIBLE_DEVICES": runtime.cuda_visible_devices,
        "LD_LIBRARY_PATH": "",
        "PYTORCH_CUDA_ALLOC_CONF": env.get("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True"),
    })
    try:
        completed = subprocess.run(
            command,
            cwd=runtime.framework_dir,
            env=env,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
    except Exception as exc:  # pragma: no cover - subprocess environment dependent
        return _result(row, "failed", error=str(exc), command=command_preview(command, runtime))

    generated = output_dir / _safe_name(str(row["spec_id"])) / "vision.jpg"
    target = runtime.ahd_root / str(row["output_image_path"])
    error: str | None = None
    if completed.returncode == 0 and generated.exists():
        ensure_output_parent(target)
        shutil.copy2(generated, target)
    else:
        stderr_tail = completed.stderr.strip().splitlines()[-8:]
        stdout_tail = completed.stdout.strip().splitlines()[-8:]
        error = "\n".join(stderr_tail or stdout_tail) or f"returncode={completed.returncode}"

    probe = probe_output_image(target)
    status = "success" if completed.returncode == 0 and probe["exists"] and probe["valid_image"] else "failed"
    return _result(
        row,
        status,
        error=None if status == "success" else error or probe.get("error"),
        command=command_preview(command, runtime),
        probe=probe,
        input_path=str(input_path),
        cosmos_output_dir=str(output_dir),
    )


def probe_output_image(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    result: dict[str, Any] = {
        "path": str(file_path),
        "exists": file_path.exists(),
        "valid_image": False,
        "width": None,
        "height": None,
        "error": None,
    }
    if not file_path.exists():
        result["error"] = "missing_file"
        return result
    try:
        from PIL import Image

        with Image.open(file_path) as image:
            image.verify()
            result["width"], result["height"] = image.size
            result["valid_image"] = True
    except Exception as exc:  # pragma: no cover - depends on local image/Pillow
        result["error"] = str(exc)
    return result


def _result(
    row: dict[str, Any],
    status: str,
    *,
    error: str | None,
    command: str,
    probe: dict[str, Any] | None = None,
    input_path: str | None = None,
    cosmos_output_dir: str | None = None,
) -> dict[str, Any]:
    result = {
        "spec_id": row.get("spec_id"),
        "spec_type": row.get("spec_type"),
        "view_stage": row.get("view_stage"),
        "output_image_path": row.get("output_image_path"),
        "status": status,
        "seed": row.get("seed"),
        "error": error,
        "generator": "Cosmos3-Nano",
        "command": command,
    }
    if probe:
        result.update({
            "image_exists": probe.get("exists"),
            "valid_image": probe.get("valid_image"),
            "width": probe.get("width"),
            "height": probe.get("height"),
        })
    if input_path:
        result["cosmos_input_path"] = input_path
    if cosmos_output_dir:
        result["cosmos_output_dir"] = cosmos_output_dir
    return result


def _safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in value)


def _shell_quote(value: str) -> str:
    if not value:
        return "''"
    if all(ch.isalnum() or ch in "/._=:-" for ch in value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"
