"""
SAPIANTA Auto-Fix Engine

C + D + E (REGISTRY) + PHASE 3 UPGRADE

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
from runtime.development.integrity_validator import IntegrityValidator


class AutoFixEngine:

    PROJECT_ROOT = Path(".")

    def __init__(self):
        self.registry = FunctionRegistry(self.PROJECT_ROOT)
        self.validator = IntegrityValidator()
        try:
            self.registry.build()
        except Exception:
            self.registry = None  # fail-safe

    # ================================================================
    # MAIN ENGINE
    # ================================================================

    def generate_fixes(self, failure_info: Dict) -> List[Dict]:

        fixes: List[Dict] = []

        system_context = failure_info.get("system_context") or {}
        context_fixes = []

        error_text = failure_info.get("error", "") or ""
        file_path = self._extract_file_from_traceback(error_text)

        # =====================================================
        # ERROR PARSING
        # =====================================================

        error_type, message, traceback = self._parse_error(failure_info)

        # =====================================================
        # CONTEXT FIXES (REGISTRY)
        # =====================================================

        try:
            for module_name in system_context.get("missing_imports", []):
                context_fixes.append({
                    "fixed": False,
                    "strategy": "context_import_fix",
                    "confidence": 0.95,
                    "file": file_path,
                    "action": "append_import",
                    "code": f"import {module_name}\n"
                })

            for func_name in system_context.get("missing_functions", []):

                found_module = None

                if self.registry:
                    found_module = self.registry.find_function(func_name)

                if not found_module:
                    found_module = self._find_function_in_project(func_name)

                if found_module:
                    context_fixes.append({
                        "fixed": False,
                        "strategy": "smart_import_function",
                        "confidence": 0.98 if self.registry else 0.9,
                        "file": file_path,
                        "action": "append_import",
                        "code": f"from {found_module} import {func_name}\n"
                    })
                else:
                    context_fixes.append({
                        "fixed": False,
                        "strategy": "context_function_stub",
                        "confidence": 0.9,
                        "file": file_path,
                        "action": "append_stub",
                        "function": func_name,
                        "code": self._generate_stub_function(func_name)
                    })

        except Exception:
            pass

        # =====================================================
        # DIRECT ERROR FIXES
        # =====================================================

        # NAME ERROR
        if error_type == "NameError":
            match = re.search(r"name '(.+?)' is not defined", message)
            if match:
                missing_name = match.group(1)

                fixes.append({
                    "fixed": False,
                    "strategy": "name_error_stub",
                    "confidence": 0.9,
                    "file": file_path,
                    "action": "append_stub",
                    "function": missing_name,
                    "code": self._generate_stub_function(missing_name)
                })

        # IMPORT ERROR
        if error_type in ["ImportError", "ModuleNotFoundError"]:
            match = re.search(r"No module named '(.+?)'", message)
            if match:
                module_name = match.group(1)

                fixes.append({
                    "fixed": False,
                    "strategy": "import_fix",
                    "confidence": 0.8,
                    "file": file_path,
                    "action": "prepend_import",
                    "code": f"import {module_name}\n"
                })

        # SYNTAX ERROR
        if error_type == "SyntaxError":
            syntax_fix = self._generate_syntax_fix(failure_info)
            if syntax_fix:
                syntax_fix.update({
                    "fixed": False,
                    "confidence": 0.85
                })
                fixes.append(syntax_fix)

        # =====================================================
        # PRIMARY ENGINE
        # =====================================================

        primary = self.attempt_fix(failure_info)
        if primary and primary.get("strategy"):
            fixes.append(primary)

        # =====================================================
        # SAFE FALLBACK (ALWAYS INCLUDED)
        # =====================================================

        fixes.append({
            "fixed": False,
            "strategy": "safe_fallback",
            "confidence": 0.1,
            "file": file_path,
            "action": "append",
            "code": "# SAFE FALLBACK FIX\npass\n"
        })

        # =====================================================
        # PRIORITY: CONTEXT FIRST
        # =====================================================

        if context_fixes:
            fixes = context_fixes + fixes

        # =====================================================
        # 🔥 VALIDATION FIX (CRITICAL PATCH)
        # =====================================================

        validated = []
        fallback_buffer = []

        for fix in fixes:
            try:
                validated_fix = self.validator.validate_fix(fix)
                validated.append(validated_fix)
            except Exception:
                fallback_buffer.append(fix)

        # če validator pobriše vse → uporabi fallback
        if not validated:
            validated = fallback_buffer

        # hard fallback (garancija)
        if not validated:
            validated = [{
                "fixed": False,
                "strategy": "safe_fallback",
                "confidence": 0.01,
                "file": None,
                "action": "append",
                "code": "# HARD FALLBACK\npass\n"
            }]

        return self._deduplicate_fixes(validated)

    # ================================================================
    # ERROR PARSER
    # ================================================================

    def _parse_error(self, failure_info: Dict):

        error_text = failure_info.get("error", "") or ""

        if "NameError" in error_text:
            return "NameError", error_text, error_text

        if "ModuleNotFoundError" in error_text:
            return "ModuleNotFoundError", error_text, error_text

        if "ImportError" in error_text:
            return "ImportError", error_text, error_text

        if "SyntaxError" in error_text:
            return "SyntaxError", error_text, error_text

        return "Unknown", error_text, error_text

    # ================================================================
    # HELPERS
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

    def attempt_fix(self, test_result):

        if test_result.get("success"):
            return {
                "fixed": False,
                "strategy": None,
                "confidence": 1.0,
                "file": None,
                "action": None,
                "code": None
            }

        return {
            "fixed": False,
            "strategy": "manual_review_required",
            "confidence": 0.2,
            "file": None,
            "action": None,
            "code": None
        }

    def _generate_syntax_fix(self, failure_info: Dict) -> Optional[Dict]:

        error_text = failure_info.get("error", "") or ""

        if "SyntaxError" not in error_text:
            return None

        file_path = self._extract_file_from_traceback(error_text)

        return {
            "strategy": "syntax_fix",
            "action": "append",
            "file": file_path,
            "code": "# SYNTAX FIX PLACEHOLDER\n"
        }

    def _extract_file_from_traceback(self, error_text: str) -> Optional[str]:

        file_match = re.search(r'File "(.+?)", line', error_text)
        if not file_match:
            return None

        return file_match.group(1)

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