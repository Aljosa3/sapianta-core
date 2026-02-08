import sys

from cli.errors import InvalidCommandError
from cli.commands import (
    init,
    input as input_cmd,
    confirm,
    show,
    list as list_cmd,
    inspect,
    sswa,   # ← DODANO
)

# Kanonični command surface (LOCKED)
COMMANDS = {
    "init": init,
    "input": input_cmd,
    "confirm": confirm,
    "show": show,
    "list": list_cmd,
    "inspect": inspect,
    "sswa": sswa,   # ← DODANO
}


def main(argv=None):
    """
    Minimal, stateless CLI router.
    - No lifecycle logic
    - No execution
    - No writes
    """
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        raise InvalidCommandError("No command provided.")

    command_name = argv[0]
    args = argv[1:]

    if command_name not in COMMANDS:
        raise InvalidCommandError(f"Unknown command: {command_name}")

    COMMANDS[command_name].run(args)
