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
from .commands.dev_list import run as dev_list_run
from .commands.dev_run_auto import run as dev_run_auto
from .commands.dev_metrics import run as dev_metrics_run
from .commands.dev_history import run as dev_history_run
from .commands.discuss import run as discuss_run
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

    elif command == "dev-list":
        dev_list_run()

    elif command == "dev-run-auto":
        dev_run_auto()

    elif command == "dev-metrics":
        dev_metrics_run()

    elif command == "dev-history":
        dev_history_run()

    elif command == "discuss":
        discuss_run(args)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
    