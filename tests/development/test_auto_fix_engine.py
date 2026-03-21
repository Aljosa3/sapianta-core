import pytest

from runtime.development.auto_fix_engine import AutoFixEngine


@pytest.fixture
def engine():
    return AutoFixEngine()


def test_name_error_generates_stub(engine):

    failure_info = {
        "error": "NameError: name 'foo' is not defined",
        "system_context": {
            "missing_functions": ["foo"]
        }
    }

    fixes = engine.generate_fixes(failure_info)

    assert len(fixes) > 0
    assert any("def foo" in (f.get("code") or "") for f in fixes)


def test_import_error_generates_import(engine):

    failure_info = {
        "error": "ModuleNotFoundError: No module named 'requests'",
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert any("import requests" in (f.get("code") or "") for f in fixes)


def test_deterministic_output(engine):

    failure_info = {
        "error": "NameError: name 'foo' is not defined",
        "system_context": {
            "missing_functions": ["foo"]
        }
    }

    fixes_1 = engine.generate_fixes(failure_info)
    fixes_2 = engine.generate_fixes(failure_info)

    assert fixes_1 == fixes_2


def test_safe_fallback_present(engine):

    failure_info = {
        "error": "UnknownError",
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert any(f.get("strategy") == "safe_fallback" for f in fixes)


def test_empty_input(engine):

    fixes = engine.generate_fixes({})

    assert isinstance(fixes, list)


def test_syntax_error(engine):

    failure_info = {
        "error": "SyntaxError: invalid syntax",
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert len(fixes) > 0
