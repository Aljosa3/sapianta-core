"""
SAPIANTA Development Loop Command

Runs the autonomous development loop continuously.
"""

import time

from runtime.development.dev_autonomous_loop import DevAutonomousLoop


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

            result = loop.run_once()

            print("cycle result:", result)

            # --- SMART IDLE BACKOFF ---
            if result.get("status") == "no_tasks":

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