from cli.errors import InvalidArgumentsError


def run(args):
    """
    Single-Shot Write Authorization (SSWA).

    Supported:
    - sswa authorize
    - sswa abort

    Constraints:
    - No execution
    - No write
    - Authorization is informational only
    """
    if not args or args[0] not in ("authorize", "abort"):
        raise InvalidArgumentsError("usage: sswa <authorize|abort>")

    action = args[0]

    print("SSWA — Single-Shot Write Authorization")
    print("------------------------------------")

    if action == "authorize":
        print("Authorization: GRANTED (armed)")
        print("Mode: SINGLE-SHOT")
        print("Status: READY (no write performed)")
        print("Next step: explicit write command required")
        return

    if action == "abort":
        print("Authorization: ABORTED")
        print("Status: TERMINATED")
        print("No write will be allowed in this session.")
        return
