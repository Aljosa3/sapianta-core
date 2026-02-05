from typing import Dict, List

from sapianta_runtime.promotion_simulation.simulate import simulate_promotion
from sapianta_runtime.validator.validate import validate_all


def preview_decisions(
    base_state: Dict[str, str],
    hypothetical_cdrs: List[dict]
) -> Dict[str, Dict[str, str]]:
    """
    READ-ONLY decision preview.

    Thin wrapper over promotion simulation.
    No writes. No inference. No side effects.
    """

    # structural validation only (no repair)
    validate_all(hypothetical_cdrs)

    # delegate to simulation
    return simulate_promotion(
        base_state=base_state,
        hypothetical_cdrs=hypothetical_cdrs
    )
