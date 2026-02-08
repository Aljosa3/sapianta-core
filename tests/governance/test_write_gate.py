# tests/governance/test_write_gate.py

from pathlib import Path
import shutil
import tempfile

import pytest

from sapianta_chat.governance.write_gate import (
    WriteGate,
    WriteGateDeny,
)


def _create_dummy_module(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    (path / "__init__.py").write_text("# dummy module\n")


def test_write_gate_allow_for_new_module():
    """
    ALLOW:
    - source exists
    - validator PASS
    - target does not exist
    """

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        out_root = tmp / "out" / "modules"
        target_root = tmp / "modules"

        source = out_root / "new_module"
        _create_dummy_module(source)

        target_root.mkdir(parents=True)

        gate = WriteGate(
            artifact="new_module",
            source_path=source,
            target_root=target_root,
            validator_passed=True,
        )

        # Should not raise
        gate.evaluate()


def test_write_gate_deny_if_target_exists():
    """
    DENY:
    - target already exists
    """

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        out_root = tmp / "out" / "modules"
        target_root = tmp / "modules"

        source = out_root / "conflict_module"
        target = target_root / "conflict_module"

        _create_dummy_module(source)
        _create_dummy_module(target)

        gate = WriteGate(
            artifact="conflict_module",
            source_path=source,
            target_root=target_root,
            validator_passed=True,
        )

        with pytest.raises(WriteGateDeny, match="Target already exists"):
            gate.evaluate()


def test_write_gate_deny_if_validator_failed():
    """
    DENY:
    - validator is not PASS
    """

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        out_root = tmp / "out" / "modules"
        target_root = tmp / "modules"

        source = out_root / "invalid_module"
        _create_dummy_module(source)

        target_root.mkdir(parents=True)

        gate = WriteGate(
            artifact="invalid_module",
            source_path=source,
            target_root=target_root,
            validator_passed=False,
        )

        with pytest.raises(WriteGateDeny, match="Validator result is not PASS"):
            gate.evaluate()


def test_write_gate_deny_if_source_missing():
    """
    DENY:
    - source path does not exist
    """

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        target_root = tmp / "modules"
        target_root.mkdir(parents=True)

        gate = WriteGate(
            artifact="missing_module",
            source_path=tmp / "out" / "modules" / "missing_module",
            target_root=target_root,
            validator_passed=True,
        )

        with pytest.raises(WriteGateDeny, match="Source path does not exist"):
            gate.evaluate()
