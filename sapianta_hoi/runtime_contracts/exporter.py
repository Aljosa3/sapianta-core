from sapianta_hoi.runtime_stub.canonical_state import CanonicalState


def export_canonical_state(state: CanonicalState) -> dict:
    """
    Deterministic export of canonical state.

    No derived values.
    No interpretation.
    No formatting variability.
    """

    return {
        "state_name": state.state_name
    }
