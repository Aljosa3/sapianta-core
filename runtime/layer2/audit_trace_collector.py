from typing import Any, Dict


class AuditTraceCollector:
    """
    Collects deterministic audit trace for execution.
    In-memory only.
    """

    def collect(
        self,
        event_id: str,
        previous_state: Any,
        new_state: Any,
        allowed: bool,
    ) -> Dict[str, Any]:

        return {
            "event_id": event_id,
            "allowed": allowed,
            "previous_state": previous_state,
            "new_state": new_state,
        }
