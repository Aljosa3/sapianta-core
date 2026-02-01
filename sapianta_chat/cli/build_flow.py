import sys

from sapianta_chat.validation.build_validator import BuildValidator
from sapianta_chat.validation.repair_plan import RepairPlanGenerator

FORBIDDEN_FILES = {".md"}
FORBIDDEN_IMPORTS = {"openai", "requests", "subprocess"}


def run_post_claude_validation(build_plan: dict, generated_root: str) -> None:
    """
    HARD-GATE VALIDATION

    - Always executed after Claude Code output
    - PASS  -> returns normally, build may continue
    - FAIL  -> prints violations and terminates process (exit code 1)
    """

    validator = BuildValidator(
        build_plan=build_plan,
        generated_root=generated_root,
        forbidden_files=FORBIDDEN_FILES,
        forbidden_imports=FORBIDDEN_IMPORTS,
    )

    result = validator.validate()

    # PASS: allow pipeline to continue
    if result.status == "PASS":
        print("[VALIDATOR] PASS")
        return

    # FAIL: hard stop
    print("[VALIDATOR] FAIL")
    for err in result.errors:
        print(f" - {err}")

    # Informational only — no execution, no mutation
    repair = RepairPlanGenerator.from_validation(result)
    repair.print_plan()

    print("[BUILD] STOPPED BY HARD-GATE")
    sys.exit(1)
