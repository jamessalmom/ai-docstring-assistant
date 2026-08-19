from ai_docstring_assistant.prompts import build_docstring_prompt
from ai_docstring_assistant.scanner import MissingDocstring


def test_prompt_includes_context_and_instructions():
    item = MissingDocstring(
        file_path="app/utils.py",
        qualified_name="parse_amount",
        kind="function",
        lineno=12,
        source_snippet="def parse_amount(raw): ...",
    )
    prompt = build_docstring_prompt(item)
    assert "app/utils.py" in prompt
    assert "parse_amount" in prompt
    assert "Google style" in prompt
    assert "def parse_amount" in prompt
