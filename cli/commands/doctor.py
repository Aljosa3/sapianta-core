"""
Sapianta CLI — doctor

Status: NON-AUTHORITATIVE
Phase: 4.B

This command performs a blind presence check of core system artifacts.
It does not interpret results.
It does not suggest actions.
It does not explain failures.
"""

from pathlib import Path


def run() -> None:
    """
    Execute a non-authoritative system presence check.
    """

    root = Path(__file__).resolve().parents[2]

    checks = {
        "Core Canon": root / "CANON.md",
        "Canon Lock": root / "governance" / "locks" / "canon.lock",
        "Core Lock": root / "governance" / "locks" / "core.lock",
        "Interaction Layer": root / "cli",
        "Invocation Gate": root / "invocation" / "controlled" / "gate.py",
        "Execution": root / "instances" / "sapianta" / "execution" / "status.md",
    }

    print("SAPIANTA SYSTEM STATUS")
    print("----------------------")

    for label, path in checks.items():
        status = "PRESENT" if path.exists() else "MISSING"
        print(f"{label}: {status}")

    print()
    print("STATUS: READY (NON-EXECUTABLE)")
