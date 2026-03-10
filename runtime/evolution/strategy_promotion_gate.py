"""
SAPIANTA Strategy Promotion Gate

Purpose
-------
Govern which strategies can become production strategies.
"""

from runtime.evolution.strategy_registry import load_registry


PROMOTION_RULES = {

    "min_acceptance_ratio": 0.6,
    "min_decisions": 20

}


def eligible_strategies():
    """
    Find strategies eligible for promotion.
    """

    registry = load_registry()

    candidates = []

    for entry in registry:

        evaluation = entry["evaluation"]

        if (
            evaluation["acceptance_ratio"] >= PROMOTION_RULES["min_acceptance_ratio"]
            and evaluation["decisions"] >= PROMOTION_RULES["min_decisions"]
        ):
            candidates.append(entry)

    return candidates


def select_best_candidate():

    candidates = eligible_strategies()

    if not candidates:
        return None

    ranked = sorted(
        candidates,
        key=lambda x: x["evaluation"]["acceptance_ratio"],
        reverse=True
    )

    return ranked[0]


if __name__ == "__main__":

    candidate = select_best_candidate()

    if candidate:

        print("Strategy eligible for promotion:")
        print(candidate["strategy_id"])

    else:

        print("No strategies meet promotion criteria.")