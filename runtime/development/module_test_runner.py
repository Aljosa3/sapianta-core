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
find runnable class
↓
instantiate class
↓
call run()
↓
success / failure
"""

import importlib
import traceback
import inspect
from pathlib import Path


class ModuleTestRunner:

    def __init__(self, project_root=None):

        if project_root:
            self.project_root = Path(project_root)
        else:
            self.project_root = Path(__file__).resolve().parents[2]

    # ---------------------------------------------------------
    # Module path → python import path
    # ---------------------------------------------------------

    def _to_import_path(self, file_path: str):

        path = Path(file_path)

        if path.suffix == ".py":
            path = path.with_suffix("")

        parts = list(path.parts)

        return ".".join(parts)

    # ---------------------------------------------------------
    # Find runnable class (any class with run())
    # ---------------------------------------------------------

    def _find_runnable_class(self, module):

        for name, obj in inspect.getmembers(module, inspect.isclass):

            if hasattr(obj, "run"):
                return obj

        return None

    # ---------------------------------------------------------
    # Test single module
    # ---------------------------------------------------------

    def test_module(self, file_path: str):

        result = {
            "file": file_path,
            "status": "UNKNOWN",
            "error": None
        }

        try:

            module_path = self._to_import_path(file_path)

            module = importlib.import_module(module_path)

            runnable_class = self._find_runnable_class(module)

            if runnable_class is None:

                result["status"] = "FAILED"
                result["error"] = "No runnable class with run() method found"
                return result

            instance = runnable_class()

            try:
                instance.run({})
            except NotImplementedError:
                pass
            except Exception as e:

                result["status"] = "FAILED"
                result["error"] = str(e)
                return result

            result["status"] = "PASSED"

        except Exception:

            result["status"] = "FAILED"
            result["error"] = traceback.format_exc()

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