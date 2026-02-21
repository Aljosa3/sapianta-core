from pathlib import Path
from typing import Iterable

from runtime.module_admission import enforce_module_admission


def discover_modules(modules_root: Path) -> Iterable[Path]:
    """
    Discovers admissible modules under /modules.

    Only modules that pass Module Builder admission
    are yielded further into the runtime.

    Fail-fast by design.
    """

    if not modules_root.is_dir():
        return []

    for entry in sorted(modules_root.iterdir()):
        if not entry.is_dir():
            continue

        # HARD GOVERNANCE BOUNDARY
        enforce_module_admission(entry)

        yield entry
