"""CLI: `python -m ai_docstring_assistant.cli path/to/file.py`.

Prints one ready-to-send prompt per missing docstring. Wire the output
into whichever LLM client you use — this tool intentionally does not
make network calls itself.
"""

from __future__ import annotations

import argparse
import sys

from .prompts import build_docstring_prompt
from .scanner import scan_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ai-docstring-assistant")
    parser.add_argument("path", help="Python file to scan")
    args = parser.parse_args(argv)

    missing = scan_file(args.path)
    if not missing:
        print(f"No missing docstrings found in {args.path}")
        return 0

    for item in missing:
        print(f"--- {item.qualified_name} (line {item.lineno}) ---")
        print(build_docstring_prompt(item))
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
