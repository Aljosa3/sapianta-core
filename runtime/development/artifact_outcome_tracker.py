import json
import os
from datetime import datetime


class ArtifactOutcomeTracker:
    """
    Deterministic append-only tracker for artifact execution outcomes.

    Stores:
        - artifact_id
        - timestamp (ISO-8601)
        - status (success / failed)
        - error (optional)

    Design principles:
        - append-only
        - deterministic serialization
        - no mutation of past records
        - fail-closed on write errors
    """

    def __init__(self, storage_path: str = "runtime/development/dev_outcomes.jsonl"):
        self.storage_path = storage_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w", encoding="utf-8") as f:
                pass  # create empty file

    def record_outcome(self, artifact_id: str, status: str, error: str = None):
        """
        Record outcome of artifact execution.

        status must be:
            - "success"
            - "failed"
        """

        if status not in ("success", "failed"):
            raise ValueError("Invalid status. Must be 'success' or 'failed'.")

        entry = {
            "artifact_id": artifact_id,
            "timestamp": self._get_timestamp(),
            "status": status,
            "error": error or ""
        }

        serialized = self._serialize(entry)

        try:
            with open(self.storage_path, "a", encoding="utf-8") as f:
                f.write(serialized + "\n")
        except Exception as e:
            # fail-closed: do not silently ignore
            raise RuntimeError(f"[OUTCOME_TRACKER] Failed to write outcome: {e}")

    def _get_timestamp(self) -> str:
        # Deterministic enough for current system stage
        return datetime.utcnow().isoformat()

    def _serialize(self, entry: dict) -> str:
        """
        Deterministic JSON serialization:
            - sorted keys
            - stable encoding
        """
        return json.dumps(entry, sort_keys=True, separators=(",", ":"))

    def load_all(self):
        """
        Load all outcomes (for dev-learn integration).
        """
        results = []

        with open(self.storage_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    results.append(json.loads(line))

        return results