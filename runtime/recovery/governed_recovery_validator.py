"""Fail-closed governed operational recovery validation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.session.governed_session_validator import validate_governed_execution_session
from sapianta_system.runtime.synchronization.governed_synchronization_validator import validate_synchronization_chain

from .governed_recovery_authorization import (
    ALLOWED_RECOVERY_SCOPE,
    validate_recovery_authorization,
)
from .governed_recovery_lineage import REQUIRED_LINEAGE_FIELDS

REQUIRED_RECOVERY_PAYLOAD_FIELDS = (
    "interruption_code",
    "continuation_intent",
)


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_recovery_payload(payload: dict) -> dict:
    errors = []
    if not isinstance(payload, dict):
        return {"valid": False, "errors": [{"field": "recovery_payload", "reason": "malformed recovery payload"}]}
    for field in REQUIRED_RECOVERY_PAYLOAD_FIELDS:
        if _missing_text(payload.get(field)):
            errors.append({"field": field, "reason": "malformed recovery payload"})
    forbidden_true_fields = (
        "retry_present",
        "fallback_present",
        "orchestration_present",
        "autonomous_continuation_present",
        "hidden_continuation_present",
    )
    for field in forbidden_true_fields:
        if payload.get(field) is not False:
            errors.append({"field": field, "reason": "hidden continuation attempts"})
    return {"valid": not errors, "errors": errors}


def validate_recovery_chain(chain: dict) -> dict:
    errors = []
    base = {
        "governed_execution_session_id": chain.get("governed_execution_session_id"),
        "governed_synchronization_chain_id": chain.get("governed_synchronization_chain_id"),
        "lineage": chain.get("lineage"),
        "recovery_scope": chain.get("recovery_scope"),
    }
    expected_replay = stable_hash(base)
    expected_id = f"GOVERNED-RECOVERY-CHAIN-{expected_replay[:24]}"
    if chain.get("governed_recovery_chain_id") != expected_id:
        errors.append({"field": "governed_recovery_chain_id", "reason": "invalid recovery lineage"})
    if chain.get("replay_identity") != expected_replay:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    if chain.get("recovery_scope") != ALLOWED_RECOVERY_SCOPE:
        errors.append({"field": "recovery_scope", "reason": "unauthorized recovery"})
    for field in REQUIRED_LINEAGE_FIELDS:
        if _missing_text(chain.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid recovery lineage"})
    recoveries = chain.get("recoveries")
    if not isinstance(recoveries, list):
        errors.append({"field": "recoveries", "reason": "malformed recovery payload"})
        recoveries = []
    previous_hash = ""
    for expected_index, recovery in enumerate(recoveries, start=1):
        if recovery.get("recovery_index") != expected_index:
            errors.append({"field": "recovery_index", "reason": "invalid recovery ordering"})
        if recovery.get("previous_recovery_hash") != previous_hash:
            errors.append({"field": "previous_recovery_hash", "reason": "recovery continuity break"})
        errors.extend(validate_recovery_payload(recovery.get("recovery_payload", {}))["errors"])
        value = {
            "governed_recovery_chain_id": recovery.get("governed_recovery_chain_id"),
            "recovery_index": recovery.get("recovery_index"),
            "previous_recovery_hash": recovery.get("previous_recovery_hash"),
            "interrupted_exchange_id": recovery.get("interrupted_exchange_id"),
            "interrupted_exchange_hash": recovery.get("interrupted_exchange_hash"),
            "interrupted_synchronization_id": recovery.get("interrupted_synchronization_id"),
            "interrupted_synchronization_hash": recovery.get("interrupted_synchronization_hash"),
            "recovery_authorization_id": recovery.get("recovery_authorization_id"),
            "recovery_payload": recovery.get("recovery_payload"),
        }
        expected_hash = stable_hash(value)
        if recovery.get("recovery_hash") != expected_hash:
            errors.append({"field": "recovery_hash", "reason": "replay mismatch"})
        previous_hash = recovery.get("recovery_hash", "")
    if chain.get("recovery_count") != len(recoveries):
        errors.append({"field": "recovery_count", "reason": "malformed recovery payload"})
    if chain.get("recovery_head_hash") != previous_hash:
        errors.append({"field": "recovery_head_hash", "reason": "recovery continuity break"})
    return {"valid": not errors, "errors": errors}


def validate_recovery_append(
    *,
    chain: dict,
    session: dict,
    synchronization_chain: dict,
    recovery_payload: dict,
    authorization: dict,
) -> dict:
    errors = list(validate_recovery_chain(chain)["errors"])
    if chain.get("closed") is True:
        errors.append({"field": "closed", "reason": "invalid recovery closure"})
    if not validate_governed_execution_session(session)["valid"]:
        errors.append({"field": "session", "reason": "invalid recovery lineage"})
    if not validate_synchronization_chain(synchronization_chain)["valid"]:
        errors.append({"field": "synchronization_chain", "reason": "invalid recovery lineage"})
    if session.get("governed_execution_session_id") != chain.get("governed_execution_session_id"):
        errors.append({"field": "governed_execution_session_id", "reason": "invalid recovery lineage"})
    if synchronization_chain.get("governed_synchronization_chain_id") != chain.get("governed_synchronization_chain_id"):
        errors.append({"field": "governed_synchronization_chain_id", "reason": "invalid recovery lineage"})
    if session.get("exchange_count", 0) == 0:
        errors.append({"field": "exchange_count", "reason": "invalid recovery lineage"})
    if synchronization_chain.get("synchronization_count", 0) == 0:
        errors.append({"field": "synchronization_count", "reason": "invalid recovery lineage"})
    errors.extend(validate_recovery_payload(recovery_payload)["errors"])
    errors.extend(validate_recovery_authorization(authorization)["errors"])
    if not errors:
        latest_exchange = session["exchanges"][-1]
        latest_synchronization = synchronization_chain["synchronizations"][-1]
        payload_exchange_id = latest_synchronization["synchronized_payload"]["last_exchange_id"]
        payload_exchange_hash = latest_synchronization["synchronized_payload"]["last_exchange_hash"]
        if payload_exchange_id != latest_exchange["governed_session_exchange_id"]:
            errors.append({"field": "interrupted_exchange_id", "reason": "invalid recovery lineage"})
        if payload_exchange_hash != latest_exchange["exchange_hash"]:
            errors.append({"field": "interrupted_exchange_hash", "reason": "invalid recovery lineage"})
    return {"valid": not errors, "errors": errors}
