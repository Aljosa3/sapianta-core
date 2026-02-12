from sapianta_hoi.execution.session_controller import SessionController
from sapianta_hoi.runtime_stub.event import Event
from sapianta_hoi.runtime_contracts.exporter import export_canonical_state


class HOIAdapter:
    """
    Deterministic HOI integration bridge.

    Responsibilities:
    - Map user input to event (strict mapping)
    - Dispatch event via SessionController
    - Export canonical state deterministically
    """

    def __init__(self, initial_state: str = "INITIAL") -> None:
        self._controller = SessionController(initial_state=initial_state)

    @property
    def current_state(self) -> str:
        return self._controller.current_state.state_name

    def handle_input(self, user_input: str) -> dict:
        """
        Deterministic input handling.

        Current phase:
        - Direct string-to-event mapping
        - No interpretation
        - No inference
        """

        event = self._map_input_to_event(user_input)

        new_state = self._controller.dispatch(event)

        return export_canonical_state(new_state)

    def _map_input_to_event(self, user_input: str) -> Event:
        """
        Strict deterministic mapping:
        user_input must exactly equal event_type.

        No fuzzy matching.
        No interpretation.
        """

        return Event(event_type=user_input)
