"""
SAPIANTA Development Loop Command

Runs the autonomous development loop continuously.
"""

import time

from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def run():

    loop = DevAutonomousLoop()

    print()
    print("SAPIANTA Development Loop")
    print("-------------------------")
    print("Press Ctrl+C to stop")
    print()

    try:

        while True:

            result = loop.run_once()

            print("cycle result:", result)

            time.sleep(5)

    except KeyboardInterrupt:

        print()
        print("Development loop stopped.")
        print()