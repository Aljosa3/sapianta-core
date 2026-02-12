from sapianta_hoi.execution.session_controller import SessionController
from sapianta_hoi.runtime_stub.event import Event
from sapianta_hoi.runtime_contracts.exporter import export_canonical_state
from sapianta_hoi.runtime_contracts.event_registry import validate_event


class HOIAdapter:
    """
    Deterministic HOI integration bridge.

    Strict guarantees:
    - Closed event domain (validated against formal registry)
    - Deterministic state transition
    - Export-only observable surface
    - No advisory logic
    - No interpretation
    - No external I/O
    """

    def __init__(self, initial_state: str = "INITIAL") -> None:
        self._controller = SessionController(initial_state=initial_state)

    @property
    def current_state(self) -> str:
        """
        Returns only the state name.
        Internal state object is not exposed.
        """
        return self._controller.current_state.state_name

    def handle_input(self, user_input: str) -> dict:
        """
        Deterministic input handling.

        Rules:
        - Input must exactly match a registered event
        - No fuzzy matching
        - No inference
        - No interpretation
        """

        # Fail-fast if event is not part of the closed registry
        validate_event(user_input)

        event = Event(event_type=user_input)

        new_state = self._controller.dispatch(event)

        return export_canonical_state(new_state)

    def get_export_snapshot(self) -> dict:
        """
        Official observable export surface.

        Used by regression harness.
        No internal state exposure.
        """
        return export_canonical_state(self._controller.current_state)
