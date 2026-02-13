import hashlib
import json
from typing import Any


class SnapshotHasher:
    """
    Produces canonical SHA256 hash from snapshot object.
    Ensures deterministic byte-level comparison.
    """

    @staticmethod
    def hash_snapshot(snapshot: Any) -> str:
        """
        Serializes snapshot using canonical JSON rules:
        - sorted keys
        - no whitespace variance
        - deterministic encoding
        """

        canonical_json = json.dumps(
            snapshot,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )

        return hashlib.sha256(
            canonical_json.encode("utf-8")
        ).hexdigest()
