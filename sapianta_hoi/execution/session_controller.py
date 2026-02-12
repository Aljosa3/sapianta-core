from sapianta_hoi.runtime_stub.canonical_state import CanonicalState
from sapianta_hoi.runtime_stub.execution_loop import execute_event
from sapianta_hoi.runtime_stub.event import Event

from sapianta_hoi.guards.state_invariants import validate_state
from sapianta_hoi.guards.transition_guard import validate_transition_guard


class SessionController:
    """
    Controlled execution session wrapper around LOCKED execution kernel.

    Guard-protected.
    Fail-fast.
    Deterministic.

    Responsibilities:
    - Hold current canonical state
    - Apply deterministic events via execution loop
    - Enforce transition validity
    - Enforce state invariants

    No side effects.
    No external I/O.
    """

    def __init__(self, initial_state: str = "INITIAL") -> None:
        self._state = CanonicalState(state_name=initial_state)
        validate_state(self._state)

    @property
    def current_state(self) -> CanonicalState:
        return self._state

    def dispatch(self, event: Event) -> CanonicalState:
        """
        Apply event through locked execution kernel,
        guarded by transition and state invariants.

        Raises:
            ValueError if transition is invalid
            ValueError if resulting state violates invariants
        """

        # Guard: validate transition explicitly
        validate_transition_guard(self._state, event)

        # Execute deterministic transition
        new_state = execute_event(self._state, event)

        # Guard: validate resulting state invariants
        validate_state(new_state)

        self._state = new_state
        return new_state
