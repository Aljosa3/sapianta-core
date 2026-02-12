from sapianta_hoi.runtime_stub.canonical_state import CanonicalState
from sapianta_hoi.runtime_stub.event import Event
from sapianta_hoi.runtime_stub.transitions import TRANSITIONS


def validate_transition_guard(state: CanonicalState, event: Event) -> None:
    """
    Guard-level transition validation.

    Raises:
        ValueError if transition is not explicitly defined.
    """

    key = (state.state_name, event.event_type)

    if key not in TRANSITIONS:
        raise ValueError(
            f"Invalid transition: {state.state_name} + {event.event_type}"
        )
