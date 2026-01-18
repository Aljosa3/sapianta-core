"""
Trace utility for SAPIANTA — CODEBASE_INIT.

The Trace class records events as they occur.
It does not interpret, classify, or evaluate them.
"""


class Trace:
    def __init__(self):
        # simple in-memory list of events
        self.events = []

    def record(self, event):
        """
        Record a trace event.

        The event is stored as-is, without interpretation.
        """
        self.events.append(event)

        # Optional: print to stdout for visibility during PoC
        print(f"[TRACE] {event}")

    def all(self):
        """
        Return all recorded events.
        """
        return list(self.events)

    def __repr__(self):
        return f"<Trace events={len(self.events)}>"
