from sapianta_hoi.runtime_stub.canonical_state import CanonicalState
from sapianta_hoi.runtime_stub.transitions import TRANSITIONS


def validate_state_completeness(state: CanonicalState) -> None:
    """
    Ensure state is structurally complete and recognized.

    Raises:
        ValueError if state is unknown or structurally invalid.
    """

    if state is None:
        raise ValueError("State cannot be None")

    if state.state_name is None:
        raise ValueError("State name cannot be None")

    # Extract all known states from transitions
    known_states = {source for (source, _) in TRANSITIONS.keys()}
    known_states.update({target for target in TRANSITIONS.values()})

    if state.state_name not in known_states:
        raise ValueError(f"Unknown state: {state.state_name}")
