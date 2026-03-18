import json
from pathlib import Path


REGISTRY_FILE = Path("runtime/development/task_registry.json")
METRICS_FILE = Path("runtime/development/dev_metrics.json")


def run():

    print("\nSAPIANTA Development Reconcile")
    print("------------------------------")

    if not REGISTRY_FILE.exists():
        print("Task registry not found.")
        return

    with open(REGISTRY_FILE) as f:
        registry = json.load(f)

    completed_tasks = registry.get("completed_tasks", [])
    rejected_tasks = registry.get("rejected_tasks", [])
    active_tasks = registry.get("active_tasks", [])

    metrics = {
        "tasks_processed": len(completed_tasks) + len(rejected_tasks),
        "completed": len(completed_tasks),
        "failed": len(rejected_tasks),
        "blocked": 0,
    }

    # Save metrics
    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(METRICS_FILE, "w") as f:
        json.dump(metrics, f, indent=2)

    print("\nReconciled Metrics:")
    print(f"Tasks processed: {metrics['tasks_processed']}")
    print(f"Completed: {metrics['completed']}")
    print(f"Failed: {metrics['failed']}")
    print(f"Active tasks: {len(active_tasks)}")

    print("\nMetrics file updated:", METRICS_FILE)