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

        # hitro preverjanje (hash index)
        if self.hash_index.has_task(task):
            return "duplicate"

        self.hash_index.add_task(task)

        # robustno preverjanje (registry stanje)
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

        if decision == DevGovernanceGate.BLOCK:

            self.registry.reject_task(task)
            self.memory.record_blocked(task)

            execution_time = time.time() - start
            self.metrics.record_cycle("blocked", execution_time)

            return {
                "status": "blocked",
                "task": task
            }

        if decision == DevGovernanceGate.REVIEW:

            execution_time = time.time() - start
            self.metrics.record_cycle("review", execution_time)

            return {
                "status": "needs_review",
                "task": task
            }

        # simulate development code

        code = """
print("development sandbox test")
"""

        result = self.sandbox.run_code(code)

        # --- AUTO REPAIR HOOK ---
        try:
            failed = False

            if isinstance(result, dict):
                failed = result.get("status") == "failed"
            elif result is False:
                failed = True

            if failed:
                print("[AUTO-REPAIR] Triggering repair...")
                from runtime.development.repair_orchestrator import main as repair_main
                repair_main()

        except Exception as e:
            print("[AUTO-REPAIR] Error:", str(e))

        if result["status"] == "success":

            self.registry.complete_task(task)
            self.memory.record_completed(task)

            execution_time = time.time() - start
            self.metrics.record_cycle("completed", execution_time)

            return {
                "status": "completed",
                "task": task
            }

        self.memory.record_failed(task)

        execution_time = time.time() - start
        self.metrics.record_cycle("failed", execution_time)

        return {
            "status": "failed",
            "task": task,
            "error": result
        }