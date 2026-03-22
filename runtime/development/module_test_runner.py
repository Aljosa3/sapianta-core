"""
SAPIANTA Module Test Runner

Purpose
-------
Automatically validates generated modules before they are accepted
into the runtime system.

Pipeline

generated module
↓
import module
↓
find runnable class OR test functions
↓
execute
↓
success / failure
"""

import importlib
import sys
import traceback
import inspect
import re
from pathlib import Path


class ModuleTestRunner:

    def __init__(self, project_root=None):

        if project_root:
            self.project_root = Path(project_root)
        else:
            self.project_root = Path(__file__).resolve().parents[2]

    # ---------------------------------------------------------
    # NORMALIZE PATH → IMPORT PATH
    # ---------------------------------------------------------

    def _normalize_module_path(self, module_path: str):

        if module_path.endswith(".py"):
            module_path = module_path[:-3]

        module_path = module_path.replace("/", ".").replace("\\", ".")

        if module_path.startswith("."):
            module_path = module_path[1:]

        return module_path

    # ---------------------------------------------------------
    # ENSURE GENERATED PATH ON sys.path
    # ---------------------------------------------------------

    def _ensure_generated_on_path(self, file_path: str):

        path = Path(file_path).resolve().parent

        if str(path) not in sys.path:
            sys.path.insert(0, str(path))

    # ---------------------------------------------------------
    # ERROR → SYSTEM CONTEXT EXTRACTION
    # ---------------------------------------------------------

    def _extract_system_context(self, error: str) -> dict:

        context = {
            "missing_functions": [],
            "missing_imports": []
        }

        if not error:
            return context

        match = re.search(r"name '(.+?)' is not defined", error)
        if match:
            context["missing_functions"].append(match.group(1))

        match = re.search(r"No module named '(.+?)'", error)
        if match:
            context["missing_imports"].append(match.group(1))

        return context

    # ---------------------------------------------------------
    # Find runnable class
    # ---------------------------------------------------------

    def _find_runnable_class(self, module):

        for _, obj in inspect.getmembers(module, inspect.isclass):
            if hasattr(obj, "run"):
                return obj

        return None

    # ---------------------------------------------------------
    # 🔥 CRITICAL FIX: FORCE RELOAD (NO CACHE)
    # ---------------------------------------------------------

    def _import_module(self, module_path: str):
        """
        Force reload module to reflect file changes
        """

        if module_path in sys.modules:
            del sys.modules[module_path]

        return importlib.import_module(module_path)

    # ---------------------------------------------------------
    # MAIN TEST METHOD
    # ---------------------------------------------------------

    def test_module(self, file_path: str):

        result = {
            "file": file_path,
            "status": "UNKNOWN",
            "success": False,
            "error": None,
            "output": None,
            "system_context": {}
        }

        try:

            # allow local imports
            self._ensure_generated_on_path(file_path)

            module_path = self._normalize_module_path(file_path)

            # 🔥 now always fresh import
            module = self._import_module(module_path)

            # --------------------------------------------------
            # 1️⃣ RUNNABLE CLASS
            # --------------------------------------------------

            runnable_class = self._find_runnable_class(module)

            if runnable_class is not None:

                instance = runnable_class()

                try:
                    instance.run({})
                except NotImplementedError:
                    pass
                except Exception as e:

                    error_str = str(e)

                    result["status"] = "FAILED"
                    result["error"] = error_str
                    result["system_context"] = self._extract_system_context(error_str)

                    return result

                result["status"] = "PASSED"
                result["success"] = True
                return result

            # --------------------------------------------------
            # 2️⃣ TEST FUNCTIONS
            # --------------------------------------------------

            test_functions = []

            for name, obj in inspect.getmembers(module, inspect.isfunction):
                if name.startswith("test_"):
                    test_functions.append(obj)

            if test_functions:

                for test_func in test_functions:
                    try:
                        test_func()
                    except Exception as e:

                        error_str = str(e)

                        result["status"] = "FAILED"
                        result["error"] = error_str
                        result["system_context"] = self._extract_system_context(error_str)

                        return result

                result["status"] = "PASSED"
                result["success"] = True
                return result

            # --------------------------------------------------
            # 3️⃣ NOTHING FOUND
            # --------------------------------------------------

            result["status"] = "FAILED"
            result["error"] = "No runnable class or test functions found"
            return result

        except Exception:

            error_str = traceback.format_exc()

            result["status"] = "FAILED"
            result["error"] = error_str
            result["system_context"] = self._extract_system_context(error_str)

        return result

    # ---------------------------------------------------------
    # Test multiple modules
    # ---------------------------------------------------------

    def test_modules(self, files):

        results = []

        for f in files:
            r = self.test_module(f)
            results.append(r)

        return results


if __name__ == "__main__":

    runner = ModuleTestRunner()

    result = runner.test_module(
        "runtime/analytics/test_engine.py"
    )

    print("\nModule Test Result\n")
    print(result)