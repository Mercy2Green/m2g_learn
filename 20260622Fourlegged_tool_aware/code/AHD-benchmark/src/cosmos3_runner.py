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
    target_output_size: str = "960x960"
    cosmos_resolution: str = "720"
    cosmos_aspect_ratio: str = "1,1"
    expected_width: int = 960
    expected_height: int = 960
    num_steps: int = 35
    guidance_scale: float = 6.0

    @property
    def framework_dir(self) -> Path:
        return self.cosmos_root / "framework"

    @property
    def python_bin(self) -> Path:
        return Path(self.conda_prefix) / "bin" / "python"


def ensure_output_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def select_cuda_visible_device_auto() -> str:
    """Return the least-used GPU index from nvidia-smi, or '0' if probing fails."""
    command = [
        "nvidia-smi",
        "--query-gpu=index,memory.used,memory.total",
        "--format=csv,noheader,nounits",
    ]
    try:
        completed = subprocess.run(command, text=True, capture_output=True, check=False, timeout=10)
    except Exception:
        return "0"
    if completed.returncode != 0:
        return "0"
    candidates: list[tuple[float, int, int]] = []
    for line in completed.stdout.splitlines():
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 3:
            continue
        try:
            index = int(parts[0])
            used = int(parts[1])
            total = int(parts[2])
        except ValueError:
            continue
        if total <= 0:
            continue
        used_ratio = used / total
        free = total - used
        candidates.append((used_ratio, -free, index))
    if not candidates:
        return "0"
    return str(sorted(candidates)[0][2])


