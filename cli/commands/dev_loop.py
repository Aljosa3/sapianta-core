"""
SAPIANTA Development Loop Command

Runs the autonomous development loop continuously.
"""

import time

from runtime.development.dev_autonomous_loop import DevAutonomousLoop
from runtime.development.plan_engine import PlanEngine


# 🔥 GLOBAL GOAL
GOAL = "build basic software utility system"


def run(args=None):

    loop = DevAutonomousLoop()
    plan_engine = PlanEngine()
    current_plan = []

    print()
    print("SAPIANTA Development Loop")
    print("-------------------------")
    print("Press Ctrl+C to stop")
    print()

    idle_cycles = 0

    try:

        while True:

            # -------------------------------------------------
            # 🧠 PLAN + FEEDBACK LOOP
            # -------------------------------------------------

            tasks = loop.registry.get_active_tasks()

            if not tasks:

                # 🔥 FEEDBACK LOOP: če plan ne obstaja ali je prazen
                if not current_plan:

                    print("[PLAN] Plan exhausted")

                    GOAL_DYNAMIC = f"{GOAL} - iteration {loop._cycle_count}"

                    print(f"[PLAN] New goal: {GOAL_DYNAMIC}")

                    current_plan = plan_engine.generate_plan(GOAL_DYNAMIC)

                    print(f"[PLAN] Generated {len(current_plan)} tasks")

                # vzamemo naslednji task iz plana
                next_task = current_plan.pop(0)

                print(f"[PLAN] Next task: {next_task}")

                loop.submit_task(next_task)

            # -------------------------------------------------
            # RUN LOOP
            # -------------------------------------------------

            result = loop.run_once()

            print("cycle result:", result)

            status = result.get("status")

            # -------------------------------------------------
            # 🔥 SAFE MODE EXIT
            # -------------------------------------------------

            if status in ["stopped_max_cycles", "stopped_timeout"]:
                print("[DEV_LOOP] SAFE STOP → exiting loop")
                break

            # -------------------------------------------------
            # 🔥 HARD STOP CONDITIONS
            # -------------------------------------------------

            if status in ["waiting_for_approval", "needs_review"]:
                print(f"[DEV_LOOP] STOP (status={status})")
                break

            if status in ["failed", "blocked"]:
                print(f"[DEV_LOOP] END (status={status})")
                break

            # 🔥 CONTINUOUS MODE
            if status == "completed":
                print("[DEV_LOOP] Task completed → continuing (PLAN MODE)")

            # -------------------------------------------------
            # SMART IDLE BACKOFF
            # -------------------------------------------------

            if status == "no_tasks":

                idle_cycles += 1
                sleep_time = min(10, 1 + idle_cycles)

                print(f"[IDLE] sleeping {sleep_time}s")
                time.sleep(sleep_time)

            else:

                idle_cycles = 0
                time.sleep(1)

    except KeyboardInterrupt:

        print()
        print("Development loop stopped.")
        print()