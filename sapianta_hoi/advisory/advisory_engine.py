from typing import Dict, Any

from sapianta_hoi.advisory.ranking_rules import rank_options
from sapianta_hoi.advisory.confidence import compute_confidence


class AdvisoryEngine:
    """
    Deterministic advisory layer.

    Pure function:
    snapshot -> advisory_payload

    No state mutation.
    No IO.
    No learning.
    """

    def generate(self, snapshot: Dict[str, Any]) -> Dict[str, Any]:
        rankings = rank_options(snapshot)
        confidence = compute_confidence(snapshot)

        return {
            "rankings": rankings,
            "confidence": confidence,
            "advisory_mode": "deterministic",
        }
