"""
SAPIANTA Semantic Test Parser (v1)

Purpose:
Extract expected behavior from simple pytest-style assertions.

Design:
- deterministic
- safe parsing (regex only)
- minimal scope (v1)
"""

import re
from typing import Optional, Dict


class SemanticTestParser:

    def parse(self, error_text: str) -> Optional[Dict]:
        """
        Extract function intent from test assertion.

        Example:
        assert add(1, 2) == 3
        """

        if not error_text:
            return None

        # 🔍 match: add(1, 2) == 3
        match = re.search(
            r"assert\s+(\w+)\((.*?)\)\s*==\s*(\d+)",
            error_text
        )

        if not match:
            return None

        func_name = match.group(1)
        args_raw = match.group(2)
        expected = int(match.group(3))

        try:
            args = [int(x.strip()) for x in args_raw.split(",")]
        except Exception:
            return None

        return {
            "function": func_name,
            "args": args,
            "expected": expected
        }

    def generate_fix(self, parsed: Dict) -> Optional[Dict]:
        """
        Generate semantic fix based on parsed test.
        """

        if not parsed:
            return None

        func = parsed["function"]
        args = parsed["args"]

        # 🔥 v1: only handle 2-arg numeric operations
        if len(args) == 2:
            a, b = args
            expected = parsed["expected"]

            # detect operation
            if a + b == expected:
                return {
                    "strategy": "semantic_add",
                    "code": f"def {func}(a, b):\n    return a + b\n"
                }

            if a * b == expected:
                return {
                    "strategy": "semantic_multiply",
                    "code": f"def {func}(a, b):\n    return a * b\n"
                }

            if b != 0 and a / b == expected:
                return {
                    "strategy": "semantic_divide",
                    "code": f"def {func}(a, b):\n    return a / b\n"
                }

        return None