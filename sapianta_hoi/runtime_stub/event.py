from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    """
    Deterministic event object
    compliant with HOI_EVENT_MODEL_SPEC_v0.1.

    Immutable.
    """

    event_type: str
