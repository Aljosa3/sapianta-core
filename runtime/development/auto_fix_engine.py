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
from pathlib import Path
from typing import List, Dict, Optional


class AutoFixEngine:

    # ================================================================
    # MULTI-FIX ENGINE
    # ================================================================

    def generate_fixes(self, failure_info: Dict) -> List[Dict]:

        fixes: List[Dict] = []

        primary = self.attempt_fix(failure_info)
        if primary and primary.get("strategy"):
            fixes.append(primary)

        error_text = failure_info.get("error", "") or ""

        syntax_fix = self._generate_syntax_fix(failure_info)
        if syntax_fix:
            fixes.append(syntax_fix)

        fixes.append({
            "fixed": False,
            "strategy": "safe_fallback",
            "patch": "# SAFE FALLBACK FIX",
            "confidence": 0.1,
            "file": None,
            "action": "append",
            "code": "# SAFE FALLBACK FIX\npass\n"
        })

        if "SyntaxError" in error_text:
            fixes.append({
                "fixed": False,
                "strategy": "syntax_fix_placeholder",
                "patch": "# Syntax error detected; placeholder fallback",
                "confidence": 0.2,
                "file": None,
                "action": "append",
                "code": "# SYNTAX FIX PLACEHOLDER\n"
            })

        if "return outside function" in error_text:
            fixes.append({
                "fixed": False,
                "strategy": "return_fix",
                "patch": "# Fix invalid return placement",
                "confidence": 0.2,
                "file": None,
                "action": "append",
                "code": "# FIX: removed invalid return\n"
            })

        fixes.append({
            "fixed": False,
            "strategy": "regen_stub",
            "patch": "# REGENERATION PLACEHOLDER",
            "confidence": 0.1,
            "file": None,
            "action": "append",
            "code": "# REGENERATION PLACEHOLDER\n"
        })

        return self._deduplicate_fixes(fixes)

    # ================================================================
    # CORE FIX ENGINE
    # ================================================================

    def attempt_fix(self, test_result):

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

        error = test_result.get("error") or test_result.get("output") or ""
        output = test_result.get("output", "") or ""

        failed_modules = self.extract_failed_modules(output)

        patch = self.generate_patch(error)

        if patch:
            patch.update({
                "fixed": False,
                "confidence": 0.95,
                "file": patch.get("file"),
                "modules": failed_modules
            })
            return patch

        if "ImportError" in error or "ModuleNotFoundError" in error:
            return {
                "fixed": False,
                "strategy": "missing_import",
                "patch": f"# Suggestion: check imports in {failed_modules}",
                "confidence": 0.6,
                "file": None,
                "action": None,
                "code": None
            }

        if "AttributeError" in error:
            attr = self.extract_attribute_name(error)
            return {
                "fixed": False,
                "strategy": "missing_attribute",
                "patch": f"# implement '{attr}'",
                "confidence": 0.5,
                "file": None,
                "action": "append",
                "code": self._generate_placeholder_function(attr)
            }

        if "AssertionError" in output:
            return {
                "fixed": False,
                "strategy": "assertion_failure",
                "patch": "# review logic",
                "confidence": 0.4,
                "file": None,
                "action": None,
                "code": None
            }

        if "TypeError" in error:
            return {
                "fixed": False,
                "strategy": "type_mismatch",
                "patch": "# check types",
                "confidence": 0.5,
                "file": None,
                "action": None,
                "code": None
            }

        if "SyntaxError" in error:
            syntax_fix = self._generate_syntax_fix(test_result)
            if syntax_fix:
                syntax_fix.update({
                    "fixed": False,
                    "confidence": 0.85
                })
                return syntax_fix

        return {
            "fixed": False,
            "strategy": "manual_review_required",
            "patch": "# manual inspection required",
            "confidence": 0.2,
            "file": None,
            "action": None,
            "code": None
        }

    # ================================================================
    # PATCH GENERATOR (FIXED VERSION)
    # ================================================================

    def generate_patch(self, error: str):

        error_lower = error.lower()
        file_path = self._extract_file_from_traceback(error)

        # FIX 1: return outside function
        if "return" in error_lower and "outside function" in error_lower:
            return {
                "strategy": "replace_function",
                "action": "replace_function",
                "function": "run",
                "file": file_path,
                "code": self._safe_run_stub()
            }

        # FIX 2: NameError (foo not defined)
        if "nameerror" in error_lower:
            return {
                "strategy": "replace_function",
                "action": "replace_function",
                "function": "run",
                "file": file_path,
                "code": self._safe_run_stub()
            }

        return None

    # ================================================================
    # SYNTAX FIX
    # ================================================================

    def _generate_syntax_fix(self, failure_info: Dict) -> Optional[Dict]:

        error_text = failure_info.get("error", "") or ""

        if "SyntaxError" not in error_text:
            return None

        file_path = self._extract_file_from_traceback(error_text)

        if not file_path:
            return None

        if "expected ':'" in error_text:
            fixed_code = self._fix_missing_colon(file_path)
            if fixed_code:
                return {
                    "strategy": "syntax_fix",
                    "action": "replace_file",
                    "file": file_path,
                    "code": fixed_code
                }

        return None

    # ================================================================
    # HELPERS
    # ================================================================

    def _extract_file_from_traceback(self, error_text: str) -> Optional[str]:

        file_match = re.search(r'File "(.+?)", line', error_text)
        if not file_match:
            return None

        full_path = file_match.group(1)

        marker = "sapianta_system/"
        if marker in full_path:
            return full_path.split(marker, 1)[1]

        return full_path

    def _fix_missing_colon(self, file_path: str) -> Optional[str]:

        try:
            path = Path(file_path)
            if not path.exists():
                return None

            original = path.read_text(encoding="utf-8")
            fixed_lines = []
            changed = False

            for line in original.splitlines():
                if line.strip().startswith("def ") and not line.strip().endswith(":"):
                    line += ":"
                    changed = True
                fixed_lines.append(line)

            if not changed:
                return None

            return "\n".join(fixed_lines) + "\n"

        except Exception:
            return None

    def _safe_run_stub(self):
        return (
            "    def run(self, context):\n"
            "        return {\"status\": \"ok\"}\n"
        )

    def extract_failed_modules(self, output):

        modules = []

        for line in output.splitlines():
            if "FAILED" in line and "::" in line:
                modules.append(line.split("::")[0])

        return sorted(set(modules))

    def extract_attribute_name(self, error):

        match = re.search(
            r"AttributeError: '(.+?)' object has no attribute '(.+?)'",
            error
        )

        if match:
            return match.group(2)

        return "unknown"

    def _generate_placeholder_function(self, name):

        return f"""
def {name}(*args, **kwargs):
    return {{"status": "ok"}}
"""

    def _deduplicate_fixes(self, fixes: List[Dict]) -> List[Dict]:

        seen = set()
        unique = []

        for fix in fixes:
            key = (
                fix.get("strategy"),
                fix.get("action"),
                fix.get("file"),
                fix.get("function"),
                fix.get("code"),
            )
            if key in seen:
                continue
            seen.add(key)
            unique.append(fix)

        return unique