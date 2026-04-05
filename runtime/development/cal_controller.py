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

                task = {
                    "description": "implement_basic_utility_function",
                    "state": "queued",
                    "metadata": {
                        "source": "CAL_BOOTSTRAP",
                        "priority": "low"
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
            task = {
                "description": gap["description"],
                "state": "queued",
                "metadata": {"source": "CAL"}
            }

            self.registry.add_task(task)
            created_tasks.append(task)

            print(f"[CAL] Created task: {task}")

        return created_tasks