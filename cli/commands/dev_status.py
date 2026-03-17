"""
SAPIANTA Development Status Command

Displays current state of the autonomous development system.
"""

from runtime.development.dev_task_registry import DevTaskRegistry


def run():

    registry = DevTaskRegistry()

    active = registry.get_active_tasks()
    completed = registry.get_completed_tasks()
    rejected = registry.get_rejected_tasks()

    print()
    print("SAPIANTA Development Status")
    print("---------------------------")

    print(f"Active tasks: {len(active)}")
    print(f"Completed tasks: {len(completed)}")
    print(f"Rejected tasks: {len(rejected)}")

    print()

    if active:
        print("Active Task Preview:")
        for task in active[:3]:
            print("-", task)

    print()