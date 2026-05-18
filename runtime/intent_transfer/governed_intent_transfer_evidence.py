"""Replay-visible evidence for inert intent transfer packages."""


def governed_intent_transfer_evidence(*, request: dict, package: dict, replay_identity: str) -> dict:
    return {
        "original_conversational_input": request["conversational_input"],
        "normalized_governed_request": request["normalized_governed_request"],
        "transfer_identity": package["transfer_identity"],
        "replay_identity": replay_identity,
        "downstream_target_description": package["downstream_runtime_target"],
        "blocked_capability_guarantees": package["blocked_capabilities"],
        "transfer_boundary_state": package["boundary_state"],
        "closure_semantics": package["deterministic_closure"],
    }
