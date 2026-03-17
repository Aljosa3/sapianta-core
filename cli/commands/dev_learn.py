"""
SAPIANTA Development Learning

Analyzes development history and suggests optimal development strategy.
"""

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

    tasks_processed = metrics.get("tasks_processed", metrics.get("processed", 0))
    completed = metrics.get("tasks_completed", metrics.get("completed", 0))
    failed = metrics.get("tasks_failed", metrics.get("failed", 0))
    blocked = metrics.get("tasks_blocked", metrics.get("blocked", 0))

    print("\nMETRICS")
    print(f"Tasks processed: {tasks_processed}")
    print(f"Completed: {completed}")
    print(f"Failed: {failed}")
    print(f"Blocked: {blocked}")

    if tasks_processed:
        success_rate = completed / tasks_processed
        print(f"Success rate: {success_rate:.2%}")
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

    # --- Insight ---
    print("\nINSIGHT")

    if success_rate < 0.05:
        insight = (
            "Implementation success rate is very low. "
            "Manual development with AI assistance recommended."
        )
    elif success_rate < 0.30:
        insight = (
            "System is partially stable. "
            "Hybrid development (human + discuss) recommended."
        )
    else:
        insight = (
            "System stable enough for discuss-driven development."
        )

    print(insight)

    # --- Strategy suggestion ---
    print("\nSTRATEGY SUGGESTION")

    if success_rate > 0.8:

        strategy = "DISCUSS_DRIVEN"

        print("\nRecommended development strategy:")
        print("DISCUSS_DRIVEN")

        print("\nReason:")
        print("High success rate indicates discuss-driven development is stable.")

    elif success_rate > 0.5:

        strategy = "HYBRID"

        print("\nRecommended development strategy:")
        print("HYBRID (discuss + manual CLI)")

        print("\nReason:")
        print(
            "Moderate success rate suggests combining automated "
            "and manual development."
        )

    else:

        strategy = "MANUAL"

        print("\nRecommended development strategy:")
        print("MANUAL AI-assisted development")

        print("\nReason:")
        print("Low success rate indicates manual development is safer.")

    # --- Next action ---
    print("\nNEXT ACTION")

    if strategy == "DISCUSS_DRIVEN":

        print("\nYou can safely use:")
        print("sapianta discuss")
        print("followed by:")
        print("sapianta dev-run-auto")

    elif strategy == "HYBRID":

        print("\nRecommended workflow:")
        print("discuss → dev-add-task → dev-run")

    else:

        print("\nRecommended workflow:")
        print("manual coding with AI assistance")