from typing import Dict, Any

from sapianta_hoi.integration.hoi_adapter import HOIAdapter


class ReplayEngine:
    """
    Deterministic replay validator.

    Replays recorded event sequence
    and verifies final snapshot hash.
    """

    def replay(self, audit_record: Dict[str, Any]) -> bool:
        adapter = HOIAdapter()

        for event in audit_record["events"]:
            adapter.handle_input(event)

        replay_snapshot = adapter.get_export_snapshot()

        return replay_snapshot == audit_record["snapshot"]
