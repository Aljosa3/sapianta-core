"""
SAPIANTA Test Validator (minimal)

Detects obviously incorrect tests (v1).
"""

import re


class TestValidator:

    def is_test_suspicious(self, test_code: str, function_name: str = "add") -> bool:
        """
        Detects obvious incorrect assertions like:
        assert add(2, 3) == 10
        """

        # najdi vse assert-e
        matches = re.findall(r"assert\s+(\w+)\((\d+),\s*(\d+)\)\s*==\s*(\d+)", test_code)

        for fn, a, b, expected in matches:

            a = int(a)
            b = int(b)
            expected = int(expected)

            # trenutno podpiramo samo add
            if fn == "add":
                real = a + b

                if real != expected:
                    print(f"[TEST VALIDATOR] Suspicious test detected: {fn}({a},{b})={real} != {expected}")
                    return True

        return False