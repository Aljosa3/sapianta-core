# SAPIANTA — Deterministic Control Layer Specification (v0.1)

## Status
- Layer 0: SEALED @ v1.2.7
- Layer 1: Event Registry Enforcement LOCKED
- Layer 1.1: Event Reference Discipline LOCKED
- Layer 2: INTRODUCED (this document)

Autonomy Level: A0 (no expansion)

---

## 1. Purpose

Layer 2 introduces the Deterministic Control Layer (DCL).

The DCL is a runtime supervision layer positioned above the Deterministic Governance Substrate.

Its purpose is to:

- Deterministically evaluate events
- Enforce state transition legality
- Enforce policy decisions
- Fail closed on violations
- Produce structured audit traces

The DCL does NOT:

- Modify Layer 0 semantics
- Introduce implicit behavior
- Introduce nondeterminism
- Expand autonomy
- Perform inference or interpretation

---

## 2. Architectural Position

External System (Domain System)
        ↓
Deterministic Control Layer (Layer 2)
        ↓
Deterministic Governance Substrate (Layer 0–1.1)

Layer 2 is domain-agnostic.

It operates purely on:

- Declared state model
- Declared event registry
- Declared policy evaluator

---

## 3. Core Components (v0.1)

### 3.1 ControlEngine

Central orchestrator.

Responsibilities:

- Accept (current_state, event, payload)
- Validate event against registry (Layer 1)
- Validate transition legality
- Invoke PolicyEvaluator
- Execute deterministic transition
- Produce audit trace
- Return structured outcome

Must be:

- Deterministic
- Side-effect free (except audit emission)
- Stateless beyond explicit input/output

---

### 3.2 StateTransitionExecutor

Pure deterministic mapping:

(current_state, event) → next_state

If mapping does not exist:
→ FAIL-CLOSED
→ Transition to ERROR

No dynamic mutation allowed.

---

### 3.3 PolicyEvaluator

Pure deterministic rule engine.

Input:
- event
- payload
- context

Output:
- ALLOW
- OVERRIDE(new_event)
- REJECT

Constraints:

- No I/O
- No randomness
- No LLM
- No implicit defaults
- Deterministic output for identical inputs

---

### 3.4 AuditTraceCollector

Produces structured trace:

- previous_state
- input_event
- policy_decision
- next_state
- outcome_status
- timestamp (deterministic source required)

Audit trace must not mutate runtime behavior.

---

## 4. Execution Semantics

Execution flow:

1. Receive event
2. Validate event domain
3. Validate transition legality
4. Evaluate policy
5. Possibly override event
6. Execute final transition
7. Emit audit trace
8. Return structured result

Any violation:
→ Immediate FAIL-CLOSED
→ ERROR state

No fallback allowed.

---

## 5. Fail-Closed Rules

The system MUST fail closed if:

- Event is not in registry
- Transition is undefined
- Policy returns invalid instruction
- Policy attempts undefined override
- Runtime invariant is violated

FAIL-CLOSED means:

- No partial execution
- No recovery attempt
- No implicit downgrade
- Immediate transition to ERROR

---

## 6. Determinism Requirements

Layer 2 MUST satisfy:

- Identical input → identical output
- No time-based branching
- No hidden global state
- No nondeterministic ordering
- No concurrency in v0.1

---

## 7. Out of Scope (v0.1)

The following are explicitly excluded:

- Multi-agent orchestration
- Distributed execution
- Persistence layer
- Dynamic policy loading
- DSL-based policy language
- Role-based access control
- Scheduling engine
- External API integration
- Asynchronous processing

These belong to Phase L2.4+.

---

## 8. Invariants

1. ControlEngine never creates new events.
2. PolicyEvaluator never mutates state directly.
3. StateTransitionExecutor is pure mapping.
4. AuditTraceCollector never influences execution outcome.
5. Layer 2 never modifies Layer 0 behavior.

---

## 9. Minimal API Contract (v0.1)

Example interface:

engine.handle_event(
    current_state: str,
    event: str,
    payload: dict
) → {
    "next_state": str,
    "status": str,  # ALLOWED | OVERRIDDEN | REJECTED | ERROR
    "audit_trace": dict
}

---

## 10. Versioning

- Spec Version: v0.1
- Deterministic Contract: LOCK required after first implementation
- Future revisions require formal governance decision

