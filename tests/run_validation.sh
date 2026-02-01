#!/usr/bin/env bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="$ROOT_DIR"

echo "[RUNNER] PYTHONPATH=$PYTHONPATH"
echo "[RUNNER] Running validation tests (FAIL + PASS)"

python3 tests/validation/fail_missing_path.py
python3 tests/validation/fail_forbidden_file.py
python3 tests/validation/fail_forbidden_import.py
python3 tests/validation/fail_combined.py
python3 tests/validation/pass_golden_path.py

echo "[RUNNER] DONE"
