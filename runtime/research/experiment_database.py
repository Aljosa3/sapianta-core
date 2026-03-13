"""
SAPIANTA Experiment Database

Purpose
-------
Persistent storage of experiment results.

Enables:
- experiment history
- regime performance analysis
- cross-strategy comparison
"""

import json
from pathlib import Path
from datetime import datetime


DB_PATH = Path("runtime/research/experiment_database.json")


class ExperimentDatabase:

    def __init__(self):

        if not DB_PATH.exists():

            DB_PATH.parent.mkdir(parents=True, exist_ok=True)

            with open(DB_PATH, "w") as f:
                json.dump([], f)

    # ---------------------------------------------------------
    # LOAD DATABASE
    # ---------------------------------------------------------

    def load(self):

        with open(DB_PATH, "r") as f:
            return json.load(f)

    # ---------------------------------------------------------
    # SAVE DATABASE
    # ---------------------------------------------------------

    def save(self, data):

        with open(DB_PATH, "w") as f:
            json.dump(data, f, indent=4)

    # ---------------------------------------------------------
    # RECORD EXPERIMENT
    # ---------------------------------------------------------

    def record(self, experiment_result):

        data = self.load()

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "strategy": experiment_result["strategy"],
            "metrics": experiment_result["metrics"],
            "results": experiment_result["results"]
        }

        data.append(entry)

        self.save(data)

    # ---------------------------------------------------------
    # STRATEGY HISTORY
    # ---------------------------------------------------------

    def strategy_history(self, strategy_name):

        data = self.load()

        return [x for x in data if x["strategy"] == strategy_name]

    # ---------------------------------------------------------
    # REGIME PERFORMANCE
    # ---------------------------------------------------------

    def regime_performance(self):

        data = self.load()

        regime_scores = {}

        for exp in data:

            for r in exp["results"]:

                regime = r["regime"]
                profit = r["profit"]

                regime_scores.setdefault(regime, []).append(profit)

        summary = {}

        for regime, profits in regime_scores.items():

            summary[regime] = sum(profits) / len(profits)

        return summary

    # ---------------------------------------------------------
    # TOP STRATEGIES
    # ---------------------------------------------------------

    def top_strategies(self, n=10):

        data = self.load()

        scored = []

        for exp in data:

            scored.append({
                "strategy": exp["strategy"],
                "score": exp["metrics"]["total_profit"]
            })

        scored.sort(key=lambda x: x["score"], reverse=True)

        return scored[:n]


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    db = ExperimentDatabase()

    data = db.load()

    print("Experiments:", len(data))

    print("\nTop strategies:")
    print(db.top_strategies(5))

    print("\nRegime performance:")
    print(db.regime_performance())
