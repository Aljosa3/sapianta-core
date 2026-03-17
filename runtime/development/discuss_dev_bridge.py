"""
SAPIANTA Discuss → Development Bridge

Purpose:
Connect discuss mode with the development runtime.

Flow:

discuss idea
    ↓
create development task
    ↓
dev_orchestrator.run_task()
"""


class DiscussDevBridge:
    """
    Bridge between sapianta discuss and development runtime.
    """

    def create_dev_task(self, idea: str) -> dict:
        """
        Convert discuss idea into development task.
        """

        task = {
            "task_type": "implementation",
            "idea": idea,
            "source": "sapianta_discuss",
        }

        return task

    def run_from_discuss(self, idea: str):
        """
        Entry point used by discuss CLI.
        """

        # Lazy import prevents pytest import errors during test collection
        from runtime.development.dev_orchestrator import DevOrchestrator

        orchestrator = DevOrchestrator()

        task = self.create_dev_task(idea)

        result = orchestrator.run_task(task)

        return result