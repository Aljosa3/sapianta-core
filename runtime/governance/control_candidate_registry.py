"""
SAPIANTA Control Candidate Registry

Inspection-first append-only registry for governed control candidates.

This module is intentionally dormant:
- no enforcement activation
- no policy participation
- no Decision Spine activation
- no runtime reads
"""

import hashlib
import json
import os
from typing import Any


CONTROL_CANDIDATES_PATH = "runtime/history/control_candidates.jsonl"
SCHEMA_VERSION = "control_candidate.v0.1"
ALLOWED_CANDIDATE_STATES = {"DRAFT", "CANDIDATE"}


def _canonical_json(data: dict) -> str:
    """
    Deterministic JSON serialization for hashing and JSONL writes.
    """
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def _hash(data: dict) -> str:
    serialized = _canonical_json(data)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def _normalize_text(value: Any) -> str:
    if value is None:
        return "unknown"

    text = str(value).strip().lower()
    if not text:
        return "unknown"

    return " ".join(text.split())


def build_candidate_signature(
    *,
    control_name: str | None = None,
    control_intent: str | None = None,
    pattern_signature_hash: str | None = None,
) -> dict:
    """
    Build a descriptive candidate signature.

    The signature describes a possible control only. It must not be used for
    enforcement until shadow validation and promotion lifecycle approve it.
    """
    normalized = {
        "control_name": _normalize_text(control_name),
        "control_intent": _normalize_text(control_intent),
        "pattern_signature_hash": _normalize_text(pattern_signature_hash),
    }

    return {
        "signature_version": "control_candidate_signature.v0.1",
        "normalized": normalized,
        "signature_hash": _hash(normalized),
    }


def build_candidate_lineage(
    *,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    audit_signature: str | None = None,
    audit_path: str | None = None,
    observed_at: str | None = None,
    source: str = "pattern_memory",
) -> dict:
    """
    Build lineage fields reused from PatternMemory observations.
    """
    return {
        "pattern_id": pattern_id,
        "pattern_hash": pattern_hash,
        "validation_id": validation_id,
        "audit_hash": audit_hash,
        "audit_signature": audit_signature,
        "audit_path": audit_path,
        "observed_at": observed_at,
        "source": source,
    }


def build_candidate_record(
    *,
    candidate_signature: dict,
    lineage: dict,
    state: str = "DRAFT",
    governance_metadata: dict | None = None,
) -> dict:
    """
    Build a deterministic ControlCandidate record without writing it.
    """
    if state not in ALLOWED_CANDIDATE_STATES:
        raise ValueError("Invalid candidate state")

    payload = {
        "schema_version": SCHEMA_VERSION,
        "state": state,
        "candidate_signature": candidate_signature,
        "lineage": lineage,
        "governance_metadata": governance_metadata or {},
    }

    candidate_hash = _hash(payload)

    return {
        **payload,
        "candidate_id": candidate_hash[:16],
        "candidate_hash": candidate_hash,
    }


def append_candidate_record(
    record: dict,
    path: str = CONTROL_CANDIDATES_PATH,
) -> dict:
    """
    Append a ControlCandidate record to JSONL storage.

    Future artifact lineage hook:
    - runtime.artifacts.artifact_registry.register_artifact may later register
      artifact_type="control_candidate" with parent_artifact=pattern_id or
      parent_artifact=pattern_hash after governance approves that linkage.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a", encoding="utf-8") as f:
        f.write(_canonical_json(record) + "\n")

    return record


def record_control_candidate(
    *,
    control_name: str | None = None,
    control_intent: str | None = None,
    pattern_signature_hash: str | None = None,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    audit_signature: str | None = None,
    audit_path: str | None = None,
    observed_at: str | None = None,
    source: str = "pattern_memory",
    state: str = "DRAFT",
    governance_metadata: dict | None = None,
) -> dict:
    """
    Convenience writer for inspection-first candidate capture.

    Future inspection hooks:
    - PatternMemory records may be transformed into DRAFT candidates here.
    - ShadowValidation may later consume CANDIDATE records after an explicit
      governed read surface is added.
    - Promotion lifecycle may move candidates beyond CANDIDATE in a separate
      append-only lifecycle registry.
    """
    candidate_signature = build_candidate_signature(
        control_name=control_name,
        control_intent=control_intent,
        pattern_signature_hash=pattern_signature_hash,
    )

    lineage = build_candidate_lineage(
        pattern_id=pattern_id,
        pattern_hash=pattern_hash,
        validation_id=validation_id,
        audit_hash=audit_hash,
        audit_signature=audit_signature,
        audit_path=audit_path,
        observed_at=observed_at,
        source=source,
    )

    record = build_candidate_record(
        candidate_signature=candidate_signature,
        lineage=lineage,
        state=state,
        governance_metadata=governance_metadata,
    )

    return append_candidate_record(record)
