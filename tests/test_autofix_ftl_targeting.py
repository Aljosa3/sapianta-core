import pytest
from runtime.development.auto_fix_engine import AutoFixEngine


def test_ftl_detects_target_function_and_generates_fix(tmp_path):

    engine = AutoFixEngine()

    failure_info = {
        "error": "AssertionError: assert add(2, 3) == 5",
        "test_output": "E assert add(2, 3) == 5",
        "file": str(tmp_path / "test_add.py"),
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert fixes, "No fixes generated"

    replace_fixes = [
        f for f in fixes
        if f.get("action") == "replace_function"
    ]

    assert replace_fixes, "No replace_function fix generated"

    best_fix = replace_fixes[0]

    assert best_fix.get("function") == "add"
    assert "def add" in best_fix.get("code", "")
    assert best_fix.get("target_function") == "add"


def test_missing_function_stub_generated(tmp_path):

    engine = AutoFixEngine()

    failure_info = {
        "error": "ImportError: cannot import name 'calculate'",
        "test_output": "",
        "file": str(tmp_path / "test_calculate.py"),
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert fixes

    stub_fixes = [
        f for f in fixes
        if f.get("strategy") == "missing_function_stub"
    ]

    assert stub_fixes, "Missing function stub not generated"

    fix = stub_fixes[0]

    assert fix["function"] == "calculate"
    assert "def calculate" in fix["code"]


def test_name_error_generates_variable_stub(tmp_path):

    engine = AutoFixEngine()

    failure_info = {
        "error": "NameError: name 'x' is not defined",
        "test_output": "",
        "file": str(tmp_path / "module.py"),
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert fixes

    name_fixes = [
        f for f in fixes
        if f.get("strategy") == "name_error_variable_stub"
    ]

    assert name_fixes

    fix = name_fixes[0]

    assert "x = 0" in fix["code"]