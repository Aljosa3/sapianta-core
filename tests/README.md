# SAPIANTA – System Invariant Tests

This directory contains **system-level invariant tests** for the SAPIANTA runtime.

These tests are **not unit tests** and **not feature tests**.
They exist to protect **core architectural and governance invariants**
that must never be broken by refactoring, optimization, or extension.

---

## Purpose

The tests in this directory ensure that:

- Normative decisions are deterministic and protected
- Governance rules are enforced at runtime
- Critical execution semantics cannot silently regress

If a test in this directory fails, it indicates a **system-level violation**,
not a minor implementation bug.

---

## Test Philosophy

SAPIANTA tests focus on **invariants**, not behavior coverage.

Key principles:

- Tests validate *where* decisions are made, not *how*
- Tests protect separation between:
  - decision vs explanation
  - execution vs audit
  - permission vs output
- Tests must fail loudly if core semantics are violated

---

## Current Invariants

### `test_guard_lifecycle.py`

Protects the following invariant:

> `Status.ALLOW` may be set **only** by runtime guards  
> and must never be invented by the orchestrator or SP passes.

Additionally verifies that:

- Execution halts without explicit guard approval
- Explain and audit layers do not influence normative decisions
- Runtime operates as a proper Python package (no implicit imports)

---

## Execution

Tests can be run manually:

```bash
python3 tests/test_guard_lifecycle.py
```

No external test framework is required.

## Governance Note

These tests are part of the technical enforcement layer
of SAPIANTA governance.

They complement (but do not replace):

- Canon documents

- Governance locks

- Architectural constraints

Breaking a test here means breaking a guarantee, not just code.

## Extension Policy

New tests may be added only when they protect a system invariant.

Do NOT add:

- convenience tests
- implementation-detail tests
- feature coverage tests

This directory is intentionally small.