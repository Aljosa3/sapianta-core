import json
from pathlib import Path


REGISTRY_FILE = Path("runtime/development/task_registry.json")


def run():

    print("\nSAPIANTA Development History")
    print("----------------------------")

    if not REGISTRY_FILE.exists():
        print("No development history available.")
        return

    with open(REGISTRY_FILE) as f:
        data = json.load(f)

    tasks = (
        data.get("completed_tasks", [])
        + data.get("rejected_tasks", [])
        + data.get("active_tasks", [])
    )

    if not tasks:
        print("No tasks recorded.")
        return

    for task in tasks:

        idea = task.get("idea", "unknown")
        source = task.get("source", "unknown")
        task_type = task.get("task_type", "unknown")

        print()
        print(f"Task: {idea}")
        print(f"Type: {task_type}")
        print(f"Source: {source}")