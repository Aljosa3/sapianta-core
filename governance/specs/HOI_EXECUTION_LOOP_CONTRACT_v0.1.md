# HOI_EXECUTION_LOOP_CONTRACT_v0.1
Status: LOCK  
Layer: HOI Execution Layer  
Scope: Deterministic Execution Loop Contract  
Compatibility:
- HOI_CANONICAL_STATE_OBJECT_SPEC_v0.1
- HOI_EVENT_MODEL_SPEC_v0.1
- HOI_STATE_MACHINE_SPEC_v0.1
- HOI_TRANSITION_VALIDATION_SPEC_v0.1

---

## 1. PURPOSE

This document defines the deterministic execution loop
that governs how HOI processes events.

It formalizes:

- Execution sequence
- Deterministic ordering
- Mutation boundaries
- Atomicity guarantees
- Rollback contract
- Side-effect prohibition
- Isolation guarantees

This specification defines how the execution kernel operates.

No LLM logic.
No advisory logic.
No adaptive behavior.

Execution-layer only.

---

## 2. EXECUTION LOOP OVERVIEW

The execution loop processes events sequentially.

Each event is processed independently and atomically.

Core principle:

Event → Validation → Transition → Post-Validation → History Append

No concurrent mutation permitted.
No parallel execution permitted.

---

## 3. SINGLE EVENT PROCESSING CONTRACT

For each event E:

1. Snapshot current state S₀
2. Execute validation pipeline
3. If validation fails:
   - Append failure record
   - Exit
4. Compute next state S₁
5. Validate post-transition invariants
6. Commit state mutation
7. Append history entry
8. Return deterministic result

Processing must be atomic.

---

## 4. ATOMICITY GUARANTEE

Execution of a single event MUST be:

- All-or-nothing
- Fully committed or fully rejected
- No partial mutation allowed

If failure occurs at any stage:

- State reverts to S₀
- No partial data remains

---

## 5. STATE MUTATION BOUNDARY

Only the following fields may be mutated:

- lifecycle.current_stage
- lifecycle.history

No other canonical state fields may be altered.

Execution loop MUST NOT mutate:

- advisory sections
- configuration sections
- guard-layer structures
- external modules

---

## 6. SEQUENTIAL PROCESSING REQUIREMENT

Events MUST be processed in strict sequence.

No:

- Out-of-order execution
- Parallel processing
- Event merging
- Event collapsing

Each event is isolated.

---

## 7. EVENT CONSUMPTION RULE

Event is considered consumed only after:

- Validation passes
- Transition applied
- History appended

If validation fails:

- Event recorded
- State unchanged
- Event still considered consumed

No retries.

---

## 8. ROLLBACK CONTRACT

If post-transition invariant check fails:

1. Abort mutation
2. Restore S₀
3. Record POST_INVARIANT_FAILURE
4. Append failure event

Rollback must be deterministic.

---

## 9. HISTORY APPEND ORDER

History MUST record:

1. Incoming event
2. Validation result
3. Transition result (if successful)
4. Failure classification (if any)

Entries MUST preserve strict chronological order.

Append-only.
No modification.
No deletion.

---

## 10. DETERMINISTIC RETURN CONTRACT

Execution loop returns a structured result:

- previous_state
- event_type
- validation_status
- new_state (if any)
- failure_type (if any)

Given identical (State, Event),
output MUST always be identical.

---

## 11. ISOLATION GUARANTEE

Execution loop MUST:

- Avoid shared mutable state
- Avoid global context dependency
- Avoid time-based branching
- Avoid external I/O dependency

Timestamp recording must be external input.

Execution loop is pure with respect to:

(State, Event) → (NewState, HistoryEntry)

---

## 12. SIDE-EFFECT PROHIBITION

Execution loop MUST NOT:

- Trigger advisory engine
- Invoke LLM
- Trigger external API
- Modify filesystem
- Send signals
- Emit asynchronous calls

Execution layer is computational only.

---

## 13. TERMINAL STATE BEHAVIOR

If state is:

- COMPLETED
- TERMINATED

Then:

- Only validation failure path allowed
- No state mutation allowed

Terminal immutability enforced.

---

## 14. ERROR PROPAGATION

Execution loop MUST NOT throw unhandled exceptions.

All errors MUST be converted into:

- Deterministic failure classification
- History append entry
- Stable state

No crash allowed.

---

## 15. DETERMINISTIC KERNEL COMPLETION

With:

- Canonical state object
- Event model
- State machine
- Validation layer
- Execution loop contract

The HOI execution kernel is fully defined.

No undefined behavior remains.

---

## 16. EXCLUDED CONCERNS

This specification does NOT include:

- Advisory evaluation
- Policy enforcement
- Business logic
- Runtime scaling
- Multi-agent orchestration

Execution-layer only.

---

## 17. LOCK READINESS

This document is LOCK-ready but currently marked:

Status: DRAFT

No extension permitted without version increment.

---

END OF SPEC

