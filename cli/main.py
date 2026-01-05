"""
Sapianta CLI — entry point

Status: NON-AUTHORITATIVE
Phase: 4.C
"""

import sys

from .commands.doctor import run as doctor_run
from .commands.version import run as version_run


def main() -> None:
    # Explicit, manual invocation only
    if len(sys.argv) < 2:
        print("Usage: sapianta <command>")
        return

    command = sys.argv[1]

    if command == "doctor":
        doctor_run()
    elif command == "version":
        version_run()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
