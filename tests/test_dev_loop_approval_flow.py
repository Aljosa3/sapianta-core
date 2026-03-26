import os
import json
import pytest

from runtime.development.dev_autonomous_loop import DevAutonomousLoop
from runtime.development.dev_task_registry import DevTaskRegistry


@pytest.fixture
def clean_registry(tmp_path, monkeypatch):
    """
    Isolated registry file for deterministic testing.
    """

    test_file = tmp_path / "task_registry.json"

    # patch registry path
    monkeypatch.setattr(
        "runtime.development.dev_task_registry.REGISTRY_FILE",
        str(test_file)
    )

    # init empty registry
    with open(test_file, "w") as f:
        json.dump({
            "active_tasks": [],
            "completed_tasks": [],
            "failed_tasks": []
        }, f)

    return test_file


def create_test_task():
    return {
        "goal": "test approval flow",
        "priority": 1,
        "id": "test-task-1"
    }


def get_task_by_goal(tasks, goal):
    return next((t for t in tasks if t.get("goal") == goal), None)


# ---------------------------------------------------------
# TEST 1 — waiting_approval persistence
# ---------------------------------------------------------

def test_waiting_approval_persisted(clean_registry):

    registry = DevTaskRegistry()

    task = create_test_task()
    registry.add_task(task)

    registry.update_task_state(task, "waiting_approval")

    registry2 = DevTaskRegistry()
    tasks = registry2.get_tasks_by_state("waiting_approval")

    assert len(tasks) == 1

    t = get_task_by_goal(tasks, "test approval flow")
    assert t is not None
    assert t["state"] == "waiting_approval"


# ---------------------------------------------------------
# TEST 2 — approval sets correct state
# ---------------------------------------------------------

def test_approve_sets_state(clean_registry):

    registry = DevTaskRegistry()

    task = create_test_task()
    registry.add_task(task)
    registry.update_task_state(task, "waiting_approval")

    registry.update_task_state(task, "approved")

    registry2 = DevTaskRegistry()
    tasks = registry2.get_tasks_by_state("approved")

    assert len(tasks) == 1

    t = get_task_by_goal(tasks, "test approval flow")
    assert t is not None
    assert t["state"] == "approved"


# ---------------------------------------------------------
# TEST 3 — approved task does NOT trigger approval again
# ---------------------------------------------------------

def test_approved_task_skips_reapproval(clean_registry, monkeypatch):

    loop = DevAutonomousLoop()
    registry = loop.registry   # 🔥 FIX

    task = create_test_task()
    task["approved"] = True

    registry.add_task(task)
    registry.update_task_state(task, "approved")

    class FakeOrchestrator:
        def run_auto(self, task, *args, **kwargs):
            return {"success": True}

    monkeypatch.setattr(
        "runtime.development.dev_orchestrator.DevelopmentOrchestrator",
        lambda: FakeOrchestrator()
    )

    result = loop.run_once()

    assert result["status"] == "completed"


# ---------------------------------------------------------
# TEST 4 — full flow simulation
# ---------------------------------------------------------

def test_full_flow(clean_registry, monkeypatch):

    loop = DevAutonomousLoop()
    registry = loop.registry   # 🔥 FIX

    task = create_test_task()
    registry.add_task(task)

    registry.update_task_state(task, "waiting_approval")

    tasks = registry.get_tasks_by_state("waiting_approval")
    assert len(tasks) == 1

    registry.update_task_state(task, "approved")
    task["approved"] = True

    class FakeOrchestrator:
        def run_auto(self, task, *args, **kwargs):
            return {"success": True}

    monkeypatch.setattr(
        "runtime.development.dev_orchestrator.DevelopmentOrchestrator",
        lambda: FakeOrchestrator()
    )

    result = loop.run_once()

    assert result["status"] == "completed"

    registry2 = DevTaskRegistry()
    completed = registry2.get_tasks_by_state("completed")

    assert len(completed) == 1

    t = get_task_by_goal(completed, "test approval flow")
    assert t is not None