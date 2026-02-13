import hashlib
import json
from typing import List, Dict, Any


class SessionRecorder:
    """
    In-memory deterministic session recorder.

    Records:
    - ordered event sequence
    - final snapshot
    - deterministic session hash
    """

    def __init__(self):
        self._events: List[str] = []
        self._final_snapshot: Dict[str, Any] = {}

    def record_event(self, event: str) -> None:
        self._events.append(event)

    def finalize(self, snapshot: Dict[str, Any]) -> None:
        self._final_snapshot = snapshot

    def export_audit_record(self) -> Dict[str, Any]:
        serialized = json.dumps(
            {
                "events": self._events,
                "snapshot": self._final_snapshot,
            },
            sort_keys=True,
            separators=(",", ":"),
        )

        audit_hash = hashlib.sha256(serialized.encode()).hexdigest()

        return {
            "events": list(self._events),
            "snapshot": self._final_snapshot,
            "audit_hash": audit_hash,
        }
