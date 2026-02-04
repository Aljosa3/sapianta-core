# PATH: runtime/raw_module_writer.py

import re
from pathlib import Path
from typing import Dict


class RawModuleWriterError(RuntimeError):
    pass


class RawModuleWriter:
    """
    HARD runtime materializer for v0.17.

    Accepts ONLY strict FILE-based raw output.
    No guessing, no repair, no fallback.
    """

    FILE_MARKER = re.compile(r"^FILE:\s+(.+)$", re.MULTILINE)

    def __init__(self, project_root: str, allowed_roots=("modules/",)):
        self.project_root = Path(project_root).resolve()
        self.allowed_roots = allowed_roots

    def write_from_raw(self, raw_text: str) -> None:
        if not isinstance(raw_text, str) or not raw_text.strip():
            raise RawModuleWriterError("Raw output is empty or not a string")

        matches = list(self.FILE_MARKER.finditer(raw_text))
        if not matches:
            raise RawModuleWriterError("No FILE markers found in raw output")

        files: Dict[str, str] = {}

        for i, match in enumerate(matches):
            path = match.group(1).strip()

            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(raw_text)
            content = raw_text[start:end].lstrip("\n")

            if not content.strip():
                raise RawModuleWriterError(f"Empty content for file: {path}")

            if path in files:
                raise RawModuleWriterError(f"Duplicate FILE path: {path}")

            if not any(path.startswith(root) for root in self.allowed_roots):
                raise RawModuleWriterError(f"Path outside allowed roots: {path}")

            files[path] = content

        for rel_path, content in files.items():
            out_path = (self.project_root / rel_path).resolve()

            if not str(out_path).startswith(str(self.project_root)):
                raise RawModuleWriterError(f"Path traversal detected: {rel_path}")

            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
