"""
SAPIANTA Autonomous Development Loop

Connects discuss → planning → governance → sandbox
into a controlled autonomous development cycle.
"""

import time

from runtime.development.dev_task_registry import DevTaskRegistry
from runtime.development.dev_task_registry_hash_index import DevTaskRegistryHashIndex
from runtime.development.dev_task_planner import DevTaskPlanner
from runtime.development.dev_governance_gate import DevGovernanceGate
from runtime.development.dev_sandbox_runner import DevSandboxRunner
from runtime.development.dev_memory import DevMemory
from runtime.development.dev_metrics import DevMetrics

from runtime.governance.promotion_gate import classify_change, requires_approval


class DevAutonomousLoop:
    """
    Executes the autonomous development pipeline.
    """

    def __init__(self):
        self.registry = DevTaskRegistry()
        self.hash_index = DevTaskRegistryHashIndex()
        self.planner = DevTaskPlanner()
        self.gate = DevGovernanceGate()
        self.sandbox = DevSandboxRunner()
        self.memory = DevMemory()
        self.metrics = DevMetrics()

    def submit_task(self, task: dict) -> str:

        if self.hash_index.has_task(task):
            return "duplicate"

        self.hash_index.add_task(task)

        before = len(self.registry.get_active_tasks())
        self.registry.add_task(task)
        after = len(self.registry.get_active_tasks())

        if after == before:
            return "duplicate"

        return "registered"

    def run_once(self):

        start = time.time()

        # ---------------------------------------------------------
        # STOP if non-approved waiting tasks exist
        # ---------------------------------------------------------

        waiting_tasks = [
            t for t in self.registry.get_tasks_by_state("waiting_approval")
            if not t.get("approved")
        ]

        if waiting_tasks:
            print("[DEV_LOOP] STOP — waiting for approval (registry-based)")

            execution_time = time.time() - start
            self.metrics.record_cycle("waiting_for_approval", execution_time)

            return {
                "status": "waiting_for_approval",
                "tasks": waiting_tasks
            }

        # ---------------------------------------------------------
        # TASK SELECTION
        # ---------------------------------------------------------

        tasks = self.registry.get_active_tasks()

        approved_tasks = [t for t in tasks if t.get("state") == "approved"]
        queued_tasks = [t for t in tasks if t.get("state") == "queued"]

        tasks = approved_tasks + queued_tasks

        if not tasks:
            execution_time = time.time() - start
            self.metrics.record_cycle("no_tasks", execution_time)
            return {"status": "no_tasks"}

        ordered = self.planner.prioritize(tasks)
        task = ordered[0]

        decision = self.gate.evaluate(task)

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

            return {
                "status": "needs_review",
                "task": task,
                "reason": f"approval_required_{level}"
            }

        # ---------------------------------------------------------
        # GOVERNANCE
        # ---------------------------------------------------------

        if decision == DevGovernanceGate.BLOCK:
            self.registry.reject_task(task)
            self.memory.record_blocked(task)

            return {"status": "blocked", "task": task}

        if decision == DevGovernanceGate.REVIEW:
            return {"status": "needs_review", "task": task}

        # ---------------------------------------------------------
        # EXECUTION
        # ---------------------------------------------------------

        from runtime.development.dev_orchestrator import DevelopmentOrchestrator

        orchestrator = DevelopmentOrchestrator()

        try:
            if task.get("approved"):
                print("[DEV_LOOP] Resuming approved task...")
            result = orchestrator.run_auto(task)

            # -----------------------------------------------------
            # 🔥 CLEAN APPROVAL HANDLING (FIXED)
            # -----------------------------------------------------

            if isinstance(result, dict) and result.get("status") == "waiting_for_approval":

                if task.get("approved"):
                    print("[DEV_LOOP] Ignoring approval — already approved")
                    success = True
                    reason = None

                else:
                    print("[DEV_LOOP] Waiting for human approval...")

                    self.registry.update_task_state(task, "waiting_approval")
                    self.memory.record_blocked(task)

                    execution_time = time.time() - start
                    self.metrics.record_cycle("waiting_for_approval", execution_time, task=task)

                    return {
                        "status": "waiting_for_approval",
                        "task": task
                    }

            # -----------------------------------------------------
            # NORMALIZATION
            # -----------------------------------------------------

            if result is False:
                success = False
                reason = "orchestrator_failed"

            elif isinstance(result, dict):
                success = result.get("success", False)
                reason = result.get("reason")

            else:
                success = bool(result)
                reason = None

        except Exception as e:
            print("[LOOP] Orchestrator execution failed:", str(e))
            success = False
            reason = str(e)

        # ---------------------------------------------------------
        # RETRY LOOP
        # ---------------------------------------------------------

        if success is True:
            self.registry.complete_task(task)
            self.memory.record_completed(task)

            return {"status": "completed", "task": task}

        task["retry_count"] = task.get("retry_count", 0) + 1

        if task["retry_count"] < 3:
            print(f"[DEV_LOOP] RETRY ({task['retry_count']})")

            self.registry.update_task_state(task, "queued")

            return {
                "status": "retrying",
                "task": task
            }

        self.registry.reject_task(task)
        self.memory.record_failed(task)

        return {
            "status": "failed",
            "task": task,
            "error": reason or "orchestrator_failed"
        }