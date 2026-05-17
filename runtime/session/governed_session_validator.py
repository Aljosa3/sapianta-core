"""Fail-closed governed execution session validation."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_session_lineage import REQUIRED_LINEAGE_FIELDS


def _missing_text(value: object) -> bool:
    return not isinstance(value, str) or not value.strip()


def validate_governed_execution_session(session: dict) -> dict:
    errors = []
    base = {"session_seed": session.get("session_seed"), "lineage": session.get("lineage")}
    expected_replay = stable_hash(base)
    expected_id = f"GOVERNED-EXECUTION-SESSION-{expected_replay[:24]}"
    if session.get("governed_execution_session_id") != expected_id:
        errors.append({"field": "governed_execution_session_id", "reason": "invalid session lineage"})
    if session.get("replay_identity") != expected_replay:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    for field in REQUIRED_LINEAGE_FIELDS:
        if _missing_text(session.get("lineage", {}).get(field)):
            errors.append({"field": field, "reason": "invalid session lineage"})
    exchanges = session.get("exchanges")
    if not isinstance(exchanges, list):
        errors.append({"field": "exchanges", "reason": "malformed session state"})
        exchanges = []
    previous_hash = ""
    for expected_index, exchange in enumerate(exchanges, start=1):
        if exchange.get("exchange_index") != expected_index:
            errors.append({"field": "exchange_index", "reason": "invalid exchange ordering"})
        if exchange.get("previous_exchange_hash") != previous_hash:
            errors.append({"field": "previous_exchange_hash", "reason": "exchange continuity break"})
        value = {
            "governed_execution_session_id": exchange.get("governed_execution_session_id"),
            "exchange_index": exchange.get("exchange_index"),
            "previous_exchange_hash": exchange.get("previous_exchange_hash"),
            "connector_id": exchange.get("connector_id"),
            "connector_result_id": exchange.get("connector_result_id"),
            "connector_replay_identity": exchange.get("connector_replay_identity"),
        }
        expected_hash = stable_hash(value)
        if exchange.get("exchange_hash") != expected_hash:
            errors.append({"field": "exchange_hash", "reason": "replay mismatch"})
        previous_hash = exchange.get("exchange_hash", "")
    if session.get("exchange_count") != len(exchanges):
        errors.append({"field": "exchange_count", "reason": "malformed session state"})
    if session.get("session_head_hash") != previous_hash:
        errors.append({"field": "session_head_hash", "reason": "exchange continuity break"})
    return {"valid": not errors, "errors": errors}


def validate_session_append(*, session: dict, connector_output: dict) -> dict:
    errors = list(validate_governed_execution_session(session)["errors"])
    if session.get("closed") is True:
        errors.append({"field": "closed", "reason": "unauthorized continuation"})
    if connector_output.get("connector_status") != "COMPLETED":
        errors.append({"field": "connector_status", "reason": "exchange continuity break"})
    evidence = connector_output.get("evidence", {})
    if evidence.get("replay_safe") is not True or evidence.get("lineage_preserved") is not True:
        errors.append({"field": "connector_evidence", "reason": "exchange continuity break"})
    return {"valid": not errors, "errors": errors}
