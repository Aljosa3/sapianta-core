import importlib
import sys

# 🔒 LOCKED: seznam OBVEZNIH modulov za delovanje sistema
REQUIRED_MODULES = [
    "sapianta_chat.cli.build_flow",
    "sapianta_chat.validation.build_validator",
    "sapianta_chat.validation.repair_plan",
]

def run_pipeline_integrity_check() -> None:
    """
    PRE-FLIGHT HARD-GATE

    - Verifies that all required pipeline modules:
      - exist
      - are importable
    - On failure: prints clear error and terminates process
    """

    errors = []

    for module_path in REQUIRED_MODULES:
        try:
            importlib.import_module(module_path)
        except Exception as e:
            errors.append(f"{module_path} -> {e}")

    if not errors:
        print("[PIPELINE] Integrity check: PASS")
        return

    print("[PIPELINE] Integrity check: FAIL")
    for err in errors:
        print(f" - {err}")

    print("[PIPELINE] STOPPED BY PRE-FLIGHT HARD-GATE")
    sys.exit(1)
