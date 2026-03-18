"""
SAPIANTA Auto-Fix Engine

Attempts to fix failed test results.

Design:
- deterministic
- rule-based (v1)
- safe (no direct file writes)
- returns patch suggestions only
"""

import re


class AutoFixEngine:

    def attempt_fix(self, test_result):

        # --------------------------------------------
        # SUCCESS CASE
        # --------------------------------------------
        if test_result.get("success"):
            return {
                "fixed": False,
                "reason": "No failures detected",
                "strategy": None,
                "patch": None,
                "confidence": 1.0
            }

        error = test_result.get("error", "")
        output = test_result.get("output", "")

        failed_modules = self.extract_failed_modules(output)

        # --------------------------------------------
        # STRATEGY 1: Missing import
        # --------------------------------------------
        if "ImportError" in error or "ModuleNotFoundError" in error:

            return {
                "fixed": False,
                "strategy": "missing_import",
                "patch": f"# Suggestion: check or add missing imports in modules: {failed_modules}",
                "confidence": 0.6
            }

        # --------------------------------------------
        # STRATEGY 2: Attribute error
        # --------------------------------------------
        if "AttributeError" in error:

            attr = self.extract_attribute_name(error)

            return {
                "fixed": False,
                "strategy": "missing_attribute",
                "patch": f"# Suggestion: implement or fix attribute '{attr}' in modules: {failed_modules}",
                "confidence": 0.5
            }

        # --------------------------------------------
        # STRATEGY 3: Assertion failure
        # --------------------------------------------
        if "AssertionError" in output:

            return {
                "fixed": False,
                "strategy": "assertion_failure",
                "patch": f"# Suggestion: review logic and expected values in modules: {failed_modules}",
                "confidence": 0.4
            }

        # --------------------------------------------
        # STRATEGY 4: Type error
        # --------------------------------------------
        if "TypeError" in error:

            return {
                "fixed": False,
                "strategy": "type_mismatch",
                "patch": f"# Suggestion: verify argument types and function signatures in modules: {failed_modules}",
                "confidence": 0.5
            }

        # --------------------------------------------
        # STRATEGY 5: Syntax error
        # --------------------------------------------
        if "SyntaxError" in error:

            return {
                "fixed": False,
                "strategy": "syntax_error",
                "patch": f"# Suggestion: fix syntax errors in modules: {failed_modules}",
                "confidence": 0.8
            }

        # --------------------------------------------
        # FALLBACK
        # --------------------------------------------
        return {
            "fixed": False,
            "strategy": "manual_review_required",
            "patch": f"# Unable to auto-fix. Inspect modules: {failed_modules}",
            "confidence": 0.2
        }

    # ------------------------------------------------
    # HELPERS
    # ------------------------------------------------

    def extract_failed_modules(self, output):

        modules = []

        for line in output.splitlines():
            if "FAILED" in line and "::" in line:
                module = line.split("::")[0]
                modules.append(module)

        return sorted(set(modules))

    def extract_attribute_name(self, error):

        match = re.search(r"'(.+?)'", error)

        if match:
            return match.group(1)

        return "unknown"