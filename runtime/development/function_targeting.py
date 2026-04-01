"""
Function Targeting Layer (FTL v2)

Purpose:
---------
Deterministically resolve the correct function to patch based on:

1) traceback analysis
2) pytest output parsing

NO fallback to random or default names.

If function cannot be resolved → return None
"""

import re
from typing import Optional


class FunctionTargeting:

    def extract_function_from_error(self, error_text: str) -> Optional[str]:
        """
        Extract function name from traceback stack.

        Example:
        File "...", line 10, in my_function
        """
        pattern = r'in\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        matches = re.findall(pattern, error_text)

        if matches:
            # take LAST occurrence (deepest stack)
            candidate = matches[-1]

            # =====================================================
            # 🔥 FILTER INVALID TARGETS (FTL v2 HARDENING)
            # =====================================================
            invalid_targets = {
                "<module>",
                "__name__",
                "pytest",
                "run",
                "main"
            }

            # 🔥 ignore test functions
            if candidate.startswith("test_"):
                return None

            if candidate in invalid_targets:
                return None

            if candidate.isidentifier():
                return candidate

        return None

    def extract_function_from_test(self, error_text: str) -> Optional[str]:
        """
        Extract function name from pytest test call.

        Supports:
        - result = my_function(...)
        - assert my_function(...) ...
        - direct calls: my_function(...)
        """

        # =====================================================
        # 1️⃣ assignment pattern
        # =====================================================
        pattern_assign = r'=\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        matches = re.findall(pattern_assign, error_text)

        if matches:
            candidate = matches[0]
            if candidate.isidentifier() and not candidate.startswith("test_"):
                return candidate

        # =====================================================
        # 2️⃣ assert pattern
        # =====================================================
        pattern_assert = r'assert\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        matches = re.findall(pattern_assert, error_text)

        if matches:
            candidate = matches[0]
            if candidate.isidentifier() and not candidate.startswith("test_"):
                return candidate

        # =====================================================
        # 3️⃣ generic call pattern (fallback)
        # =====================================================
        pattern_call = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        matches = re.findall(pattern_call, error_text)

        for candidate in matches:

            if candidate.startswith("test_"):
                continue

            if candidate in {"assert", "return", "if", "for", "while"}:
                continue

            if candidate.isidentifier():
                return candidate

        return None

    def resolve_target_function(self, error_text: str) -> Optional[str]:
        """
        Resolution priority:

        1) traceback (most reliable)
        2) test call parsing
        """

        fn = self.extract_function_from_error(error_text)
        if fn and fn.isidentifier():
            return fn

        fn = self.extract_function_from_test(error_text)
        if fn and fn.isidentifier():
            return fn

        # 🚫 NO fallback allowed
        return None