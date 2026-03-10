import json
import os
import hashlib
from datetime import datetime


REGISTRY_PATH = "runtime/history/artifact_registry.jsonl"


def _hash_artifact(data: dict) -> str:
    serialized = json.dumps(data, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()


def register_artifact(
    artifact_type: str,
    domain_id: str,
    artifact_location: str,
    producer: str,
    metadata: dict
):

    artifact = {
        "artifact_id": _hash_artifact(metadata)[:16],
        "artifact_type": artifact_type,
        "domain_id": domain_id,
        "timestamp": datetime.utcnow().isoformat(),
        "artifact_hash": _hash_artifact(metadata),
        "artifact_location": artifact_location,
        "producer": producer,
        "metadata": metadata
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)

    with open(REGISTRY_PATH, "a") as f:
        f.write(json.dumps(artifact) + "\n")

    return artifact