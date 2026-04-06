import pytest

from runtime.development.cal_controller import CALController
from runtime.development.dev_task_registry import DevTaskRegistry


def test_cal_generates_exploration_task_on_stagnation():

    # fresh registry → no tasks
    registry = DevTaskRegistry()

    cal = CALController(registry=registry)

    # 1. bootstrap
    cal.run_cycle()

    # 2. exploration
    tasks = cal.run_cycle()

    # CAL should generate something
    assert len(tasks) > 0

    task = tasks[0]

    # must be exploration task (NOT stagnation text)
    assert task["description"].startswith("explore_")

    # must be registered
    queued = registry.get_tasks_by_state("queued")
    assert len(queued) >= 1

    # ensure no raw stagnation description leaked
    assert "System idle detected" not in task["description"]


def test_cal_exploration_is_deterministic():

    registry = DevTaskRegistry()
    cal = CALController(registry=registry)

    # 1. bootstrap
    bootstrap = cal.run_cycle()[0]["description"]

    # 2. first exploration
    first = cal.run_cycle()[0]["description"]

    # 3. second exploration
    second = cal.run_cycle()[0]["description"]

    # bootstrap must NOT be exploration
    assert not bootstrap.startswith("explore_")

    # exploration must start after bootstrap
    assert first.startswith("explore_")
    assert second.startswith("explore_")

    # progression must exist
    assert first != second


def test_cal_does_not_duplicate_tasks():

    registry = DevTaskRegistry()
    cal = CALController(registry=registry)

    cal.run_cycle()
    cal.run_cycle()
    cal.run_cycle()

    queued = registry.get_tasks_by_state("queued")

    descriptions = [t["description"] for t in queued]

    # no duplicates allowed
    assert len(descriptions) == len(set(descriptions))