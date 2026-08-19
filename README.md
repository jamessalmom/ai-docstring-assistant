# ai-docstring-assistant

Scans a Python codebase with `ast` for public functions/classes missing
docstrings, and builds small, focused prompts ready to send to an AI
coding assistant (Claude Code, OpenAI Codex, or any LLM you plug in) —
one function at a time, so the human reviewing the result can actually
verify each docstring instead of rubber-stamping a whole rewritten file.

## Why one prompt per item

Asking a model to "document this whole file" tends to produce plausible-
sounding but occasionally wrong docstrings that are tedious to spot-check.
Scoping each prompt to a single function/class with its own snippet keeps
the diff small and the review fast — which is the actual point of using
AI here: raise documentation coverage without lowering its accuracy.

## Usage

```bash
python -m ai_docstring_assistant.cli path/to/file.py
```

```
--- parse_amount (line 12) ---
You are documenting a function in a Python codebase.

File: path/to/file.py
Name: parse_amount

Source:
```python
def parse_amount(raw):
```

Write a concise docstring (Google style) for this function: one summary
line, then Args/Returns/Raises sections only if applicable. ...
```

This tool deliberately makes **no network calls** — pipe its output into
whichever LLM client/CLI you already use, and paste the result back as
the docstring after reviewing it.

## Development

```bash
pip install pytest ruff
pytest
ruff check .
```

## License

MIT — see [LICENSE](LICENSE).
