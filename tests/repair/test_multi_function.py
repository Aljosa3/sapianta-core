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

                if all(k in namespace for k in ["a", "b", "c"]):
                    if (
                        namespace["a"]() == 1 and
                        namespace["b"]() == 2 and
                        namespace["c"]() == 3
                    ):
                        return True

            except Exception:
                pass

    return False


def test_only_target_function_is_fixed(tmp_path):
    file = tmp_path / "module.py"

    file.write_text("""
def a():
    return 1

def b()
    return 2

def c():
    return 3
""")

    success = run_repair(file)

    assert success is True