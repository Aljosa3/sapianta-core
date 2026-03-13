"""
SAPIANTA Strategy Registry

Purpose
-------
Persistent registry of discovered strategies and their performance.

Allows cumulative research instead of restarting search from scratch.
"""

import json
from pathlib import Path


REGISTRY_PATH = Path("runtime/research/strategy_registry.json")


class StrategyRegistry:

    def __init__(self):

        if not REGISTRY_PATH.exists():

            REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)

            with open(REGISTRY_PATH, "w") as f:
                json.dump([], f)

    # ---------------------------------------------------------
    # LOAD REGISTRY
    # ---------------------------------------------------------

    def load(self):

        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)

    # ---------------------------------------------------------
    # SAVE REGISTRY
    # ---------------------------------------------------------

    def save(self, data):

        with open(REGISTRY_PATH, "w") as f:
            json.dump(data, f, indent=4)

    # ---------------------------------------------------------
    # ADD STRATEGY
    # ---------------------------------------------------------

    def register(self, strategy_name, score):

        data = self.load()

        entry = {
            "strategy": strategy_name,
            "score": score
        }

        data.append(entry)

        self.save(data)

    # ---------------------------------------------------------
    # GET BEST STRATEGY
    # ---------------------------------------------------------

    def best(self):

        data = self.load()

        if not data:
            return None

        return max(data, key=lambda x: x["score"])

    # ---------------------------------------------------------
    # LEADERBOARD
    # ---------------------------------------------------------

    def leaderboard(self, top_n=10):

        data = self.load()

        sorted_data = sorted(
            data,
            key=lambda x: x["score"],
            reverse=True
        )

        return sorted_data[:top_n]


# ---------------------------------------------------------
# TEST
# ---------------------------------------------------------

if __name__ == "__main__":

    registry = StrategyRegistry()

    registry.register("strategy_test", 12.5)
    registry.register("strategy_test_2", 8.3)

    print("\nBest strategy:")
    print(registry.best())

    print("\nLeaderboard:")
    print(registry.leaderboard())