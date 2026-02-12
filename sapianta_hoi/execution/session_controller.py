from sapianta_hoi.runtime_stub.canonical_state import CanonicalState
from sapianta_hoi.runtime_stub.execution_loop import execute_event
from sapianta_hoi.runtime_stub.event import Event


class SessionController:
    """
    Controlled execution session wrapper around LOCKED execution kernel.

    Responsibilities:
    - Hold current canonical state
    - Apply deterministic events via execution loop
    - Remain pure in-memory

    No side effects.
    No external I/O.
    """

    def __init__(self, initial_state: str = "INITIAL") -> None:
        self._state = CanonicalState(state_name=initial_state)

    @property
    def current_state(self) -> CanonicalState:
        return self._state

    def dispatch(self, event: Event) -> CanonicalState:
        """
        Apply event through locked execution kernel.
        """
        new_state = execute_event(self._state, event)
        self._state = new_state
        return new_state
