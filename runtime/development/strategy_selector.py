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
    # UPDATED: FIX RANKING ENGINE (ADAPTIVE PATCH)
    # ================================================================

    def rank(self, fixes: List[Dict]) -> List[Dict]:
        """
        Deterministic + adaptive ranking of fixes.

        Priority:
        1. intent/semantic fixes (highest)
        2. adaptive score (confidence + heuristics + memory)
        3. strategy priority (tie-breaker)
        """

        # =====================================================
        # 🧠 ADAPTIVE STRATEGY WEIGHTING (MINIMAL, SAFE)
        # =====================================================

        def adaptive_score(f):
            base = f.get("confidence", 0)
            strategy = str(f.get("strategy", ""))

            # 🔥 heuristic boost
            if "callsite" in strategy:
                base += 0.05

            # 🔥 penalize fallback
            if "fallback" in strategy:
                base -= 0.2

            # =====================================================
            # 🧠 FixMemory influence (MINIMAL, NON-INTRUSIVE)
            # =====================================================
            try:
                if hasattr(self, "fix_memory") and strategy:
                    error_text = f.get("error", "")
                    best = self.fix_memory.get_best_strategy(error_text)

                    if best == strategy:
                        base += 0.5  # 🔥 minimal adaptive boost

            except Exception:
                pass
            # =====================================================

            return base

        # =====================================================

        return sorted(
            fixes,
            key=lambda f: (
                0 if str(f.get("strategy", "")).startswith("intent_") or
                     str(f.get("strategy", "")).startswith("semantic_")
                else 1,
                -adaptive_score(f),
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

            # 🔥 NEW semantic strategies
            "type_error_signature_fix": 2,
            "type_error_keyword_fix": 2,
            "type_error_multiple_values_fix_function": 2,
            "type_error_multiple_values_fix_callsite": 1,  # slightly preferred
            "type_error_multiple_values_fix_function_fallback": 3,

            "safe_fallback": 10,
            "regen_stub": 20,
        }

        return priority_map.get(strategy, 100)