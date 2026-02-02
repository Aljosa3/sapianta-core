from sapianta_chat.cli.commands.export_build import export_build

def route_command(command: str, context: dict):
    parts = command.strip().split()

    if parts[0] == ":export-build":
        if len(parts) != 2:
            raise ValueError("Usage: :export-build <path>")
        export_build(context["build_plan"], parts[1])
        return

    raise ValueError(f"Unknown command: {command}")
