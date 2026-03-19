"""
SAPIANTA Fix Memory

Stores mapping between error signatures and successful fix strategies.

Design:
- deterministic
- lightweight
- no external dependencies
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

        with open(self.STORAGE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=2)

    # ------------------------------------------------
    # CORE LOGIC
    # ------------------------------------------------

    def _signature(self, error_text: str) -> str:
        """
        Create deterministic error signature.
        """

        if not error_text:
            return "unknown_error"

        # simple normalization (v1)
        return error_text.strip().split("\n")[0][:200]

    def record_success(self, error_text: str, strategy: str):
        """
        Store successful fix.
        """

        sig = self._signature(error_text)

        if sig not in self.memory:
            self.memory[sig] = {}

        if strategy not in self.memory[sig]:
            self.memory[sig][strategy] = 0

        self.memory[sig][strategy] += 1

        self._save()

    def get_best_strategy(self, error_text: str) -> Optional[str]:
        """
        Return best known strategy for given error.
        """

        sig = self._signature(error_text)

        if sig not in self.memory:
            return None

        strategies = self.memory[sig]

        # pick most successful
        return max(strategies, key=strategies.get)