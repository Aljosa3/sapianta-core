import sys
import subprocess


VALID_TYPES = {"cosmetic", "parametric", "structural"}


def run(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python promotion_gate_validator.py <change_type> [--approve-structural]")
        sys.exit(1)

    change_type = sys.argv[1]

    if change_type not in VALID_TYPES:
        print("Invalid change type.")
        sys.exit(1)

    approve_structural = "--approve-structural" in sys.argv

    if change_type == "structural" and not approve_structural:
        print("STRUCTURAL change requires explicit approval flag.")
        sys.exit(1)

    print("Running determinism checks...")
    run("pytest -q")

    print("Running layer freeze check...")
    run("python scripts/check_layer_freeze.py")

    print("Promotion Gate PASSED.")


if __name__ == "__main__":
    main()