def resolve_cuda_visible_devices(value: str) -> str:
    normalized = str(value).strip().lower()
    if normalized == "auto":
        return select_cuda_visible_device_auto()
    return str(value)


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
        "resolution": runtime.cosmos_resolution,
        "aspect_ratio": runtime.cosmos_aspect_ratio,
        "num_frames": 1,
        "num_steps": runtime.num_steps,
        "guidance": runtime.guidance_scale,
        "extra": {
            "spec_id": row.get("spec_id"),
            "spec_type": row.get("spec_type"),
            "prompt_source": row.get("prompt_source"),
            "target_output_size": runtime.target_output_size,
            "expected_width": runtime.expected_width,
            "expected_height": runtime.expected_height,
            "cosmos_resolution": runtime.cosmos_resolution,
            "cosmos_aspect_ratio": runtime.cosmos_aspect_ratio,
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


def find_generated_vision_image(output_dir: Path, sample_name: str) -> Path | None:
    candidates = [
        output_dir / "t2i" / "vision.jpg",
        output_dir / sample_name / "vision.jpg",
        output_dir / "vision.jpg",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate

    vision_matches = sorted(path for path in output_dir.rglob("vision.jpg") if path.is_file())
    if len(vision_matches) == 1:
        return vision_matches[0]

    image_matches = sorted(
        path for path in output_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png"}
    )
    if len(image_matches) == 1:
        return image_matches[0]

    return None


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
        return _result(row, "failed", runtime, error=str(exc), command=command_preview(command, runtime))

    sample_name = _safe_name(str(row["spec_id"]))
    generated = find_generated_vision_image(output_dir, sample_name)
    target = runtime.ahd_root / str(row["output_image_path"])
    error: str | None = None
    if completed.returncode == 0 and generated is not None:
        ensure_output_parent(target)
        shutil.copy2(generated, target)
    else:
        stderr_tail = completed.stderr.strip().splitlines()[-8:]
        stdout_tail = completed.stdout.strip().splitlines()[-8:]
        log_error = "\n".join(stderr_tail or stdout_tail) or f"returncode={completed.returncode}"
        if completed.returncode == 0 and generated is None:
            error = f"Generated image not found. {_output_dir_diagnostics(output_dir)}"
        else:
            error = f"{log_error}\n{_output_dir_diagnostics(output_dir)}"

    probe = probe_output_image(target)
    status = "success" if completed.returncode == 0 and probe["exists"] and probe["valid_image"] else "failed"
    return _result(
        row,
        status,
        runtime,
        error=None if status == "success" else error or probe.get("error"),
        command=command_preview(command, runtime),
        probe=probe,
        input_path=str(input_path),
        cosmos_output_dir=str(output_dir),
        cosmos_generated_image_path=str(generated) if generated is not None else None,
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
        fallback = _probe_image_with_stdlib(file_path)
        if fallback is not None:
            result.update(fallback)
        else:
            result["error"] = str(exc)
    return result


def _probe_image_with_stdlib(path: Path) -> dict[str, Any] | None:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        width = int.from_bytes(data[16:20], "big")
        height = int.from_bytes(data[20:24], "big")
        return {"valid_image": width > 0 and height > 0, "width": width, "height": height, "error": None}

    if data.startswith(b"\xff\xd8"):
        index = 2
        while index + 9 < len(data):
            if data[index] != 0xFF:
                index += 1
                continue
            marker = data[index + 1]
            index += 2
            if marker in {0xD8, 0xD9}:
                continue
            if index + 2 > len(data):
                break
            segment_length = int.from_bytes(data[index : index + 2], "big")
            if segment_length < 2 or index + segment_length > len(data):
                break
            if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
                height = int.from_bytes(data[index + 3 : index + 5], "big")
                width = int.from_bytes(data[index + 5 : index + 7], "big")
                return {"valid_image": width > 0 and height > 0, "width": width, "height": height, "error": None}
            index += segment_length

    return None


def _result(
    row: dict[str, Any],
    status: str,
    runtime: Cosmos3Runtime,
    *,
    error: str | None,
    command: str,
    probe: dict[str, Any] | None = None,
    input_path: str | None = None,
    cosmos_output_dir: str | None = None,
    cosmos_generated_image_path: str | None = None,
) -> dict[str, Any]:
    result = {
        "spec_id": row.get("spec_id"),
        "spec_type": row.get("spec_type"),
        "view_stage": row.get("view_stage"),
        "output_image_path": row.get("output_image_path"),
        "output_image_path_is_placeholder": row.get("output_image_path_is_placeholder"),
        "legacy_output_image_path": row.get("legacy_output_image_path"),
        "runtime_output_layout": row.get("runtime_output_layout"),
        "status": status,
        "seed": row.get("seed"),
        "error": error,
        "generator": "Cosmos3-Nano",
        "command": command,
        "target_output_size": runtime.target_output_size,
        "cosmos_resolution": runtime.cosmos_resolution,
        "cosmos_aspect_ratio": runtime.cosmos_aspect_ratio,
        "expected_width": runtime.expected_width,
        "expected_height": runtime.expected_height,
        "image_size_matches_expected": None,
        "warning": None,
    }
    if probe:
        width = probe.get("width")
        height = probe.get("height")
        matches_expected = (
            width == runtime.expected_width
            and height == runtime.expected_height
        )
        result.update({
            "image_exists": probe.get("exists"),
            "valid_image": probe.get("valid_image"),
            "width": width,
            "height": height,
            "image_size_matches_expected": matches_expected if width and height else None,
        })
        if status == "success" and not matches_expected:
            result["warning"] = "image_size_mismatch"
    if input_path:
        result["cosmos_input_path"] = input_path
    if cosmos_output_dir:
        result["cosmos_output_dir"] = cosmos_output_dir
    if cosmos_generated_image_path:
        result["cosmos_generated_image_path"] = cosmos_generated_image_path
    return result


def _legacy_target_size_to_cosmos_fields(resolution: str) -> tuple[str, str]:
    """Convert a legacy target pixel size into Cosmos preset fields.

    This is retained only for old callers. The primary configuration path is
    explicit `cosmos_input.resolution` plus `cosmos_input.aspect_ratio`.
    Cosmos `resolution` is an internal preset/bucket, not a final pixel size.
    """
    value = str(resolution).lower().strip()
    if "x" not in value:
        return value, "1,1"
    width_text, height_text = value.split("x", 1)
    width = int(width_text)
    height = int(height_text)
    exact_image_tiers = {
        (256, 256): ("256", "1,1"),
        (640, 640): ("480", "1,1"),
        (960, 960): ("720", "1,1"),
        (1024, 1024): ("768", "1,1"),
        (1440, 1440): ("1080", "1,1"),
        (1280, 720): ("720", "16,9"),
        (720, 1280): ("720", "9,16"),
        (1024, 768): ("768", "4,3"),
        (768, 1024): ("768", "3,4"),
    }
    if (width, height) in exact_image_tiers:
        return exact_image_tiers[(width, height)]

    if width == height:
        raise ValueError(
            f"Unsupported square Cosmos3 image size: {resolution}. "
            "Use one of 256x256, 640x640, 960x960, 1024x1024, 1440x1440."
        )
    if width * 9 == height * 16:
        return str(height), "16,9"
    if width * 16 == height * 9:
        return str(height), "9,16"
    if width * 3 == height * 4:
        return str(height), "4,3"
    if width * 4 == height * 3:
        return str(height), "3,4"
    raise ValueError(f"Unsupported Cosmos3 resolution/aspect ratio: {resolution}")


def _output_dir_diagnostics(output_dir: Path, max_entries: int = 20) -> str:
    if not output_dir.exists():
        return f"output_dir does not exist: {output_dir}"
    files = sorted(path for path in output_dir.rglob("*") if path.is_file())
    if not files:
        return f"output_dir contains no files: {output_dir}"
    entries = [f"{path.relative_to(output_dir)} ({path.stat().st_size} bytes)" for path in files[:max_entries]]
    suffix = "" if len(files) <= max_entries else f"; ... {len(files) - max_entries} more files"
    return f"output_dir files: {entries}{suffix}"


def _safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in value)


def _shell_quote(value: str) -> str:
    if not value:
        return "''"
    if all(ch.isalnum() or ch in "/._=:-" for ch in value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"
