# AUTHORITY_REVOCATION_AND_LIFECYCLE

## Status
- Phase: FAZA 26C
- Type: Governance / Design-only
- Execution: Forbidden
- Lifecycle state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **lifecycle of authority**
and the rules for **revocation, expiration, and invalidation**
within the SAPIANTA system.

It answers the question:

When does authority stop being authority?

The goal is to:
- prevent lingering or zombie authority
- make authority time-bound and context-bound
- ensure immediate effect of revocation
- separate authority existence from authority usability

Authority is temporary by default.

---

## 2. Core Principle

Every authority MUST have a lifecycle.

There is:
- no permanent authority
- no implicit continuity
- no immunity to revocation

If authority lifecycle cannot be determined,
the authority is invalid.

---

## 3. Authority Lifecycle States

An authority exists in exactly one of the following states:

- CREATED — authority is defined but inactive
- ACTIVE — authority may be verified and used
- EXPIRED — authority validity period has ended
- REVOKED — authority has been explicitly withdrawn
- SUPERSEDED — authority replaced by a newer authority
- ARCHIVED — authority retained for audit only

Only **ACTIVE** authority may be verified.

---

## 4. Creation Phase

Authority creation:
- defines authority type
- defines scope
- defines temporal bounds
- assigns unique authority identifier

Creation does NOT imply activation.

CREATED authority is inert.

---

## 5. Activation Rules

Authority enters ACTIVE state only when:
- activation conditions are satisfied
- system phase allows activation
- no conflicting governance lock exists

Activation MUST be explicit.

Implicit activation is forbidden.

---

## 6. Expiration

Authority MUST define expiration semantics.

Expiration may be:
- time-based
- event-based
- single-use

Expired authority:
- becomes immediately invalid
- MUST fail verification
- cannot be reactivated

Expiration is irreversible.

---

## 7. Revocation

Authority may be revoked:
- by governance decision
- by higher authority
- by system integrity event

Revocation:
- takes effect immediately
- overrides expiration timing
- invalidates all pending uses

Revoked authority MUST NOT be revalidated.

---

## 8. Supersession

Authority may be superseded by:
- updated scope
- renewed validity
- governance restructuring

Superseded authority:
- becomes invalid for use
- remains visible for audit
- MUST reference the replacing authority

Supersession does NOT imply revocation.

---

## 9. Archival

Authority enters ARCHIVED state when:
- expired or revoked
- no longer operationally relevant

Archived authority:
- MUST NOT be used
- MUST NOT be reactivated
- MAY be inspected for audit

Archival preserves history, not power.

---

## 10. Revocation Triggers

Revocation MUST occur when:
- governance phase is locked
- execution boundary is violated
- authority misuse is detected
- anchor enforcement failure (E3) occurs

Revocation triggers are deterministic.

---

## 11. System Behavior on Invalid Authority

If authority is:
- EXPIRED
- REVOKED
- SUPERSEDED
- ARCHIVED

Then:
- verification MUST fail
- execution MUST be denied (R2)
- denial reason MUST reference lifecycle state

No fallback is allowed.

---

## 12. Audit Requirements

Lifecycle transitions MUST be:
- logged
- timestamped
- attributable

Audit logs MUST record:
- previous state
- new state
- transition reason

Auditability is mandatory.

---

## 13. Design-Time Constraint

This document:
- defines lifecycle semantics only
- performs no execution
- performs no authority issuance
- performs no state mutation

Runtime lifecycle handling is defined later.

---

## 14. Closing Statement

Authority exists in time.

What once allowed execution
must eventually expire, be replaced, or be revoked.

No lifecycle → no authority.
