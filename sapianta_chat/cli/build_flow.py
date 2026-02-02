# PATH: sapianta_chat/cli/build_flow.py

import json
import sys
from pathlib import Path
from typing import Dict, Any

from sapianta_chat.validation.build_validator import BuildValidator
from sapianta_chat.validation.repair_plan import RepairPlanGenerator

from runtime.claude_executor import ClaudeExecutor
from runtime.module_writer import ModuleWriter


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

    if result.status == "PASS":
        print("[VALIDATOR] PASS")
        return

    print("[VALIDATOR] FAIL")
    for err in result.errors:
        print(f" - {err}")

    # Informational only — no execution, no mutation
    repair = RepairPlanGenerator.from_validation(result)
    repair.print_plan()

    print("[BUILD] STOPPED BY HARD-GATE")
    sys.exit(1)


def run_build_pipeline(
    build_plan: Dict[str, Any],
    build_plan_path: str,
    project_root: str = ".",
    workdir: str = "generated_output",
) -> None:
    """
    FULL POST-CLAUDE HARD-GATED BUILD PIPELINE

    Flow:
    1. Execute Claude Code (raw output)
    2. Write files to disk (ModuleWriter) INTO workdir
    3. Run post-Claude validator AGAINST workdir (HARD GATE)
    """

    # 🔒 Dedicated build output root
    workdir_path = Path(workdir).resolve()
    workdir_path.mkdir(parents=True, exist_ok=True)

    # 1️⃣ Claude execution (writes raw output only)
    executor = ClaudeExecutor(
        build_plan_path=build_plan_path,
        output_root=str(workdir_path),
    )

    executor.execute()

    raw_output_path = workdir_path / "claude_raw_output.json"

    if not raw_output_path.exists():
        print("[BUILD] FAIL: Claude produced no output")
        sys.exit(1)

    with raw_output_path.open("r", encoding="utf-8") as f:
        claude_output = json.load(f)

    # 2️⃣ Write generated modules STRICTLY into workdir
    writer = ModuleWriter(project_root=str(workdir_path))

    try:
        writer.write(claude_output)
    except Exception as e:
        print(f"[BUILD] FAIL during write phase: {e}")
        sys.exit(1)

    # 3️⃣ Post-Claude hard-gate validation (ONLY workdir is scanned)
    run_post_claude_validation(
        build_plan=build_plan,
        generated_root=str(workdir_path),
    )

    print("[BUILD] COMPLETED SUCCESSFULLY (PASS)")
