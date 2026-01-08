# AUTHORITY_TYPES

## Status
- Phase: FAZA 26A
- Type: Governance / Design-only
- Execution: Forbidden
- Authority state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **canonical types of authority**
recognized by the SAPIANTA system.

It answers the foundational question:

> Who is allowed to authorize what — and why?

Authority Types form the **root layer** for:
- authority verification
- execution eligibility
- permission enforcement
- revocation and lifecycle handling

No authority type → no valid authority.

---

## 2. Core Principle

All authority in the system MUST:
- belong to exactly one Authority Type
- be explicitly declared
- be verifiable
- be revocable

Implicit authority is forbidden.

---

## 3. Authority Type Overview

The system recognizes **five** authority types.

| Code | Authority Type | Description |
|-----:|---------------|-------------|
| A0 | System Authority | Inherent system-level authority |
| A1 | Canon Authority | Authority derived from locked canon |
| A2 | Governance Authority | Authority granted by governance rules |
| A3 | Human Authority | Authority originating from a human actor |
| A4 | Delegated Authority | Authority delegated by another authority |

No other authority types are permitted.

---

## 4. A0 — System Authority

### Definition
Authority inherent to the SAPIANTA system itself.

### Characteristics
- Exists by definition
- Cannot be delegated
- Cannot be revoked
- Bound to system identity

### Scope
- Canon enforcement
- Phase locking
- Integrity guarantees
- Fatal failure handling

### Restrictions
- MUST NOT authorize execution
- MUST NOT impersonate human intent

---

## 5. A1 — Canon Authority

### Definition
Authority derived directly from locked canonical documents.

### Characteristics
- Emerges from LOCKED canon
- Immutable once locked
- Applies universally

### Scope
- Normative rules
- Invariant enforcement
- Structural constraints

### Restrictions
- Cannot be overridden
- Cannot be revoked individually
- Changes require new canon phase

---

## 6. A2 — Governance Authority

### Definition
Authority defined by governance processes and documents.

### Characteristics
- Explicitly granted
- Context-dependent
- Time-bound if specified

### Scope
- Permission granting
- Role definition
- Operational constraints

### Restrictions
- MUST be verifiable
- MAY be revoked
- MUST respect Canon Authority

---

## 7. A3 — Human Authority

### Definition
Authority originating from an identifiable human actor.

### Characteristics
- Requires explicit identity
- Requires explicit intent
- Contextual and scoped

### Scope
- Execution approval
- High-risk decisions
- External commitments

### Restrictions
- MUST be authenticated
- MUST NOT be inferred
- MAY be revoked or expire

---

## 8. A4 — Delegated Authority

### Definition
Authority delegated from another valid authority.

### Characteristics
- Always derivative
- Limited to delegation scope
- Traceable to origin authority

### Scope
- Operational convenience
- Automation boundaries
- Temporary permissions

### Restrictions
- Cannot exceed parent authority
- Revoked if parent is revoked
- MUST declare delegator

---

## 9. Authority Type Constraints

The system MUST enforce:

- One authority → one type
- No authority stacking across types
- No circular delegation
- No anonymous authority
- No authority escalation by inference

Violations default to **E2 Refusal**.

---

## 10. Relationship to Other Phases

This document is the foundation for:

- FAZA 26B — Authority Verification & Validity
- FAZA 26C — Authority Revocation & Lifecycle
- FAZA 25 — Execution Eligibility
- FAZA 24 — Message Routing & Refusal

Without Authority Types, those phases are undefined.

---

## 11. Design-Time Constraint

This document:
- defines authority taxonomy only
- performs no verification
- performs no execution
- performs no routing

It is purely normative.

---

## 12. Closing Statement

Authority is not power.

Authority is **permission under law**.

If authority is unclear:
- the system must refuse
- the system must not guess
- the system must not act

No authority type → no legitimacy.
