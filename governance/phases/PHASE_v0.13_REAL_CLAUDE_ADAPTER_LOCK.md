# PHASE v0.13 — REAL CLAUDE ADAPTER
## STATUS: LOCKED

---

## Purpose

This phase introduces a **real LLM execution adapter** into the SAPIANTA Chat system.

The adapter replaces the previous stub executor while **preserving the entire build pipeline unchanged**.

The adapter is strictly execution-only and does not participate in:
- validation
- interpretation
- planning
- decision making

---

## Scope (EXPLICIT)

Included in this phase:

- Execution adapter interface
- Deterministic prompt rendering
- Real Claude adapter implementation
- Adapter-only test suite

Excluded from this phase:

- Build pipeline logic changes
- Validator logic
- Retry / fallback logic
- LLM output interpretation
- Repo introspection
- File I/O
- SDK configuration management

---

## Architecture Invariants (HARD)

The Real Claude Adapter MUST:

1. Accept a locked `SAPIANTA_BUILD_PLAN_V1`
2. Render a deterministic prompt
3. Perform exactly **one (1)** LLM call
4. Return **raw string output only**
5. Raise a hard failure on technical errors

The adapter MUST NOT:

- retry requests
- repair output
- validate output
- interpret the build plan
- access the repository
- access validators or writers
- modify pipeline behavior

---

## Adapter Contract (LOCKED)

### Interface

execute(build_plan) -> raw_output: str


This is the **only allowed method**.

---

## Prompt Determinism

- Prompt rendering is a pure function of the build plan
- Identical build plans MUST produce identical prompts
- Prompt structure, header, and footer are frozen

Any change to the prompt template requires a new phase version.

---

## Failure Semantics

- Adapter failures are **hard**
- No retry logic is permitted
- No fallback execution is permitted
- All semantic judgment is deferred to the validator

---

## Test Guarantees

The following properties are verified by tests:

- Single LLM call per execution
- Deterministic prompt rendering
- Raw output passthrough
- Hard failure on invalid backend output

---

## Locked Artifacts

The following artifacts are locked as part of this phase:

- `sapianta_chat/execution/adapter_interface.py`
- `sapianta_chat/execution/prompt_renderer.py`
- `sapianta_chat/execution/claude_adapter.py`
- `tests/execution/*`

---

## Backward Compatibility

- The build pipeline remains unchanged
- Validator remains the sole authority for PASS / FAIL
- Adapter is backend-agnostic and replaceable

---

## Phase Completion Statement

PHASE v0.13 — REAL CLAUDE ADAPTER is complete and locked.

Any modification to adapter behavior, prompt structure, or execution semantics
requires a new phase version.

---

LOCK CONFIRMED.
