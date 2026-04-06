import pytest

from runtime.development.cal_controller import CALController
from runtime.development.dev_task_registry import DevTaskRegistry


class DummyResult:
    def __init__(self, success):
        self.success = success


def test_fix_task_generated_on_failure():

    registry = DevTaskRegistry()
    cal = CALController(registry=registry)

    # simulate task
    task = {
        "description": "explore_test_generation",
        "state": "queued",
        "metadata": {"score": -0.5}
    }

    # simulate failure
    result = DummyResult(success=False)

    # apply learning update
    cal._update_score_from_result(task, result)

    # decision
    if cal._should_generate_fix(task):

        fix_description = f"fix_{task['description']}"

        fix_task = {
            "description": fix_description,
            "state": "queued",
            "metadata": {"score": 0.0}
        }

        registry.add_task(fix_task)

    queued = registry.get_tasks_by_state("queued")

    assert any(t["description"].startswith("fix_") for t in queued)


def test_no_fix_task_on_success():

    registry = DevTaskRegistry()
    cal = CALController(registry=registry)

    task = {
        "description": "explore_test_generation",
        "state": "queued",
        "metadata": {"score": 0.5}
    }

    result = DummyResult(success=True)

    cal._update_score_from_result(task, result)

    assert not cal._should_generate_fix(task)