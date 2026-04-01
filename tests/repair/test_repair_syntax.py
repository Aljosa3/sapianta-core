import tempfile
from pathlib import Path

from runtime.development.dev_orchestrator import DevOrchestrator


def run_repair(file_path: Path):
    orch = DevOrchestrator()

    # 🔥 CRITICAL FIX: vključimo file
    failure_info = {
        "success": False,
        "error": "SyntaxError",
        "output": "",
        "file": str(file_path),  # ✅ KLJUČNI FIX
    }

    implementation_plan = [str(file_path)]

    fixes = orch.auto_fix_engine.generate_fixes(failure_info)

    for attempt in range(3):
        for fix in fixes:

            # 🔥 dodatna varnost (preskoči invalid fixes)
            fix_code = fix.get("code")
            if not isinstance(fix_code, str) or not fix_code.strip():
                continue

            applied = orch.apply_fix(fix, implementation_plan)

            if not applied:
                continue

            try:
                code = file_path.read_text()
                namespace = {}

                # 🔥 compile check (hitrejši fail)
                compile(code, str(file_path), "exec")
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