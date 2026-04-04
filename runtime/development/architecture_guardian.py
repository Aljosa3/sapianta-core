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
import re
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

        # 🔥 MINIMAL ADD: runtime protection (critical for your system)
        self.runtime_protected_paths = [
            "runtime/governance",
            "runtime/system",
            "runtime/ledger",
            "runtime/safety",
            "runtime/layer2",
        ]

        # 🚫 forbidden patterns (simple)
        self.forbidden_patterns = [
            "os.system",
            "subprocess",
            "eval(",
            "exec(",
            "__import__",
        ]

        # 🔥 MINIMAL ADD: regex patterns (more robust detection)
        self.forbidden_regex = [
            r"\beval\s*\(",
            r"\bexec\s*\(",
            r"os\.system\s*\(",
            r"subprocess\.",
            r"__import__\s*\(",
        ]

        # 🔥 OBSERVABILITY (MINIMAL)
        self.stats = {
            "validations": 0,
            "blocks": 0,
            "last_block_reason": None,
        }

    # ==========================================================
    # MAIN ENTRY
    # ==========================================================
    def validate(self, file_path: str, code: str) -> Dict[str, Any]:
        try:
            # 🔥 OBSERVABILITY
            self.stats["validations"] += 1

            # 🔥 FAIL-SAFE INPUT CHECK
            if not isinstance(file_path, str) or not isinstance(code, str):
                raise Exception("[GUARDIAN BLOCK] Invalid input types")

            # 🔥 NEW: filesystem validation (centralized)
            self._validate_existing_file(file_path)

            self._check_protected_path(file_path)
            self._check_runtime_protected_path(file_path)
            self._check_syntax(code)
            self._check_indentation(code)
            self._check_forbidden_patterns(code)
            self._check_forbidden_regex(code)

            # 🔥 NEW: centralized pattern detection (post-check)
            self._validate_code_security(code)

            return {
                "status": "VALID",
                "success": True,
                "errors": [],
            }

        except Exception as e:
            # 🔥 OBSERVABILITY
            self.stats["blocks"] += 1
            self.stats["last_block_reason"] = str(e)

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

    def _check_runtime_protected_path(self, file_path: str):
        for protected in self.runtime_protected_paths:
            if file_path.startswith(protected):
                raise Exception(
                    f"[GUARDIAN BLOCK] Runtime protected path: {protected}"
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

    def _check_forbidden_regex(self, code: str):
        for pattern in self.forbidden_regex:
            if re.search(pattern, code):
                raise Exception(
                    f"[SECURITY BLOCK] Forbidden pattern detected (regex): {pattern}"
                )

    # ==========================================================
    # 🔥 CENTRALIZED SECURITY LAYER (NEW)
    # ==========================================================

    DANGEROUS_PATTERNS = [
        "os.system",
        "eval(",
        "exec(",
        "subprocess",
        "__import__",
    ]

    def _detect_dangerous_patterns(self, code: str) -> list:
        if not code:
            return []

        found = []
        for pattern in self.DANGEROUS_PATTERNS:
            if pattern in code:
                found.append(pattern)
        return found

    def _validate_code_security(self, code: str):
        dangerous = self._detect_dangerous_patterns(code)

        if dangerous:
            raise Exception(
                f"[GUARDIAN BLOCK] Dangerous code detected: {dangerous}"
            )

    def _validate_existing_file(self, file_path: str):
        if not file_path:
            return

        from pathlib import Path

        path = Path(file_path)

        if not path.exists():
            return

        try:
            content = path.read_text()
        except Exception:
            raise Exception(
                "[GUARDIAN BLOCK] Failed to read file for validation"
            )

        dangerous = self._detect_dangerous_patterns(content)

        if dangerous:
            raise Exception(
                f"[GUARDIAN BLOCK] Dangerous existing file: {dangerous}"
            )