"""
SAPIANTA Test Runner

Executes pytest programmatically and produces structured diagnostics
for the AI Software Factory (ASF).

Design goals:
- deterministic execution
- governance-compatible
- no side effects outside test execution
- machine-readable diagnostics
"""

import subprocess
import time
import re
from pathlib import Path


class TestRunResult:

    def __init__(self):
        self.success = True
        self.tests_total = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.failed_modules = []
        self.execution_time = 0.0
        self.test_files = 0
        self.coverage_potential = 0.0

        # raw outputs
        self.raw_output = ""
        self.raw_error = ""

        # ✅ NEW
        self.return_code = 0
        self.timeout = False


class TestRunner:

    def __init__(self, project_root=".", timeout=60):
        self.project_root = Path(project_root)
        self.timeout = timeout

    def run_tests(self):

        start = time.time()

        cmd = [
            "pytest",
            "-q",
            "--disable-warnings",
            "--maxfail=50"
        ]

        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            end = time.time()

            diagnostics = self.collect_results(result.stdout, result.stderr)

            diagnostics.execution_time = round(end - start, 3)
            diagnostics.success = result.returncode == 0
            diagnostics.raw_output = result.stdout
            diagnostics.raw_error = result.stderr
            diagnostics.return_code = result.returncode

            return diagnostics

        except subprocess.TimeoutExpired as e:

            end = time.time()

            diagnostics = TestRunResult()

            diagnostics.success = False
            diagnostics.timeout = True
            diagnostics.execution_time = round(end - start, 3)
            diagnostics.raw_output = e.stdout or ""
            diagnostics.raw_error = f"TIMEOUT after {self.timeout}s"
            diagnostics.return_code = -1

            return diagnostics

        except Exception as e:

            end = time.time()

            diagnostics = TestRunResult()

            diagnostics.success = False
            diagnostics.execution_time = round(end - start, 3)
            diagnostics.raw_error = str(e)
            diagnostics.return_code = -2

            return diagnostics

    def collect_results(self, stdout, stderr):

        result = TestRunResult()

        summary_line = None

        for line in stdout.splitlines():
            if "passed" in line or "failed" in line:
                summary_line = line

        if summary_line:

            passed = re.search(r"(\d+)\s+passed", summary_line)
            failed = re.search(r"(\d+)\s+failed", summary_line)

            if passed:
                result.tests_passed = int(passed.group(1))

            if failed:
                result.tests_failed = int(failed.group(1))

        result.tests_total = result.tests_passed + result.tests_failed
        result.failed_modules = self.detect_failed_modules(stdout)
        result.test_files = self.count_test_files()
        result.coverage_potential = self.estimate_coverage(result)

        return result

    def detect_failed_modules(self, stdout):

        failed = []

        for line in stdout.splitlines():
            if "FAILED" in line and "::" in line:

                module = line.split("::")[0]

                module = module.replace("tests/test_", "")
                module = module.replace(".py", "")
                module = module.replace("_", ".")

                failed.append(module)

        return sorted(set(failed))

    def count_test_files(self):

        test_dir = self.project_root / "tests"

        if not test_dir.exists():
            return 0

        return len(list(test_dir.glob("test_*.py")))

    def estimate_coverage(self, result):

        if result.test_files == 0:
            return 0.0

        return round(
            result.tests_passed / max(result.test_files, 1),
            2
        )

    # ✅ NEW: failure extraction (for AutoFixEngine)
    def extract_failures(self, diagnostics):

        lines = diagnostics.raw_output.splitlines()

        failures = [line for line in lines if "FAILED" in line]

        return failures

    def to_dict(self, diagnostics):

        return {
            "success": diagnostics.success,
            "tests_total": diagnostics.tests_total,
            "tests_passed": diagnostics.tests_passed,
            "tests_failed": diagnostics.tests_failed,
            "failed_modules": diagnostics.failed_modules,
            "execution_time": diagnostics.execution_time,
            "coverage_potential": diagnostics.coverage_potential,
            "timeout": diagnostics.timeout,
            "return_code": diagnostics.return_code,
            "raw_error": diagnostics.raw_error[:300]
        }

    def print_summary(self, diagnostics):

        data = self.to_dict(diagnostics)

        print("\nSAPIANTA Test Runner")
        print("--------------------")

        print("Success:", data["success"])
        print("Total tests:", data["tests_total"])
        print("Passed:", data["tests_passed"])
        print("Failed:", data["tests_failed"])
        print("Execution time:", data["execution_time"], "s")
        print("Coverage potential:", data["coverage_potential"])

        if data["timeout"]:
            print("⚠️ TIMEOUT detected")

        if data["failed_modules"]:
            print("\nFailed modules:")
            for m in data["failed_modules"]:
                print(" -", m)

        if not data["success"]:
            print("\nError snippet:")
            print(data["raw_error"])


if __name__ == "__main__":

    runner = TestRunner(".", timeout=60)

    diagnostics = runner.run_tests()

    runner.print_summary(diagnostics)