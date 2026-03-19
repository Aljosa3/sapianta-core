"""
SAPIANTA Strategy Selector

Purpose
-------
Deterministic selection of development strategy based on evaluation feedback.
Also provides deterministic ranking of fix strategies.
"""

from typing import List, Dict


class StrategySelector:

    """
    Selects generation strategy and ranks fixes.
    """

    # ================================================================
    # EXISTING: STRATEGY SELECTION (KEEP)
    # ================================================================

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

    # ================================================================
    # NEW: FIX RANKING ENGINE
    # ================================================================

    def rank(self, fixes: List[Dict]) -> List[Dict]:
        """
        Deterministic ranking of fixes.

        Priority:
        1. confidence (descending)
        2. strategy priority (tie-breaker)
        """

        return sorted(
            fixes,
            key=lambda f: (
                -f.get("confidence", 0),
                self._strategy_priority(f.get("strategy"))
            )
        )

    # ================================================================
    # INTERNAL PRIORITY MAP
    # ================================================================

    def _strategy_priority(self, strategy: str) -> int:
        """
        Lower number = higher priority
        """

        priority_map = {
            "name_error_stub": 0,
            "import_stub": 1,
            "syntax_fix": 2,
            "replace_function": 3,
            "missing_attribute": 4,
            "type_mismatch": 5,
            "assertion_failure": 6,
            "safe_fallback": 10,
            "regen_stub": 20,
        }

        return priority_map.get(strategy, 100)