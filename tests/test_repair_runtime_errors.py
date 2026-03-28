from runtime.development.auto_fix_engine import AutoFixEngine


def test_name_error_repair():

    engine = AutoFixEngine()

    failure_info = {
        "error": "NameError: name 'a' is not defined",
        "file": "runtime/development/generated/test_module.py",
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert len(fixes) > 0

    assert any(
        fix["strategy"] == "name_error_variable_stub"
        for fix in fixes
    )


def test_import_error_repair():

    engine = AutoFixEngine()

    failure_info = {
        "error": "ModuleNotFoundError: No module named 'non_existing_module'",
        "file": "runtime/development/generated/test_module.py",
        "system_context": {}
    }

    fixes = engine.generate_fixes(failure_info)

    assert len(fixes) > 0

    assert any(
        fix["strategy"] == "import_error_try_wrapper"
        for fix in fixes
    )