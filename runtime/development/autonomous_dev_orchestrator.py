"""
SAPIANTA Autonomous Development Orchestrator

Coordinates autonomous system improvement cycles.

Pipeline:

SystemReflectionEngine
        ↓
ImprovementPlanner
        ↓
Development Task Queue
"""

from runtime.system.improvement_planner import ImprovementPlanner


class AutonomousDevOrchestrator:

    def __init__(self, repo_path="."):

        self.repo_path = repo_path
        self.planner = ImprovementPlanner(repo_path)

    # ---------------------------------------------------------
    # DEVELOPMENT CYCLE
    # ---------------------------------------------------------

    def run_cycle(self):

        print("\nSAPIANTA Autonomous Development Cycle")
        print("-------------------------------------")

        tasks = self.planner.generate_tasks()

        if not tasks:
            print("\nSystem healthy — no development tasks generated.")
            return []

        print("\nGenerated Development Tasks:\n")

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        return tasks

    # ---------------------------------------------------------
    # TASK EXPORT
    # ---------------------------------------------------------

    def export_tasks(self):

        tasks = self.planner.generate_tasks()

        task_objects = []

        for i, task in enumerate(tasks, 1):

            task_objects.append({
                "task_id": f"TASK-{i:03}",
                "description": task,
                "status": "pending"
            })

        return task_objects