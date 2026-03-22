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

# 🔥 NEW: Promotion Gate
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
        """
        Submit new development task with proper duplicate detection.
        """

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
        """
        Execute one development cycle.
        """

        start = time.time()

        tasks = self.registry.get_active_tasks()

        if not tasks:

            execution_time = time.time() - start
            self.metrics.record_cycle("no_tasks", execution_time)

            return {"status": "no_tasks"}

        ordered = self.planner.prioritize(tasks)
        task = ordered[0]

        decision = self.gate.evaluate(task)

        # ---------------------------------------------------------
        # 🔥 PROMOTION GATE ENFORCEMENT (NEW)
        # ---------------------------------------------------------

        # trenutno minimal heuristic (SAFE MODE)
        affected_files = ["runtime/development/"]

        level = classify_change(affected_files)
        needs_approval = requires_approval(level)

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
        # EXISTING GOVERNANCE GATE
        # ---------------------------------------------------------

        if decision == DevGovernanceGate.BLOCK:

            self.registry.reject_task(task)
            self.memory.record_blocked(task)

            execution_time = time.time() - start
            self.metrics.record_cycle("blocked", execution_time, task=task)

            return {"status": "blocked", "task": task}

        if decision == DevGovernanceGate.REVIEW:

            execution_time = time.time() - start
            self.metrics.record_cycle("review", execution_time, task=task)

            return {"status": "needs_review", "task": task}

        # ---------------------------------------------------------
        # REAL EXECUTION VIA ORCHESTRATOR
        # ---------------------------------------------------------

        from runtime.development.dev_orchestrator import DevelopmentOrchestrator

        orchestrator = DevelopmentOrchestrator()

        try:
            result = orchestrator.run_auto(task.get("goal", ""))

            # 🔥 NORMALIZATION LAYER

            if result is False:
                success = False
                reason = "orchestrator_failed"

            elif isinstance(result, dict):
                success = result.get("success", False)

                # 🔥 EMPTY GENERATION → REVIEW
                if not success and result.get("reason") == "no_valid_files":
                    success = None

                reason = result.get("reason")

            else:
                success = bool(result)
                reason = None

        except Exception as e:
            print("[LOOP] Orchestrator execution failed:", str(e))
            success = False
            reason = str(e)

        # ---------------------------------------------------------
        # AUTO REPAIR HOOK
        # ---------------------------------------------------------

        try:
            if success is False:
                print("[AUTO-REPAIR] Triggering repair...")
                from runtime.development.repair_orchestrator import main as repair_main
                repair_main()
        except Exception as e:
            print("[AUTO-REPAIR] Error:", str(e))

        # ---------------------------------------------------------
        # RESULT HANDLING
        # ---------------------------------------------------------

        if success is True:

            self.registry.complete_task(task)
            self.memory.record_completed(task)

            execution_time = time.time() - start
            self.metrics.record_cycle("completed", execution_time, task=task)

            return {
                "status": "completed",
                "task": task
            }

        # 🔥 EMPTY CASE → REVIEW

        if success is None:

            execution_time = time.time() - start
            self.metrics.record_cycle("needs_review", execution_time, task=task)

            return {
                "status": "needs_review",
                "task": task,
                "reason": "no_valid_files_generated"
            }

        # FAILED PATH

        self.registry.reject_task(task)
        self.memory.record_failed(task)

        execution_time = time.time() - start
        self.metrics.record_cycle("failed", execution_time, task=task)

        return {
            "status": "failed",
            "task": task,
            "error": reason or "orchestrator_failed"
        }