# PATH: runtime/claude_executor.py

import json
import os
from typing import Dict, Any

from runtime.execution_backend import get_execution_backend


class ClaudeExecutionError(RuntimeError):
    pass


class ClaudeExecutor:
    """
    Executes a Claude Code build based strictly on a
    SAPIANTA_BUILD_PLAN_V1 JSON artifact.

    Responsibilities:
    - load and verify build plan
    - delegate execution to ExecutionAdapter
    - persist raw Claude output (legacy behavior, v0.14)

    This class:
    - does NOT modify the build plan
    - does NOT perform validation
    - does NOT make governance decisions
    """

    EXPECTED_PROTOCOL = "SAPIANTA_BUILD_PLAN_V1"

    def __init__(self, build_plan_path: str, output_root: str):
        self.build_plan_path = build_plan_path
        self.output_root = output_root

    def execute(self) -> None:
        build_plan = self._load_build_plan()
        self._prepare_output_root()

        # ---- EXECUTION BOUNDARY (v0.14) ----
        raw_output = self._execute_with_backend(build_plan)

        self._write_raw_output(raw_output)

        print("[CLAUDE] Execution completed")

    # ---------- internals ----------

    def _load_build_plan(self) -> Dict[str, Any]:
        if not os.path.exists(self.build_plan_path):
            raise ClaudeExecutionError(
                f"Build plan not found: {self.build_plan_path}"
            )

        with open(self.build_plan_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if data.get("protocol") != self.EXPECTED_PROTOCOL:
            raise ClaudeExecutionError(
                f"Invalid build plan protocol: {data.get('protocol')}"
            )

        return data

    def _prepare_output_root(self) -> None:
        os.makedirs(self.output_root, exist_ok=True)

    def _execute_with_backend(self, build_plan: Dict[str, Any]) -> str:
        """
        Delegates execution to the selected ExecutionAdapter.

        v0.14:
        - real execution adapter
        - exactly one execution call
        - raw string output only
        """
        adapter = get_execution_backend()
        raw_output = adapter.execute(build_plan)

        if not isinstance(raw_output, str):
            raise ClaudeExecutionError(
                "Execution backend returned non-string output"
            )

        return raw_output

    def _write_raw_output(self, output: str) -> None:
        out_path = os.path.join(self.output_root, "claude_raw_output.json")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)

        print(f"[CLAUDE] Raw output written to {out_path}")
