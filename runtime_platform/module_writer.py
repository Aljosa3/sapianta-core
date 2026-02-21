# PATH: runtime/module_writer.py

from pathlib import Path
from typing import Dict, Any


class ModuleWriteError(RuntimeError):
    pass


class ModuleWriter:
    """
    Writes Claude-generated draft files to disk.

    HARD RULES:
    - writes ONLY files explicitly provided in draft["files"]
    - writes ONLY inside project root
    - NO markdown files
    - no interpretation, no modification
    """

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()

    def write(self, draft: Dict[str, Any]) -> None:
        files = draft.get("files")

        if not isinstance(files, dict) or not files:
            raise ModuleWriteError("Draft contains no files to write.")

        written = 0

        for rel_path, content in files.items():
            self._write_single_file(rel_path, content)
            written += 1

        print(f"[WRITER] {written} files written successfully")

    # ---------- internals ----------

    def _write_single_file(self, rel_path: str, content: str) -> None:
        if not isinstance(rel_path, str) or not isinstance(content, str):
            raise ModuleWriteError("Invalid file entry in draft.")

        if rel_path.endswith(".md"):
            raise ModuleWriteError(
                f"Markdown files are forbidden: {rel_path}"
            )

        target_path = (self.project_root / rel_path).resolve()

        # 🔒 HARD SECURITY: prevent path traversal
        if not str(target_path).startswith(str(self.project_root)):
            raise ModuleWriteError(
                f"Illegal write path outside project root: {rel_path}"
            )

        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content, encoding="utf-8")

        print(f"[WRITER] wrote {rel_path}")
