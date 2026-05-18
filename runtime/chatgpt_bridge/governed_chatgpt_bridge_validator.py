"""Fail-closed validation for governed ChatGPT bridge calls."""

from __future__ import annotations

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash
from sapianta_system.runtime.operator.governed_operator_validator import validate_operator_response, validate_operator_target


def validate_chatgpt_bridge_request(request: dict) -> dict:
    errors = []
    artifact = request.get("artifact")
    if not isinstance(artifact, str) or not artifact.strip():
        errors.append({"field": "artifact", "reason": "artifact must be non-empty"})
    errors.extend(validate_operator_target(host=request.get("host", ""))["errors"])
    if not isinstance(request.get("port"), int) or request["port"] <= 0:
        errors.append({"field": "port", "reason": "invalid port"})
    value = {"artifact": request.get("artifact"), "host": request.get("host"), "port": request.get("port")}
    expected = stable_hash(value)
    if request.get("replay_identity") != expected:
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    expected_id = f"CHATGPT-BRIDGE-REQUEST-{expected[:24]}"
    if request.get("chatgpt_bridge_request_id") != expected_id:
        errors.append({"field": "chatgpt_bridge_request_id", "reason": "malformed bridge request"})
    return {"valid": not errors, "errors": errors}


def validate_chatgpt_bridge_runtime_response(response: dict) -> dict:
    return validate_operator_response(response)
