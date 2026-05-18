"""Fail-closed validation for the MCP-ready wrapper."""

from __future__ import annotations

from sapianta_system.runtime.chatgpt_bridge.governed_chatgpt_bridge_validator import validate_chatgpt_bridge_runtime_response
from sapianta_system.runtime.operator.governed_operator_validator import validate_operator_target


def validate_mcp_tool_input(payload: dict) -> dict:
    errors = []
    if not isinstance(payload, dict):
        return {"valid": False, "errors": [{"field": "input", "reason": "malformed MCP input"}]}
    artifact = payload.get("artifact")
    if not isinstance(artifact, str) or not artifact.strip():
        errors.append({"field": "artifact", "reason": "artifact must be non-empty"})
    host = payload.get("host", "127.0.0.1")
    errors.extend(validate_operator_target(host=host)["errors"])
    port = payload.get("port", 8110)
    if not isinstance(port, int) or port <= 0:
        errors.append({"field": "port", "reason": "invalid port"})
    return {"valid": not errors, "errors": errors}


def validate_mcp_tool_output(response: dict) -> dict:
    errors = []
    if response.get("status") != "RETURNED":
        errors.append({"field": "status", "reason": "bridge response not returned"})
    if response.get("closure") != "PASS":
        errors.append({"field": "closure", "reason": "bridge closure not passed"})
    for field in ("request_id", "response_id", "replay_identity"):
        value = response.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append({"field": field, "reason": "malformed bridge response"})
    evidence = response.get("evidence")
    if not isinstance(evidence, dict):
        errors.append({"field": "evidence", "reason": "missing replay evidence"})
    elif evidence.get("localhost_only") is not True or evidence.get("response_returned") is not True or evidence.get("replay_safe") is not True:
        errors.append({"field": "evidence", "reason": "missing replay evidence"})
    return {"valid": not errors, "errors": errors}


def validate_bridge_runtime_response(response: dict) -> dict:
    return validate_chatgpt_bridge_runtime_response(response)
