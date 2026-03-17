"""
SAPIANTA CLI — List Development Tasks

Displays tasks tracked in DevTaskRegistry.
"""

from runtime.development.dev_task_registry import DevTaskRegistry


def run():

    registry = DevTaskRegistry()

    active = registry.get_active_tasks()
    completed = registry.get_completed_tasks()
    rejected = registry.get_rejected_tasks()

    print("\nSAPIANTA Development Tasks")
    print("--------------------------")

    print(f"\nACTIVE TASKS ({len(active)})")
    if not active:
        print("- none")
    else:
        for t in active:
            print(f"- {t}")

    print(f"\nCOMPLETED TASKS ({len(completed)})")
    if not completed:
        print("- none")
    else:
        for t in completed:
            print(f"- {t}")

    print(f"\nREJECTED TASKS ({len(rejected)})")
    if not rejected:
        print("- none")
    else:
        for t in rejected:
            print(f"- {t}")