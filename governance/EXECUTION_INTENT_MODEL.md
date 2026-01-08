# EXECUTION_INTENT_MODEL

## Status
- Phase: FAZA 27A
- Type: Governance / Design-to-Technical Bridge
- Execution: Forbidden
- Intent state: Declarative only
- Lock state: NOT LOCKED

---

## 1. Purpose

This document defines the **Execution Intent Model**.

It answers the question:

> How does the system represent an intention to execute **without executing**?

The goal is to:
- formally separate *intent* from *execution*
- allow technical preparation without side effects
- make execution readiness inspectable
- prevent accidental or implicit execution

Execution Intent is **not action**.  
Execution Intent is **structure**.

---

## 2. Core Principle

An **Execution Intent** represents a *hypothetical desire to execute*,
expressed in a structured, inspectable, and non-operative form.

Rules:
- Intent MUST NOT cause side effects
- Intent MUST NOT cross the Execution Gate
- Intent MUST be rejectable, inspectable, and exportable
- Intent MAY be refused, denied, or failed like any other claim

Intent without permission remains intent.

---

## 3. What Execution Intent Is (and Is Not)

### Execution Intent IS:
- a declarative object
- a candidate for evaluation
- input to governance checks
- input to dry-run planning

### Execution Intent IS NOT:
- execution
- simulation with effects
- implicit approval
- deferred execution

No intent implies permission.  
No permission implies execution.

---

## 4. Execution Intent Entity

ExecutionIntent
├── intent_id: string
├── declared_by: authority_id
├── intent_type: execution | dry_run | inspection
├── target_scope: string
├── requested_action: string
├── parameters: map<string, any>
├── declared_at: timestamp
├── anchor_bindings: [AnchorBinding]
├── authority_binding: AuthorityReference
├── execution_state: declared | refused | denied | eligible

---

## 5. Field Definitions

### 5.1 intent_id
Unique identifier for the intent.

- MUST be unique
- MUST be immutable
- Used for traceability and audit

---

### 5.2 declared_by
Authority that declared the intent.

- MUST reference a valid Authority
- Subject to Authority Verification (FAZA 26)

---

### 5.3 intent_type
Defines what kind of intent is being expressed.

Allowed values:
- execution — request to execute (will be blocked pre-gate)
- dry_run — request to evaluate execution hypothetically
- inspection — request to inspect execution readiness

---

### 5.4 target_scope
Human-readable identifier of *what* would be affected.

Examples:
- module name
- resource identifier
- abstract execution domain

---

### 5.5 requested_action
Description of the desired operation.

Rules:
- MUST be descriptive
- MUST NOT trigger behavior
- Used only for evaluation and messaging

---

### 5.6 parameters
Key-value parameters for the requested action.

Rules:
- Pure data only
- No callable references
- No executable payloads

---

### 5.7 anchor_bindings
Knowledge Anchors that justify the intent.

Rules:
- REQUIRED for binding intents
- Evaluated using FAZA 23 enforcement rules
- Missing anchors default to refusal (E2)

---

### 5.8 authority_binding
Reference to the authority claiming the intent.

Rules:
- Evaluated before eligibility
- Invalid authority → Denial (R2)

---

### 5.9 execution_state
Current governance-evaluated state of the intent.

Allowed values:
- declared — intent registered
- refused — failed governance or anchors
- denied — authority or phase restriction
- eligible — would be executable **if gate opened**

Eligible ≠ Executed.

---

## 6. Evaluation Flow (Non-Executable)

1. Intent declared
2. Anchor bindings validated
3. Authority verified
4. Execution eligibility evaluated
5. Execution Gate checked
6. State resolved

At no point does execution occur.

---

## 7. Failure and Refusal Handling

Execution Intent participates fully in:
- Claim Classification
- Refusal & Failure Messages
- Message Routing

Examples:
- Missing anchor → R1 Refusal
- Invalid authority → R2 Denial
- Gate bypass attempt → F1 Failure

---

## 8. Design-Time Constraint

This model:
- defines representation only
- performs no execution
- performs no simulation
- performs no side effects

It is consumed by:
- Dry-Run Planning (FAZA 27B)
- Execution Boundary Adapter (FAZA 27C)

---

## 9. Closing Statement

Execution Intent is **permission-aware desire**, not action.

The system may understand intent.
The system may evaluate intent.
The system may reject intent.

The system MUST NOT execute intent.

Intent ends at the gate.
