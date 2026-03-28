"""
SAPIANTA Fix Memory

Stores mapping between error signatures and successful fix strategies.

Design:
- deterministic
- lightweight
- persistent (JSON-based)
- append-only learning
"""

import json
from pathlib import Path
from typing import Optional, Dict


class FixMemory:

    STORAGE_PATH = Path("runtime/development/fix_memory_store.json")

    def __init__(self):
        self.memory = self._load()

    # ------------------------------------------------
    # LOAD / SAVE
    # ------------------------------------------------

    def _load(self) -> Dict:

        if not self.STORAGE_PATH.exists():
            return {}

        try:
            with open(self.STORAGE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _save(self):

        self.STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(self.STORAGE_PATH, "w", encoding="utf-8") as f:
                json.dump(self.memory, f, indent=2)
        except Exception:
            pass  # never break runtime

    # ------------------------------------------------
    # CORE LOGIC
    # ------------------------------------------------

    def _signature(self, error_text: str) -> str:
        """
        Create deterministic error signature (normalized).
        """

        if not error_text:
            return "unknown_error"

        # 🔥 improved normalization
        return error_text.strip().split("\n")[0][:120]

    # ------------------------------------------------
    # LEARNING
    # ------------------------------------------------

    def record_success(self, error_text: str, strategy: str):
        """
        Store successful fix (increment counter).
        """

        if not strategy:
            return

        sig = self._signature(error_text)

        if sig not in self.memory:
            self.memory[sig] = {}

        self.memory[sig][strategy] = self.memory[sig].get(strategy, 0) + 1

        self._save()

    # ------------------------------------------------
    # RETRIEVAL
    # ------------------------------------------------

    def get_best_strategy(self, error_text: str) -> Optional[str]:
        """
        Return best known strategy for given error.
        """

        sig = self._signature(error_text)

        if sig not in self.memory:
            return None

        strategies = self.memory[sig]

        if not strategies:
            return None

        # 🔥 deterministic best pick
        return max(strategies, key=strategies.get)

    def get_strategy_score(self, error_text: str, strategy: str) -> int:
        """
        Return how often a strategy succeeded for this error.
        (used later for weighted ranking)
        """

        sig = self._signature(error_text)

        if sig not in self.memory:
            return 0

        return self.memory[sig].get(strategy, 0)