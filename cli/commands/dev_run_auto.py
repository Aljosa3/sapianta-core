"""
SAPIANTA CLI — Autonomous Development Runner

Runs development cycles until no active tasks remain.
"""

import time

from runtime.development.dev_autonomous_loop import DevAutonomousLoop
from runtime.development.dev_task_registry import DevTaskRegistry


def run():

    loop = DevAutonomousLoop()

    print("\nSAPIANTA Autonomous Development Runner")
    print("--------------------------------------")

    cycle = 0

    while True:

        # reload registry each cycle so we read the latest state from disk
        registry = DevTaskRegistry()
        active = registry.get_active_tasks()

        if not active:
            print("\nNo active tasks remaining.")
            break

        cycle += 1
        print(f"\nCycle {cycle}")

        result = loop.run_once()

        print(f"Result: {result}")

        # small pause to avoid tight loop
        time.sleep(0.2)