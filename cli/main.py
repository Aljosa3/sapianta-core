"""
Sapianta CLI — entry point

Status: NON-AUTHORITATIVE
Phase: 4.B
"""

from .commands.doctor import run as doctor_run


def main() -> None:
    # Explicit, manual invocation only
    doctor_run()


if __name__ == "__main__":
    main()
