# MESSAGE_ROUTING_CONTRACT

## Status
- Phase: FAZA 24C.1
- Type: Governance / Design-only
- Execution: Forbidden
- Routing state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **canonical contract for routing system messages**
from internal decision outcomes to user-facing CLI output.

It answers the question:

> Who is allowed to emit messages, when, and under what constraints?

The goal is to:
- eliminate ad-hoc CLI behavior
- enforce deterministic message delivery
- prevent silence, leakage, or improvisation
- strictly separate decision logic from presentation

Routing is not presentation.
Routing is governance.

---

## 2. Core Principle

The CLI MUST NOT decide **what** to say.

The CLI MAY ONLY:
- receive a finalized Message Object
- render it exactly once
- terminate or return control as instructed

All message intent is resolved **before** routing.

No intent resolution occurs in the CLI.

---

## 3. Message Routing Boundary

Message routing exists as a strict boundary between:

- internal system evaluation
- external user interaction

Only **Message Objects** may cross this boundary.

Raw errors, exceptions, or explanations MUST NOT cross.

---

## 4. Message Object Requirement

Every non-success outcome MUST be represented
as exactly one Message Object of type:

- R1 — Refusal
- R2 — Denial
- F1 — Failure

No other message types are permitted.

If no Message Object exists:
→ routing MUST NOT occur
→ silence is a violation

---

## 5. Routing Authority

Only the following components MAY emit a Message Object
into the routing layer:

- Claim Classification Engine
- Knowledge Anchor Enforcement
- Permission / Phase Gate
- Governance Lock Enforcement

No other component has routing authority.

The CLI has **zero routing authority**.

---

## 6. Deterministic Routing Rules

Routing behavior is fixed and non-negotiable.

| Message Type | CLI Action |
|--------------|-----------|
| R1 (Refusal) | Render message, return control to user |
| R2 (Denial)  | Render message, terminate interaction |
| F1 (Failure) | Render message, hard-stop immediately |
| Success      | Continue normal flow |

No downgrades.
No retries.
No fallbacks.

---

## 7. Rendering Constraint

The CLI MUST:

- render the message exactly as received
- preserve structure and wording
- avoid embellishment or simplification
- avoid additional context or explanation

Formatting MAY be applied,
but content MUST NOT change.

---

## 8. Termination Semantics

### 8.1 Return Control
Applies to:
- R1 (Refusal)

Meaning:
- user may issue a new request
- no system state is altered

---

### 8.2 Terminate Interaction
Applies to:
- R2 (Denial)

Meaning:
- current interaction ends
- no continuation within the same context
- system remains intact

---

### 8.3 Hard Stop
Applies to:
- F1 (Failure)

Meaning:
- immediate halt
- no recovery
- no further output
- no cleanup logic
- no explanation beyond the message itself

---

## 9. Prohibited Behavior

The routing layer MUST NOT:

- suppress messages
- merge multiple messages
- convert failures into refusals
- retry after F1
- explain message meaning
- emit raw errors or stack traces
- allow the CLI to improvise responses

Any such behavior is a governance violation.

---

## 10. Design-Time Constraint

This document:
- defines routing semantics only
- contains no implementation
- performs no execution
- performs no evaluation

It is enforced by:
- Refusal & Failure Messages (FAZA 24B)
- Claim Classification Model
- Knowledge Anchor Enforcement
- Governance Lock System

---

## 11. Closing Statement

Message routing is the **final line of trust**.

If the system fails to route lawfully:
- correct decisions become unreliable
- refusal becomes silence
- failure becomes confusion

No routing contract → no predictable system behavior.
