from runtime.development.auto_fix_engine import AutoFixEngine


def test_type_error_repair(tmp_path):

    file = tmp_path / "test_module.py"

    file.write_text(
        "def f(a):\n    return a\n",
        encoding="utf-8"
    )

    engine = AutoFixEngine()

    failure_info = {
        "error": "TypeError: f() takes 1 positional argument but 2 were given",
        "file": str(file)
    }

    fixes = engine.generate_fixes(failure_info)

    type_fixes = [f for f in fixes if f.get("strategy") == "type_error_signature_fix"]

    assert type_fixes, "No TypeError fix generated"

    fix = type_fixes[0]

    assert "def f(a, arg2)" in fix["code"]


def test_full_self_healing_pipeline_type_error(tmp_path):

    file = tmp_path / "mod.py"

    file.write_text(
        "def f(a):\n    return a\n",
        encoding="utf-8"
    )

    from runtime.development.dev_orchestrator import DevOrchestrator

    orch = DevOrchestrator()

    failure_info = {
        "error": "TypeError: f() takes 1 positional argument but 2 were given",
        "file": str(file)
    }

    fixes = orch.auto_fix_engine.generate_fixes(failure_info)

    success = False

    for fix in fixes:
        if orch.apply_fix(fix, [str(file)]):
            try:
                code = file.read_text()
                compile(code, str(file), "exec")

                namespace = {}
                exec(code, namespace)

                assert namespace["f"](1, 2) == 1
                success = True
                break
            except Exception:
                continue

    assert success, "Pipeline repair failed"