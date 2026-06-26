from __future__ import annotations

import os
import re
import ast
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


ENV_PATTERN = re.compile(r"\$\{([A-Z0-9_]+)(?::-(.*?))?\}")


def load_dotenv(env_path: str | Path = ".env") -> None:
    path = Path(env_path)
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def _substitute_env(value: Any) -> Any:
    if isinstance(value, str):
        def replace(match: re.Match[str]) -> str:
            env_key = match.group(1)
            default = match.group(2) or ""
            return os.environ.get(env_key, default)

        return ENV_PATTERN.sub(replace, value)
    if isinstance(value, list):
        return [_substitute_env(item) for item in value]
    if isinstance(value, dict):
        return {key: _substitute_env(item) for key, item in value.items()}
    return value


def load_yaml(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")
    text = file_path.read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text) or {}
    else:
        data = _load_yaml_subset(text)
    if not isinstance(data, dict):
        raise ValueError(f"YAML root must be a mapping: {file_path}")
    return _substitute_env(data)


def _load_yaml_subset(text: str) -> dict[str, Any]:
    """Parse the small YAML subset used by this benchmark when PyYAML is absent.

    This is intentionally limited: mappings, lists, inline scalar lists, quoted
    strings, booleans, numbers, and literal block scalars. Install PyYAML for
    general YAML support.
    """
    raw_lines = text.splitlines()
    lines: list[tuple[int, str, int]] = []
    for line_no, raw in enumerate(raw_lines):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        lines.append((indent, raw.strip(), line_no))
    if not lines:
        return {}
    parsed, index = _parse_yaml_block(lines, 0, lines[0][0], raw_lines)
    if index != len(lines):
        raise ValueError("Could not parse complete YAML file with fallback parser.")
    if not isinstance(parsed, dict):
        raise ValueError("Fallback YAML parser expected a mapping at root.")
    return parsed


def _parse_yaml_block(
    lines: list[tuple[int, str, int]],
    index: int,
    indent: int,
    raw_lines: list[str],
) -> tuple[Any, int]:
    if index >= len(lines):
        return {}, index
    is_list = lines[index][0] == indent and lines[index][1].startswith("- ")
    if is_list:
        result: list[Any] = []
        while index < len(lines):
            current_indent, content, _line_no = lines[index]
            if current_indent < indent:
                break
            if current_indent > indent:
                break
            if not content.startswith("- "):
                break
            item_text = content[2:].strip()
            index += 1
            if not item_text:
                item, index = _parse_yaml_block(lines, index, _next_indent(lines, index, indent), raw_lines)
                result.append(item)
                continue
            if _looks_like_key_value(item_text):
                key, value_text = _split_key_value(item_text)
                item_dict: dict[str, Any] = {}
                item_dict[key] = _parse_yaml_value(value_text)
                if index < len(lines) and lines[index][0] > indent:
                    child, index = _parse_yaml_block(lines, index, lines[index][0], raw_lines)
                    if isinstance(child, dict):
                        item_dict.update(child)
                    else:
                        raise ValueError("List item continuation must be a mapping.")
                result.append(item_dict)
            else:
                result.append(_parse_yaml_value(item_text))
        return result, index

    result_dict: dict[str, Any] = {}
    while index < len(lines):
        current_indent, content, line_no = lines[index]
        if current_indent < indent:
            break
        if current_indent > indent:
            break
        if not _looks_like_key_value(content):
            raise ValueError(f"Invalid YAML mapping line: {content}")
        key, value_text = _split_key_value(content)
        index += 1
        if value_text == "|":
            value, index = _collect_block_scalar(lines, index, current_indent, raw_lines, line_no)
        elif value_text == "":
            if index < len(lines) and lines[index][0] > current_indent:
                value, index = _parse_yaml_block(lines, index, lines[index][0], raw_lines)
            else:
                value = {}
        else:
            value = _parse_yaml_value(value_text)
        result_dict[key] = value
    return result_dict, index


def _collect_block_scalar(
    lines: list[tuple[int, str, int]],
    index: int,
    parent_indent: int,
    raw_lines: list[str],
    parent_line_no: int,
) -> tuple[str, int]:
    collected: list[str] = []
    block_indent: int | None = None
    while index < len(lines):
        indent, _content, line_no = lines[index]
        if indent <= parent_indent:
            break
        if block_indent is None:
            block_indent = indent
        raw = raw_lines[line_no]
        collected.append(raw[block_indent:])
        index += 1
    if block_indent is None:
        return "", index
    return "\n".join(collected).rstrip(), index


def _next_indent(lines: list[tuple[int, str, int]], index: int, fallback: int) -> int:
    if index < len(lines):
        return lines[index][0]
    return fallback + 2


def _looks_like_key_value(text: str) -> bool:
    return ":" in text and not text.startswith(("http://", "https://"))


def _split_key_value(text: str) -> tuple[str, str]:
    key, value = text.split(":", 1)
    return key.strip(), value.strip()


def _parse_yaml_value(text: str) -> Any:
    if text == "":
        return ""
    lower = text.lower()
    if lower == "true":
        return True
    if lower == "false":
        return False
    if lower in {"null", "none"}:
        return None
    if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
        return ast.literal_eval(text)
    if (text.startswith("[") and text.endswith("]")) or (text.startswith("{") and text.endswith("}")):
        return ast.literal_eval(text)
    try:
        if "." in text:
            return float(text)
        return int(text)
    except ValueError:
        return text


def enabled_items(config: dict[str, Any], key: str) -> list[dict[str, Any]]:
    items = config.get(key, [])
    if not isinstance(items, list):
        raise ValueError(f"Config key '{key}' must be a list")
    return [item for item in items if item.get("enabled", True)]


def snapshot_configs(paths: list[str | Path], output_dir: str | Path) -> None:
    snapshot_dir = Path(output_dir) / "config_snapshot"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    for path in paths:
        src = Path(path)
        if src.exists():
            (snapshot_dir / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
