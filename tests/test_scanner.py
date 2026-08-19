from ai_docstring_assistant.scanner import scan_source

SOURCE = '''
def documented():
    """Already has a docstring."""
    return 1


def undocumented(x, y):
    return x + y


class Foo:
    def method_without_doc(self):
        return None

    def _private_helper(self):
        return None


class _PrivateClass:
    def whatever(self):
        return None
'''


def test_finds_undocumented_top_level_function():
    missing = scan_source(SOURCE)
    names = [m.qualified_name for m in missing]
    assert "undocumented" in names
    assert "documented" not in names


def test_finds_undocumented_method_but_skips_private():
    missing = scan_source(SOURCE)
    names = [m.qualified_name for m in missing]
    assert "Foo.method_without_doc" in names
    assert "Foo._private_helper" not in names


def test_skips_private_classes_entirely():
    missing = scan_source(SOURCE)
    file_paths = [m.qualified_name for m in missing if "_PrivateClass" in m.qualified_name]
    assert file_paths == []
