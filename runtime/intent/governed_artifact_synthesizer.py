"""Deterministic bounded artifact synthesis."""

from __future__ import annotations

import re

ARTIFACT_PATTERN = re.compile(r"^[A-Z0-9_]{1,96}$")

ARTIFACT_BY_INTENT = {
    "GOVERNANCE_ARTIFACT_CREATION": "TEST_OPERATIONAL_REPLAY_PROOF_V1",
    "RUNTIME_VALIDATION_REQUEST": "GOVERNED_RUNTIME_VALIDATION_V1",
    "REPLAY_INSPECTION_REQUEST": "GOVERNED_REPLAY_INSPECTION_V1",
}

MODE_BY_INTENT = {
    "GOVERNANCE_ARTIFACT_CREATION": "BOUNDED_ARTIFACT_SYNTHESIS",
    "RUNTIME_VALIDATION_REQUEST": "BOUNDED_RUNTIME_VALIDATION_PREVIEW",
    "REPLAY_INSPECTION_REQUEST": "BOUNDED_REPLAY_INSPECTION_PREVIEW",
}


def synthesize_governed_artifact(intent_class: str) -> dict:
    artifact = ARTIFACT_BY_INTENT.get(intent_class)
    governance_mode = MODE_BY_INTENT.get(intent_class)
    valid = bool(artifact and governance_mode and ARTIFACT_PATTERN.fullmatch(artifact))
    return {
        "valid": valid,
        "artifact_candidate": artifact,
        "governance_mode": governance_mode,
    }
