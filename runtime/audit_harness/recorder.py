import sys
import datetime
from pathlib import Path
from typing import Optional


class StdoutRecorder:
    """
    AUDIT HARNESS (WRITE-ONLY)
    - zajema stdout
    - ne interpretira vsebine
    - brez spomina v runtime (samo zapis)
    """

    def __init__(self, base_dir: Optional[Path] = None):
        ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        self.base_dir = base_dir or Path("audit_logs")
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.base_dir / f"audit_{ts}.log"

        self._original_stdout = sys.stdout
        self._file = open(self.log_path, "w", encoding="utf-8")

    def start(self):
        sys.stdout = self

    def stop(self):
        sys.stdout = self._original_stdout
        self._file.close()

    def write(self, data: str):
        self._original_stdout.write(data)
        self._file.write(data)

    def flush(self):
        self._original_stdout.flush()
        self._file.flush()
