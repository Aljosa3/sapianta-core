"""
SAPIANTA Artifact Registry

Purpose
-------
Append-only registry of all artifacts produced by the system.

Features
--------

• deterministic artifact hashing
• append-only artifact history
• artifact lineage tracking
• reproducibility support
"""

import json
import os
import hashlib
from datetime import datetime


REGISTRY_PATH = "runtime/history/artifact_registry.jsonl"


# ------------------------------------------------------------
# HASHING
# ------------------------------------------------------------

def _hash_artifact(data: dict) -> str:

    serialized = json.dumps(data, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()


# ------------------------------------------------------------
# REGISTER ARTIFACT
# ------------------------------------------------------------

def register_artifact(
    artifact_type: str,
    domain_id: str,
    artifact_location: str,
    producer: str,
    metadata: dict
):

    artifact_hash = _hash_artifact(metadata)

    artifact = {
        "artifact_id": artifact_hash[:16],
        "artifact_type": artifact_type,
        "domain_id": domain_id,
        "timestamp": datetime.utcnow().isoformat(),
        "artifact_hash": artifact_hash,
        "artifact_location": artifact_location,
        "producer": producer,
        "metadata": metadata
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)

    with open(REGISTRY_PATH, "a") as f:
        f.write(json.dumps(artifact) + "\n")

    return artifact


# ------------------------------------------------------------
# QUERY FUNCTIONS
# ------------------------------------------------------------

def list_artifacts():

    if not os.path.exists(REGISTRY_PATH):
        return []

    artifacts = []

    with open(REGISTRY_PATH) as f:
        for line in f:
            artifacts.append(json.loads(line))

    return artifacts


def find_by_type(artifact_type: str):

    return [
        a for a in list_artifacts()
        if a["artifact_type"] == artifact_type
    ]


def find_by_domain(domain_id: str):

    return [
        a for a in list_artifacts()
        if a["domain_id"] == domain_id
    ]


def find_by_id(artifact_id: str):

    for artifact in list_artifacts():
        if artifact["artifact_id"] == artifact_id:
            return artifact

    return None


# ------------------------------------------------------------
# DEBUG
# ------------------------------------------------------------

if __name__ == "__main__":

    print("Registered artifacts:")

    for artifact in list_artifacts():
        print(artifact["artifact_id"], artifact["artifact_type"])