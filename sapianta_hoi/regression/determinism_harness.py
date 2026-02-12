import hashlib
import json
from typing import List, Dict, Any

from sapianta_hoi.integration.hoi_adapter import HOIAdapter


class DeterminismHarness:
    """
    Production-grade determinism regression harness.

    Guarantees:
    - Same input sequence → identical export snapshot
    - Hash-based verification using canonical JSON
    - No access to private runtime internals
    - Fail-fast on mismatch
    """

    def __init__(self, initial_state: str = "INITIAL") -> None:
        self._initial_state = initial_state

    def run_sequence(self, events: List[str]) -> Dict[str, Any]:
        adapter = HOIAdapter(initial_state=self._initial_state)

        for e in events:
            adapter.handle_input(e)

        # Use official observable export surface only
        snapshot = adapter.get_export_snapshot()

        # Canonical JSON serialization
        serialized = json.dumps(
            snapshot,
            sort_keys=True,
            separators=(",", ":"),
        )

        hash_value = hashlib.sha256(serialized.encode()).hexdigest()

        return {
            "snapshot": snapshot,
            "hash": hash_value,
        }

    def assert_deterministic(self, events: List[str]) -> None:
        first = self.run_sequence(events)
        second = self.run_sequence(events)

        if first["hash"] != second["hash"]:
            raise RuntimeError("Determinism violation detected.")

        print("Determinism validated.")
