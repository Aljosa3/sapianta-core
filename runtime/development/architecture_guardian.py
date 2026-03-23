"""
SAPIANTA Architecture Guardian

Purpose
-------
Validates AI-generated artifacts before execution.

Prevents:
- syntax errors
- invalid indentation
- forbidden operations
- mutation of protected system areas

Fail-closed design.
"""

import ast
import os
from typing import Dict, Any


class ArchitectureGuardian:
    def __init__(self):
        # 🔒 protected paths (NO WRITE / NO MODIFY)
        self.protected_paths = [
            "sapianta_system/kernel",
            "sapianta_system/replay",
            "sapianta_system/governance",
            "sapianta_system/constitution",
        ]

        # 🚫 forbidden patterns
        self.forbidden_patterns = [
            "os.system",
            "subprocess",
            "eval(",
            "exec(",
            "__import__",
        ]

    # ==========================================================
    # MAIN ENTRY
    # ==========================================================
    def validate(self, file_path: str, code: str) -> Dict[str, Any]:
        try:
            self._check_protected_path(file_path)
            self._check_syntax(code)
            self._check_indentation(code)
            self._check_forbidden_patterns(code)

            return {
                "status": "VALID",
                "success": True,
                "errors": [],
            }

        except Exception as e:
            return {
                "status": "INVALID",
                "success": False,
                "error": str(e),
            }

    # ==========================================================
    # CHECKS
    # ==========================================================
    def _check_protected_path(self, file_path: str):
        for protected in self.protected_paths:
            if protected in file_path:
                raise Exception(
                    f"[GUARDIAN BLOCK] Attempt to modify protected path: {protected}"
                )

    def _check_syntax(self, code: str):
        try:
            ast.parse(code)
        except SyntaxError as e:
            raise Exception(f"[SYNTAX ERROR] {str(e)}")

    def _check_indentation(self, code: str):
        lines = code.split("\n")

        for i, line in enumerate(lines):
            if "\t" in line:
                raise Exception(
                    f"[INDENT ERROR] Tab detected at line {i+1}. Use spaces only."
                )

            # mixed indentation check (basic)
            if line.startswith(" ") and len(line) > 1:
                spaces = len(line) - len(line.lstrip(" "))
                if spaces % 4 != 0:
                    raise Exception(
                        f"[INDENT ERROR] Invalid indentation (not multiple of 4) at line {i+1}"
                    )

    def _check_forbidden_patterns(self, code: str):
        for pattern in self.forbidden_patterns:
            if pattern in code:
                raise Exception(
                    f"[SECURITY BLOCK] Forbidden pattern detected: {pattern}"
                )