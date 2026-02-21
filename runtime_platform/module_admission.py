from pathlib import Path
from typing import Dict, Any


class ModuleAdmissionError(RuntimeError):
    """
    Raised when a module or draft fails admission or preflight checks.
    """
    pass


def enforce_module_admission(module_dir: Path) -> None:
    """
    Enforces MODULE_ADMISSION_ENFORCEMENT governance rule.

    A module is admissible if and only if:
    - it is a directory
    - it resides under /modules (enforced by caller)
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


def preflight_draft_check(draft: Dict[str, Any]) -> None:
    """
    Pre-write safety check for Claude-generated module drafts.

    This function runs BEFORE any filesystem write.
    It does NOT replace enforce_module_admission().

    Purpose:
    - block forbidden file types
    - block forbidden target paths
    - block illegal architectural imports

    Fail-fast. No correction. No fallback.
    """

    # --- structural sanity check ---
    if "files" not in draft or not isinstance(draft["files"], dict):
        raise ModuleAdmissionError(
            "Draft rejected: missing or invalid 'files' section"
        )

    files = draft["files"]

    for path, content in files.items():

        # --- type safety ---
        if not isinstance(path, str) or not isinstance(content, str):
            raise ModuleAdmissionError(
                f"Draft rejected: invalid file entry ({path})"
            )

        # --- forbidden file types ---
        if path.endswith(".md"):
            raise ModuleAdmissionError(
                f"Draft rejected: markdown file generation is forbidden ({path})"
            )

        # --- forbidden target paths ---
        if path.startswith(("runtime/", "governance/")):
            raise ModuleAdmissionError(
                f"Draft rejected: forbidden target path ({path})"
            )

        # --- illegal architectural imports ---
        if (
            "import wiring" in content
            or "from runtime.wiring" in content
            or "import runtime.wiring" in content
        ):
            raise ModuleAdmissionError(
                f"Draft rejected: illegal wiring import in {path}"
            )
