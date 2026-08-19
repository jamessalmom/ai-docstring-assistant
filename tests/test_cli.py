from pathlib import Path

from ai_docstring_assistant.cli import main


def test_cli_reports_no_missing_docstrings(tmp_path: Path, capsys):
    file_path = tmp_path / "clean.py"
    file_path.write_text('def foo():\n    """Has a docstring."""\n    return 1\n')

    exit_code = main([str(file_path)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "No missing docstrings" in captured.out


def test_cli_prints_prompt_for_missing_docstring(tmp_path: Path, capsys):
    file_path = tmp_path / "dirty.py"
    file_path.write_text("def foo():\n    return 1\n")

    main([str(file_path)])
    captured = capsys.readouterr()

    assert "foo" in captured.out
    assert "Google style" in captured.out
