# ai-docstring-assistant

Uses `ast` to find public functions and classes without docstrings in a Python codebase, and builds one short prompt per item for an AI assistant (Claude Code, OpenAI Codex or any other model). Each prompt covers a single function, so whoever reviews the result can check each docstring instead of approving a whole rewritten file.

## Why one prompt per item

When you ask a model to document an entire file, most docstrings come out plausible and a few come out wrong, and the wrong ones are hard to find. With one function per prompt the diff stays small and the review is quick. The goal is more documentation without losing accuracy.

## Usage

```bash
python -m ai_docstring_assistant.cli path/to/file.py
```

````
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
````

The tool makes no network calls. Pipe the output into the LLM client you already use, review the answer and paste it in as the docstring.

## Development

```bash
pip install pytest ruff
pytest
ruff check .
```

## License

MIT, see [LICENSE](LICENSE).
