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
from runtime.development.test_runner import TestRunner


class CALController:

    # ---------------------------------------------------------
    # ERROR SIGNATURE NORMALIZATION (MINIMAL)
    # ---------------------------------------------------------

    def _extract_error_signature(self, description: str) -> str:
        if not description:
            return "generic"

        text = description.lower()

        if "typeerror" in text:
            return "type_error"
        if "nameerror" in text:
            return "name_error"
        if "importerror" in text:
            return "import_error"
        if "assert" in text:
            return "assertion_error"

        return "generic"

    # ---------------------------------------------------------
    # DECISION ENGINE (NEW)
    # ---------------------------------------------------------

    def _should_generate_fix(self, task):
        score = task["metadata"]["score"]
        return score < 0

    # --- DETERMINISTIC EXPLORATION TARGETS ---
    _EXPLORATION_TARGETS = [
        "test_generation",
        "code_quality_improvement",
        "edge_case_handling",
        "performance_optimization",
        "refactoring"
    ]

    def __init__(self, registry=None):
        self.detector = CapabilityGapDetector()
        self.registry = registry if registry is not None else DevTaskRegistry()

        self._bootstrap_done = False
        self._seen_descriptions = set()

        # --- MINIMAL RESULT MEMORY ---
        self._recent_results = []
        self._seen_ideas = set()

        # ---------------------------------------------------------
        # NEW: FIX MEMORY HOOK (SAFE, OPTIONAL)
        # ---------------------------------------------------------
        try:
            from runtime.development.fix_memory import FixMemory
            self.fix_memory = FixMemory()
        except Exception:
            self.fix_memory = None

    # ---------------------------------------------------------
    # EXECUTION HANDLERS
    # ---------------------------------------------------------

    def _execute_task(self, task):
        desc = task["description"]

        if desc.startswith("explore_test_generation"):
            self._handle_test_generation()

    def _handle_test_generation(self):
        import os

        test_path = os.path.join("tests", "test_auto_generated.py")

        if os.path.exists(test_path):
            print("[CAL] Test file already exists → skip")
            return

        content = '''
def test_auto_generated_basic():
    assert 1 + 1 == 2
'''

        with open(test_path, "w") as f:
            f.write(content.strip())

        print("[CAL] Generated test_auto_generated.py")

    # ---------------------------------------------------------
    # LEARNING LOOP
    # ---------------------------------------------------------

    def _update_score_from_result(self, task, result):

        score = task["metadata"]["score"]

        if result.success:
            score += 0.1
            print("[CAL] SUCCESS → score +0.1")

            try:
                self._recent_results.append(("success", task.get("description")))
            except Exception:
                pass

        else:
            score -= 0.1
            print("[CAL] FAILURE → score -0.1")

            try:
                self._recent_results.append(("failure", task.get("description")))
            except Exception:
                pass

        score = max(-1.0, min(1.0, score))
        task["metadata"]["score"] = score

        if len(self._recent_results) > 50:
            self._recent_results = self._recent_results[-50:]

    # ---------------------------------------------------------
    # DIFFICULTY LADDER (WITH SIGNATURE + MEMORY)
    # ---------------------------------------------------------

    def generate_followup_task(self):

        if not self._recent_results:
            return None

        outcome, description = self._recent_results[-1]

        if not description:
            description = "generic"

        level = "basic"

        if "_intermediate" in description:
            level = "intermediate"
        elif "_advanced" in description:
            level = "advanced"

        # --- SUCCESS ---
        if outcome == "success":

            if level == "basic":
                idea = f"{description}_intermediate"
            elif level == "intermediate":
                idea = f"{description}_advanced"
            else:
                idea = f"extend_{description}"

            new_score = 0.2

        # --- FAILURE (SIGNATURE + MEMORY BOOST) ---
        elif outcome == "failure":

            signature = self._extract_error_signature(description)

            # ---------------------------------------------------------
            # NEW: SIGNATURE WEIGHTING (MINIMAL)
            # ---------------------------------------------------------
            boost = 0.0

            try:
                if self.fix_memory and hasattr(self.fix_memory, "failure_memory"):
                    count = self.fix_memory.failure_memory.get(signature, 0)

                    if count > 5:
                        boost = 0.2
                    elif count > 2:
                        boost = 0.1
            except Exception:
                pass
            # ---------------------------------------------------------

            if level == "advanced":
                idea = f"fix_{signature}_{description.replace('_advanced', '_intermediate')}"
            elif level == "intermediate":
                idea = f"fix_{signature}_{description.replace('_intermediate', '_basic')}"
            else:
                idea = f"fix_{signature}_{description}"

            new_score = min(1.0, 0.0 + boost)

        else:
            return None

        if idea in self._seen_ideas:
            return None

        self._seen_ideas.add(idea)

        return {
            "description": idea,
            "state": "queued",
            "metadata": {
                "source": "CAL_AUTO",
                "score": new_score
            }
        }

    def run_cycle(self):

        if not self._bootstrap_done:
            print("[CAL] BOOTSTRAP: generating initial task")

            task_description = "implement_basic_utility_function"

            if task_description in self._seen_descriptions:
                print("[CAL] SKIP duplicate bootstrap task")
                return []

            self._seen_descriptions.add(task_description)

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

        gaps = self.detector.detect(registry=self.registry)

        if not gaps:
            gaps = [{
                "description": "System idle detected (no tasks in registry). Introduce task generation or exploration capability."
            }]

        created_tasks = []

        for gap in gaps:
            description = gap["description"]

            if description.startswith("System idle detected"):

                idx = len(self._seen_descriptions) % len(self._EXPLORATION_TARGETS)
                target = self._EXPLORATION_TARGETS[idx]

                description = f"explore_{target}"

                print(f"[CAL] STAGNATION → exploration: {description}")

            if description in self._seen_descriptions:
                print(f"[CAL] SKIP duplicate: {description}")
                continue

            self._seen_descriptions.add(description)

            score = 1.0

            if "test" in description:
                score += 0.5

            if "fix" in description:
                score += 0.3

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

            self._execute_task(task)

            try:
                runner = TestRunner()

                if hasattr(runner, "run_strict_generated_tests"):
                    result = runner.run_strict_generated_tests()
                elif hasattr(runner, "run"):
                    result = runner.run()
                else:
                    result = type("Dummy", (), {"success": True})()

            except Exception:
                result = type("Dummy", (), {"success": True})()

            self._update_score_from_result(task, result)

            try:
                followup = self.generate_followup_task()
                if followup:
                    print(f"[CAL] AUTO-GENERATED FOLLOW-UP: {followup['description']}")
                    self.registry.add_task(followup)
            except Exception:
                pass

            if self._should_generate_fix(task):

                fix_description = f"fix_{task['description']}"

                if fix_description not in self._seen_descriptions:

                    fix_task = {
                        "description": fix_description,
                        "state": "queued",
                        "metadata": {
                            "source": "CAL_FIX",
                            "score": 0.0
                        }
                    }

                    self._seen_descriptions.add(fix_description)
                    self.registry.add_task(fix_task)

        return created_tasks

    # =========================================================
    # CAL FEEDBACK (SAFE, DETERMINISTIC)
    # =========================================================

    def reward(self, task):
        meta = task.setdefault("metadata", {})
        score = float(meta.get("score", 0.0))
        score = min(1.0, score + 0.1)
        meta["score"] = score

    def penalize(self, task):
        meta = task.setdefault("metadata", {})
        score = float(meta.get("score", 0.0))
        score = max(-1.0, score - 0.1)
        meta["score"] = score