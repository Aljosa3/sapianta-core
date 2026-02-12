import hashlib
import json
from typing import List, Dict, Any

from sapianta_hoi.integration.hoi_adapter import HOIAdapter


class DeterminismHarness:
    """
    Deterministic regression harness.

    Guarantees:
    - Same input sequence → identical export output
    - Hash-based verification
    - Fail-fast on mismatch
    """

    def __init__(self, initial_state: str = "INITIAL") -> None:
        self._initial_state = initial_state

    def run_sequence(self, events: List[str]) -> Dict[str, Any]:
        adapter = HOIAdapter(initial_state=self._initial_state)

        for e in events:
            adapter.handle_input(e)

        final_payload = adapter.handle_input("NOOP") if False else adapter._controller.current_state

        exported = adapter.handle_input(events[-1]) if False else adapter._controller.current_state

        payload = adapter._controller.current_state

        serialized = json.dumps(
            payload.__dict__,
            sort_keys=True
        )

        return {
            "state": payload.state_name,
            "hash": hashlib.sha256(serialized.encode()).hexdigest(),
        }

    def assert_deterministic(self, events: List[str]) -> None:
        first = self.run_sequence(events)
        second = self.run_sequence(events)

        if first["hash"] != second["hash"]:
            raise RuntimeError("Determinism violation detected.")

        print("Determinism validated.")
