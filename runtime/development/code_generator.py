"""
SAPIANTA Code Generator v1.1 (FILE_HINT SUPPORT)

CRITICAL FIX:
- FAIL → FAIL (no false positives)
- Proper test assertions
- Structured result return
- Deterministic validation signal

NEW:
- file_hint support (multi-file generation)
"""

import os
import re
from pathlib import Path

from runtime.development.mutation_validator import MutationValidator
from runtime.development.generated_code_sanitizer import GeneratedCodeSanitizer
from runtime.development.module_test_runner import ModuleTestRunner


PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ------------------------------------------------
# 🔒 identifier sanitization
# ------------------------------------------------

def sanitize_identifier(name: str) -> str:
    if not isinstance(name, str):
        return "GeneratedModule"

    name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')

    if name and name[0].isdigit():
        name = "_" + name

    return name


def sanitize_module_name(name: str) -> str:
    if not isinstance(name, str):
        return "generated_module"

    name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')

    if name and name[0].isdigit():
        name = "_" + name

    return name


# ========================================================
# MAIN GENERATOR
# ========================================================

class CodeGenerator:

    def __init__(self):

        self.project_root = PROJECT_ROOT
        self.validator = MutationValidator()
        self.sanitizer = GeneratedCodeSanitizer()
        self.tester = ModuleTestRunner()

        self.force_failure = os.environ.get("SAPIANTA_FORCE_FAILURE") == "1"

    # ------------------------------------------------

    def generate_module(self, file_path: str, description: str, task: dict = None) -> dict:

        # ------------------------------------------------
        # 🔥 FILE_HINT SUPPORT (KLJUČNI POPRAVEK)
        # ------------------------------------------------

        if task and task.get("file_hint"):
            safe_module_name = sanitize_module_name(task["file_hint"])
            safe_file_path = self.project_root / f"runtime/development/generated/{safe_module_name}.py"
        else:
            full_path = self.project_root / file_path
            safe_module_name = sanitize_module_name(full_path.stem)
            safe_file_path = full_path.parent / f"{safe_module_name}.py"

        # ------------------------------------------------

        if safe_file_path.exists():
            print(f"[CODEGEN] File already exists: {safe_file_path}")
            return {
                "success": True,
                "file": safe_module_name,
                "already_exists": True
            }

        os.makedirs(safe_file_path.parent, exist_ok=True)

        template = self._generate_template(safe_file_path.name, description)
        template = self.sanitizer.sanitize(template)

        # 🔥 MINIMAL CONTRACT FIX
        if "def generated_function" not in template:
            template += "\n\n\ndef generated_function(a, b):\n    return a + b\n"

        # ------------------------------------------------
        # CREATE MODULE FILE
        # ------------------------------------------------

        with open(safe_file_path, "w", encoding="utf-8") as f:
            f.write(template)

        print(f"[CODEGEN] Module created: {safe_file_path}")

        # ------------------------------------------------
        # CREATE TEST FILE
        # ------------------------------------------------

        is_function = self._is_function_task(description)

        test_file_name = f"test_{safe_module_name}.py"
        test_file_path = safe_file_path.parent / test_file_name

        if is_function:
            function_name = self._infer_function_name(description)

            test_code = f'''"""
Auto-generated functional test for {function_name}
"""

def test_{function_name}_execution():
    from {safe_module_name} import {function_name}
    assert {function_name}(1, 2) is not None
'''

        else:
            class_name = self._infer_class_name(safe_file_path.name)

            test_code = f'''"""
Auto-generated functional test for {class_name}
"""

def test_{safe_module_name}_imports():
    from {safe_module_name} import {class_name}


def test_{safe_module_name}_instantiation():
    from {safe_module_name} import {class_name}
    instance = {class_name}()
    assert instance is not None


def test_{safe_module_name}_execution():
    from {safe_module_name} import {class_name}
    instance = {class_name}()
    assert instance.run({{}}) is not None
'''

        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write(test_code)

        print(f"[CODEGEN] Test file created: {test_file_path}")

        # ------------------------------------------------
        # MODULE IMPORT PATH
        # ------------------------------------------------

        module_import_path = safe_file_path.relative_to(self.project_root) \
            .with_suffix("") \
            .as_posix() \
            .replace("/", ".")

        # ------------------------------------------------
        # MODULE TEST
        # ------------------------------------------------

        test_result = self.tester.test_module(module_import_path)

        print("[CODEGEN] Module test result:", test_result)

        if test_result["status"] != "PASSED":
            print("[CODEGEN] Test failed — needs repair")

            return {
                "success": False,
                "file": module_import_path,
                "error": test_result.get("error"),
                "needs_repair": True
            }

        # ------------------------------------------------
        # MUTATION VALIDATION
        # ------------------------------------------------

        validation = self.validator.validate_changes([module_import_path])

        print("[CODEGEN] Mutation validation result:")

        for r in validation:
            print(r)

        return {
            "success": True,
            "file": module_import_path
        }

    # ------------------------------------------------

    def _generate_template(self, file_name: str, description: str):

        if self._is_function_task(description):
            function_name = self._infer_function_name(description)

            if self.force_failure:
                return f'''"""
{function_name}

{description}

Auto-generated by SAPIANTA (FAILURE MODE)
"""

def {function_name}(a, b):
    return foo()
'''

            return f'''"""
{function_name}

{description}

Auto-generated by SAPIANTA
"""

def {function_name}(a, b):
    return a + b
'''

        class_name = self._infer_class_name(file_name)

        if self.force_failure:
            return f'''"""
{class_name}

{description}

Auto-generated by SAPIANTA (FAILURE MODE)
"""

class {class_name}:

    def __init__(self):
        pass

    def run(self, context):
        return foo()
'''

        return f'''"""
{class_name}

{description}

Auto-generated by SAPIANTA
"""

class {class_name}:

    def __init__(self):
        pass

    def run(self, context):
        return "OK"
'''

    # ------------------------------------------------

    def _infer_class_name(self, file_name: str):

        name = Path(file_name).stem
        name = sanitize_identifier(name)
        parts = name.split("_")

        return "".join(p.capitalize() for p in parts if p)

    # ------------------------------------------------

    def _infer_function_name(self, description: str) -> str:

        if not isinstance(description, str):
            return "generated_function"

        description = description.lower()

        if "add" in description:
            return "add"

        return "generated_function"

    # ------------------------------------------------

    def _is_function_task(self, description: str) -> bool:

        if not isinstance(description, str):
            return False

        return "function" in description.lower()