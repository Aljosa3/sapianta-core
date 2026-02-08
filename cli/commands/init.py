from cli.adapters.lifecycle_reader import get_current_lifecycle
from cli.errors import InvalidArgumentsError


def run(args):
    """
    Human-triggered lifecycle initialization (READ-ONLY phase).

    Behavior:
    - If a lifecycle exists: display its metadata
    - If none exists: state that no lifecycle is present

    Constraints:
    - No state mutation
    - No implicit transitions
    - No lifecycle creation
    """
    if args:
        raise InvalidArgumentsError("init takes no arguments")

    lifecycle = get_current_lifecycle()

    if lifecycle is None:
        print("No active lifecycle found.")
        print("Status: READY_FOR_INITIALIZATION (read-only)")
        return

    print("Active lifecycle detected:")
    print(f"- lifecycle_id: {lifecycle.get('lifecycle_id')}")
    print(f"- status: {lifecycle.get('status')}")
    print(f"- created_at: {lifecycle.get('created_at')}")
