import json
from pathlib import Path


METRICS_FILE = Path("runtime/development/dev_metrics.json")
REGISTRY_FILE = Path("runtime/development/task_registry.json")


def run():

    print("\nSAPIANTA Development Learning")
    print("-----------------------------")

    # --- Load metrics ---
    if METRICS_FILE.exists():
        with open(METRICS_FILE) as f:
            metrics = json.load(f)
    else:
        metrics = {}

    tasks_processed = metrics.get("tasks_processed", 0)
    completed = metrics.get("completed", 0)
    failed = metrics.get("failed", 0)
    blocked = metrics.get("blocked", 0)

    print("\nMETRICS")
    print(f"Tasks processed: {tasks_processed}")
    print(f"Completed: {completed}")
    print(f"Failed: {failed}")
    print(f"Blocked: {blocked}")

    if tasks_processed:
        success_rate = completed / tasks_processed * 100
        print(f"Success rate: {success_rate:.2f}%")
    else:
        success_rate = 0
        print("Success rate: n/a")

    # --- Load history ---
    print("\nHISTORY ANALYSIS")

    if not REGISTRY_FILE.exists():
        print("No development history available.")
        return

    with open(REGISTRY_FILE) as f:
        data = json.load(f)

    completed_tasks = data.get("completed_tasks", [])
    rejected_tasks = data.get("rejected_tasks", [])

    sources = {}

    for task in completed_tasks:
        src = task.get("source", "unknown")
        sources[src] = sources.get(src, 0) + 1

    print("\nSuccessful implementations by source:")

    if not sources:
        print("none")
    else:
        for src, count in sources.items():
            print(f"{src}: {count}")

    print("\nRejected implementations:", len(rejected_tasks))

    # --- Simple insight ---
    print("\nINSIGHT")

    if success_rate < 5:
        print(
            "Implementation success rate is very low. "
            "Manual development with AI assistance recommended."
        )
    elif success_rate < 30:
        print(
            "System is partially stable. "
            "Hybrid development (human + discuss) recommended."
        )
    else:
        print(
            "System stable enough for discuss-driven development."
        )