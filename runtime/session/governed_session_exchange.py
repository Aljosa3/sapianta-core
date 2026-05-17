"""Deterministic governed session exchange chaining."""

from __future__ import annotations

from copy import deepcopy

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_session_validator import validate_session_append


def _exchange_record(*, session: dict, connector_output: dict) -> dict:
    index = session["exchange_count"] + 1
    connector_result = connector_output["result"]
    value = {
        "governed_execution_session_id": session["governed_execution_session_id"],
        "exchange_index": index,
        "previous_exchange_hash": session["session_head_hash"],
        "connector_id": connector_output["registration"]["connector_id"],
        "connector_result_id": connector_result["connector_result_id"],
        "connector_replay_identity": connector_result["replay_identity"],
    }
    exchange_hash = stable_hash(value)
    return {
        **value,
        "governed_session_exchange_id": f"GOVERNED-SESSION-EXCHANGE-{exchange_hash[:24]}",
        "exchange_hash": exchange_hash,
    }


def append_governed_exchange(*, session: dict, connector_output: dict) -> dict:
    validation = validate_session_append(session=session, connector_output=connector_output)
    if not validation["valid"]:
        return {"session": deepcopy(session), "validation": validation, "states": ["BLOCKED"]}
    exchange = _exchange_record(session=session, connector_output=connector_output)
    next_session = deepcopy(session)
    next_session["exchanges"].append(exchange)
    next_session["exchange_count"] += 1
    next_session["session_head_hash"] = exchange["exchange_hash"]
    return {
        "session": next_session,
        "exchange": exchange,
        "validation": {"valid": True, "errors": []},
        "states": ["EXCHANGE_APPENDED"],
    }
