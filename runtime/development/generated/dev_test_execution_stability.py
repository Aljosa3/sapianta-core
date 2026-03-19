import subprocess
import time
import os

from runtime.development.test_runner import TestRunner


def count_python_processes():
    result = subprocess.run(
        ["ps", "-eo", "comm"],
        capture_output=True,
        text=True
    )
    return result.stdout.count("python")


def test_no_process_leak():

    before = count_python_processes()

    runner = TestRunner(".", timeout=5)
    diagnostics = runner.run_tests()

    time.sleep(1)  # allow OS cleanup

    after = count_python_processes()

    assert diagnostics.return_code is not None
    assert after <= before + 1  # allow main process only


def test_runner_returns_result():

    runner = TestRunner(".", timeout=5)
    diagnostics = runner.run_tests()

    assert isinstance(diagnostics.success, bool)
    assert diagnostics.execution_time > 0