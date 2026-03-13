"""
SAPIANTA Regime Analyzer

Purpose
-------
Analyze experiment history to understand strategy performance
across different market regimes.

Enables regime-aware strategy development.
"""

from runtime.research.experiment_database import ExperimentDatabase


class RegimeAnalyzer:

    def __init__(self):

        self.db = ExperimentDatabase()

    # ---------------------------------------------------------
    # GLOBAL REGIME PERFORMANCE
    # ---------------------------------------------------------

    def regime_statistics(self):

        data = self.db.load()

        regime_stats = {}

        for exp in data:

            strategy = exp["strategy"]

            for r in exp["results"]:

                regime = r["regime"]
                profit = r["profit"]

                if regime not in regime_stats:

                    regime_stats[regime] = {
                        "profits": [],
                        "strategies": []
                    }

                regime_stats[regime]["profits"].append(profit)
                regime_stats[regime]["strategies"].append(strategy)

        summary = {}

        for regime, values in regime_stats.items():

            profits = values["profits"]

            avg_profit = sum(profits) / len(profits)

            summary[regime] = {
                "experiments": len(profits),
                "avg_profit": avg_profit,
                "max_profit": max(profits),
                "min_profit": min(profits)
            }

        return summary

    # ---------------------------------------------------------
    # BEST STRATEGIES PER REGIME
    # ---------------------------------------------------------

    def best_strategies_by_regime(self):

        data = self.db.load()

        regime_best = {}

        for exp in data:

            strategy = exp["strategy"]

            for r in exp["results"]:

                regime = r["regime"]
                profit = r["profit"]

                if regime not in regime_best:

                    regime_best[regime] = {
                        "strategy": strategy,
                        "profit": profit
                    }

                else:

                    if profit > regime_best[regime]["profit"]:

                        regime_best[regime] = {
                            "strategy": strategy,
                            "profit": profit
                        }

        return regime_best

    # ---------------------------------------------------------
    # STRATEGY REGIME PROFILE
    # ---------------------------------------------------------

    def strategy_profile(self, strategy_name):

        history = self.db.strategy_history(strategy_name)

        regime_scores = {}

        for exp in history:

            for r in exp["results"]:

                regime = r["regime"]
                profit = r["profit"]

                regime_scores.setdefault(regime, []).append(profit)

        profile = {}

        for regime, profits in regime_scores.items():

            profile[regime] = sum(profits) / len(profits)

        return profile


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    analyzer = RegimeAnalyzer()

    print("\nRegime statistics:")
    print(analyzer.regime_statistics())

    print("\nBest strategies per regime:")
    print(analyzer.best_strategies_by_regime())
