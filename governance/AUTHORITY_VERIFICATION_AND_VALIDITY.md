# AUTHORITY_VERIFICATION_AND_VALIDITY

## Status
- Phase: FAZA 26B
- Type: Governance / Design-only
- Execution: Forbidden
- Verification state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines **how authority is verified and validated**
before it can authorize execution in the SAPIANTA system.

It answers the question:

Is this authority valid *here*, *now*, and *for this action*?

The goal is to:
- prevent stale or reused authority
- eliminate implicit trust
- ensure temporal and contextual correctness
- separate authority declaration from authority validity

Declared authority ≠ valid authority.

---

## 2. Core Principle

Authority MUST be verified **every time** it is used.

There is:
- no caching of authority decisions
- no implicit carry-over
- no trust by prior success

Verification is mandatory, repeatable, and deterministic.

---

## 3. Authority Verification Process

Authority verification consists of the following steps:

1. Authority presence check
2. Authority type validation
3. Scope validation
4. Temporal validity check
5. Context compatibility check
6. Revocation check

Failure at any step invalidates authority.

---

## 4. Authority Presence Check

The system MUST verify that:
- an authority is explicitly provided
- authority type is declared
- authority reference is complete

Missing authority → **R2 Denial**

There are no defaults.

---

## 5. Authority Type Validation

The declared authority type MUST:
- exist in AUTHORITY_TYPES
- be allowed for the requested execution category

Invalid or unknown authority type → **R2 Denial**

---

## 6. Scope Validation

Authority scope MUST cover:
- requested execution type
- affected resources
- operational domain

Out-of-scope authority → **R2 Denial**

Scope MUST NOT be inferred or expanded.

---

## 7. Temporal Validity

Authority MUST be valid at the time of verification.

Checks include:
- activation time (not before)
- expiration time (not after)
- single-use constraints (if defined)

Expired or premature authority → **R2 Denial**

---

## 8. Context Compatibility

Authority MUST be compatible with:
- current system phase
- execution environment
- governance state

Authority valid in one phase is not valid in another
unless explicitly declared.

Mismatch → **R2 Denial**

---

## 9. Revocation Check

The system MUST verify that authority:
- has not been revoked
- has not been superseded
- has not been invalidated by governance lock

Revoked authority → **R2 Denial**

Revocation takes effect immediately.

---

## 10. Verification Outcome

Authority verification yields exactly one outcome:

- VALID — authority may be used for execution eligibility
- INVALID — execution is denied

There is no partial validity.

---

## 11. Failure Behavior

Authority verification failure:
- MUST be explicit
- MUST produce a Denial (R2) message
- MUST state the failing verification step

The system MUST NOT:
- continue execution
- downgrade to refusal (R1)
- explain away failure

---

## 12. Audit Requirements

Every verification attempt MUST be:
- logged
- timestamped
- attributable to an authority reference

Audit data MUST include:
- authority type
- verification result
- failure reason (if any)

---

## 13. Design-Time Constraint

This document:
- defines verification semantics only
- performs no execution
- performs no authority assignment
- performs no state mutation

Runtime implementation is defined later.

---

## 14. Closing Statement

Authority is not a badge.
Authority is not a role.
Authority is not trust.

Authority is **a claim** that must survive verification.

No valid authority → no execution.
