# WRITE-GATE IMPLEMENTATION — v1.0 (LOCK)

## Status
LOCKED — implementation is canonical and frozen

## Scope
This document locks the minimal implementation of WRITE-GATE
as introduced in SAPIANTA v0.21.

The implementation is considered complete, correct,
and sufficient for governed self-write operations.

---

## 1. Implementation Identity

The canonical WRITE-GATE implementation is defined by:

- Class: `WriteGate`
- Exception: `WriteGateDeny`
- Location: `sapianta_chat/governance/write_gate.py`

No alternative implementation is permitted within this phase.

---

## 2. Functional Responsibilities

WRITE-GATE implementation is responsible for:

- evaluating explicit WRITE-INTENT inputs
- enforcing promotion preconditions
- issuing a binary decision:
  - ALLOW (implicit return)
  - DENY (via exception)

WRITE-GATE performs no execution beyond evaluation.

---

## 3. Explicitly Enforced Conditions

The implementation MUST enforce:

1. Explicit artifact identification
2. Explicit source path existence under staging
3. Explicit target canonical domain
4. Validator authority (PASS only)
5. Canonical collision prevention

Failure of any condition results in DENY.

---

## 4. Explicitly Forbidden Behaviors

The implementation MUST NOT:

- perform file system writes
- perform promotion operations
- modify artifacts
- attempt recovery or correction
- interpret intent contextually
- override validator results

WRITE-GATE is a decision boundary only.

---

## 5. Determinism

Given identical inputs, WRITE-GATE MUST:

- produce identical decisions
- raise identical denial reasons
- perform no side effects

Non-deterministic behavior is forbidden.

---

## 6. Test Coverage Lock

The following test cases are considered canonical
and normative for this implementation:

- ALLOW for non-existing canonical target
- DENY when canonical target exists
- DENY when validator result is not PASS
- DENY when source path does not exist

Any change to behavior requires:
- updated tests
- a new LOCK document
- explicit governance approval

---

## 7. Authority Boundary

WRITE-GATE implementation authority is final
for legitimacy decisions.

It does not compete with:
- validators (correctness)
- runtime (execution)
- planners (intent generation)

Layer separation is mandatory.

---

## 8. Change Policy

Any modification to:

- logic
- semantics
- scope
- decision criteria

constitutes a breaking governance change
and MUST NOT occur within v0.21.

---

## END OF DOCUMENT
