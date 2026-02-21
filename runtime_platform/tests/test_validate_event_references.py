import subprocess
import tempfile
from pathlib import Path


# Absolute path to validator
PROJECT_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = PROJECT_ROOT / "scripts/validation/validate_event_references.py"


def run_validator(cwd: Path):
    return subprocess.run(
        ["python3", str(VALIDATOR)],
        cwd=cwd,
        capture_output=True,
        text=True,
    )


def test_validator_fails_on_unknown_event():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        (tmp_path / "governance/registry").mkdir(parents=True)

        (tmp_path / "governance/registry/EVENT_REGISTRY_v0.1.json").write_text(
            '{"events":[{"id":"EVT_ALLOWED"}]}',
            encoding="utf-8"
        )

        (tmp_path / "runtime.py").write_text(
            'event = "EVT_UNKNOWN"\n',
            encoding="utf-8"
        )

        result = run_validator(tmp_path)

        assert result.returncode != 0
        assert "FAIL" in result.stdout


def test_validator_passes_on_allowed_event():
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        (tmp_path / "governance/registry").mkdir(parents=True)

        (tmp_path / "governance/registry/EVENT_REGISTRY_v0.1.json").write_text(
            '{"events":[{"id":"EVT_ALLOWED"}]}',
            encoding="utf-8"
        )

        (tmp_path / "runtime.py").write_text(
            'event = "EVT_ALLOWED"\n',
            encoding="utf-8"
        )

        result = run_validator(tmp_path)

        assert result.returncode == 0
        assert "PASS" in result.stdout
