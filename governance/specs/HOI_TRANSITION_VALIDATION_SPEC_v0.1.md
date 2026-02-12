# HOI_TRANSITION_VALIDATION_SPEC_v0.1
Status: LOCK  
Layer: HOI Execution Layer  
Scope: Deterministic Transition Validation  
Compatibility:
- HOI_CANONICAL_STATE_OBJECT_SPEC_v0.1
- HOI_STATE_MACHINE_SPEC_v0.1
- HOI_EVENT_MODEL_SPEC_v0.1

---

## 1. PURPOSE

This document defines the deterministic validation layer that governs:

Event → State Transition execution

It formalizes:

- Validation order
- Pre-transition validation
- Guard evaluation
- Post-transition invariant validation
- Failure handling contract
- Deterministic error generation

This layer contains no advisory logic.
No LLM involvement.
No adaptive behavior.

Execution-layer only.

---

## 2. VALIDATION LAYER ROLE

The validation layer sits between:

Event ingestion
and
State mutation

It MUST:

1. Validate event structure
2. Validate event enumeration
3. Validate state compatibility
4. Validate transition legality
5. Validate guard conditions
6. Validate terminal immutability
7. Validate post-transition invariants

Only if ALL checks pass may mutation occur.

---

## 3. VALIDATION ORDER (STRICT)

Validation MUST occur in the following order:

1. Event structural validation
2. Event enumeration validation
3. Terminal state check
4. Transition table validation
5. Guard condition validation
6. Pre-transition invariant validation
7. Execute transition
8. Post-transition invariant validation
9. Append history entry

Order is fixed.
Reordering is not permitted.

---

## 4. EVENT STRUCTURAL VALIDATION

Event MUST contain:

- event_type
- source
- timestamp

Optional:
- correlation_id
- metadata

If missing required fields → validation failure.

No partial acceptance permitted.

---

## 5. ENUMERATION VALIDATION

event_type MUST match allowed enumeration defined in:

HOI_EVENT_MODEL_SPEC_v0.1

Unknown event → validation failure.

---

## 6. TERMINAL STATE CHECK

If lifecycle.current_stage is:

- COMPLETED
- TERMINATED

Then:

- No transition permitted
- Validation fails
- Illegal transition handling triggered

Terminal immutability is absolute.

---

## 7. TRANSITION TABLE VALIDATION

Current state and event MUST match allowed mapping
defined in:

HOI_STATE_MACHINE_SPEC_v0.1
HOI_EVENT_MODEL_SPEC_v0.1

If mapping invalid → validation failure.

No fallback mapping allowed.
No implicit transition allowed.

---

## 8. GUARD CONDITION VALIDATION

Guard conditions defined in:

HOI_STATE_MACHINE_SPEC_v0.1

MUST be evaluated deterministically.

Guards MUST NOT:

- Query external systems
- Use stochastic logic
- Use LLM logic
- Mutate state

If guard fails → validation failure.

---

## 9. PRE-TRANSITION INVARIANT CHECK

Current state MUST satisfy invariant
defined for lifecycle.current_stage.

If invariant violated → hard validation failure.

No auto-repair allowed.

---

## 10. POST-TRANSITION INVARIANT CHECK

After mutation:

New state MUST satisfy invariant
defined for target state.

If violated:

- Transition MUST be rolled back
- Validation failure recorded
- State remains unchanged

No partial state permitted.

---

## 11. FAILURE HANDLING CONTRACT

If ANY validation step fails:

1. lifecycle.current_stage remains unchanged
2. ILLEGAL_TRANSITION_ATTEMPT event generated
3. Failure reason recorded
4. lifecycle.history appended
5. No other mutation allowed

Failure handling is deterministic.

No silent failure allowed.
No retries.
No auto-correction.

---

## 12. ERROR CLASSIFICATION

Validation failures are classified as:

- STRUCTURAL_ERROR
- ENUMERATION_ERROR
- TERMINAL_STATE_ERROR
- TRANSITION_MAPPING_ERROR
- GUARD_FAILURE
- PRE_INVARIANT_FAILURE
- POST_INVARIANT_FAILURE

Classification MUST be explicit and recorded.

---

## 13. DETERMINISTIC CONTRACT

Given:

(CurrentState, Event)

Validation result MUST always be identical.

No hidden context allowed.
No external dependency allowed.
No time-based branching allowed.

Validation function is pure.

---

## 14. RELATIONSHIP TO STATE MACHINE

State machine defines allowed transitions.
Event model defines allowed inputs.
Validation layer enforces correctness.

Validation layer MUST NOT:

- Introduce new states
- Modify transition table
- Inject advisory logic

It only enforces.

---

## 15. EXCLUDED CONCERNS

This specification does NOT include:

- Advisory evaluation
- Policy evaluation
- Guard layer modifications
- Runtime optimization
- Production deployment constraints

Execution-layer only.

---

## 16. LOCK READINESS

This document is LOCK-ready but currently marked:

Status: DRAFT

No extension permitted without version increment.

---

END OF SPEC
