"""Replay-visible evidence for governed transfer ingestion."""


def governed_intent_transfer_ingestion_evidence(
    *, transfer_package: dict, response: dict, validation: dict
) -> dict:
    return {
        "original_conversational_input": transfer_package["conversational_input"],
        "normalized_governed_request": transfer_package["normalized_governed_request"],
        "transfer_package": transfer_package,
        "transfer_identity": response["transfer_identity"],
        "replay_identity": response["replay_identity"],
        "ingestion_identity": response["ingestion_identity"],
        "ingestion_validation_outcome": validation,
        "blocked_capability_guarantees": response["blocked_capabilities"],
        "ingestion_boundary_state": response["boundary_state"],
        "deterministic_closure_semantics": response["deterministic_closure"],
    }
