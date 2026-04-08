"""
SAPIANTA Test Validator (v2 — deterministic safety gate)

Purpose:
- blocks low-quality / unsafe / trivial tests
- detects suspicious assertions (semantic mismatch)
- enforces minimal test quality before pipeline execution

Design:
- deterministic (no LLM)
- fail-safe (reject on uncertainty)
- lightweight (regex-based)
"""


import re


def _is_valid_python(code: str) -> bool:
    import ast
    try:
        ast.parse(code)
        return True
    except Exception:
        return False


class TestValidator:

    MIN_ASSERTS = 2

    # -------------------------------------------------
    # MAIN VALIDATION ENTRY
    # -------------------------------------------------
    def validate(self, test_code: str) -> dict:
        """
        Returns:
            {
                "valid": bool,
                "reason": str
            }
        """

        if not test_code or not isinstance(test_code, str):
            return {"valid": False, "reason": "empty_test"}

        if not _is_valid_python(test_code):
            return {"valid": False, "reason": "invalid_python_syntax"}

        # -------------------------------------------------
        # RULE 1: must contain assert
        # -------------------------------------------------
        if "assert" not in test_code:
            return {"valid": False, "reason": "no_assert"}

        # -------------------------------------------------
        # RULE 2: minimum number of asserts
        # -------------------------------------------------
        if test_code.count("assert") < self.MIN_ASSERTS:
            return {"valid": False, "reason": "too_few_asserts"}

        # -------------------------------------------------
        # RULE 3: forbid trivial asserts
        # -------------------------------------------------
        forbidden_patterns = [
            "assert True",
            "assert False",
            "assert 1 == 1",
        ]

        for pattern in forbidden_patterns:
            if pattern in test_code:
                return {"valid": False, "reason": "trivial_assert"}

        # -------------------------------------------------
        # RULE 4: basic input variation check
        # -------------------------------------------------
        numbers = re.findall(r"\d+", test_code)
        if len(set(numbers)) < 2:
            return {"valid": False, "reason": "no_input_variation"}

        # -------------------------------------------------
        # RULE 5: forbid unsafe operations
        # -------------------------------------------------
        forbidden_ops = ["exec(", "eval(", "os.", "subprocess"]

        for op in forbidden_ops:
            if op in test_code:
                return {"valid": False, "reason": "unsafe_code"}

        # -------------------------------------------------
        # RULE 6: semantic sanity check (important)
        # -------------------------------------------------
        if self.is_test_suspicious(test_code):
            return {"valid": False, "reason": "suspicious_logic"}

        return {"valid": True, "reason": "ok"}

    # -------------------------------------------------
    # SEMANTIC CHECK (v1 extended)
    # -------------------------------------------------
    def is_test_suspicious(self, test_code: str) -> bool:
        """
        Detects incorrect expectations for simple known patterns.

        Example:
            assert add(2, 3) == 10  → suspicious
        """

        matches = re.findall(
            r"assert\s+(\w+)\((\d+),\s*(\d+)\)\s*==\s*(\d+)",
            test_code
        )

        for fn, a, b, expected in matches:

            a = int(a)
            b = int(b)
            expected = int(expected)

            # -------------------------------------------------
            # KNOWN FUNCTION RULES (extendable)
            # -------------------------------------------------

            if fn == "add":
                real = a + b
                if real != expected:
                    print(
                        f"[TEST VALIDATOR] Suspicious: {fn}({a},{b})={real} != {expected}"
                    )
                    return True

            elif fn == "sub":
                real = a - b
                if real != expected:
                    return True

            elif fn == "mul":
                real = a * b
                if real != expected:
                    return True

            elif fn == "div" and b != 0:
                real = a / b
                if real != expected:
                    return True

        return False