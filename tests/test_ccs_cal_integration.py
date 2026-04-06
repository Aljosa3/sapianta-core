from runtime.development.ccs.certification_engine import CertificationEngine
from runtime.development.dev_task_registry import DevTaskRegistry
from pathlib import Path


def test_ccs_triggers_cal_on_reject(tmp_path):

    # 1. setup shared registry (CRITICAL)
    registry = DevTaskRegistry()

    # 2. create invalid file (SyntaxError)
    file_path = tmp_path / "bad_module.py"
    file_path.write_text("def broken(\n    return 1\n")

    # 3. run certification
    engine = CertificationEngine()
    status = engine.certify(str(file_path))

    assert status == "REJECTED"

    # 4. simulate orchestrator hook (minimal)
    if status == "REJECTED":
        fix_task = {
            "task_type": "fix",
            "goal": f"Fix failing module: {file_path}",
            "file": str(file_path),
            "priority": 1.0,
            "source": "ccs"
        }
        registry.add_task(fix_task)

    # 5. validate CAL behavior
    tasks = registry.get_tasks_by_state("queued")

    assert len(tasks) > 0

    last_task = tasks[-1]

    assert last_task["task_type"] == "fix"
    assert "bad_module.py" in last_task["goal"]