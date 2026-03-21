import importlib
import sys

from cli.errors import InvalidCommandError


# Kanonični command surface (LOCKED + lazy loading)
COMMANDS = {
    # --- CORE ---
    "init": "cli.commands.init",
    "input": "cli.commands.input",
    "confirm": "cli.commands.confirm",
    "show": "cli.commands.show",
    "list": "cli.commands.list",
    "inspect": "cli.commands.inspect",
    "sswa": "cli.commands.sswa",
    "discuss": "cli.commands.discuss",

    # --- DEV ---
    "dev_run": "cli.commands.dev_run",
    "dev_loop": "cli.commands.dev_loop",
    "dev_run_auto": "cli.commands.dev_run_auto",
    "dev_metrics": "cli.commands.dev_metrics",
    "dev_status": "cli.commands.dev_status",
    "dev_history": "cli.commands.dev_history",  # ✅ ključna registracija
    "dev_list": "cli.commands.dev_list",
    "dev_add_task": "cli.commands.dev_add_task",
    "dev_reconcile": "cli.commands.dev_reconcile",
    "dev_learn": "cli.commands.dev_learn",

    # --- TASK ---
    "add_task": "cli.commands.add_task",

    # --- REPAIR ---
    "fix": "cli.commands.fix",
}


def main(argv=None):
    """
    Minimal, stateless CLI router.
    - Lazy command loading
    - No lifecycle logic
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

    command_path = COMMANDS[command_name]

    try:
        module = importlib.import_module(command_path)
    except Exception as e:
        raise InvalidCommandError(
            f"Failed to load command '{command_name}': {str(e)}"
        )

    # ✅ robust execution contract
    if hasattr(module, "run") and callable(module.run):
        module.run(args)
    else:
        raise InvalidCommandError(
            f"Command '{command_name}' does not implement callable run(args)"
        )