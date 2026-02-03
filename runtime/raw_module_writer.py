import os
import re
from typing import List, Tuple


FILE_MARKER = re.compile(r"^### FILE:\s*(.+)$", re.MULTILINE)


class RawModuleWriterError(RuntimeError):
    pass


def parse_files(raw_text: str) -> List[Tuple[str, str]]:
    """
    Parse raw text into a list of (path, content) using markers:

    ### FILE: path/to/file.ext
    <content>
    """
    if not isinstance(raw_text, str) or not raw_text.strip():
        raise RawModuleWriterError("Raw output is empty or not a string")

    matches = list(FILE_MARKER.finditer(raw_text))
    if not matches:
        raise RawModuleWriterError("No FILE markers found in raw output")

    files = []
    for i, m in enumerate(matches):
        path = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw_text)
        content = raw_text[start:end].lstrip("\n")
        files.append((path, content))

    return files


def write_files(files: List[Tuple[str, str]], project_root: str) -> None:
    for rel_path, content in files:
        out_path = os.path.join(project_root, rel_path)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
