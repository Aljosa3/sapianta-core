# LOCK_READY — Knowledge Anchor Enforcement Levels

## Status
- Phase: FAZA 23A
- Type: Governance / Design-only
- Execution: Forbidden
- Enforcement state: Mandatory
- Lock state: READY FOR LOCK

---

## 1. Purpose

This document defines **how strictly Knowledge Anchors are enforced**
within the SAPIANTA system.

It answers the question:

> What happens when an anchor is violated, missing, or misused?

The goal is to:
- eliminate silent failures
- prevent soft rule erosion
- enforce predictable system behavior
- separate advisory guidance from binding law

---

## 2. Enforcement Levels Overview

Every Knowledge Anchor MUST declare **exactly one** enforcement level.

The system recognizes four enforcement levels:

| Level | Name     | Effect |
|------:|----------|--------|
| E0    | Advisory | Informational only |
| E1    | Warning  | Non-blocking violation |
| E2    | Refusal  | Operation must stop |
| E3    | Fail     | System must hard-stop |

---

## 3. E0 — Advisory

**Meaning:**
- The anchor provides guidance only
- Violation does not invalidate output

**System behavior:**
- Continues normally
- May optionally note deviation

**Allowed usage:**
- Best practices
- Design recommendations
- Non-binding conventions

**Example:**
> Anchor: “Prefer immutable data structures” (E0)  
> Outcome: System may proceed even if mutable structures are used.

---

## 4. E1 — Warning

**Meaning:**
- The anchor defines a recommended constraint
- Violation is allowed but must be visible

**System behavior:**
- Continues execution
- MUST emit a warning
- Warning must be attached to output metadata

**Allowed usage:**
- Soft governance rules
- Transitional constraints
- Migration phases

**Example:**
> Anchor: “Deprecated interface must not be used” (E1)  
> Outcome: System proceeds but emits a deprecation warning.

---

## 5. E2 — Refusal

**Meaning:**
- The anchor defines a binding rule
- Violation invalidates the operation

**System behavior:**
- MUST refuse to proceed
- MUST return an explicit refusal reason
- MUST NOT generate a normal response

**Allowed usage:**
- Security boundaries
- Governance constraints
- Canonical invariants

**Example:**
> Anchor: “Execution requires explicit human approval” (E2)  
> Outcome: System refuses execution attempt.

---

## 6. E3 — Fail

**Meaning:**
- The anchor defines a system-critical invariant
- Violation indicates a fatal breach

**System behavior:**
- MUST hard-stop processing
- MUST surface a fatal error
- MUST NOT attempt recovery or explanation

**Allowed usage:**
- Canon violations
- Integrity guarantees
- Anti-manipulation rules

**Example:**
> Anchor: “Execution without permission gate is forbidden” (E3)  
> Outcome: System halts immediately.

---

## 7. Missing Anchor Enforcement

If a **binding claim** (reasoning, planning, execution eligibility)
is made **without an explicit Knowledge Anchor**:

- Default enforcement level is **E2 (Refusal)**
- The system MUST refuse the claim
- The refusal reason MUST explicitly state:

Binding claim lacks Knowledge Anchor.

There are **no silent fallbacks**.

---

## 8. Multiple Anchors with Different Levels

When multiple anchors apply to the same operation:

- The **highest enforcement level wins**
- Levels are ordered: **E3 > E2 > E1 > E0**
- The system MUST explicitly state which anchor caused the outcome

**Example:**
- Anchor A: E1 (Warning)
- Anchor B: E2 (Refusal)

→ Outcome: **Refusal (E2)** with reference to Anchor B.

---

## 9. Anchor Enforcement Scope

Enforcement applies to **all layers**, including:
- Reasoning conclusions
- Planning descriptions
- Execution eligibility
- Permission checks
- Governance evaluation

No component is exempt.

---

## 10. Prohibited Behavior

The system MUST NOT:
- downgrade enforcement levels implicitly
- ignore anchor levels for convenience
- convert E2/E3 violations into explanations
- continue processing after an E3 violation
- invent or infer anchors retroactively

---

## 11. Closing Statement

Knowledge Anchors are **not documentation**.

They are **law**.

If the law is violated:
- the system must react
- the reaction must be visible
- the reaction must be deterministic

No enforcement → no authority.

---

## Lock Declaration

This document is **normative**.

Once locked:
- Enforcement semantics MUST NOT change
- Levels E0–E3 are fixed
- Any future extension requires a new governance phase

**LOCK_READY**