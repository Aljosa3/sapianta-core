# sapianta_runtime/cdr/reader.py

import json
from pathlib import Path


def load_cdrs(cdr_path: Path):
    if not cdr_path.exists():
        raise RuntimeError("CDR path does not exist")

    records = []
    for file in sorted(cdr_path.iterdir()):
        if file.suffix != ".json":
            continue
        with file.open("r", encoding="utf-8") as f:
            records.append(json.load(f))

    return records
