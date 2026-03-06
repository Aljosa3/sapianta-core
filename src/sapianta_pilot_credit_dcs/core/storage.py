from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any

class ArtifactStorage:
    def __init__(self, root_dir: str):
        self.root = Path(root_dir)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path_for(self, artifact_type: str, artifact_hash: str) -> Path:
        d = self.root / artifact_type.lower()
        d.mkdir(parents=True, exist_ok=True)
        return d / f"{artifact_hash}.json"

    def write_immutable(self, artifact: Dict[str, Any]) -> None:
        path = self._path_for(artifact["artifact_type"], artifact["hash"])
        if path.exists():
            raise FileExistsError("Artifact already exists (immutability enforced).")
        path.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    def find_by_hash(self, artifact_hash: str) -> Dict[str, Any]:
        for d in self.root.iterdir():
            if d.is_dir():
                candidate = d / f"{artifact_hash}.json"
                if candidate.exists():
                    return json.loads(candidate.read_text())
        raise FileNotFoundError("Artifact not found.")
