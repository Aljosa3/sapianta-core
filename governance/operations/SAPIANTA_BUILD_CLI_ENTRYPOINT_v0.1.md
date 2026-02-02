# SAPIANTA — Canonical Build CLI Entrypoint
## Version: v0.1
## Status: LOCKED

---

## Purpose

Define the single canonical command used to execute the
SAPIANTA build pipeline via the official CLI interface.

This entrypoint is the only supported way to run the build
pipeline in governed mode.

---

## Canonical Command

```bash
export EXECUTION_BACKEND=claude
python3 -m sapianta_chat.cli.main build build_plan.json --workdir out/
```
---

## Definition Source

- CLI entrypoint: sapianta_chat/cli/main.py
- Build subcommand: build
- Pipeline orchestration: sapianta_chat/cli/build_flow.py
- Execution delegation: runtime/claude_executor.py

---

## Notes

Direct invocation of build_flow.py is not considered a canonical CLI entrypoint.
This command ensures:
- Pipeline Integrity Check
- Proper execution backend wiring
- Validator-controlled PASS / FAIL semantics

LOCK CONFIRMED.

---