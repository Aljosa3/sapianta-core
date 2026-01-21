from pathlib import Path


class ModuleAdmissionError(RuntimeError):
    """
    Raised when a module fails admission checks.
    """
    pass


def enforce_module_admission(module_dir: Path) -> None:
    """
    Enforces MODULE_ADMISSION_ENFORCEMENT governance rule.

    A module is admissible if and only if:
    - it resides under /modules
    - it contains a .module_builder_manifest file at its root

    This function is fail-fast and has no fallback behavior.
    """

    if not module_dir.is_dir():
        raise ModuleAdmissionError(
            f"Module path is not a directory: {module_dir}"
        )

    manifest_path = module_dir / ".module_builder_manifest"

    if not manifest_path.is_file():
        raise ModuleAdmissionError(
            f"Module rejected (missing Module Builder manifest): {module_dir}"
        )
