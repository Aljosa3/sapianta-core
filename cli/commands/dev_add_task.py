"""
SAPIANTA CLI — Add Development Task

Registers a new development task in the DevTaskRegistry.
"""

from runtime.development.dev_autonomous_loop import DevAutonomousLoop


def run(args):

    if not args:
        print("Usage: sapianta dev-add-task \"task description\"")
        return

    idea = " ".join(args)

    task = {
        "task_type": "implementation",
        "idea": idea,
        "source": "cli"
    }

    loop = DevAutonomousLoop()

    result = loop.submit_task(task)

    if result == "duplicate":
        print("Task already registered.")
        return

    print("Task registered.")