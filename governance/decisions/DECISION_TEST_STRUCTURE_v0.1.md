# DECISION_TEST_STRUCTURE_v0.1

Status: DECISION / LOCKED  
Phase: IMPLEMENTATION  
Applies to: SAPIANTA system repository  
Decision date: 2026-02-10

---

## 1. DECISION CONTEXT

As the SAPIANTA system evolves, multiple categories of tests are introduced,
including:

- governance enforcement tests
- invariant and guard tests
- runtime interaction tests
- system-level validation tests

A clear and consistent test organization strategy is required to ensure:
- auditability
- discoverability
- deterministic execution
- governance clarity

---

## 2. DECISION STATEMENT

All **system-level, governance, enforcement, invariant, and guard tests**
MUST be located in the **root `tests/` directory** of the repository.

This directory is the canonical location for tests that validate:
- cross-cutting system behavior
- governance enforcement (e.g. HASBT, WRITE-GATE)
- invariants spanning multiple modules
- runtime and lifecycle constraints

---

## 3. RATIONALE

The root `tests/` directory is selected because:

- enforcement mechanisms (e.g. HASBT) are not owned by a single module
- governance logic spans multiple subsystems
- centralized tests improve audit readability
- pytest discovery is simplified
- system-level intent is made explicit

This avoids fragmentation of enforcement tests across module-local test folders.

---

## 4. ALLOWED EXCEPTIONS

Module-local test directories (e.g. `<module>/tests/`) MAY be used only for:

- pure utility functions
- isolated library behavior
- components without governance impact

Such tests MUST NOT:
- assert governance behavior
- validate enforcement mechanisms
- validate system invariants

---

## 5. CURRENT STATE ALIGNMENT

At the time of this decision:

- HASBT enforcement tests are located in `tests/`
- guard and invariant tests already exist in `tests/`
- pytest is configured to discover tests from `tests/`

This decision formalizes the existing, functioning structure.

---

## 6. PROHIBITED BEHAVIOR

The following is explicitly forbidden:

- relocating governance or enforcement tests into module-local directories
- duplicating enforcement tests across multiple locations
- mixing enforcement tests with unit-level module tests

Any deviation requires a new DECISION document.

---

## 7. FINAL LOCK STATEMENT

This decision LOCKS the test organization strategy.

All future governance, enforcement, and invariant tests MUST comply.

---

DECISION CONFIRMATION:
Centralized test structure enforced.
Governance clarity preserved.
Auditability maintained.
