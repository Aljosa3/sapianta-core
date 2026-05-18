"""Fail-closed validation for governed transfer ingestion."""

REQUIRED_BLOCKED_CAPABILITIES = {
    "execution",
    "automatic_dispatch",
    "orchestration",
    "retries_fallbacks",
    "hidden_continuation",
    "authority_escalation",
    "direct_codex_dispatch",
    "hidden_page_ingestion",
    "full_conversation_ingestion",
}

SUPPORTED_TARGETS = {
    "GOVERNED_INTERPRETATION_REQUEST",
    "GOVERNED_SYNTHESIS_REQUEST",
    "GOVERNED_OBSERVABILITY_REQUEST",
}


def validate_intent_transfer_ingestion_request(request: dict) -> dict:
    errors = []
    if not isinstance(request, dict):
        return {"valid": False, "errors": [{"field": "request", "reason": "malformed ingestion request"}]}
    package = request.get("transfer_package")
    if not isinstance(package, dict):
        return {"valid": False, "errors": [{"field": "transfer_package", "reason": "malformed transfer package"}]}
    if request.get("replay_identity") != package.get("replay_identity"):
        errors.append({"field": "replay_identity", "reason": "replay mismatch"})
    if request.get("transfer_identity") != package.get("transfer_identity"):
        errors.append({"field": "transfer_identity", "reason": "transfer identity mismatch"})
    if package.get("transfer_status") != "TRANSFER_READY":
        errors.append({"field": "transfer_status", "reason": "transfer not ready"})
    if package.get("requires_preview") is not True:
        errors.append({"field": "requires_preview", "reason": "preview required"})
    if package.get("requires_confirmation") is not True:
        errors.append({"field": "requires_confirmation", "reason": "confirmation required"})
    if package.get("execution_authority") is not False:
        errors.append({"field": "execution_authority", "reason": "authority escalation forbidden"})
    if package.get("chatgpt_authority") is not False:
        errors.append({"field": "chatgpt_authority", "reason": "chatgpt authority forbidden"})
    if package.get("downstream_runtime_target") not in SUPPORTED_TARGETS:
        errors.append({"field": "downstream_runtime_target", "reason": "malformed runtime target"})
    if not REQUIRED_BLOCKED_CAPABILITIES.issubset(set(package.get("blocked_capabilities", []))):
        errors.append({"field": "blocked_capabilities", "reason": "blocked capability guarantees missing"})
    boundary = package.get("boundary_state", {})
    expected_boundary = {
        "chatgpt_authority": False,
        "execution_authority": False,
        "automatic_dispatch": False,
        "orchestration": False,
        "hidden_continuation": False,
        "preview_required": True,
        "confirmation_required": True,
    }
    for field, expected in expected_boundary.items():
        if boundary.get(field) is not expected:
            errors.append({"field": field, "reason": "transfer boundary mismatch"})
    for field in ("execution", "automatic_dispatch", "orchestration", "hidden_continuation"):
        if package.get(field) is True:
            errors.append({"field": field, "reason": "blocked ingestion capability detected"})
    return {"valid": not errors, "errors": errors}
