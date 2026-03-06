#!/usr/bin/env bash
set -euo pipefail

echo "[SAPIANTA] Running Promotion Gate v0.2..."

OUTPUT=$(python3 tools/governance/promotion_gate_v02.py --staged)

echo "$OUTPUT"

if echo "$OUTPUT" | grep -q "Change Classification: STRUCTURAL"; then
    echo ""
    echo "[SAPIANTA] STRUCTURAL change detected."
    echo "[SAPIANTA] Commit blocked."
    echo "If intentional, run:"
    echo "SAPIANTA_APPROVE_STRUCTURAL=1 git commit ..."
    
    if [[ "${SAPIANTA_APPROVE_STRUCTURAL:-}" != "1" ]]; then
        exit 1
    fi
fi

exit 0