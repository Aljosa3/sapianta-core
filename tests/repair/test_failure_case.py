from pathlib import Path
from runtime.development.dev_orchestrator import DevOrchestrator


def run_repair(file_path: Path):
    orch = DevOrchestrator()

    failure_info = {
        "success": False,
        "error": "SyntaxError",
        "output": "",
    }

    implementation_plan = [str(file_path)]

    fixes = orch.auto_fix_engine.generate_fixes(failure_info)

    for attempt in range(3):
        for fix in fixes:
            orch.apply_fix(fix, implementation_plan)

    return {"success": False}


def test_unfixable_code_fails_gracefully(tmp_path):
    file = tmp_path / "module.py"

    file.write_text("this is not python ### !!!")

    result = run_repair(file)

    assert result["success"] is False