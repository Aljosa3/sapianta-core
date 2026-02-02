# PHASE v0.14 — WIRING REAL EXECUTION ADAPTER
## Status: LOCKED

---

## Purpose

This phase wires a **real execution adapter** into the SAPIANTA build pipeline,
replacing the previously implicit stub execution path.

The goal of v0.14 is **pure wiring**:
to ensure that the build pipeline delegates execution exclusively through
a formal `ExecutionAdapter`, without altering pipeline semantics.

---

## Scope (EXPLICIT)

### Included

- Runtime wiring of execution backend
- Removal of implicit / stub execution logic
- Introduction of execution backend selection layer
- Canonical CLI entrypoint definition

### Excluded

- Execution client implementation (ClaudeClient)
- Retry or fallback logic
- Output interpretation or repair
- Validator changes
- Writer changes
- In-memory execution refactor

---

## Architectural Change Summary

### Before v0.14

- Execution occurred via an implicit stub inside runtime logic
- Execution backend was not explicitly modeled
- Real LLM execution could not be wired cleanly

### After v0.14

- Runtime delegates execution **exclusively** via `ExecutionAdapter`
- Stub execution logic is fully removed
- Execution backend selection is explicit and isolated
- Pipeline semantics remain unchanged

---

## Execution Flow (v0.14)

Build Plan (JSON)  
→ CLI (`sapianta_chat.cli.main build`)  
→ `run_build_pipeline`  
→ `ClaudeExecutor.execute()`  
→ `ExecutionAdapter.execute(build_plan)`  
→ **raw string output**  
→ `claude_raw_output.json` (legacy I/O preserved)  
→ Module Writer  
→ Validator (PASS / FAIL)

---

## Hard Invariants (ENFORCED)

- Execution occurs via exactly **one adapter call**
- Adapter returns **raw string output only**
- Runtime performs no interpretation or validation
- Validator remains the sole authority for build success
- Execution failures are **hard** (no retry, no fallback)

---

## Expected Failure Boundary (CONFIRMED)

During validation of v0.14, execution correctly fails with:

```bash
ModuleNotFoundError: No module named 'runtime.claude_client'
```

This failure is:
- Expected
- Correct
- Architecturally intentional

It confirms that:
- Wiring is active
- Stub execution is removed
- Runtime now depends on an explicit execution client

---

## Canonical CLI Entrypoint

The canonical build command is defined and locked as:

```bash
export EXECUTION_BACKEND=claude
python3 -m sapianta_chat.cli.main build build_plan.json --workdir out/
```

Reference:
governance/operations/SAPIANTA_BUILD_CLI_ENTRYPOINT_v0.1.md

---

## Locked Artifacts

The following artifacts are locked as part of v0.14:
- runtime/claude_executor.py
- runtime/execution_backend.py
- governance/operations/SAPIANTA_BUILD_CLI_ENTRYPOINT_v0.1.md

---

## Backward Compatibility

- Build pipeline behavior is preserved
- Validator logic is unchanged
- Writer logic is unchanged
- Build plan format is unchanged

## Phase Completion Statement

PHASE v0.14 establishes a clean and explicit execution boundary
for real LLM backends.
The system is now correctly wired for execution client implementation,
which will be introduced in the next phase.

LOCK CONFIRMED.