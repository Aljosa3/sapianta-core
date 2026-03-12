"""
SAPIANTA Strategy Memory

Stores tested strategies and their performance.
Prevents repeating weak strategies.
"""

import json
import os
from datetime import datetime


MEMORY_PATH = "runtime/memory/strategy_memory.json"


class StrategyMemory:

    def __init__(self):

        if not os.path.exists(MEMORY_PATH):
            with open(MEMORY_PATH, "w") as f:
                json.dump([], f)

    # ------------------------------------------------
    # LOAD MEMORY
    # ------------------------------------------------

    def load(self):

        with open(MEMORY_PATH, "r") as f:
            return json.load(f)

    # ------------------------------------------------
    # SAVE MEMORY
    # ------------------------------------------------

    def save(self, memory):

        with open(MEMORY_PATH, "w") as f:
            json.dump(memory, f, indent=2)

    # ------------------------------------------------
    # REGISTER STRATEGY
    # ------------------------------------------------

    def register(self, strategy, evaluation):

        memory = self.load()

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "strategy": strategy,
            "evaluation": evaluation
        }

        memory.append(entry)

        self.save(memory)

    # ------------------------------------------------
    # CHECK IF STRATEGY EXISTS
    # ------------------------------------------------

    def exists(self, strategy):

        memory = self.load()

        for entry in memory:

            if entry["strategy"] == strategy:
                return True

        return False
