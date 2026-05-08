"""
SAPIANTA Autonomous Development Loop

Connects discuss → planning → governance → sandbox
into a controlled autonomous development cycle.
"""

import time
import os

# DEV MODE FLAG (default: OFF)
DEV_MODE = os.getenv("SAPIANTA_DEV_MODE", "0") == "1"
FAST_TEST = os.getenv("SAPIANTA_FAST_TEST", "0") == "1"

# SAFE AUTONOMOUS MODE CONFIG
MAX_CYCLES = int(os.getenv("SAPIANTA_MAX_CYCLES", "10"))
MAX_RUNTIME = int(os.getenv("SAPIANTA_MAX_RUNTIME", "60"))  # seconds
SLEEP_INTERVAL = float(os.getenv("SAPIANTA_SLEEP", "0.5"))

from runtime.development.dev_task_registry import DevTaskRegistry
from runtime.development.dev_task_registry_hash_index import DevTaskRegistryHashIndex
from runtime.development.dev_task_planner import DevTaskPlanner
from runtime.development.dev_governance_gate import DevGovernanceGate
from runtime.development.dev_sandbox_runner import DevSandboxRunner
from runtime.development.dev_memory import DevMemory
from runtime.development.dev_metrics import DevMetrics
from runtime.development.dev_orchestrator import DevelopmentOrchestrator

# --- CAL INTEGRATION START ---
from runtime.development.cal_controller import CALController
# --- CAL INTEGRATION END ---

from runtime.governance.promotion_gate import classify_change, requires_approval

# --- CAL SCORE UPDATE HELPER (NEW) ---
def _update_score(score: float, delta: float) -> float:
    score += delta
    return max(-1.0, min(1.0, score))
# --- CAL SCORE UPDATE HELPER END ---


