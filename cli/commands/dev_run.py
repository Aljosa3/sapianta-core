"""
SAPIANTA Development Run Command

Executes one autonomous development cycle.
"""

from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def run():

    loop = DevAutonomousLoop()

    result = loop.run_once()

    print()
    print("SAPIANTA Development Run")
    print("------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")

    print()