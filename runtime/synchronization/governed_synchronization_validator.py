"""Fail-closed governed state synchronization validation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.session.governed_session_validator import validate_governed_execution_session

from .governed_synchronization_boundary import (
    ALLOWED_SYNCHRONIZATION_SCOPE,
    ALLOWED_SYNCHRONIZED_FIELDS,
    PROHIBITED_SYNCHRONIZED_FIELDS,
)
from .governed_synchronization_lineage import REQUIRED_LINEAGE_FIELDS


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_synchronization_payload(payload: dict) -> dict:
    errors = []
    if not isinstance(payload, dict) or not payload:
        return {"valid": False, "errors": [{"field": "synchronized_payload", "reason": "malformed synchronization payload"}]}
    declared = set(payload)
    unauthorized = sorted(declared - set(ALLOWED_SYNCHRONIZED_FIELDS))
    if unauthorized:
        errors.append({"field": "synchronized_payload", "reason": "unauthorized synchronization fields"})
    if declared & set(PROHIBITED_SYNCHRONIZED_FIELDS):
        errors.append({"field": "synchronized_payload", "reason": "prohibited synchronized state"})
    for field in declared:
        if _missing_text(payload.get(field)):
            errors.append({"field": field, "reason": "malformed synchronization payload"})
    return {"valid": not errors, "errors": errors}


def validate_synchronization_chain(chain: dict) -> dict:
    errors = []
    base = {
        "governed_execution_session_id": chain.get("governed_execution_session_id"),
        "lineage": chain.get("lineage"),
        "synchronization_scope": chain.get("synchronization_scope"),
    }
    expected_replay = stable_hash(base)
    expected_id = f"GOVERNED-SYNCHRONIZATION-CHAIN-{expected_replay[:24]}"
    if chain.get("governed_synchronization_chain_id") != expected_id:
        errors.append({"field": "governed_synchronization_chain_id", "reason": "invalid synchronization lineage"})
    if chain.get("replay_identity") != expected_replay:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    if chain.get("synchronization_scope") != ALLOWED_SYNCHRONIZATION_SCOPE:
        errors.append({"field": "synchronization_scope", "reason": "unauthorized synchronization scope"})
    for field in REQUIRED_LINEAGE_FIELDS:
        if _missing_text(chain.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid synchronization lineage"})
    states = chain.get("synchronizations")
    if not isinstance(states, list):
        errors.append({"field": "synchronizations", "reason": "malformed synchronization payload"})
        states = []
    previous_hash = ""
    for expected_index, state in enumerate(states, start=1):
        if state.get("synchronization_index") != expected_index:
            errors.append({"field": "synchronization_index", "reason": "invalid synchronization ordering"})
        if state.get("previous_synchronization_hash") != previous_hash:
            errors.append({"field": "previous_synchronization_hash", "reason": "synchronization continuity break"})
        errors.extend(validate_synchronization_payload(state.get("synchronized_payload", {}))["errors"])
        value = {
            "governed_synchronization_chain_id": state.get("governed_synchronization_chain_id"),
            "synchronization_index": state.get("synchronization_index"),
            "previous_synchronization_hash": state.get("previous_synchronization_hash"),
            "session_head_hash": state.get("session_head_hash"),
            "exchange_index": state.get("exchange_index"),
            "synchronized_payload": state.get("synchronized_payload"),
        }
        expected_hash = stable_hash(value)
        if state.get("synchronization_hash") != expected_hash:
            errors.append({"field": "synchronization_hash", "reason": "replay mismatch"})
        previous_hash = state.get("synchronization_hash", "")
    if chain.get("synchronization_count") != len(states):
        errors.append({"field": "synchronization_count", "reason": "malformed synchronization payload"})
    if chain.get("synchronization_head_hash") != previous_hash:
        errors.append({"field": "synchronization_head_hash", "reason": "synchronization continuity break"})
    return {"valid": not errors, "errors": errors}


def validate_synchronization_append(*, chain: dict, session: dict, synchronized_payload: dict) -> dict:
    errors = list(validate_synchronization_chain(chain)["errors"])
    if not validate_governed_execution_session(session)["valid"]:
        errors.append({"field": "session", "reason": "invalid synchronization lineage"})
    if chain.get("closed") is True:
        errors.append({"field": "closed", "reason": "invalid synchronization closure"})
    if session.get("governed_execution_session_id") != chain.get("governed_execution_session_id"):
        errors.append({"field": "governed_execution_session_id", "reason": "invalid synchronization lineage"})
    if session.get("exchange_count", 0) == 0:
        errors.append({"field": "exchange_count", "reason": "synchronization continuity break"})
    payload_validation = validate_synchronization_payload(synchronized_payload)
    errors.extend(payload_validation["errors"])
    if payload_validation["valid"]:
        latest = session["exchanges"][-1]
        expected_payload = {
            "last_exchange_id": latest["governed_session_exchange_id"],
            "last_exchange_hash": latest["exchange_hash"],
            "last_connector_result_id": latest["connector_result_id"],
            "last_result_status": "RETURNED",
        }
        for field, value in synchronized_payload.items():
            if expected_payload.get(field) != value:
                errors.append({"field": field, "reason": "synchronization continuity break"})
    return {"valid": not errors, "errors": errors}