class DevAutonomousLoop:
    """
    Executes the autonomous development pipeline.
    """

    def __init__(self, reset: bool = True):

        try:
            self.registry = DevTaskRegistry()
            self.hash_index = DevTaskRegistryHashIndex()

            if reset:
                if hasattr(self.registry, "clear"):
                    self.registry.clear()

                if hasattr(self.hash_index, "clear"):
                    self.hash_index.clear()

        except Exception:
            self.registry = DevTaskRegistry()
            self.hash_index = DevTaskRegistryHashIndex()

        self.planner = DevTaskPlanner()
        self.gate = DevGovernanceGate()
        self.sandbox = DevSandboxRunner()
        self.memory = DevMemory()
        self.metrics = DevMetrics()

        # --- CAL INTEGRATION START ---
        self.cal = CALController(registry=self.registry)
        # --- CAL INTEGRATION END ---

        self._cycle_count = 0
        self._start_time = None
        self._last_system_stable = False

    def _sleep_if_dev(self):
        if DEV_MODE:
            time.sleep(SLEEP_INTERVAL)

    def submit_task(self, task: dict) -> str:

        existing_tasks = self.registry.get_active_tasks()

        for t in existing_tasks:
            if t == task:
                return "duplicate"

        try:
            if hasattr(self.hash_index, "add_task"):
                self.hash_index.add_task(task)
        except Exception:
            pass

        before = len(existing_tasks)

        self.registry.add_task(task)

        after = len(self.registry.get_active_tasks())

        if after == before:
            return "duplicate"

        return "registered"

    def run_once(self):

        start = time.time()

        # --- CAL CYCLE START ---
        in_pytest = "PYTEST_CURRENT_TEST" in os.environ

        cal_task = None

        if not in_pytest:
            try:
                cal_context = {"system_stable": self._last_system_stable}
                cal_task = self.cal.run_cycle(context=cal_context)

                # --- CAL → REGISTRY INTEGRATION (SAFE, DETERMINISTIC) ---
                if cal_task and isinstance(cal_task, dict):

                    existing_tasks = self.registry.get_active_tasks()

                    is_duplicate = any(t == cal_task for t in existing_tasks)

                    if not is_duplicate:
                        try:
                            if hasattr(self.hash_index, "add_task"):
                                self.hash_index.add_task(cal_task)
                        except Exception:
                            pass

                        self.registry.add_task(cal_task)
                # --- END CAL INTEGRATION ---

            except Exception as e:
                print("[CAL] ERROR:", str(e))
                
        # --- CAL CYCLE END ---

        # =====================================================
        # 🛑 GLOBAL QUIESCENCE (PLAN + EXECUTION GUARD)
        # =====================================================
        if self._last_system_stable:
            print("[GLOBAL QUIESCENCE] system stable → skipping planning + execution")

            execution_time = time.time() - start
            self.metrics.record_cycle("stable", execution_time)

            return {
                "status": "stable",
                "system_stable": True
            }
        # =====================================================

        if self._start_time is None:
            self._start_time = start

        self._cycle_count += 1

        if DEV_MODE and self._cycle_count > MAX_CYCLES:
            print(f"[SAFE_MODE] STOP → max cycles reached ({MAX_CYCLES})")
            return {"status": "stopped_max_cycles"}

        elapsed = start - self._start_time
        if DEV_MODE and elapsed > MAX_RUNTIME:
            print(f"[SAFE_MODE] STOP → max runtime exceeded ({MAX_RUNTIME}s)")
            return {"status": "stopped_timeout"}

        # ---------------------------------------------------------
        # WAITING APPROVAL HANDLING
        # ---------------------------------------------------------

        waiting_tasks = [
            t for t in self.registry.get_tasks_by_state("waiting_approval")
            if not t.get("approved")
        ]

        if waiting_tasks:

            print("[DEV_LOOP] STOP — waiting for approval")

            execution_time = time.time() - start
            self.metrics.record_cycle("waiting_for_approval", execution_time)

            return {
                "status": "waiting_for_approval",
                "tasks": waiting_tasks,
                "system_stable": self._last_system_stable
            }

        # ---------------------------------------------------------
        # PRIORITY-AWARE TASK SELECTION (FIXED)
        # ---------------------------------------------------------

        task = self.registry.pop_next_task()

        # 🔥 FALLBACK: approved tasks (CRITICAL FIX)
        if not task:
            approved_tasks = self.registry.get_tasks_by_state("approved")

            if approved_tasks:
                task = approved_tasks[0]  # deterministic fallback
            else:

                # ---------------------------------------------------------
                # CAL FOLLOW-UP TASK GENERATION (SAFE MINIMAL)
                # ---------------------------------------------------------
                try:
                    if hasattr(self, "cal") and self.cal:
                        new_task = self.cal.generate_followup_task()

                        if new_task:
                            print(f"[CAL] LOOP GENERATED TASK: {new_task['description']}")
                            self.registry.add_task(new_task)
                            return {"status": "generated", "task": new_task, "system_stable": self._last_system_stable}
                except Exception:
                    pass
                # ---------------------------------------------------------

                execution_time = time.time() - start
                self.metrics.record_cycle("no_tasks", execution_time)
                return {"status": "no_tasks", "system_stable": self._last_system_stable}

        # ---------------------------------------------------------
        # OPTIONAL: deterministic exploration (SAFE)
        # ---------------------------------------------------------
        if self._cycle_count % 3 == 0:
            alt_tasks = [
                t for t in self.registry.get_active_tasks()
                if t.get("state") == "queued"
            ]
            if alt_tasks:
                task = alt_tasks[-1]  # exploration fallback
        # ---------------------------------------------------------

        decision = self.gate.final_decision(
            self.gate.evaluate(task)
        )

        # ---------------------------------------------------------
        # PROMOTION GATE
        # ---------------------------------------------------------

        affected_files = ["runtime/development/"]
        level = classify_change(affected_files)

        if level == "COSMETIC":
            needs_approval = False
        else:
            needs_approval = False if task.get("approved") else requires_approval(level)

        print(f"[GATE] Level: {level} | Approval required: {needs_approval}")

        if needs_approval:
            self.memory.record_blocked(task)

            execution_time = time.time() - start
            self.metrics.record_cycle("needs_review", execution_time, task=task)

            self._sleep_if_dev()
            return {
                "status": "needs_review",
                "task": task,
                "reason": f"approval_required_{level}",
                "system_stable": self._last_system_stable
            }

        # ---------------------------------------------------------
        # GOVERNANCE
        # ---------------------------------------------------------

        if decision == DevGovernanceGate.BLOCK:
            self.registry.reject_task(task)
            self.memory.record_blocked(task)

            return {"status": "blocked", "task": task, "system_stable": self._last_system_stable}

        if decision == DevGovernanceGate.REVIEW:
            print("[DEV_LOOP] REVIEW decision (non-DEV mode)")

            execution_time = time.time() - start
            self.metrics.record_cycle("needs_review", execution_time, task=task)

            self._sleep_if_dev()
            return {"status": "needs_review", "task": task, "system_stable": self._last_system_stable}

        # --- EXECUTION FREQUENCY SCALING (deterministic) ---
        metadata = task.get("metadata", {})
        score = metadata.get("score", 0)

        K = 2  # conservative amplification

        effective_score = max(score, 0)
        runs = int(1 + effective_score * K)

        # safety cap (prevent runaway loops)
        runs = min(runs, 3)
        # --- END EXECUTION FREQUENCY SCALING ---

        # ---------------------------------------------------------
        # EXECUTION
        # ---------------------------------------------------------

        orchestrator = DevelopmentOrchestrator()

        print(f"[DEBUG] EXECUTING TASK → {task}")

        try:
            # 🔥 FORCE REAL EXECUTION (CCS TEST MODE)
            if task.get("approved"):
                print("[DEV_LOOP] Resuming approved task...")

            print("[DEBUG] CALLING run_auto()")
            result = None
            for _ in range(runs):
                result = orchestrator.run_auto(task)
                if isinstance(result, dict) and result.get("status") == "failed":
                    break

            # 🔥 GLOBAL STABILITY PROPAGATION (CRITICAL FIX)
            if isinstance(result, dict) and result.get("system_stable"):
                self._last_system_stable = True

            # requeue task if it had multiple execution attempts
            if runs > 1 and isinstance(result, dict) and result.get("status") != "completed":
                self.registry.submit_task(task)

            print(f"[DEBUG] run_auto RESULT → {result}")

            if isinstance(result, dict) and result.get("status") == "waiting_for_approval":

                if task.get("approved"):
                    success = False
                    reason = "approval_already_granted"

                else:
                    success = False
                    reason = "approval_required"

            elif result is False:
                success = False
                reason = "orchestrator_failed"

            elif isinstance(result, dict):
                success = bool(result.get("success"))
                reason = None if success else (result.get("reason") or "incomplete_execution")

                if "repair_iterations" in result:
                    self.metrics.record_repair_iterations(result["repair_iterations"])

                self._last_system_stable = bool(result.get("system_stable", False))

            else:
                success = False
                reason = "invalid_result_type"

        except Exception as e:
            print("[LOOP] Orchestrator execution failed:", str(e))
            success = False
            reason = str(e)
            self._last_system_stable = False

        # ---------------------------------------------------------
        # RESULT HANDLING
        # ---------------------------------------------------------

        if success is True:

            # =====================================================
            # 🧠 CAL FEEDBACK (SUCCESS)
            # =====================================================
            try:
                if hasattr(self, "cal") and self.cal:
                    self.cal.reward(task)
            except Exception as e:
                print("[CAL] reward error:", str(e))
            # =====================================================

            if task.get("metadata"):
                score = _update_score(task["metadata"].get("score", 0), -0.1)
                # apply score decay (temporal adaptation)
                score = round(score * 0.98, 4)
                task["metadata"]["score"] = score

            self.registry.complete_task(task)
            self.memory.record_completed(task)

            # --- SCORE-AWARE GENERATION (CAL minimal deterministic) ---
            metadata = task.get("metadata", {})
            score = metadata.get("score", 0)

            # HIGH SCORE → AMPLIFY (generate similar task)
            idea = task.get("idea", "")

            # prevent recursive amplification
            if "extend:" in idea:
                pass

            elif score > 0.5:
                new_task = {
                    "task_type": task.get("task_type"),
                    "idea": f"extend: {idea}",
                    "source": "cal_amplify",
                    "metadata": {"parent_score": score}
                }
                self.registry.submit_task(new_task)

            # LOW SCORE → FIX TASK
            elif score < -0.5:
                new_task = {
                    "task_type": "fix",
                    "idea": f"improve: {task.get('idea')}",
                    "source": "cal_repair",
                    "metadata": {"parent_score": score}
                }
                self.registry.submit_task(new_task)

            # --- END SCORE-AWARE GENERATION ---

            self._sleep_if_dev()
            return {
                "status": "completed",
                "task": task,
                "system_stable": self._last_system_stable
            }

        task["retry_count"] = task.get("retry_count", 0) + 1

        current_error = reason

        if current_error is None:
            self._last_error = None
            self._stagnation = 0
        else:
            if getattr(self, "_last_error", None) == current_error:
                self._stagnation = getattr(self, "_stagnation", 0) + 1
            else:
                self._stagnation = 0

            self._last_error = current_error

        print(f"[DEV_LOOP] RETRY ({task['retry_count']})")

        if task["retry_count"] < 1:
            self.registry.update_task_state(task, "queued")

            self._sleep_if_dev()

            if reason == "incomplete_execution":
                status = "needs_review"
            else:
                status = "retrying"

            return {
                "status": status,
                "task": task,
                "reason": reason or "execution_failed",
                "system_stable": self._last_system_stable
            }

        if getattr(self, "_stagnation", 0) > 2:
            return {
                "status": "needs_review",
                "task": task,
                "reason": "stagnation_detected",
                "system_stable": self._last_system_stable
            }

        if task.get("metadata"):
            score = _update_score(task["metadata"].get("score", 0), -0.1)
            # apply score decay (temporal adaptation)
            score = round(score * 0.98, 4)
            task["metadata"]["score"] = score

        # =====================================================
        # 🧠 CAL FEEDBACK (FAILURE)
        # =====================================================
        try:
            if hasattr(self, "cal") and self.cal and hasattr(self.cal, "penalize"):
                self.cal.penalize(task)
        except Exception as e:
            print("[CAL] penalize error:", str(e))
        # =====================================================

        self.registry.reject_task(task)
        self.memory.record_failed(task)

        self._sleep_if_dev()
        return {
            "status": "failed",
            "task": task,
            "error": reason or "orchestrator_failed",
            "system_stable": self._last_system_stable
        }
