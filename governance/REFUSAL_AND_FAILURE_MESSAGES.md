REFUSAL_AND_FAILURE_MESSAGES

Status

Phase: FAZA 24B

Type: Governance / Design-only

Execution: Forbidden

Message state: Mandatory

Lock state: NOT LOCKED

1. Purpose

This document defines how the system communicates refusal and failure.

It answers the question:
How does SAPIANTA say “no” — clearly, lawfully, and predictably?

The goal is to:

eliminate silence

eliminate vague answers

replace confusion with structured feedback

make refusal usable, not frustrating

2. Core Principle

Whenever the system cannot proceed, it MUST respond with a structured refusal or failure message.

Silence is forbidden.
Generic explanations are forbidden.

3. Message Types

The system recognizes exactly three non-success message types:

R1 — Refusal
R2 — Denial
F1 — Failure

Their meanings are:

R1: Lawful stop, user-correctable

R2: Permission-based stop

F1: Fatal system violation

4. R1 — Refusal (Recoverable)

Meaning

The request is understood

The request is invalid in the current context

The user may correct or rephrase

Typical causes

Binding claim without Knowledge Anchor

Planning request without Planning Anchor

Ambiguous claim defaulted to C2

Missing classification prerequisites

Required fields

type: R1

claim_type: C0–C4

reason_code: string

human_message: string

correction_hint: string (optional)

Example (plain text)
REFUSAL (R1)
Claim type: C2 — Binding
Reason: Missing Knowledge Anchor
Message: This request asserts system validity without a Knowledge Anchor.
Hint: Provide a valid anchor reference or rephrase as informational.

5. R2 — Denial (Permission-Based)

Meaning

The request is valid in general

The requester lacks permission or authority

Typical causes

Execution eligibility queried by non-authorized context

Locked phase access

Governance-restricted operations

Required fields

type: R2

denied_scope: execution | governance | state

reason_code: string

human_message: string

Example (plain text)
DENIAL (R2)
Scope: Execution
Reason: Execution Era not entered
Message: Execution is not permitted in the current system phase.

6. F1 — Failure (Fatal)

Meaning

A core invariant was violated

System integrity is at risk

No continuation is allowed

Typical causes

E3 Knowledge Anchor violation

Execution attempt without gate

Anchor tampering or inference

Post-lock modification attempt

Required fields

type: F1

violation: string

anchor_id: string (if applicable)

fatal: true

Behavior

Immediate hard stop

No recovery

No explanation beyond violation notice

Example (plain text)
FAILURE (F1)
Violation: Execution without permission gate
Anchor: EXECUTION_BOUNDARY
System halted.

7. Mapping to Claim Classification

C0 → None

C1 → None or R1

C2 → R1

C3 → R1

C4 → F1

Execution attempts never downgrade to refusal.

8. Prohibited Behavior

The system MUST NOT:

stay silent

explain instead of refusing

convert failures into advice

downgrade F1 to R1

emit unstructured text

9. Design-Time Constraint

This document:

defines message semantics only

performs no routing

performs no execution

performs no evaluation

It is enforced by:

Claim Classification Model

Knowledge Anchor Enforcement Levels

10. Closing Statement

Refusal is not a bug.
Refusal is communication of law.

If the system cannot act:

it must say why

it must say how to fix it

or it must stop — visibly

No message → no trust.