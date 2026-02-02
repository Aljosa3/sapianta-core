# PATH: sapianta_chat/cli/main.py

import argparse
import json
import sys
from pathlib import Path

from sapianta_chat.cli.pipeline_integrity import run_pipeline_integrity_check
from sapianta_chat.cli.build_flow import run_build_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="sapianta-chat",
        description="SAPIANTA Chat — governed module build system",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # ---- build command ----
    build_parser = subparsers.add_parser(
        "build",
        help="Execute a governed build plan",
    )

    build_parser.add_argument(
        "build_plan",
        type=str,
        help="Path to reviewed build plan JSON",
    )

    build_parser.add_argument(
        "--project-root",
        default=".",
        help="Project root for module writing and validation",
    )

    build_parser.add_argument(
        "--workdir",
        default="generated_output",
        help="Working directory for Claude raw output",
    )

    args = parser.parse_args()

    # 🔒 PRE-FLIGHT HARD-GATE
    run_pipeline_integrity_check()

    if args.command == "build":
        _handle_build(args)


def _handle_build(args) -> None:
    build_plan_path = Path(args.build_plan)

    if not build_plan_path.exists():
        print(f"[CLI] Build plan not found: {build_plan_path}")
        sys.exit(1)

    try:
        with build_plan_path.open("r", encoding="utf-8") as f:
            build_plan = json.load(f)
    except Exception as e:
        print(f"[CLI] Failed to load build plan: {e}")
        sys.exit(1)

    run_build_pipeline(
        build_plan=build_plan,
        build_plan_path=str(build_plan_path),
        project_root=args.project_root,
        workdir=args.workdir,
    )


if __name__ == "__main__":
    main()
