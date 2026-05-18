"""Deterministic inert intent transfer envelopes."""

from sapianta_bridge.human_interaction_continuity.interaction_session import stable_hash

from .governed_intent_transfer_boundary import transfer_boundary_state

BLOCKED_CAPABILITIES = [
    "execution",
    "automatic_dispatch",
    "orchestration",
    "retries_fallbacks",
    "hidden_continuation",
    "authority_escalation",
    "direct_codex_dispatch",
    "hidden_page_ingestion",
    "full_conversation_ingestion",
]


def build_intent_transfer_package(*, request: dict) -> dict:
    boundary = transfer_boundary_state()
    seed = {
        "conversational_input": request["conversational_input"],
        "normalized_governed_request": request["normalized_governed_request"],
        "governance_mode": request["governance_mode"],
        "bridge_replay_identity": request["bridge_replay_identity"],
    }
    transfer_identity = stable_hash(seed)
    return {
        "package_version": "GOVERNED_INTENT_TRANSFER_PACKAGE_V1",
        "transfer_status": "TRANSFER_READY",
        "transfer_identity": f"INTENT-TRANSFER-{transfer_identity[:24]}",
        "replay_identity": request["bridge_replay_identity"],
        "conversational_input": request["conversational_input"],
        "normalized_governed_request": request["normalized_governed_request"],
        "governance_mode": request["governance_mode"],
        "downstream_runtime_target": request["normalized_governed_request"]["request_type"],
        "requires_preview": True,
        "requires_confirmation": True,
        "execution_authority": False,
        "chatgpt_authority": False,
        "blocked_capabilities": BLOCKED_CAPABILITIES,
        "transfer_boundary_statement": boundary["transfer_boundary_statement"],
        "deterministic_closure": "PREVIEW_ONLY",
        "boundary_state": boundary,
    }
