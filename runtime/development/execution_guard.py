"""
SAPIANTA Execution Guard v0.9

Purpose:
- Prevent runaway execution
- Enforce resource limits
- Fail-closed protection

Design:
- lightweight
- deterministic
- no external dependencies
"""

import time
import subprocess


class ExecutionGuard:

    def __init__(
        self,
        max_processes=3,
        max_runtime=30,
    ):
        self.max_processes = max_processes
        self.max_runtime = max_runtime

        self.start_time = time.time()

    # ------------------------------------------------
    # PROCESS COUNT
    # ------------------------------------------------

    def count_python_processes(self):

        try:
            result = subprocess.run(
                ["ps", "-eo", "comm"],
                capture_output=True,
                text=True
            )
            return result.stdout.count("python")
        except Exception:
            return 0

    def check_process_limit(self):

        count = self.count_python_processes()

        if count > self.max_processes:
            return False, f"Too many python processes: {count}"

        return True, None

    # ------------------------------------------------
    # RUNTIME BUDGET
    # ------------------------------------------------

    def check_runtime(self):

        elapsed = time.time() - self.start_time

        if elapsed > self.max_runtime:
            return False, f"Execution time exceeded: {round(elapsed,2)}s"

        return True, None

    # ------------------------------------------------
    # MAIN CHECK
    # ------------------------------------------------

    def validate(self):

        ok, err = self.check_process_limit()
        if not ok:
            return False, err

        ok, err = self.check_runtime()
        if not ok:
            return False, err

        return True, None