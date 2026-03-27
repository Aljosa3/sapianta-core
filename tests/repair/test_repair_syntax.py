import tempfile
from pathlib import Path

from runtime.development.dev_orchestrator import DevOrchestrator


def run_repair(file_path: Path):
    orch = DevOrchestrator()

    # simulacija minimalnega failure info
    failure_info = {
        "success": False,
        "error": "SyntaxError",
        "output": "",
    }

    implementation_plan = [str(file_path)]

    fixes = orch.auto_fix_engine.generate_fixes(failure_info)

    for attempt in range(3):
        for fix in fixes:
            applied = orch.apply_fix(fix, implementation_plan)

            if not applied:
                continue

            try:
                code = file_path.read_text()
                namespace = {}
                exec(code, namespace)

                if "add" in namespace:
                    if namespace["add"](1, 2) == 3:
                        return {"success": True, "attempts": attempt + 1}

            except Exception:
                pass

    return {"success": False, "attempts": 3}


def test_syntax_error_repair(tmp_path):
    file = tmp_path / "module.py"

    broken_code = """
def add(a, b)
    return a + b
"""

    file.write_text(broken_code)

    result = run_repair(file)

    assert result["success"] is True

    fixed_code = file.read_text()

    # mora biti valid python
    compile(fixed_code, str(file), "exec")

    namespace = {}
    exec(fixed_code, namespace)

    assert namespace["add"](1, 2) == 3