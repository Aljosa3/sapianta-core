"""
SAPIANTA Development Sandbox Runner

Purpose:
Execute development tasks inside an isolated environment
before integration into the main system.

Flow:

AI generated code
    ↓
sandbox execution
    ↓
test validation
    ↓
approval or rejection
"""

import subprocess
import tempfile
import os


class DevSandboxRunner:
    """
    Executes Python code safely in a temporary sandbox.
    """

    def run_code(self, code: str) -> dict:
        """
        Execute Python code inside a temporary sandbox file.
        """

        with tempfile.TemporaryDirectory() as tmpdir:

            file_path = os.path.join(tmpdir, "sandbox_test.py")

            with open(file_path, "w") as f:
                f.write(code)

            try:
                result = subprocess.run(
                    ["python3", file_path],
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                return {
                    "status": "success" if result.returncode == 0 else "error",
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                }

            except subprocess.TimeoutExpired:

                return {
                    "status": "timeout",
                    "stdout": "",
                    "stderr": "execution timeout",
                }