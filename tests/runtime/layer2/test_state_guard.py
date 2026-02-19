import pytest

from runtime.layer2.state_guard import StateGuard
from runtime.layer2.exceptions import StateMutationError


def test_no_mutation_pass():
    guard = StateGuard()
    state = {"x": 1}
    snapshot = guard.snapshot(state)
    guard.validate_no_mutation(state, snapshot)


def test_mutation_detected():
    guard = StateGuard()
    state = {"x": 1}
    snapshot = guard.snapshot(state)

    state["x"] = 2

    with pytest.raises(StateMutationError):
        guard.validate_no_mutation(state, snapshot)
