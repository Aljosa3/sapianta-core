# AUTHORITY_TYPES

## Status
- Phase: FAZA 26A
- Type: Governance / Design-only
- Execution: Forbidden
- Authority state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines **types of authority** recognized by the SAPIANTA system.

It answers the question:

Who is allowed to authorize execution — and in what capacity?

The goal is to:
- separate *capability* from *permission*
- prevent implicit authority
- avoid single-point-of-trust failures
- make execution approval explicit, auditable, and revocable

No authority → no execution.

---

## 2. Core Principle

Execution is never authorized by the system itself.

Execution is authorized **only** by an explicit Authority
recognized by governance rules.

Authority is:
- external to reasoning
- external to planning
- required before execution eligibility
- evaluated before gate opening

---

## 3. Authority vs Role vs Identity

These concepts MUST NOT be conflated:

- **Identity** — who someone is
- **Role** — what they normally do
- **Authority** — what they are allowed to approve

Authority is:
- contextual
- scoped
- revocable
- explicit

---

## 4. Authority Types Overview

The system recognizes the following authority types:

| Code | Authority Type        | Description |
|----:|-----------------------|-------------|
| A0  | None                  | No authority |
| A1  | Human Operator        | Explicit human approval |
| A2  | Delegated Authority   | Human-delegated approval |
| A3  | Multi-Party Authority | Consensus-based approval |
| A4  | Emergency Authority   | Exceptional override |
| A5  | System Authority      | Non-human, rule-bound |

---

## 5. A0 — No Authority

### Meaning
- No execution approval capability
- Default state for all contexts

### Rules
- Execution is forbidden
- Any execution attempt → R2 Denial

This is the **default authority**.

---

## 6. A1 — Human Operator Authority

### Meaning
- Direct approval by a human
- Conscious, intentional consent

### Properties
- Must be explicit
- Must be traceable
- Must be time-bound (optionally)
- Must be revocable

### Typical usage
- Manual execution approval
- Sensitive operations
- First-time execution paths

---

## 7. A2 — Delegated Authority

### Meaning
- Authority delegated by a human operator
- Delegation is explicit and limited

### Properties
- Delegation scope MUST be defined
- Delegation MUST be revocable
- Delegation MUST reference source authority

### Typical usage
- Trusted automation
- Narrow execution domains
- Scheduled or repeated actions

Delegation never exceeds original authority.

---

## 8. A3 — Multi-Party Authority

### Meaning
- Execution requires multiple approvals
- No single entity can authorize alone

### Properties
- Required quorum MUST be defined
- Approval aggregation MUST be explicit
- Partial approval is insufficient

### Typical usage
- High-risk execution
- Governance-sensitive actions
- Shared ownership environments

---

## 9. A4 — Emergency Authority

### Meaning
- Exceptional authority used only under defined emergency conditions

### Properties
- Strictly limited scope
- Mandatory post-action review
- Strong audit requirements

### Rules
- Cannot bypass core invariants
- Cannot disable governance logging
- Cannot self-grant permanence

Emergency does not mean unaccountable.

---

## 10. A5 — System Authority

### Meaning
- Authority granted to the system itself
- Only under predefined, verifiable conditions

### Properties
- Fully rule-bound
- No discretion
- No self-extension

### Typical usage
- Self-protection
- Integrity preservation
- Automatic safe shutdowns

System Authority never authorizes *new* capabilities.

---

## 11. Authority Scope

Every authority MUST declare scope:

- execution_type (what can be executed)
- duration (how long it is valid)
- context (where it applies)

Out-of-scope execution is forbidden.

---

## 12. Prohibited Authority Behavior

The system MUST NOT:
- infer authority
- escalate authority implicitly
- reuse expired authority
- merge authorities silently
- allow authority without traceability

---

## 13. Design-Time Constraint

This document:
- defines authority categories only
- performs no authorization
- performs no execution
- performs no evaluation

Evaluation is defined in:
- Execution Eligibility Rules
- Execution Gate Definition
- Authority Verification Protocol (future)

---

## 14. Closing Statement

Authority is **power with responsibility**.

If execution occurs:
- someone authorized it
- the authority can be named
- the authority can be audited
- the authority can be revoked

No authority → no execution.
