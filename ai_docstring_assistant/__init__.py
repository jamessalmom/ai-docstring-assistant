"""ai_docstring_assistant

A small CLI that scans a Python codebase for public functions/classes
missing docstrings and builds ready-to-review prompts for an AI coding
assistant (Claude Code, OpenAI Codex, or any LLM you plug in) to draft
them — plus a `LLMProvider` protocol so the actual model call is your
choice, not baked into this tool.

Built out of a real workflow: using AI agents to raise documentation and
test coverage on an existing codebase without spending hours doing it by
hand, while keeping a human in the loop for every generated docstring.
"""

from .prompts import build_docstring_prompt
from .scanner import MissingDocstring, scan_source

__all__ = ["MissingDocstring", "build_docstring_prompt", "scan_source"]
__version__ = "0.1.0"
