from sapianta_hoi.runtime_stub.canonical_state import CanonicalState
from sapianta_hoi.runtime_stub.event import Event
from sapianta_hoi.runtime_stub.transitions import TRANSITIONS
from sapianta_hoi.runtime_stub.validation import validate_transition


def execute_event(
    state: CanonicalState,
    event: Event
) -> CanonicalState:
    """
    Minimal deterministic execution loop
    compliant with HOI_EXECUTION_LOOP_CONTRACT_v0.1.

    Strict behavior:
    - Validate transition
    - If valid → return new CanonicalState
    - If invalid → return unchanged state

    No side effects.
    No logging.
    No I/O.
    No mutation.
    """

    if not validate_transition(state, event):
        return state

    next_state_name = TRANSITIONS[(state.state_name, event.event_type)]
    return state.with_state(next_state_name)
