"""Finds public functions/classes without docstrings using the `ast` module."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MissingDocstring:
    file_path: str
    qualified_name: str
    kind: str  # "function" | "class" | "method"
    lineno: int
    source_snippet: str


def _is_public(name: str) -> bool:
    return not name.startswith("_")


def scan_source(source: str, file_path: str = "<string>") -> list[MissingDocstring]:
    tree = ast.parse(source)
    lines = source.splitlines()
    results: list[MissingDocstring] = []

    def visit(node: ast.AST, prefix: str = "") -> None:
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if _is_public(child.name):
                    if ast.get_docstring(child) is None:
                        kind = "method" if prefix else "function"
                        snippet = "\n".join(lines[child.lineno - 1 : child.lineno + 1])
                        results.append(
                            MissingDocstring(
                                file_path=file_path,
                                qualified_name=f"{prefix}{child.name}",
                                kind=kind,
                                lineno=child.lineno,
                                source_snippet=snippet,
                            )
                        )
                    # Only descend into a function's own nested defs if it's
                    # part of the public API surface; nested defs inside a
                    # private function aren't public API either.
                    visit(child, prefix=f"{prefix}{child.name}.")
            elif isinstance(child, ast.ClassDef):
                if _is_public(child.name):
                    if ast.get_docstring(child) is None:
                        snippet = "\n".join(lines[child.lineno - 1 : child.lineno + 1])
                        results.append(
                            MissingDocstring(
                                file_path=file_path,
                                qualified_name=f"{prefix}{child.name}",
                                kind="class",
                                lineno=child.lineno,
                                source_snippet=snippet,
                            )
                        )
                    # Don't report methods of a private class as missing
                    # docstrings: if the class itself isn't public API,
                    # neither are its members.
                    visit(child, prefix=f"{prefix}{child.name}.")
            else:
                visit(child, prefix=prefix)

    visit(tree)
    return results


def scan_file(path: str | Path) -> list[MissingDocstring]:
    path = Path(path)
    return scan_source(path.read_text(), file_path=str(path))
