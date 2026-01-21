from pathlib import Path
import shutil
import pytest

from runtime.wiring.runtime_wiring import RuntimeWiring
from runtime.module_admission import ModuleAdmissionError


def test_runtime_rejects_module_without_builder_manifest(tmp_path, monkeypatch):
    """
    Runtime MUST fail-fast if any module under /modules
    does not contain .module_builder_manifest.
    """

    # Create temporary /modules directory
    modules_root = tmp_path / "modules"
    modules_root.mkdir()

    # Create a fake module WITHOUT manifest
    bad_module = modules_root / "bad_module"
    bad_module.mkdir()

    # Monkeypatch working directory so runtime sees tmp modules/
    monkeypatch.chdir(tmp_path)

    # Runtime initialization MUST fail
    with pytest.raises(ModuleAdmissionError):
        RuntimeWiring()
