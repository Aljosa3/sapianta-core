"""
CALController — Minimal Continuous Autonomous Learning layer

Purpose:
- observes system state
- detects capability gaps
- generates new development tasks

NO LLM
NO NON-DETERMINISM
"""

from runtime.development.capability_gap_detector import CapabilityGapDetector
from runtime.development.dev_task_registry import DevTaskRegistry


class CALController:
    def __init__(self, registry=None):
        self.detector = CapabilityGapDetector()
        self.registry = registry if registry is not None else DevTaskRegistry()

        # --- CAL BOOTSTRAP FLAG ---
        self._bootstrap_done = False

        # --- CAL FILTERING STATE ---
        self._seen_descriptions = set()

    def run_cycle(self):
        """
        Single CAL cycle:
        - detect gaps
        - register new tasks
        """

        gaps = self.detector.detect()

        # --- CAL BOOTSTRAP START ---
        if not gaps:

            if not self._bootstrap_done:
                print("[CAL] BOOTSTRAP: generating initial task")

                task_description = "implement_basic_utility_function"

                if task_description in self._seen_descriptions:
                    print("[CAL] SKIP duplicate bootstrap task")
                    return []

                self._seen_descriptions.add(task_description)

                # --- CLAMPED SCORE (NEW) ---
                score = max(-1.0, min(1.0, 0.1))

                task = {
                    "description": task_description,
                    "state": "queued",
                    "metadata": {
                        "source": "CAL_BOOTSTRAP",
                        "priority": "low",
                        "score": score
                    }
                }

                self.registry.add_task(task)

                self._bootstrap_done = True
                return [task]

            print("[CAL] No capability gaps detected")
            return []
        # --- CAL BOOTSTRAP END ---

        created_tasks = []

        for gap in gaps:
            description = gap["description"]

            # --- DEDUPLICATION ---
            if description in self._seen_descriptions:
                print(f"[CAL] SKIP duplicate: {description}")
                continue

            self._seen_descriptions.add(description)

            # --- BASIC SCORING ---
            score = 1.0

            if "test" in description:
                score += 0.5

            if "fix" in description:
                score += 0.3

            # --- CLAMP (NEW) ---
            score = max(-1.0, min(1.0, score))

            task = {
                "description": description,
                "state": "queued",
                "metadata": {
                    "source": "CAL",
                    "score": score
                }
            }

            self.registry.add_task(task)
            created_tasks.append(task)

            print(f"[CAL] Created task: {task}")

        return created_tasks