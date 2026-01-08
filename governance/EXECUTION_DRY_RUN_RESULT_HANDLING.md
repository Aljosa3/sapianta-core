# Execution Dry-Run Result Handling & Messaging

## Status
- Phase: FAZA 27C
- Type: Governance / Design-only
- Execution: Forbidden
- Handling mode: Read-only
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines **how results of Execution Dry-Run evaluation are handled,
communicated, and propagated** through the system.

It answers the question:

> Once eligibility is evaluated, how does the system respond — and what happens next?

The goal is to:
- make dry-run outcomes actionable
- ensure consistent messaging
- prevent silent failures
- guarantee deterministic follow-up behavior

---

## 2. Core Principle

Every Dry-Run MUST produce **exactly one terminal result**.

That result:
- MUST be surfaced to the caller
- MUST map to a defined message type
- MUST determine whether execution is allowed to proceed

No ambiguous or partial outcomes are permitted.

---

## 3. Dry-Run Outcomes

Dry-Run may yield exactly one of the following outcomes:

| Result     | Meaning |
|------------|---------|
| ELIGIBLE   | Execution may proceed (subject to final gate) |
| REFUSED    | Execution is invalid but correctable |
| DENIED     | Execution is blocked by authority or phase |
| FAILED     | Fatal violation — system integrity risk |

---

## 4. Outcome → Message Mapping

Each outcome MUST map to a single message category:

| Dry-Run Result | Message Type |
|----------------|--------------|
| ELIGIBLE       | Success (no refusal message) |
| REFUSED        | R1 — Refusal |
| DENIED         | R2 — Denial |
| FAILED         | F1 — Failure |

The system MUST NOT invent new message types.

---

## 5. ELIGIBLE Handling

### Meaning
- All eligibility checks passed
- No normative violations detected

### System behavior
- MUST explicitly state eligibility
- MUST NOT execute automatically
- MUST require explicit execution invocation

### Output requirements
- eligibility confirmation
- summary of checks passed
- timestamped evaluation context

---

## 6. REFUSED Handling (R1)

### Meaning
- Execution intent is invalid in current form
- User may correct or reattempt

### System behavior
- MUST return an R1 Refusal message
- MUST specify blocking stage
- MUST include correction hints when possible

### Post-handling state
- Execution remains forbidden
- Dry-run may be reattempted after correction

---

## 7. DENIED Handling (R2)

### Meaning
- Execution is valid in theory
- Authority, phase, or permission is insufficient

### System behavior
- MUST return an R2 Denial message
- MUST specify denied scope
- MUST NOT suggest workarounds that bypass authority

### Post-handling state
- Execution remains forbidden
- Only authority change or phase transition may unblock

---

## 8. FAILED Handling (F1)

### Meaning
- A system-critical invariant was violated
- Integrity or safety is at risk

### System behavior
- MUST emit an F1 Failure message
- MUST hard-stop processing
- MUST NOT continue evaluation or interaction

### Post-handling state
- System enters halted or protected mode
- Human intervention may be required

---

## 9. Escalation Rules

Some outcomes may require escalation.

Rules:
- FAILED → escalation_required = true
- DENIED → escalation_required = optional (policy-defined)
- REFUSED → escalation_required = false
- ELIGIBLE → escalation_required = false

Escalation mechanisms are defined outside this document.

---

## 10. Prohibited Behavior

The system MUST NOT:
- downgrade FAILED to REFUSED or DENIED
- auto-execute after ELIGIBLE
- hide blocking reasons
- emit unstructured messages
- allow execution without explicit confirmation

---

## 11. Relationship to CLI and Interfaces

All interfaces (CLI, API, UI):
- MUST surface dry-run results verbatim
- MUST NOT reinterpret outcome semantics
- MAY format output, but not alter meaning

---

## 12. Closing Statement

Dry-Run results are **decisions**, not suggestions.

If execution is blocked:
- the system must say why
- the system must say at which stage
- the system must not proceed

Eligibility without discipline is danger.

Dry-run handling is the last line of safety.
