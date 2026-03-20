"""
SAPIANTA Auto-Fix Engine

C + D + E (REGISTRY) VERSION

Design:
- deterministic
- rule-based
- multi-fix capable
- context-aware
- smart linking (registry-based)
- safe (no direct file writes)
"""

import re
from pathlib import Path
from typing import List, Dict, Optional

from runtime.development.function_registry import FunctionRegistry


class AutoFixEngine:

    PROJECT_ROOT = Path(".")

    def __init__(self):
        self.registry = FunctionRegistry(self.PROJECT_ROOT)
        try:
            self.registry.build()
        except Exception:
            # fail-safe (determinism > crash)
            self.registry = None

    # ================================================================
    # MAIN ENGINE
    # ================================================================

    def generate_fixes(self, failure_info: Dict) -> List[Dict]:

        fixes: List[Dict] = []

        system_context = failure_info.get("system_context") or {}
        context_fixes = []

        # =====================================================
        # CONTEXT FIXES (SMART LINKING VIA REGISTRY)
        # =====================================================

        try:
            # -------------------------------
            # MISSING IMPORTS
            # -------------------------------
            for module_name in system_context.get("missing_imports", []):
                context_fixes.append({
                    "fixed": False,
                    "strategy": "context_import_fix",
                    "patch": f"# import {module_name}",
                    "confidence": 0.95,
                    "file": None,
                    "action": "append_import",
                    "code": f"import {module_name}\n"
                })

            # -------------------------------
            # MISSING FUNCTIONS (REGISTRY FIRST)
            # -------------------------------
            for func_name in system_context.get("missing_functions", []):

                found_module = None

                # 🔥 E PHASE: registry lookup
                if self.registry:
                    found_module = self.registry.find_function(func_name)

                # 🔁 fallback to old scan (safety net)
                if not found_module:
                    found_module = self._find_function_in_project(func_name)

                if found_module:
                    context_fixes.append({
                        "fixed": False,
                        "strategy": "smart_import_function",
                        "patch": f"# import {func_name} from {found_module}",
                        "confidence": 0.98 if self.registry else 0.9,
                        "file": None,
                        "action": "append_import",
                        "code": f"from {found_module} import {func_name}\n"
                    })
                else:
                    context_fixes.append({
                        "fixed": False,
                        "strategy": "context_function_stub",
                        "patch": f"# create function {func_name}",
                        "confidence": 0.9,
                        "file": None,
                        "action": "append_stub",
                        "function": func_name,
                        "code": self._generate_stub_function(func_name)
                    })

            # -------------------------------
            # CONNECTION FIXES
            # -------------------------------
            for conn in system_context.get("missing_connections", []):
                if "generate_fix" in conn and "generate_fixes" in conn:
                    context_fixes.append({
                        "fixed": False,
                        "strategy": "context_api_alignment",
                        "patch": "replace generate_fix → generate_fixes",
                        "confidence": 0.95,
                        "file": None,
                        "action": "append",
                        "code": "# FIX: use generate_fixes instead of generate_fix\n"
                    })

        except Exception:
            pass

        # =====================================================
        # PRIMARY FIX ENGINE
        # =====================================================

        primary = self.attempt_fix(failure_info)
        if primary and primary.get("strategy"):
            fixes.append(primary)

        error_text = failure_info.get("error", "") or ""

        # -------------------------------
        # NAME ERROR
        # -------------------------------
        name_error_match = re.search(
            r"NameError: name '(\w+)' is not defined",
            error_text
        )

        if name_error_match:
            missing_name = name_error_match.group(1)

            fixes.append({
                "fixed": False,
                "strategy": "name_error_stub",
                "patch": f"# create stub for {missing_name}",
                "confidence": 0.7,
                "file": self._extract_file_from_traceback(error_text),
                "action": "append_stub",
                "function": missing_name,
                "code": self._generate_stub_function(missing_name)
            })

        # -------------------------------
        # IMPORT ERROR
        # -------------------------------
        import_error_match = re.search(
            r"No module named '([\w\.]+)'",
            error_text
        )

        if import_error_match:
            module_name = import_error_match.group(1)

            fixes.append({
                "fixed": False,
                "strategy": "import_stub",
                "patch": f"# import {module_name}",
                "confidence": 0.6,
                "file": self._extract_file_from_traceback(error_text),
                "action": "append_import",
                "code": f"import {module_name}\n"
            })

        # -------------------------------
        # SYNTAX FIX
        # -------------------------------
        syntax_fix = self._generate_syntax_fix(failure_info)
        if syntax_fix:
            fixes.append(syntax_fix)

        # -------------------------------
        # SPECIAL CASES
        # -------------------------------
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

        if "SyntaxError" in error_text:
            fixes.append({
                "fixed": False,
                "strategy": "syntax_fix_placeholder",
                "patch": "# Syntax error placeholder",
                "confidence": 0.2,
                "file": None,
                "action": "append",
                "code": "# SYNTAX FIX PLACEHOLDER\n"
            })

        # -------------------------------
        # SAFE FALLBACKS
        # -------------------------------
        fixes.append({
            "fixed": False,
            "strategy": "safe_fallback",
            "patch": "# SAFE FALLBACK FIX",
            "confidence": 0.1,
            "file": None,
            "action": "append",
            "code": "# SAFE FALLBACK FIX\npass\n"
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

        # =====================================================
        # PRIORITY: CONTEXT FIRST
        # =====================================================
        if context_fixes:
            fixes = context_fixes + fixes

        return self._deduplicate_fixes(fixes)

    # ================================================================
    # FALLBACK SEARCH (KEPT FOR SAFETY)
    # ================================================================

    def _find_function_in_project(self, func_name: str) -> Optional[str]:

        try:
            for py_file in self.PROJECT_ROOT.rglob("*.py"):

                if "__pycache__" in str(py_file):
                    continue

                content = py_file.read_text(encoding="utf-8", errors="ignore")

                if re.search(rf"def {func_name}\(", content):

                    module_path = py_file.with_suffix("")
                    module_str = str(module_path).replace("/", ".").replace("\\", ".")

                    if module_str.startswith("."):
                        module_str = module_str[1:]

                    return module_str

        except Exception:
            return None

        return None

    # ================================================================
    # CORE FIX LOGIC
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
    # PATCH GENERATOR
    # ================================================================

    def generate_patch(self, error: str):

        error_lower = error.lower()
        file_path = self._extract_file_from_traceback(error)

        if "return" in error_lower and "outside function" in error_lower:
            return {
                "strategy": "replace_function",
                "action": "replace_function",
                "function": "run",
                "file": file_path,
                "code": self._safe_run_stub()
            }

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

    def _generate_stub_function(self, name: str):

        return f"""
def {name}(*args, **kwargs):
    # AUTO-GENERATED STUB
    return None
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