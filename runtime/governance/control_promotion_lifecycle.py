"""
SAPIANTA Control Promotion Lifecycle

Inspection-first append-only lifecycle events for control candidates.

This module is intentionally dormant:
- no enforcement activation
- no active control loading
- no Decision Spine activation
- no policy participation
- no production reads
"""

import hashlib
import json
import os


CONTROL_PROMOTION_EVENTS_PATH = "runtime/history/control_promotion_events.jsonl"
SCHEMA_VERSION = "control_promotion_event.v0.1"
ALLOWED_LIFECYCLE_STATES = {
    "DRAFT",
    "CANDIDATE",
    "SHADOW",
    "REVIEW",
    "APPROVED",
    "ACTIVE",
    "DEPRECATED",
    "REVOKED",
}
ALLOWED_TRANSITIONS = {
    ("DRAFT", "CANDIDATE"),
    ("CANDIDATE", "SHADOW"),
    ("SHADOW", "REVIEW"),
    ("REVIEW", "APPROVED"),
    ("APPROVED", "ACTIVE"),
    ("ACTIVE", "DEPRECATED"),
    ("DEPRECATED", "REVOKED"),
}


def _canonical_json(data: dict) -> str:
    """
    Deterministic JSON serialization for hashing and JSONL writes.
    """
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def _hash(data: dict) -> str:
    serialized = _canonical_json(data)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def validate_lifecycle_state(state: str | None) -> str | None:
    """
    Validate a lifecycle state without implying transition legality.
    """
    if state is None:
        return None

    if state not in ALLOWED_LIFECYCLE_STATES:
        raise ValueError("Invalid lifecycle state")

    return state


def is_valid_transition(previous_state: str | None, next_state: str | None) -> bool:
    """
    Return whether a lifecycle transition is explicitly allowed.
    """
    previous_state = validate_lifecycle_state(previous_state)
    next_state = validate_lifecycle_state(next_state)

    return (previous_state, next_state) in ALLOWED_TRANSITIONS


def build_promotion_lineage(
    *,
    candidate_id: str | None = None,
    candidate_hash: str | None = None,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    shadow_result_id: str | None = None,
    shadow_result_hash: str | None = None,
    approval_id: str | None = None,
    approval_hash: str | None = None,
) -> dict:
    """
    Build candidate, pattern, audit, shadow, and approval lineage refs.
    """
    return {
        "candidate_id": candidate_id,
        "candidate_hash": candidate_hash,
        "pattern_id": pattern_id,
        "pattern_hash": pattern_hash,
        "validation_id": validation_id,
        "audit_hash": audit_hash,
        "shadow_result_id": shadow_result_id,
        "shadow_result_hash": shadow_result_hash,
        "approval_id": approval_id,
        "approval_hash": approval_hash,
    }


def build_promotion_event_record(
    *,
    candidate_id: str | None = None,
    candidate_hash: str | None = None,
    shadow_result_id: str | None = None,
    shadow_result_hash: str | None = None,
    approval_id: str | None = None,
    approval_hash: str | None = None,
    previous_state: str | None = None,
    next_state: str = "DRAFT",
    transition_reason: str | None = None,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    governance_metadata: dict | None = None,
) -> dict:
    """
    Build a deterministic promotion lifecycle event without writing it.
    """
    previous_state = validate_lifecycle_state(previous_state)
    next_state = validate_lifecycle_state(next_state)

    if not is_valid_transition(previous_state, next_state):
        raise ValueError("Invalid lifecycle transition")

    lineage = build_promotion_lineage(
        candidate_id=candidate_id,
        candidate_hash=candidate_hash,
        pattern_id=pattern_id,
        pattern_hash=pattern_hash,
        validation_id=validation_id,
        audit_hash=audit_hash,
        shadow_result_id=shadow_result_id,
        shadow_result_hash=shadow_result_hash,
        approval_id=approval_id,
        approval_hash=approval_hash,
    )

    payload = {
        "schema_version": SCHEMA_VERSION,
        "previous_state": previous_state,
        "next_state": next_state,
        "transition_reason": transition_reason,
        "lineage": lineage,
        "governance_metadata": governance_metadata or {},
    }

    event_hash = _hash(payload)

    return {
        **payload,
        "promotion_event_id": event_hash[:16],
        "promotion_event_hash": event_hash,
    }


def append_promotion_event(
    record: dict,
    path: str = CONTROL_PROMOTION_EVENTS_PATH,
) -> dict:
    """
    Append a control promotion lifecycle event to JSONL storage.

    Future integration hooks:
    - approval_gate may later produce approval_id and approval_hash before an
      APPROVED or ACTIVE transition is recorded.
    - artifact_registry may later register control promotion artifacts with
      parent_artifact=candidate_id, shadow_result_id, or approval_id.
    - ACTIVE records must not be loaded by production until a separate governed
      control loader exists.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a", encoding="utf-8") as f:
        f.write(_canonical_json(record) + "\n")

    return record


def record_promotion_event(
    *,
    candidate_id: str | None = None,
    candidate_hash: str | None = None,
    shadow_result_id: str | None = None,
    shadow_result_hash: str | None = None,
    approval_id: str | None = None,
    approval_hash: str | None = None,
    previous_state: str | None = None,
    next_state: str = "DRAFT",
    transition_reason: str | None = None,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    governance_metadata: dict | None = None,
) -> dict:
    """
    Convenience writer for inspection-first promotion lifecycle events.

    Future inspection hooks:
    - ShadowValidation may provide shadow_result_id and shadow_result_hash.
    - Human approval flow may provide approval_id and approval_hash.
    - Runtime control loading must remain a separate explicitly governed step.
    """
    record = build_promotion_event_record(
        candidate_id=candidate_id,
        candidate_hash=candidate_hash,
        shadow_result_id=shadow_result_id,
        shadow_result_hash=shadow_result_hash,
        approval_id=approval_id,
        approval_hash=approval_hash,
        previous_state=previous_state,
        next_state=next_state,
        transition_reason=transition_reason,
        pattern_id=pattern_id,
        pattern_hash=pattern_hash,
        validation_id=validation_id,
        audit_hash=audit_hash,
        governance_metadata=governance_metadata,
    )

    return append_promotion_event(record)
