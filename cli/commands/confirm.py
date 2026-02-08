from cli.errors import InvalidArgumentsError


def run(args):
    """
    Explicit human confirmation.

    Supported:
    - confirm yes
    - confirm no

    Constraints:
    - No execution
    - No write
    - No lifecycle mutation
    """
    if not args or args[0] not in ("yes", "no"):
        raise InvalidArgumentsError("usage: confirm <yes|no>")

    decision = args[0]

    print("Human confirmation")
    print("------------------")

    if decision == "yes":
        print("Decision: YES")
        print("Result: CONFIRMED (no execution performed)")
        print("Next step: Eligible for HCBPF / SSWA when explicitly triggered")
        return

    if decision == "no":
        print("Decision: NO")
        print("Result: TERMINATED (read-only)")
        print("No further actions will be taken.")
        return
