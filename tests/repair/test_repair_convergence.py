from pathlib import Path
from runtime.development.dev_orchestrator import DevOrchestrator


def run_repair(file_path: Path):
    orch = DevOrchestrator()

    failure_info = {
        "success": False,
        "error": "SyntaxError",
        "output": "",
        "file": str(file_path),   # 🔥 CRITICAL FIX
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


def test_repair_converges(tmp_path):
    file = tmp_path / "module.py"

    file.write_text("""
def add(a, b)
    return a + b
""")

    result = run_repair(file)

    assert result["success"] is True
    assert result["attempts"] <= 3