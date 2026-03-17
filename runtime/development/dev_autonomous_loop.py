"""
SAPIANTA Autonomous Development Loop

Connects discuss → planning → governance → sandbox
into a controlled autonomous development cycle.
"""

from runtime.development.dev_task_registry import DevTaskRegistry
from runtime.development.dev_task_registry_hash_index import DevTaskRegistryHashIndex
from runtime.development.dev_task_planner import DevTaskPlanner
from runtime.development.dev_governance_gate import DevGovernanceGate
from runtime.development.dev_sandbox_runner import DevSandboxRunner
from runtime.development.dev_memory import DevMemory


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

    def submit_task(self, task: dict) -> str:
        """
        Submit new development task.
        """

        if self.hash_index.has_task(task):
            return "duplicate"

        self.hash_index.add_task(task)
        self.registry.add_task(task)

        return "registered"

    def run_once(self):
        """
        Execute one development cycle.
        """

        tasks = self.registry.get_active_tasks()

        if not tasks:
            return {"status": "no_tasks"}

        ordered = self.planner.prioritize(tasks)

        task = ordered[0]

        decision = self.gate.evaluate(task)

        if decision == DevGovernanceGate.BLOCK:

            self.registry.reject_task(task)
            self.memory.record_blocked(task)

            return {
                "status": "blocked",
                "task": task
            }

        if decision == DevGovernanceGate.REVIEW:

            return {
                "status": "needs_review",
                "task": task
            }

        # simulate development code

        code = """
print("development sandbox test")
"""

        result = self.sandbox.run_code(code)

        if result["status"] == "success":

            self.registry.complete_task(task)
            self.memory.record_completed(task)

            return {
                "status": "completed",
                "task": task
            }

        self.memory.record_failed(task)

        return {
            "status": "failed",
            "task": task,
            "error": result
        }