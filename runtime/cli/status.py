"""
SAPIANTA Status CLI

Displays current task states from registry.
"""

import json
from runtime.development.dev_task_registry import DevTaskRegistry


def status():
    registry = DevTaskRegistry()

    result = {
        "queued": [],
        "running": [],
        "waiting_approval": [],
        "approved": [],
        "completed": registry.get_completed_tasks(),
        "failed": registry.get_rejected_tasks()
    }

    for task in registry.get_active_tasks():
        state = task.get("state", "queued")

        if state not in result:
            result[state] = []

        result[state].append(task)

    print(json.dumps(result, indent=2))


def run(args):
    status()