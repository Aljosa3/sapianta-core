"""
SAPIANTA Strategy Selector

Purpose
-------
Deterministic selection of development strategy based on evaluation feedback.
"""


class StrategySelector:

    """
    Selects generation strategy based on previous evaluation score.
    """

    def select(self, evaluation: dict) -> str:
        """
        Returns strategy type:
        - "standard"
        - "fallback"
        """

        score = evaluation.get("score", 0)

        # deterministic thresholds
        if score < 0.4:
            return "fallback"

        return "standard"