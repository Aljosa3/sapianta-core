from sapianta_hoi.runtime_stub.event import Event


class EventDispatcher:
    """
    Deterministic event factory.

    Converts raw event identifier into Event object.

    No interpretation logic.
    No advisory behavior.
    """

    @staticmethod
    def create(event_type: str) -> Event:
        return Event(event_type=event_type)
