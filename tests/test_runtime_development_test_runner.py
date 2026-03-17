from unittest.mock import patch
from runtime.development.test_runner import TestRunner


def test_runner_executes():

    with patch("subprocess.run") as mock_run:

        mock_run.return_value.returncode = 0

        runner = TestRunner()

        result = runner.run_tests()

        print(result)
        print(type(result))
        print(dir(result))

        assert result is not None