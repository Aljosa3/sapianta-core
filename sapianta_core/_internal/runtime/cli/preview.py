import json
import sys
from pathlib import Path

# ensure repo root is on PYTHONPATH
REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from sapianta_core._internal.runtime.decision_preview.preview import preview_decisions


def load_json(path: Path):
    if not path.exists():
        raise RuntimeError(f"File not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    if len(sys.argv) != 3:
        print("Usage: sapianta-preview <base_state.json> <cdrs.json>")
        sys.exit(1)

    base_state_path = Path(sys.argv[1])
    cdrs_path = Path(sys.argv[2])

    base_state = load_json(base_state_path)
    hypothetical_cdrs = load_json(cdrs_path)

    result = preview_decisions(
        base_state=base_state,
        hypothetical_cdrs=hypothetical_cdrs
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
