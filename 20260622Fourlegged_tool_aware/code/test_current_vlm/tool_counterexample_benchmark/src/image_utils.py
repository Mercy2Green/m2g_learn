from __future__ import annotations

import base64
import mimetypes
from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
PLACEHOLDER_IMAGE = "__placeholder_image__"


def list_images(image_dir: str | Path, root_dir: str | Path, allow_placeholder: bool = False) -> list[Path]:
    path = Path(image_dir)
    if not path.is_absolute():
        path = Path(root_dir) / path
    if not path.exists() or not path.is_dir():
        return [Path(PLACEHOLDER_IMAGE)] if allow_placeholder else []
    images = sorted(item for item in path.iterdir() if item.suffix.lower() in IMAGE_EXTENSIONS and item.is_file())
    if not images and allow_placeholder:
        return [Path(PLACEHOLDER_IMAGE)]
    return images


def is_placeholder_image(image_path: str | Path) -> bool:
    return str(image_path) == PLACEHOLDER_IMAGE


def image_to_data_url(image_path: str | Path) -> str:
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image file not found: {path}")
    mime_type = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def image_to_base64(image_path: str | Path) -> str:
    """Return raw base64 image string without a data URL prefix."""
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image file not found: {path}")
    return base64.b64encode(path.read_bytes()).decode("ascii")
