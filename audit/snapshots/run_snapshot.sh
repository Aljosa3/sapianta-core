#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT_FILE="$REPO_ROOT/audit/snapshots/hoi_hds_v0_3_snapshot.json"

python3 "$REPO_ROOT/modules/hds_json_output_v0_3/cli.py" > "$OUT_FILE"

echo "Snapshot written to: $OUT_FILE"
