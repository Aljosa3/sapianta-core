from sapianta_hoi.runtime_stub.canonical_state import CanonicalState


def validate_state(state: CanonicalState) -> None:
    """
    Enforce canonical state invariants.

    Fail-fast philosophy:
    - State must exist
    - state_name must be a non-empty string
    """

    if state is None:
        raise ValueError("CanonicalState cannot be None")

    if not isinstance(state.state_name, str):
        raise ValueError("state_name must be a string")

    if state.state_name == "":
        raise ValueError("state_name cannot be empty")
