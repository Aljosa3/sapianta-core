"""
SAPIANTA Add Task Command

Adds a new task into the development loop.
"""

from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def run(args=None):

    if not args or len(args) == 0:
        print("Usage: python -m cli add_task \"task description\"")
        return

    goal = " ".join(args)

    loop = DevAutonomousLoop()

    task = {
        "goal": goal,
        "priority": 1
    }

    result = loop.submit_task(task)

    print()
    print("[ADD TASK]")
    print("----------")
    print("goal:", goal)
    print("status:", result)
    print()