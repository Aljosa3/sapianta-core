import pytest

from runtime.layer2.control_engine import ControlEngine
from runtime.layer2.policy_evaluator import PolicyEvaluator
from runtime.layer2.state_transition_executor import StateTransitionExecutor
from runtime.layer2.audit_trace_collector import AuditTraceCollector
from runtime.layer2.transition_contract import TransitionContract
from runtime.layer2.exceptions import (
    PolicyDeniedError,
    PreInvariantViolationError,
    PostInvariantViolationError,
)


class AllowPolicy(PolicyEvaluator):
    def evaluate(self, event_id, state):
        return True


class DenyPolicy(PolicyEvaluator):
    def evaluate(self, event_id, state):
        return False


def increment(state):
    return state + 1


def always_true(state):
    return True


def always_false(state):
    return False


def build_engine(policy):
    return ControlEngine(
        policy_evaluator=policy,
        transition_executor=StateTransitionExecutor(),
        audit_collector=AuditTraceCollector(),
    )


def test_control_engine_happy_path():
    engine = build_engine(AllowPolicy())

    contract = TransitionContract(
        event_id="E1",
        state_type=int,
        transition_fn=increment,
        pre_invariants=[always_true],
        post_invariants=[always_true],
    )

    trace = engine.process("E1", 1, contract)

    assert trace["allowed"] is True
    assert trace["new_state"] == 2


def test_policy_denied():
    engine = build_engine(DenyPolicy())

    contract = TransitionContract(
        event_id="E1",
        state_type=int,
        transition_fn=increment,
        pre_invariants=[],
        post_invariants=[],
    )

    with pytest.raises(PolicyDeniedError):
        engine.process("E1", 1, contract)


def test_pre_invariant_failure():
    engine = build_engine(AllowPolicy())

    contract = TransitionContract(
        event_id="E1",
        state_type=int,
        transition_fn=increment,
        pre_invariants=[always_false],
        post_invariants=[always_true],
    )

    with pytest.raises(PreInvariantViolationError):
        engine.process("E1", 1, contract)


def test_post_invariant_failure():
    engine = build_engine(AllowPolicy())

    contract = TransitionContract(
        event_id="E1",
        state_type=int,
        transition_fn=increment,
        pre_invariants=[always_true],
        post_invariants=[always_false],
    )

    with pytest.raises(PostInvariantViolationError):
        engine.process("E1", 1, contract)
