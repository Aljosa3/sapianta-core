from dataclasses import dataclass


@dataclass(frozen=True)
class CanonicalState:
    """
    Minimal immutable canonical state object
    compliant with HOI_CANONICAL_STATE_OBJECT_SPEC_v0.1.

    Immutable (frozen=True).
    No runtime mutation allowed.
    """

    state_name: str

    def with_state(self, new_state: str) -> "CanonicalState":
        """
        Returns a new CanonicalState instance.
        Pure functional transition.
        """
        return CanonicalState(state_name=new_state)
