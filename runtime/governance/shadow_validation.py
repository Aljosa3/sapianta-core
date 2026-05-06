"""
SAPIANTA Shadow Validation

Inspection-first append-only shadow result registry for control candidates.

This module is intentionally dormant:
- no enforcement activation
- no policy decision modification
- no Decision Spine mutation
- no runtime blocking
- no envelope mutation
- no runtime reads
"""

import hashlib
import json
import os


SHADOW_VALIDATION_PATH = "runtime/history/shadow_validation.jsonl"
SCHEMA_VERSION = "shadow_validation.v0.1"
ALLOWED_SHADOW_STATES = {
    "RECORDED",
    "WOULD_PASS",
    "WOULD_BLOCK",
    "INCONCLUSIVE",
}


def _canonical_json(data: dict) -> str:
    """
    Deterministic JSON serialization for hashing and JSONL writes.
    """
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def _hash(data: dict) -> str:
    serialized = _canonical_json(data)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def derive_shadow_state(*, would_block: bool, would_pass: bool) -> str:
    """
    Derive a deterministic result state from shadow booleans.
    """
    if would_block and not would_pass:
        return "WOULD_BLOCK"

    if would_pass and not would_block:
        return "WOULD_PASS"

    if not would_block and not would_pass:
        return "INCONCLUSIVE"

    return "RECORDED"


def build_shadow_lineage(
    *,
    candidate_id: str | None = None,
    candidate_hash: str | None = None,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    audit_signature: str | None = None,
    audit_path: str | None = None,
    envelope_hash: str | None = None,
) -> dict:
    """
    Build lineage fields across candidate, pattern, audit, and envelope refs.
    """
    return {
        "candidate_id": candidate_id,
        "candidate_hash": candidate_hash,
        "pattern_id": pattern_id,
        "pattern_hash": pattern_hash,
        "validation_id": validation_id,
        "audit_hash": audit_hash,
        "audit_signature": audit_signature,
        "audit_path": audit_path,
        "envelope_hash": envelope_hash,
    }


def build_shadow_result_record(
    *,
    candidate_id: str | None = None,
    candidate_hash: str | None = None,
    production_decision: str | None = None,
    would_block: bool = False,
    would_pass: bool = False,
    envelope_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    audit_signature: str | None = None,
    audit_path: str | None = None,
    state: str | None = None,
    replay_context: dict | None = None,
    governance_metadata: dict | None = None,
) -> dict:
    """
    Build a deterministic ShadowValidation result without writing it.
    """
    result_state = state or derive_shadow_state(
        would_block=would_block,
        would_pass=would_pass,
    )

    if result_state not in ALLOWED_SHADOW_STATES:
        raise ValueError("Invalid shadow result state")

    lineage = build_shadow_lineage(
        candidate_id=candidate_id,
        candidate_hash=candidate_hash,
        pattern_id=pattern_id,
        pattern_hash=pattern_hash,
        validation_id=validation_id,
        audit_hash=audit_hash,
        audit_signature=audit_signature,
        audit_path=audit_path,
        envelope_hash=envelope_hash,
    )

    payload = {
        "schema_version": SCHEMA_VERSION,
        "state": result_state,
        "production_decision": production_decision,
        "would_block": bool(would_block),
        "would_pass": bool(would_pass),
        "lineage": lineage,
        "replay_context": replay_context or {},
        "governance_metadata": governance_metadata or {},
    }

    shadow_hash = _hash(payload)

    return {
        **payload,
        "shadow_result_id": shadow_hash[:16],
        "shadow_result_hash": shadow_hash,
    }


def append_shadow_result(
    record: dict,
    path: str = SHADOW_VALIDATION_PATH,
) -> dict:
    """
    Append a ShadowValidation result to JSONL storage.

    Future integration hooks:
    - Decision Spine may later call this after envelope creation, passing only
      envelope_hash and production_decision, without changing policy_result.
    - Replay tooling may later compare shadow_result_hash values beside, not
      inside, the production DecisionEnvelope chain.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a", encoding="utf-8") as f:
        f.write(_canonical_json(record) + "\n")

    return record


def record_shadow_result(
    *,
    candidate_id: str | None = None,
    candidate_hash: str | None = None,
    production_decision: str | None = None,
    would_block: bool = False,
    would_pass: bool = False,
    envelope_hash: str | None = None,
    validation_id: str | None = None,
    audit_hash: str | None = None,
    pattern_id: str | None = None,
    pattern_hash: str | None = None,
    audit_signature: str | None = None,
    audit_path: str | None = None,
    state: str | None = None,
    replay_context: dict | None = None,
    governance_metadata: dict | None = None,
) -> dict:
    """
    Convenience writer for inspection-first shadow result capture.

    Future inspection hooks:
    - ControlCandidate records may be shadow-tested after explicit governed
      read APIs exist.
    - Promotion lifecycle may reference shadow_result_id and shadow_result_hash
      as evidence before review or approval.
    """
    record = build_shadow_result_record(
        candidate_id=candidate_id,
        candidate_hash=candidate_hash,
        production_decision=production_decision,
        would_block=would_block,
        would_pass=would_pass,
        envelope_hash=envelope_hash,
        validation_id=validation_id,
        audit_hash=audit_hash,
        pattern_id=pattern_id,
        pattern_hash=pattern_hash,
        audit_signature=audit_signature,
        audit_path=audit_path,
        state=state,
        replay_context=replay_context,
        governance_metadata=governance_metadata,
    )

    return append_shadow_result(record)
