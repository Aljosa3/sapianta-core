"""
Formal Execution Entry Wrapper — SAPIANTA v1.2.x

Defines the canonical execution surface of the Execution Layer.

This wrapper does NOT alter kernel logic.
It formalizes a single public execution entry-point.
"""

from sapianta_hoi.execution.session_controller import SessionController
from sapianta_hoi.execution.event_dispatcher import EventDispatcher


def execute(event_type: str, initial_state: str = "INITIAL"):
    """
    Canonical execution entry-point.

    Parameters:
        event_type: str
            Raw event identifier.
        initial_state: str
            Canonical starting state.

    Returns:
        CanonicalState
    """

    controller = SessionController(initial_state=initial_state)
    event = EventDispatcher.create(event_type)
    return controller.dispatch(event)
