"""Governed transfer ingestion responses."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_intent_transfer_ingestion_boundary import ingestion_boundary_state
from .governed_intent_transfer_ingestion_evidence import governed_intent_transfer_ingestion_evidence
from .governed_intent_transfer_ingestion_pipeline import build_preview_ready_governance_intake
from .governed_intent_transfer_ingestion_replay import build_intent_transfer_ingestion_replay_identity
from .governed_intent_transfer_ingestion_validator import validate_intent_transfer_ingestion_request


def _blocked(request: dict, errors: list[dict]) -> dict:
    package = request.get("transfer_package", {}) if isinstance(request, dict) else {}
    return {
        "ingestion_status": "BLOCKED",
        "ingestion_identity": "",
        "replay_identity": request.get("replay_identity", "") if isinstance(request, dict) else "",
        "transfer_identity": request.get("transfer_identity", "") if isinstance(request, dict) else "",
        "governance_mode": package.get("governance_mode"),
        "preview_required": True,
        "confirmation_required": True,
        "authority_validated": False,
        "authority_granted": False,
        "downstream_runtime_target": package.get("downstream_runtime_target"),
        "blocked_capabilities": package.get("blocked_capabilities", []),
        "ingestion_boundary_statement": ingestion_boundary_state()["ingestion_boundary_statement"],
        "deterministic_closure": "BLOCKED",
        "boundary_state": ingestion_boundary_state(),
        "validation": {"valid": False, "errors": errors},
    }


def ingest_governed_intent_transfer(request: dict) -> dict:
    validation = validate_intent_transfer_ingestion_request(request)
    if not validation["valid"]:
        return _blocked(request, validation["errors"])
    package = request["transfer_package"]
    intake = build_preview_ready_governance_intake(transfer_package=package)
    replay_identity = build_intent_transfer_ingestion_replay_identity(
        request=request,
        validation=validation,
        intake=intake,
    )
    ingestion_identity = f"INTENT-TRANSFER-INGESTION-{stable_hash({'request': request, 'intake': intake})[:24]}"
    response = {
        "ingestion_status": "INGESTED_PREVIEW_READY",
        "ingestion_identity": ingestion_identity,
        "replay_identity": replay_identity,
        "transfer_identity": package["transfer_identity"],
        "governance_mode": package["governance_mode"],
        "preview_required": True,
        "confirmation_required": True,
        "authority_validated": True,
        "authority_granted": False,
        "downstream_runtime_target": package["downstream_runtime_target"],
        "blocked_capabilities": package["blocked_capabilities"],
        "ingestion_boundary_statement": ingestion_boundary_state()["ingestion_boundary_statement"],
        "deterministic_closure": "PREVIEW_READY",
        "boundary_state": ingestion_boundary_state(),
        "timeline_state": [
            "TRANSFER_VALIDATED",
            "REPLAY_CONTINUITY_VALIDATED",
            "PREVIEW_READY",
        ],
        "preview_ready_governance_intake": intake,
        "validation": validation,
    }
    response["evidence"] = governed_intent_transfer_ingestion_evidence(
        transfer_package=package,
        response=response,
        validation=validation,
    )
    return response
