# EXECUTION_ELIGIBILITY_RULES

## Status
- Phase: FAZA 25B
- Type: Governance / Design-only
- Execution: Forbidden
- Eligibility state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **Execution Eligibility Rules**.

It answers the question:

> Under what exact conditions may a request be considered eligible
> to pass the Execution Gate?

These rules:
- are strictly normative
- contain no execution logic
- contain no implementation detail
- define eligibility only

Eligibility does NOT mean execution.

---

## 2. Core Principle

A request is **execution-eligible** if and only if
**all mandatory eligibility rules are satisfied**.

Eligibility is:
- binary (eligible / not eligible)
- deterministic
- non-negotiable

Partial eligibility does not exist.

---

## 3. Mandatory Eligibility Conditions

All of the following conditions MUST be satisfied.

Failure of any single condition
results in **REFUSE (R1/R2)** or **FAIL (F1)**.

---

## 4. Claim Classification Requirement

### Rule E-01

Only the following claim types MAY be considered for execution eligibility:

- C3 — Action Request
- C4 — Execution Request

All other claim types (C0–C2):
→ **REFUSE (R1)**

Reason:
Non-actionable claims are not execution candidates.

---

## 5. Knowledge Anchor Binding Requirement

### Rule E-02

The request MUST include at least one valid **Knowledge Anchor Binding**
that explicitly allows execution consideration.

Requirements:
- anchor exists
- anchor version is specified
- enforcement level is respected
- binding scope includes `eligibility` or `execution`

Missing or invalid anchor:
→ **REFUSE (R1)**

Tampered or inferred anchor:
→ **FAIL (F1)**

---

## 6. Enforcement Level Constraint

### Rule E-03

If any applicable Knowledge Anchor resolves to:

- E2 (Refusal)
→ execution eligibility MUST be refused

- E3 (Fail)
→ system MUST hard-stop

Execution eligibility is impossible
under E2 or E3 constraints.

---

## 7. Execution Boundary Compliance

### Rule E-04

The request MUST comply with all active **Execution Boundary** rules.

If execution is forbidden by boundary definition:
→ **DENY (R2)**

Execution boundaries override intent,
planning, and user authority.

---

## 8. System Phase Constraint

### Rule E-05

Execution eligibility is dependent on the current system phase.

If the system phase is locked
or execution has not been entered:

→ **DENY (R2)**

No phase override is allowed.

---

## 9. Authority & Context Requirement

### Rule E-06

The caller context MUST be authorized
to request execution eligibility.

Context includes:
- interface (CLI / API / internal)
- user role (if applicable)
- governance scope

Unauthorized context:
→ **DENY (R2)**

---

## 10. Planning Dependency Rule

### Rule E-07

If execution eligibility depends on a plan:

- the plan MUST exist
- the plan MUST be bound to anchors
- the plan MUST be consistent with eligibility anchors

Missing or unbound plan:
→ **REFUSE (R1)**

---

## 11. Prohibited Eligibility Shortcuts

The system MUST NOT:

- infer eligibility
- auto-upgrade claim types
- reinterpret anchor intent
- bypass enforcement resolution
- downgrade refusal into explanation
- continue after a fail condition

---

## 12. Determinism Guarantee

Given identical input conditions,
eligibility evaluation MUST always
produce the same result.

No randomness.
No learning.
No optimization.

---

## 13. Relationship to Execution Gate

These rules are **consumed by** the Execution Gate.

The Execution Gate:
- applies these rules
- does not modify them
- does not extend them

Rules live here.
Decisions live at the gate.

---

## 14. Closing Statement

Execution eligibility is **not permission**.

It is a legal acknowledgment
that execution may be considered.

No eligibility → no gate passage.  
No gate passage → no execution.  
No law → no eligibility.

---
