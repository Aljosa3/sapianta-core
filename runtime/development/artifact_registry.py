"""
SAPIANTA Artifact Registry (DETERMINISTIC, SINGLE SOURCE OF TRUTH)

Purpose:
- eliminate runtime content scanning
- enforce explicit artifact typing
- provide deterministic file classification
"""

import json
from pathlib import Path
from typing import Dict, Optional


class ArtifactRegistry:

    REGISTRY_PATH = Path("runtime/development/artifacts.json")

    def __init__(self):
        self._data: Dict[str, str] = {}
        self._load()

    # ======================
    # LOAD / SAVE
    # ======================

    def _load(self):
        if self.REGISTRY_PATH.exists():
            try:
                self._data = json.loads(self.REGISTRY_PATH.read_text())
            except Exception:
                # FAIL-CLOSED
                self._data = {}
        else:
            self._data = {}

    def _save(self):
        self.REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.REGISTRY_PATH.write_text(json.dumps(self._data, indent=2, sort_keys=True))

    # ======================
    # PUBLIC API
    # ======================

    def register(self, file_path: str, artifact_type: str):
        """
        Deterministic write-time registration
        """
        # 🔥 NORMALIZE PATH (CRITICAL FOR CONSISTENCY)
        file_path = str(Path(file_path).resolve())

        self._data[file_path] = artifact_type
        self._save()

    def get_type(self, file_path: str) -> Optional[str]:
        # 🔥 NORMALIZE PATH (CONSISTENCY)
        file_path = str(Path(file_path).resolve())

        return self._data.get(file_path)

    def require_type(self, file_path: str) -> str:
        """
        FAIL-CLOSED access (with backward compatibility)
        """

        # 🔥 NORMALIZE PATH (CRITICAL)
        file_path = str(Path(file_path).resolve())

        if file_path in self._data:
            return self._data[file_path]

        # =====================================================
        # 🔥 BACKWARD COMPATIBILITY (ONE-TIME AUTO-REGISTER)
        # =====================================================
        try:
            content = Path(file_path).read_text(encoding="utf-8")

            if "# SAPIANTA_TYPE: TEST" in content:
                detected = "TEST"
            elif "# SAPIANTA_TYPE: MODULE" in content:
                detected = "MODULE"
            else:
                raise RuntimeError

            # 🔥 AUTO-REGISTER (deterministic upgrade path)
            self.register(file_path, detected)

            return detected

        except Exception:
            raise RuntimeError(f"[ARTIFACT_REGISTRY] Missing type for: {file_path}")


# Singleton (safe, deterministic)
artifact_registry = ArtifactRegistry()