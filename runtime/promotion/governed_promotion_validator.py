"""Fail-closed certified promotion pipeline validation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.recovery.governed_recovery_validator import validate_recovery_chain
from sapianta_system.runtime.session.governed_session_validator import validate_governed_execution_session
from sapianta_system.runtime.synchronization.governed_synchronization_validator import validate_synchronization_chain

from .governed_promotion_authorization import (
    ALLOWED_CERTIFICATION_SCOPE,
    validate_promotion_authorization,
)
from .governed_promotion_lineage import REQUIRED_LINEAGE_FIELDS

REQUIRED_PROMOTION_PAYLOAD_FIELDS = (
    "certification_intent",
    "certification_basis",
)


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_promotion_payload(payload: dict) -> dict:
    errors = []
    if not isinstance(payload, dict):
        return {"valid": False, "errors": [{"field": "promotion_payload", "reason": "malformed promotion payload"}]}
    for field in REQUIRED_PROMOTION_PAYLOAD_FIELDS:
        if _missing_text(payload.get(field)):
            errors.append({"field": field, "reason": "malformed promotion payload"})
    forbidden_true_fields = (
        "deployment_present",
        "rollout_present",
        "orchestration_present",
        "autonomous_rollout_present",
        "hidden_approval_present",
    )
    for field in forbidden_true_fields:
        if payload.get(field) is not False:
            errors.append({"field": field, "reason": "deployment semantics disguised as certification"})
    return {"valid": not errors, "errors": errors}


def validate_promotion_pipeline(pipeline: dict) -> dict:
    errors = []
    base = {
        "governed_execution_session_id": pipeline.get("governed_execution_session_id"),
        "governed_synchronization_chain_id": pipeline.get("governed_synchronization_chain_id"),
        "governed_recovery_chain_id": pipeline.get("governed_recovery_chain_id"),
        "lineage": pipeline.get("lineage"),
        "certification_scope": pipeline.get("certification_scope"),
    }
    expected_replay = stable_hash(base)
    expected_id = f"CERTIFIED-PROMOTION-PIPELINE-{expected_replay[:24]}"
    if pipeline.get("certified_promotion_pipeline_id") != expected_id:
        errors.append({"field": "certified_promotion_pipeline_id", "reason": "invalid promotion lineage"})
    if pipeline.get("replay_identity") != expected_replay:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    if pipeline.get("certification_scope") != ALLOWED_CERTIFICATION_SCOPE:
        errors.append({"field": "certification_scope", "reason": "unauthorized promotion"})
    for field in REQUIRED_LINEAGE_FIELDS:
        if _missing_text(pipeline.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid promotion lineage"})
    promotions = pipeline.get("promotions")
    if not isinstance(promotions, list):
        errors.append({"field": "promotions", "reason": "malformed promotion payload"})
        promotions = []
    previous_hash = ""
    for expected_index, promotion in enumerate(promotions, start=1):
        if promotion.get("promotion_index") != expected_index:
            errors.append({"field": "promotion_index", "reason": "invalid promotion ordering"})
        if promotion.get("previous_promotion_hash") != previous_hash:
            errors.append({"field": "previous_promotion_hash", "reason": "invalid certification continuity"})
        errors.extend(validate_promotion_payload(promotion.get("promotion_payload", {}))["errors"])
        value = {
            "certified_promotion_pipeline_id": promotion.get("certified_promotion_pipeline_id"),
            "promotion_index": promotion.get("promotion_index"),
            "previous_promotion_hash": promotion.get("previous_promotion_hash"),
            "promoted_runtime_state_id": promotion.get("promoted_runtime_state_id"),
            "synchronization_lineage_id": promotion.get("synchronization_lineage_id"),
            "recovery_lineage_id": promotion.get("recovery_lineage_id"),
            "promotion_authorization_id": promotion.get("promotion_authorization_id"),
            "promotion_payload": promotion.get("promotion_payload"),
        }
        expected_hash = stable_hash(value)
        if promotion.get("promotion_hash") != expected_hash:
            errors.append({"field": "promotion_hash", "reason": "replay mismatch"})
        previous_hash = promotion.get("promotion_hash", "")
    if pipeline.get("promotion_count") != len(promotions):
        errors.append({"field": "promotion_count", "reason": "malformed promotion payload"})
    if pipeline.get("promotion_head_hash") != previous_hash:
        errors.append({"field": "promotion_head_hash", "reason": "invalid certification continuity"})
    return {"valid": not errors, "errors": errors}


def validate_promotion_append(
    *,
    pipeline: dict,
    session: dict,
    synchronization_chain: dict,
    recovery_chain: dict,
    promotion_payload: dict,
    authorization: dict,
) -> dict:
    errors = list(validate_promotion_pipeline(pipeline)["errors"])
    if pipeline.get("closed") is True:
        errors.append({"field": "closed", "reason": "invalid promotion closure"})
    if not validate_governed_execution_session(session)["valid"]:
        errors.append({"field": "session", "reason": "invalid promotion lineage"})
    if not validate_synchronization_chain(synchronization_chain)["valid"]:
        errors.append({"field": "synchronization_chain", "reason": "invalid promotion lineage"})
    if not validate_recovery_chain(recovery_chain)["valid"]:
        errors.append({"field": "recovery_chain", "reason": "invalid promotion lineage"})
    bindings = (
        ("governed_execution_session_id", session.get("governed_execution_session_id")),
        ("governed_synchronization_chain_id", synchronization_chain.get("governed_synchronization_chain_id")),
        ("governed_recovery_chain_id", recovery_chain.get("governed_recovery_chain_id")),
    )
    for field, value in bindings:
        if pipeline.get(field) != value:
            errors.append({"field": field, "reason": "invalid promotion lineage"})
    if session.get("exchange_count", 0) == 0:
        errors.append({"field": "exchange_count", "reason": "invalid promotion lineage"})
    if synchronization_chain.get("synchronization_count", 0) == 0:
        errors.append({"field": "synchronization_count", "reason": "invalid promotion lineage"})
    if recovery_chain.get("recovery_count", 0) == 0:
        errors.append({"field": "recovery_count", "reason": "invalid promotion lineage"})
    errors.extend(validate_promotion_payload(promotion_payload)["errors"])
    errors.extend(validate_promotion_authorization(authorization)["errors"])
    if not errors:
        latest_recovery = recovery_chain["recoveries"][-1]
        latest_synchronization = synchronization_chain["synchronizations"][-1]
        if latest_recovery["interrupted_synchronization_hash"] != latest_synchronization["synchronization_hash"]:
            errors.append({"field": "recovery_lineage_id", "reason": "invalid certification continuity"})
        if latest_synchronization["session_head_hash"] != session["session_head_hash"]:
            errors.append({"field": "promoted_runtime_state_id", "reason": "invalid certification continuity"})
    return {"valid": not errors, "errors": errors}
