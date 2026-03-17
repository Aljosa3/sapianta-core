"""
Sapianta CLI — entry point

Status: NON-AUTHORITATIVE
Phase: 4.C
"""

import sys

from .commands.doctor import run as doctor_run
from .commands.version import run as version_run
from .commands.dev_status import run as dev_status_run
from .commands.dev_run import run as dev_run
from .commands.dev_loop import run as dev_loop
from .commands import dev_add_task


def main() -> None:
    # Explicit, manual invocation only
    if len(sys.argv) < 2:
        print("Usage: sapianta <command>")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "doctor":
        doctor_run()

    elif command == "version":
        version_run()

    elif command == "dev-status":
        dev_status_run()

    elif command == "dev-run":
        dev_run()

    elif command == "dev-loop":
        dev_loop()

    elif command == "dev-add-task":
        dev_add_task.run(args)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
    