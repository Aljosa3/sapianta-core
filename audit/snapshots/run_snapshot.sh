#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT_FILE="$REPO_ROOT/audit/snapshots/hoi_hds_v0_3_snapshot.json"

python3 "$REPO_ROOT/modules/hoi_to_hds_json_adapter_v0_1/cli.py" > "$OUT_FILE"

echo "Snapshot written to: $OUT_FILE"
