"""
SAPIANTA Promotion Gate

Controls promotion of research artifacts into runtime strategies.
"""

from datetime import datetime
from runtime.strategies.strategy_registry import register_strategy


ALLOWED_TYPES = [
    "experiment_result",
    "strategy",
    "model"
]


def evaluate_artifact(artifact: dict):

    artifact_type = artifact.get("artifact_type")

    if artifact_type not in ALLOWED_TYPES:
        return "REJECTED"

    metadata = artifact.get("metadata", {})

    performance = metadata.get("performance_score")

    if performance is None:
        return "REQUIRES_REVIEW"

    if performance >= 0.7:
        return "APPROVED"

    return "REJECTED"


def promotion_decision(artifact: dict):

    result = evaluate_artifact(artifact)

    decision = {
        "artifact_id": artifact["artifact_id"],
        "artifact_type": artifact["artifact_type"],
        "promotion_result": result,
        "timestamp": datetime.utcnow().isoformat()
    }

    # If approved, register strategy in runtime registry
    if result == "APPROVED":
        register_strategy(artifact)

    return decision