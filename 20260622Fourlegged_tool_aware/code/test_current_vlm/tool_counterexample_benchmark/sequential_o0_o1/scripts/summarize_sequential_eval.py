from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from sequential_o0_o1.sequential_evaluator import summarize_raw_file  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize isolated sequential O0/O1 evaluation results.")
    parser.add_argument("--input_dir", required=True)
    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    if not input_dir.is_absolute():
        input_dir = (ROOT / input_dir).resolve()
    result = summarize_raw_file(input_dir)
    print(json.dumps({"input_dir": str(input_dir), **result}, ensure_ascii=False))


if __name__ == "__main__":
    main()
