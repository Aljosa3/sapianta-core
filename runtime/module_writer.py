from pathlib import Path

def write(draft: dict):
    for path, content in draft["files"].items():
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
