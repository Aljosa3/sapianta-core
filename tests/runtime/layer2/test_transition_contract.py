import pytest

from runtime.layer2.transition_contract import TransitionContract
from runtime.layer2.exceptions import ContractViolationError


def dummy_transition(state):
    return state + 1


def test_contract_valid_event_and_state():
    contract = TransitionContract(
        event_id="E1",
        state_type=int,
        transition_fn=dummy_transition,
        pre_invariants=[],
        post_invariants=[],
    )

    contract.validate_event("E1")
    contract.validate_state_type(1)


def test_contract_event_mismatch():
    contract = TransitionContract(
        event_id="E1",
        state_type=int,
        transition_fn=dummy_transition,
        pre_invariants=[],
        post_invariants=[],
    )

    with pytest.raises(ContractViolationError):
        contract.validate_event("E2")


def test_contract_state_type_mismatch():
    contract = TransitionContract(
        event_id="E1",
        state_type=int,
        transition_fn=dummy_transition,
        pre_invariants=[],
        post_invariants=[],
    )

    with pytest.raises(ContractViolationError):
        contract.validate_state_type("not-an-int")
