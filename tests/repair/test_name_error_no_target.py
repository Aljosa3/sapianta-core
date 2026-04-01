import pytest
from runtime.development.auto_fix_engine import AutoFixEngine


def test_name_error_without_target_file_resolution(tmp_path):
    """
    🔥 CRITICAL TEST:
    NameError without target_function must still resolve valid file_path
    """

    # create fake generated module
    module_path = tmp_path / "my_module.py"
    module_path.write_text("print(x)\n")  # NameError: x

    failure_info = {
        "error": "NameError: name 'x' is not defined",
        "test_output": f"""
Traceback (most recent call last):
  File "{module_path}", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
""",
        "file": str(module_path),
        "system_context": {}
    }

    engine = AutoFixEngine()

    fixes = engine.generate_fixes(failure_info)

    # =====================================================
    # ASSERTIONS
    # =====================================================

    assert fixes, "❌ No fixes generated"

    # 🔥 CRITICAL: all fixes must target correct file
    for fix in fixes:
        assert fix["file"] == str(module_path), \
            f"❌ Wrong target file: {fix['file']}"

    # 🔥 CRITICAL: must include NameError fix
    strategies = [f["strategy"] for f in fixes]

    assert any("name_error" in s for s in strategies), \
        "❌ NameError fix missing"

def test_name_error_function_stub(tmp_path):

    module = tmp_path / "m.py"
    module.write_text("foo(1,2)\n")

    failure_info = {
        "error": "NameError: name 'foo' is not defined",
        "test_output": f"""
Traceback (most recent call last):
  File "{module}", line 1, in <module>
    foo(1,2)
NameError: name 'foo' is not defined
""",
        "file": str(module),
        "system_context": {}
    }

    from runtime.development.auto_fix_engine import AutoFixEngine

    engine = AutoFixEngine()
    fixes = engine.generate_fixes(failure_info)

    strategies = [f["strategy"] for f in fixes]

    assert "name_error_function_stub" in strategies, \
        "❌ Function stub was not generated"