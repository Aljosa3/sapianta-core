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
• replay verification support
"""

import json
import os
import hashlib
from datetime import datetime, UTC


REGISTRY_PATH = "runtime/history/artifact_registry.jsonl"


# ------------------------------------------------------------
# HASHING
# ------------------------------------------------------------

def _canonical_json(data: dict) -> str:
    """
    Deterministic JSON serialization.
    """
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    )


def _hash_artifact(data: dict) -> str:

    serialized = _canonical_json(data)

    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


def _build_hash_payload(
    artifact_type: str,
    domain_id: str,
    artifact_location: str,
    producer: str,
    metadata: dict
) -> dict:
    """
    Full deterministic payload used for hashing.
    Prevents collisions across different artifact contexts.
    """
    return {
        "artifact_type": artifact_type,
        "domain_id": domain_id,
        "artifact_location": artifact_location,
        "producer": producer,
        "metadata": metadata
    }


# ------------------------------------------------------------
# REGISTER ARTIFACT
# ------------------------------------------------------------

def register_artifact(
    artifact_type: str,
    domain_id: str,
    artifact_location: str,
    producer: str,
    metadata: dict,
    parent_artifact: str | None = None
):

    hash_payload = _build_hash_payload(
        artifact_type,
        domain_id,
        artifact_location,
        producer,
        metadata
    )

    artifact_hash = _hash_artifact(hash_payload)

    artifact = {
        "artifact_id": artifact_hash[:16],
        "artifact_type": artifact_type,
        "domain_id": domain_id,
        "timestamp": datetime.now(UTC).isoformat(),
        "artifact_hash": artifact_hash,
        "artifact_location": artifact_location,
        "producer": producer,
        "parent_artifact": parent_artifact,
        "metadata": metadata
    }

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)

    with open(REGISTRY_PATH, "a", encoding="utf-8") as f:
        f.write(_canonical_json(artifact) + "\n")

    return artifact


# ------------------------------------------------------------
# QUERY FUNCTIONS
# ------------------------------------------------------------

def list_artifacts():

    if not os.path.exists(REGISTRY_PATH):
        return []

    artifacts = []

    with open(REGISTRY_PATH, encoding="utf-8") as f:
        for line in f:

            if not line.strip():
                continue

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


def find_children(parent_artifact: str):

    return [
        a for a in list_artifacts()
        if a.get("parent_artifact") == parent_artifact
    ]


# ------------------------------------------------------------
# REPLAY VERIFICATION
# ------------------------------------------------------------

def verify_artifact(artifact):

    hash_payload = _build_hash_payload(
        artifact["artifact_type"],
        artifact["domain_id"],
        artifact["artifact_location"],
        artifact["producer"],
        artifact["metadata"]
    )

    expected_hash = _hash_artifact(hash_payload)

    return expected_hash == artifact["artifact_hash"]


def verify_registry():

    """
    Verify integrity of entire registry.
    """

    results = []

    for artifact in list_artifacts():

        ok = verify_artifact(artifact)

        results.append({
            "artifact_id": artifact["artifact_id"],
            "valid": ok
        })

    return results


# ------------------------------------------------------------
# DEBUG
# ------------------------------------------------------------

if __name__ == "__main__":

    print("Registered artifacts:")

    for artifact in list_artifacts():
        print(
            artifact["artifact_id"],
            artifact["artifact_type"]
        )