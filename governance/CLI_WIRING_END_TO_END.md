# CLI_WIRING_END_TO_END

## Status
- Phase: FAZA 24C.3
- Type: Governance / Design-only
- Execution: Forbidden
- Wiring state: Mandatory
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **end-to-end wiring** of the SAPIANTA CLI.

It answers the question:

> How does a user request flow through the system — from input to lawful output?

The goal is to:
- make the CLI behavior fully predictable
- expose every decision boundary
- prevent hidden shortcuts
- ensure refusals and failures propagate correctly

This document defines **flow**, not logic.

---

## 2. High-Level Flow Overview

The CLI follows a **strict linear pipeline**:

1. User Input
2. Claim Classification
3. Anchor Binding Validation
4. Message Routing
5. CLI Output Adapter
6. Terminal Output

No step may be skipped.
No step may be reordered.

---

## 3. Step-by-Step Flow Definition

### 3.1 User Input

- Input is received as raw text
- No interpretation occurs at this stage
- Input is treated as untrusted

The CLI MUST NOT:
- assume intent
- assume execution
- infer permissions

---

### 3.2 Claim Classification

The input is classified according to the **Claim Classification Model**.

Possible outcomes:
- C0 — Informational
- C1 — Clarification
- C2 — Binding claim
- C3 — Planning request
- C4 — Execution attempt

Classification MUST occur before any reasoning or planning.

---

### 3.3 Anchor Binding Validation

If the claim type is **C2, C3, or C4**:

- Anchor bindings are REQUIRED
- Bindings are validated structurally
- Enforcement levels are evaluated

Possible outcomes:
- Valid → continue
- Missing / invalid → R1 Refusal
- E3 violation → F1 Failure

No reasoning proceeds without valid anchors.

---

### 3.4 Message Routing

Based on the validated result, the system selects exactly one message path:

- Success output
- R1 — Refusal
- R2 — Denial
- F1 — Failure

Routing MUST be deterministic.

The router:
- selects message type
- populates required fields
- performs no rendering

---

### 3.5 CLI Output Adapter

The routed Message Object is passed to the **CLI Output Adapter**.

The adapter:
- renders the message verbatim
- selects stdout or stderr
- applies formatting only

The adapter MUST NOT:
- modify meaning
- suppress content
- add explanation

---

### 3.6 Terminal Output

The final rendered output is displayed to the user.

Additionally:
- exit code is emitted
- process terminates immediately after output

No further processing occurs.

---

## 4. Refusal & Failure Propagation Rules

- R1 and R2 MUST terminate the pipeline
- F1 MUST hard-stop immediately
- No downstream recovery is allowed

Failures override all other outputs.

---

## 5. Determinism Guarantees

Given the same:
- input
- system state
- governance locks

The CLI MUST produce:
- the same message type
- the same content
- the same exit code

Non-determinism is forbidden.

---

## 6. Prohibited Shortcuts

The CLI MUST NOT:

- bypass claim classification
- bypass anchor validation
- render messages directly
- catch and suppress failures
- convert failures into refusals
- continue after message emission

Any shortcut is a governance breach.

---

## 7. Design-Time Constraint

This document:
- defines wiring only
- contains no algorithms
- contains no implementation code
- performs no evaluation
- performs no execution

It is enforced by:
- Claim Classification Model
- Knowledge Anchor System
- Refusal & Failure Messages
- CLI Output Adapter

---

## 8. Closing Statement

The CLI is not an interface.

It is a **legal corridor**.

Every word that exits it has passed:
- classification
- law
- enforcement
- routing
- rendering

If one step is skipped:
- refusal becomes opinion
- failure becomes silence
- authority collapses

End-to-end means end-to-end.
