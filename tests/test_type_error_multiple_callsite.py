from pathlib import Path


def test_type_error_multiple_values_callsite(tmp_path):
    """
    Scenario:
    Function is correct, call-site is wrong.

    Expected:
    System fixes call-site (removes duplicate keyword argument)
    """

    # ------------------------------------------------------------
    # CREATE MODULE
    # ------------------------------------------------------------
    file = tmp_path / "mod.py"

    file.write_text(
        "def f(a):\n"
        "    return a\n\n"
        "def run():\n"
        "    return f(1, a=2)\n",
        encoding="utf-8"
    )

    # ------------------------------------------------------------
    # PREPARE FAILURE
    # ------------------------------------------------------------
    from runtime.development.dev_orchestrator import DevOrchestrator

    orch = DevOrchestrator()

    failure_info = {
        "error": "TypeError: f() got multiple values for argument 'a'",
        "file": str(file)
    }

    # ------------------------------------------------------------
    # GENERATE FIXES
    # ------------------------------------------------------------
    fixes = orch.auto_fix_engine.generate_fixes(failure_info)

    success = False

    # ------------------------------------------------------------
    # APPLY FIXES
    # ------------------------------------------------------------
    for fix in fixes:

        if not orch.apply_fix(fix, [str(file)]):
            continue

        try:
            code = file.read_text(encoding="utf-8")

            # must compile
            compile(code, str(file), "exec")

            namespace = {}
            exec(code, namespace)

            # run fixed function
            result = namespace["run"]()

            assert result == 1  # keyword argument removed

            success = True
            break

        except Exception:
            continue

    assert success, "Call-site repair failed"