"""
SAPIANTA Strategy Selector

Selects the best approved strategy from the Strategy Registry.
"""

from runtime.strategies.strategy_registry import load_strategies


def select_strategy():
    """
    Select the best strategy based on performance score.
    """

    strategies = load_strategies()

    if not strategies:
        return None

    # rank by performance_score
    ranked = sorted(
        strategies,
        key=lambda s: s.get("metadata", {}).get("performance_score", 0),
        reverse=True
    )

    return ranked[0]