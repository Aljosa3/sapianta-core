"""
SAPIANTA Semi-Automatic Development Command

Flow:
submit → dev_loop → auto-approve (correct task) → dev_loop
"""

import time

from runtime.development.dev_autonomous_loop import DevAutonomousLoop
from runtime.development.dev_task_registry import DevTaskRegistry


def run(args):

    if not args:
        print("[DEV_AUTO] Usage: dev_auto \"your task\"")
        return

    goal = " ".join(args)

    loop = DevAutonomousLoop()
    registry = DevTaskRegistry()

    print()
    print("SAPIANTA DEV AUTO")
    print("-------------------------")
    print(f"GOAL: {goal}")
    print()

    # ---------------------------------------------------------
    # STEP 1 — SUBMIT TASK
    # ---------------------------------------------------------

    task = {
        "goal": goal,
        "priority": 1
    }

    result = loop.submit_task(task)
    print("[DEV_AUTO] submit:", result)

    # ---------------------------------------------------------
    # STEP 2 — FIRST RUN
    # ---------------------------------------------------------

    result = loop.run_once()
    print("[DEV_AUTO] run1:", result)

    # ---------------------------------------------------------
    # STEP 3 — AUTO APPROVE (🔥 FIXED TARGETING)
    # ---------------------------------------------------------

    waiting = registry.get_tasks_by_state("waiting_approval")

    target_task = None
    for t in waiting:
        if t.get("goal") == goal:
            target_task = t
            break

    if target_task:
        print("[DEV_AUTO] AUTO APPROVING:")
        print(target_task)

        registry.update_task_state(target_task, "approved")
        target_task["approved"] = True

        registry._persist()
    else:
        print("[DEV_AUTO] No matching task found for auto-approval")

    # ---------------------------------------------------------
    # STEP 4 — SECOND RUN
    # ---------------------------------------------------------

    result = loop.run_once()
    print("[DEV_AUTO] run2:", result)

    print()
    print("[DEV_AUTO] DONE")