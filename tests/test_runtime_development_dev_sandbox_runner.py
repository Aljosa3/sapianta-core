from runtime.development.dev_sandbox_runner import DevSandboxRunner


def test_sandbox_executes_code():

    runner = DevSandboxRunner()

    code = """
print("sandbox works")
"""

    result = runner.run_code(code)

    assert result["status"] == "success"
    assert "sandbox works" in result["stdout"]


def test_sandbox_timeout():

    runner = DevSandboxRunner()

    code = """
while True:
    pass
"""

    result = runner.run_code(code)

    assert result["status"] == "timeout"