"""
SAPIANTA Pattern Memory

Inspection-only append-only memory for unknown governance failure patterns.

This module is intentionally dormant:
- no enforcement
- no policy participation
- no Decision Spine activation
- no runtime reads
"""

import hashlib
import json
import os
from typing import Any


PATTERN_MEMORY_PATH = "runtime/history/pattern_memory.jsonl"
SCHEMA_VERSION = "pattern_memory.v0.1"


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


def build_failure_signature(
    *,
    rule: str | None = None,
    status: str | None = None,
    stage: str | None = None,
    reason: str | None = None,
    evidence: str | None = None,
) -> dict:
    """
    Build a normalized governance failure signature.

    The signature is descriptive only. It must not be used for enforcement
    until a separate governed promotion lifecycle activates a control.
    """
    normalized = {
        "rule": _normalize_text(rule),
        "status": _normalize_text(status),
        "stage": _normalize_text(stage),
        "reason": _normalize_text(reason),
        "evidence": _normalize_text(evidence),
    }

    return {
        "signature_version": "failure_signature.v0.1",
        "normalized": normalized,
        "signature_hash": _hash(normalized),
    }


def build_pattern_record(
    *,
    failure_signature: dict,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    audit_signature: str | None = None,
    audit_path: str | None = None,
    observed_at: str | None = None,
    source: str = "inspection",
    metadata: dict | None = None,
) -> dict:
    """
    Build a lineage-linked PatternMemory record without writing it.
    """
    lineage = {
        "validation_id": validation_id,
        "audit_hash": audit_hash,
        "audit_signature": audit_signature,
        "audit_path": audit_path,
        "observed_at": observed_at,
        "source": source,
    }

    payload = {
        "schema_version": SCHEMA_VERSION,
        "failure_signature": failure_signature,
        "lineage": lineage,
        "metadata": metadata or {},
    }

    pattern_hash = _hash(payload)

    return {
        **payload,
        "pattern_id": pattern_hash[:16],
        "pattern_hash": pattern_hash,
    }


def append_pattern_record(record: dict, path: str = PATTERN_MEMORY_PATH) -> dict:
    """
    Append a PatternMemory record to JSONL storage.

    Future inspection hook:
    - validator_service.save_audit may call this after audit creation to link
      rejected validation evidence to unknown governance patterns.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a", encoding="utf-8") as f:
        f.write(_canonical_json(record) + "\n")

    return record


def record_failure_pattern(
    *,
    rule: str | None = None,
    status: str | None = None,
    stage: str | None = None,
    reason: str | None = None,
    evidence: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    audit_signature: str | None = None,
    audit_path: str | None = None,
    observed_at: str | None = None,
    source: str = "inspection",
    metadata: dict | None = None,
) -> dict:
    """
    Convenience writer for inspection-only pattern capture.

    Future inspection hooks:
    - ControlCandidate Registry may reference pattern_id as source evidence.
    - ShadowValidation may later read promoted candidates, not this memory.
    - Promotion lifecycle may link approvals back to pattern_hash lineage.
    """
    failure_signature = build_failure_signature(
        rule=rule,
        status=status,
        stage=stage,
        reason=reason,
        evidence=evidence,
    )

    record = build_pattern_record(
        failure_signature=failure_signature,
        validation_id=validation_id,
        audit_hash=audit_hash,
        audit_signature=audit_signature,
        audit_path=audit_path,
        observed_at=observed_at,
        source=source,
        metadata=metadata,
    )

    return append_pattern_record(record)
