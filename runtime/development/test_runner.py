"""
SAPIANTA Test Runner

Executes pytest in isolated subprocess and produces structured diagnostics
for the AI Software Factory (ASF).

Design goals:
- deterministic execution
- no process leaks
- full subprocess isolation
- governance-compatible
- machine-readable diagnostics
"""

import subprocess
import time
import re
import sys
import os
import signal
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

        self.raw_output = ""
        self.raw_error = ""

        self.return_code = 0
        self.timeout = False


class TestRunner:

    def __init__(self, project_root=".", timeout=10):
        self.project_root = Path(project_root)
        self.timeout = timeout

        # 🔥 ključna sprememba → eksplicitno test območje
        self.generated_test_path = "runtime/development/generated"

    def run_tests(self):

        start = time.time()

        if os.environ.get("SAPIANTA_TEST_RUNNER") == "1":
            diagnostics = TestRunResult()
            diagnostics.success = False
            diagnostics.raw_error = "Recursive TestRunner invocation prevented"
            diagnostics.return_code = -3
            return diagnostics

        # 🔥 KLJUČNA SPREMEMBA → ciljamo generated teste
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            self.generated_test_path,
            "-v",                         # 👈 boljši output za parsing
            "--maxfail=1",
            "--disable-warnings",
            "--tb=short",
            "-p",
            "no:anyio",
        ]

        env = os.environ.copy()
        env["SAPIANTA_TEST_RUNNER"] = "1"

        process = subprocess.Popen(
            cmd,
            cwd=self.project_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            preexec_fn=os.setsid,
            env=env
        )

        diagnostics = TestRunResult()

        try:
            output, _ = process.communicate(timeout=self.timeout)
            end = time.time()

            diagnostics = self.collect_results(output)
            diagnostics.execution_time = round(end - start, 3)
            diagnostics.success = process.returncode == 0
            diagnostics.raw_output = output
            diagnostics.return_code = process.returncode

            return diagnostics

        except subprocess.TimeoutExpired:

            end = time.time()

            diagnostics.success = False
            diagnostics.timeout = True
            diagnostics.execution_time = round(end - start, 3)
            diagnostics.raw_error = f"TIMEOUT after {self.timeout}s"
            diagnostics.return_code = -1

            try:
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            except Exception:
                pass

            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                except Exception:
                    pass

            return diagnostics

        except Exception as e:

            end = time.time()

            diagnostics.success = False
            diagnostics.execution_time = round(end - start, 3)
            diagnostics.raw_error = str(e)
            diagnostics.return_code = -2

            return diagnostics

        finally:
            if process.poll() is None:
                try:
                    os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                except Exception:
                    pass

    def collect_results(self, stdout):

        result = TestRunResult()

        # 🔥 izboljšan parsing
        for line in stdout.splitlines():

            if "collected" in line:
                match = re.search(r"collected (\d+) items", line)
                if match:
                    result.tests_total = int(match.group(1))

            if "passed" in line or "failed" in line:
                passed = re.search(r"(\d+)\s+passed", line)
                failed = re.search(r"(\d+)\s+failed", line)

                if passed:
                    result.tests_passed = int(passed.group(1))

                if failed:
                    result.tests_failed = int(failed.group(1))

        result.failed_modules = self.detect_failed_modules(stdout)
        result.test_files = self.count_test_files()
        result.coverage_potential = self.estimate_coverage(result)

        return result

    def detect_failed_modules(self, stdout):

        failed = []

        for line in stdout.splitlines():
            if "FAILED" in line and "::" in line:

                module = line.split("::")[0]

                module = module.replace(".py", "")
                module = module.replace("/", ".")
                module = module.replace("\\", ".")

                failed.append(module)

        return sorted(set(failed))

    def count_test_files(self):

        test_dir = self.project_root / self.generated_test_path

        if not test_dir.exists():
            return 0

        return len(list(test_dir.glob("test_*.py")))

    def estimate_coverage(self, result):

        if result.test_files == 0:
            return 0.0

        return round(
            result.tests_passed / max(result.tests_total, 1),
            2
        )

    def extract_failures(self, diagnostics):

        return [
            line for line in diagnostics.raw_output.splitlines()
            if "FAILED" in line
        ]

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

    runner = TestRunner(".", timeout=10)
    diagnostics = runner.run_tests()
    runner.print_summary(diagnostics)