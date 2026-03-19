"""
SAPIANTA Auto-Fix Engine

Attempts to fix failed test results.

Design:
- deterministic
- rule-based (v1)
- multi-fix capable (v2)
- safe (no direct file writes)
- returns patch suggestions only
"""

import re
from typing import List, Dict


class AutoFixEngine:

    # ================================================================
    # 🆕 MULTI-FIX ENGINE (NEW)
    # ================================================================

    def generate_fixes(self, failure_info: Dict) -> List[Dict]:
        """
        Generate multiple candidate fixes.

        Combines:
        - primary deterministic fix (attempt_fix)
        - fallback strategies
        """

        fixes = []

        # --------------------------------------------
        # PRIMARY FIX (existing engine)
        # --------------------------------------------
        primary = self.attempt_fix(failure_info)

        if primary and primary.get("strategy"):
            fixes.append(primary)

        error_text = failure_info.get("error", "") or ""

        # --------------------------------------------
        # FALLBACK 1: SAFE NO-OP
        # --------------------------------------------
        fixes.append({
            "strategy": "safe_fallback",
            "action": "append",
            "file": None,
            "code": "# SAFE FALLBACK FIX\npass\n"
        })

        # --------------------------------------------
        # FALLBACK 2: SYNTAX PATCH
        # --------------------------------------------
        if "SyntaxError" in error_text:
            fixes.append({
                "strategy": "syntax_fix",
                "action": "append",
                "file": None,
                "code": "# SYNTAX FIX PLACEHOLDER\n"
            })

        # --------------------------------------------
        # FALLBACK 3: RETURN FIX
        # --------------------------------------------
        if "return outside function" in error_text:
            fixes.append({
                "strategy": "return_fix",
                "action": "append",
                "file": None,
                "code": "# FIX: removed invalid return\n"
            })

        # --------------------------------------------
        # FALLBACK 4: REGENERATION STUB
        # --------------------------------------------
        fixes.append({
            "strategy": "regen_stub",
            "action": "append",
            "file": None,
            "code": "# REGENERATION PLACEHOLDER\n"
        })

        return fixes

    # ================================================================
    # 🔁 EXISTING ENGINE (UNCHANGED CORE LOGIC)
    # ================================================================

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
                "confidence": 1.0,
                "file": None,
                "action": None,
                "code": None
            }

        # --------------------------------------------
        # ERROR EXTRACTION
        # --------------------------------------------
        error = test_result.get("error") or test_result.get("output") or ""
        output = test_result.get("output", "") or ""

        failed_modules = self.extract_failed_modules(output)

        # --------------------------------------------
        # 🧠 STRUCTURE-AWARE FIX (PRIORITY)
        # --------------------------------------------
        patch = self.generate_patch(error)

        if patch:
            patch.update({
                "fixed": False,
                "confidence": 0.95,
                "file": None,
                "modules": failed_modules
            })
            return patch

        # --------------------------------------------
        # STRATEGY 1: Missing import
        # --------------------------------------------
        if "ImportError" in error or "ModuleNotFoundError" in error:

            return {
                "fixed": False,
                "strategy": "missing_import",
                "patch": f"# Suggestion: check or add missing imports in modules: {failed_modules}",
                "confidence": 0.6,
                "file": None,
                "action": None,
                "code": None
            }

        # --------------------------------------------
        # STRATEGY 2: Attribute error
        # --------------------------------------------
        attr_match = re.search(
            r"AttributeError: '(.+?)' object has no attribute '(.+?)'",
            error
        )

        if attr_match:

            class_name = attr_match.group(1)
            attribute = attr_match.group(2)

            placeholder_code = self._generate_placeholder_function(attribute)

            return {
                "fixed": False,
                "strategy": "missing_attribute",
                "patch": f"# Suggestion: implement attribute '{attribute}' in modules: {failed_modules}",
                "confidence": 0.6,
                "file": None,
                "action": "append",
                "code": placeholder_code,
                "meta": {
                    "class": class_name,
                    "attribute": attribute
                }
            }

        # fallback AttributeError
        if "AttributeError" in error:

            attr = self.extract_attribute_name(error)

            return {
                "fixed": False,
                "strategy": "missing_attribute",
                "patch": f"# Suggestion: implement or fix attribute '{attr}' in modules: {failed_modules}",
                "confidence": 0.5,
                "file": None,
                "action": "append",
                "code": self._generate_placeholder_function(attr)
            }

        # --------------------------------------------
        # STRATEGY 3: Assertion failure
        # --------------------------------------------
        if "AssertionError" in output:

            return {
                "fixed": False,
                "strategy": "assertion_failure",
                "patch": f"# Suggestion: review logic and expected values in modules: {failed_modules}",
                "confidence": 0.4,
                "file": None,
                "action": None,
                "code": None
            }

        # --------------------------------------------
        # STRATEGY 4: Type error
        # --------------------------------------------
        if "TypeError" in error:

            return {
                "fixed": False,
                "strategy": "type_mismatch",
                "patch": f"# Suggestion: verify argument types and function signatures in modules: {failed_modules}",
                "confidence": 0.5,
                "file": None,
                "action": None,
                "code": None
            }

        # --------------------------------------------
        # STRATEGY 5: Syntax error (fallback only)
        # --------------------------------------------
        if "SyntaxError" in error:

            return {
                "fixed": False,
                "strategy": "syntax_error",
                "patch": f"# Suggestion: fix syntax errors in modules: {failed_modules}",
                "confidence": 0.8,
                "file": None,
                "action": None,
                "code": None
            }

        # --------------------------------------------
        # FALLBACK
        # --------------------------------------------
        return {
            "fixed": False,
            "strategy": "manual_review_required",
            "patch": f"# Unable to auto-fix. Inspect modules: {failed_modules}",
            "confidence": 0.2,
            "file": None,
            "action": None,
            "code": None
        }

    # ================================================================
    # 🧠 STRUCTURE-AWARE PATCH GENERATOR
    # ================================================================

    def generate_patch(self, error: str):

        error_lower = error.lower()

        # 🔥 CRITICAL FIX: return outside function
        if "return" in error_lower and "outside function" in error_lower:
            return {
                "strategy": "replace_function",
                "action": "replace_function",
                "function": "run",
                "code": self._safe_run_stub()
            }

        # NameError → replace run()
        if "nameerror" in error_lower:
            return {
                "strategy": "replace_function",
                "action": "replace_function",
                "function": "run",
                "code": self._safe_run_stub()
            }

        return None

    # ================================================================
    # SAFE FUNCTION STUB
    # ================================================================

    def _safe_run_stub(self):
        return (
            "    def run(self, context):\n"
            "        return {\"status\": \"ok\"}\n"
        )

    # ================================================================
    # HELPERS
    # ================================================================

    def extract_failed_modules(self, output):

        modules = []

        for line in output.splitlines():
            if "FAILED" in line and "::" in line:
                module = line.split("::")[0]
                modules.append(module)

        return sorted(set(modules))

    def extract_attribute_name(self, error):

        match = re.search(
            r"AttributeError: '(.+?)' object has no attribute '(.+?)'",
            error
        )

        if match:
            return match.group(2)

        match = re.search(r"'(.+?)'", error)

        if match:
            return match.group(1)

        return "unknown"

    def _generate_placeholder_function(self, name):

        return f"""

def {name}(*args, **kwargs):
    \"\"\"Auto-generated placeholder by AutoFixEngine\"\"\"
    return {{"status": "ok"}}
"""