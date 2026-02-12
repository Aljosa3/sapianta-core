from sapianta_hoi.runtime_stub.canonical_state import CanonicalState
from sapianta_hoi.runtime_stub.event import Event
from sapianta_hoi.runtime_stub.transitions import TRANSITIONS


def validate_transition(state: CanonicalState, event: Event) -> bool:
    """
    Validation pipeline compliant with:
    HOI_TRANSITION_VALIDATION_SPEC_v0.1

    Pure check:
    - Does (state, event) exist in transition mapping?
    """

    key = (state.state_name, event.event_type)
    return key in TRANSITIONS
