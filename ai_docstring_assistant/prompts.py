"""Builds a focused prompt per missing docstring, ready to send to an LLM.

Deliberately small in scope per call: one function/class at a time keeps
the generated docstring accurate and easy for a human to review, instead
of asking a model to rewrite a whole file at once.
"""

from __future__ import annotations

from .scanner import MissingDocstring

_TEMPLATE = """You are documenting a {kind} in a Python codebase.

File: {file_path}
Name: {qualified_name}

Source:
```python
{snippet}
```

Write a concise docstring (Google style) for this {kind}: one summary \
line, then Args/Returns/Raises sections only if applicable. Do not \
change the code itself, only produce the docstring text."""


def build_docstring_prompt(item: MissingDocstring) -> str:
    return _TEMPLATE.format(
        kind=item.kind,
        file_path=item.file_path,
        qualified_name=item.qualified_name,
        snippet=item.source_snippet,
    )
