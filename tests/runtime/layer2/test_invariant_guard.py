import pytest

from runtime.layer2.invariant_guard import InvariantGuard
from runtime.layer2.exceptions import (
    PreInvariantViolationError,
    PostInvariantViolationError,
)


def always_true(state):
    return True


def always_false(state):
    return False


def test_pre_invariant_pass():
    guard = InvariantGuard()
    guard.validate_pre(1, [always_true])


def test_pre_invariant_fail():
    guard = InvariantGuard()

    with pytest.raises(PreInvariantViolationError):
        guard.validate_pre(1, [always_false])


def test_post_invariant_pass():
    guard = InvariantGuard()
    guard.validate_post(1, [always_true])


def test_post_invariant_fail():
    guard = InvariantGuard()

    with pytest.raises(PostInvariantViolationError):
        guard.validate_post(1, [always_false])
