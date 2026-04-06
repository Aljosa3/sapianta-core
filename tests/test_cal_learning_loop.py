import pytest

from runtime.development.cal_controller import CALController
from runtime.development.dev_task_registry import DevTaskRegistry


class DummyResult:
    def __init__(self, success):
        self.success = success


def test_score_increases_on_success():

    registry = DevTaskRegistry()
    cal = CALController(registry=registry)

    task = {
        "description": "explore_test_generation",
        "state": "queued",
        "metadata": {"score": 0.0}
    }

    result = DummyResult(success=True)

    cal._update_score_from_result(task, result)

    assert task["metadata"]["score"] > 0.0


def test_score_decreases_on_failure():

    registry = DevTaskRegistry()
    cal = CALController(registry=registry)

    task = {
        "description": "explore_test_generation",
        "state": "queued",
        "metadata": {"score": 0.0}
    }

    result = DummyResult(success=False)

    cal._update_score_from_result(task, result)

    assert task["metadata"]["score"] < 0.0


def test_score_is_clamped():

    registry = DevTaskRegistry()
    cal = CALController(registry=registry)

    task = {
        "description": "explore_test_generation",
        "state": "queued",
        "metadata": {"score": 1.0}
    }

    result = DummyResult(success=True)

    cal._update_score_from_result(task, result)

    assert task["metadata"]["score"] <= 1.0