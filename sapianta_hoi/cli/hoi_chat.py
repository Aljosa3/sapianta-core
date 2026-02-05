"""
HOI Runtime CLI — Read-only Stub

This CLI provides a minimal interactive loop for the HOI runtime.

It intentionally:
- does not interpret input
- does not ask smart questions
- does not recommend
- does not execute
- does not generate decisions

It exists solely to:
- accept user input
- allow explicit stop
- return responsibility to the human
"""

import sys

from sapianta_hoi.runtime_stub.session import HOISession
from sapianta_hoi.runtime_stub.stop_conditions import STOP_CONDITIONS


def print_intro():
    print("SAPIANTA — HOI Runtime (read-only)")
    print("---------------------------------")
    print("This session is for orientation only.")
    print("No actions will be taken.")
    print("Type ':stop' to end the session.")
    print()


def print_stop(reason: str):
    print()
    print("HOI has stopped.")
    print(f"Reason: {reason}")
    print("No decisions were made.")
    print("Responsibility remains with you.")
    print()


def main():
    session = HOISession()
    print_intro()

    while session.active:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            session.stop("user_requests_pause")
            break

        if not user_input:
            # Empty input is accepted as valid silence
            continue

        if user_input.startswith(":stop"):
            session.stop("user_requests_pause")
            break

        # Accept input without interpretation
        session.receive_input(user_input)

    summary = session.summary()

    print_stop("user_requests_pause")
    print("Session summary:")
    for key, value in summary.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
