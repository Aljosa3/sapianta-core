from sapianta_hoi.runtime_stub.transitions import TRANSITIONS


# Extract allowed event types from transition definitions
ALLOWED_EVENTS = {
    event_type for (_, event_type) in TRANSITIONS.keys()
}


def validate_event_type(event_type: str) -> None:
    """
    Ensure event_type is formally registered.

    Raises:
        ValueError if event not allowed.
    """

    if event_type not in ALLOWED_EVENTS:
        raise ValueError(f"Unregistered event type: {event_type}")
