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
import json
import re
from pathlib import Path


class TestRunResult:

    def __init__(self):
        self.tests_total = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.failed_modules = []
        self.execution_time = 0.0
        self.test_files = 0
        self.coverage_potential = 0.0


class TestRunner:

    def __init__(self, project_root="."):
        self.project_root = Path(project_root)

    def run_tests(self):

        start = time.time()

        cmd = [
            "pytest",
            "-q",
            "--disable-warnings",
            "--maxfail=50"
        ]

        result = subprocess.run(
            cmd,
            cwd=self.project_root,
            capture_output=True,
            text=True
        )

        end = time.time()

        diagnostics = self.collect_results(result.stdout, result.stderr)

        diagnostics.execution_time = round(end - start, 3)

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

        # simple heuristic

        return round(
            result.tests_passed / max(result.test_files, 1),
            2
        )

    def to_dict(self, diagnostics):

        return {
            "tests_total": diagnostics.tests_total,
            "tests_passed": diagnostics.tests_passed,
            "tests_failed": diagnostics.tests_failed,
            "failed_modules": diagnostics.failed_modules,
            "execution_time": diagnostics.execution_time,
            "test_files": diagnostics.test_files,
            "coverage_potential": diagnostics.coverage_potential
        }

    def print_summary(self, diagnostics):

        data = self.to_dict(diagnostics)

        print("\nSAPIANTA Test Runner")
        print("--------------------")

        print("Total tests:", data["tests_total"])
        print("Passed:", data["tests_passed"])
        print("Failed:", data["tests_failed"])
        print("Execution time:", data["execution_time"], "s")
        print("Coverage potential:", data["coverage_potential"])

        if data["failed_modules"]:
            print("\nFailed modules:")

            for m in data["failed_modules"]:
                print(" -", m)


if __name__ == "__main__":

    runner = TestRunner(".")

    diagnostics = runner.run_tests()

    runner.print_summary(diagnostics)