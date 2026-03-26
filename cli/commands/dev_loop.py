"""
SAPIANTA Development Loop Command

Runs the autonomous development loop continuously.
"""

import time

from runtime.development.dev_autonomous_loop import DevAutonomousLoop
from runtime.development.capability_gap_detector import CapabilityGapDetector


# 🔥 NOVO: GLOBAL GOAL
GOAL = "build basic software utility system"


def run(args=None):

    loop = DevAutonomousLoop()

    print()
    print("SAPIANTA Development Loop")
    print("-------------------------")
    print("Press Ctrl+C to stop")
    print()

    idle_cycles = 0

    try:

        while True:

            # -------------------------------------------------
            # 🧠 AUTO TASK GENERATION (GOAL-DRIVEN)
            # -------------------------------------------------

            tasks = loop.registry.get_active_tasks()

            all_tasks = (
                loop.registry.get_tasks_by_state("completed") +
                loop.registry.get_tasks_by_state("approved") +
                loop.registry.get_tasks_by_state("queued") +
                loop.registry.get_tasks_by_state("waiting_approval")
            )

            if not tasks:

                existing_goals = {t.get("goal") for t in all_tasks}

                print("[AUTO] No active tasks → generating new task")

                detector = CapabilityGapDetector()
                gaps = detector.detect()

                if gaps:
                    goal = gaps[0]
                else:
                    # 🔥 GOAL-DRIVEN FALLBACK
                    fallback_goals = [
                        f"{GOAL} - logging module",
                        f"{GOAL} - config system",
                        f"{GOAL} - validation module",
                        f"{GOAL} - error handling",
                        f"{GOAL} - file processing"
                    ]

                    goal = next(
                        (g for g in fallback_goals if g not in existing_goals),
                        f"{GOAL} - helper module"
                    )

                new_task = {
                    "goal": goal,
                    "priority": 1
                }

                print(f"[AUTO] New task generated: {new_task}")

                loop.submit_task(new_task)

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
                print("[DEV_LOOP] Task completed → continuing (AUTO MODE)")

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