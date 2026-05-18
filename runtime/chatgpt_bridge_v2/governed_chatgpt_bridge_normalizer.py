"""Deterministic conversational normalization."""

from sapianta_system.runtime.intent import create_governed_intent_request
from sapianta_system.runtime.codex_synthesis import create_governed_codex_task_request

NORMALIZATION_RULES = {
    "prepare finalize milestone": {
        "normalized_request_type": "GOVERNED_SYNTHESIS_REQUEST",
        "governance_mode": "BOUNDED_CODEX_SYNTHESIS",
        "downstream_text": "prepare finalize milestone",
    },
    "prepare governance validation": {
        "normalized_request_type": "GOVERNED_INTERPRETATION_REQUEST",
        "governance_mode": "BOUNDED_RUNTIME_VALIDATION_PREVIEW",
        "downstream_text": "runtime validation",
    },
    "inspect previous execution": {
        "normalized_request_type": "GOVERNED_OBSERVABILITY_REQUEST",
        "governance_mode": "READ_ONLY_EXECUTION_OBSERVABILITY",
        "downstream_text": "inspect governed execution",
    },
    "show execution trace": {
        "normalized_request_type": "GOVERNED_OBSERVABILITY_REQUEST",
        "governance_mode": "READ_ONLY_EXECUTION_OBSERVABILITY",
        "downstream_text": "inspect governed execution",
    },
}


def normalize_conversational_request(conversational_input: str) -> dict:
    normalized = " ".join(conversational_input.lower().split())
    rule = NORMALIZATION_RULES.get(normalized)
    if not rule:
        return {"valid": False, "reason": "ambiguous or unsupported conversational request"}
    request_type = rule["normalized_request_type"]
    downstream_text = rule["downstream_text"]
    if request_type == "GOVERNED_INTERPRETATION_REQUEST":
        downstream_request = create_governed_intent_request(natural_language=downstream_text)
    elif request_type == "GOVERNED_SYNTHESIS_REQUEST":
        downstream_request = create_governed_codex_task_request(natural_language=downstream_text)
    else:
        downstream_request = {
            "observability_action": "INSPECT_GOVERNED_EXECUTION",
            "read_only": True,
            "execution_triggered": False,
        }
    return {
        "valid": True,
        "normalized_request_type": request_type,
        "normalized_conversational_request": normalized,
        "governance_mode": rule["governance_mode"],
        "downstream_governance_request": downstream_request,
    }
