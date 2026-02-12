# HOI_STATE_MACHINE_SPEC_v0.1
Status: DRAFT  
Layer: HOI Execution Layer  
Scope: Deterministic State Machine Specification  
Compatibility: HOI_CANONICAL_STATE_OBJECT_SPEC_v0.1  

---

## 1. PURPOSE

This document defines the deterministic state machine governing the
`lifecycle.current_stage` field of the canonical HOI state object.

This specification:

- Defines enumerated states
- Defines legal transitions
- Defines transition guards (preconditions)
- Defines illegal transition handling
- Aligns stage invariants with canonical state object
- Defines append-only lifecycle history behavior
- Prohibits runtime learning or adaptive behavior
- Contains no advisory logic
- Contains no guard layer modifications

This is execution-layer only.

---

## 2. STATE ENUMERATION

The following states are canonical and exhaustive.

They MUST align exactly with:

`state.lifecycle.current_stage`

### 2.1 Enumerated States

1. INIT  
2. ACTIVE  
3. PAUSED  
4. COMPLETED  
5. TERMINATED  

No additional states are permitted.

---

## 3. STATE DEFINITIONS

### 3.1 INIT
- Initial state after canonical state object creation.
- No execution has occurred.
- history MUST contain exactly one entry: INIT.

### 3.2 ACTIVE
- Execution is in progress.
- System is operational.
- Deterministic evaluation allowed.

### 3.3 PAUSED
- Execution temporarily halted.
- No forward progression permitted.
- No evaluation occurs.

### 3.4 COMPLETED
- Execution finished successfully.
- Terminal state.
- No further transitions permitted.

### 3.5 TERMINATED
- Execution stopped irreversibly.
- Terminal state.
- No further transitions permitted.

---

## 4. LEGAL TRANSITIONS

All transitions are deterministic and finite.

### 4.1 Allowed Transitions

| From       | To          |
|------------|------------|
| INIT       | ACTIVE     |
| ACTIVE     | PAUSED     |
| ACTIVE     | COMPLETED  |
| ACTIVE     | TERMINATED |
| PAUSED     | ACTIVE     |
| PAUSED     | TERMINATED |

No other transitions are permitted.

---

## 5. TRANSITION GUARDS (PRECONDITIONS)

Transitions MUST satisfy deterministic preconditions.

### 5.1 INIT → ACTIVE
- Canonical state object exists
- lifecycle.history contains exactly one entry (INIT)
- No terminal flag set

### 5.2 ACTIVE → PAUSED
- lifecycle.current_stage == ACTIVE
- No terminal condition recorded

### 5.3 ACTIVE → COMPLETED
- Execution objective reached
- No invariant violations
- No termination flag

### 5.4 ACTIVE → TERMINATED
- Explicit termination event recorded
- Deterministic condition triggered

### 5.5 PAUSED → ACTIVE
- Explicit resume event recorded
- No terminal state reached

### 5.6 PAUSED → TERMINATED
- Explicit termination event recorded

Guards MUST be purely deterministic.
No probabilistic logic allowed.
No LLM evaluation allowed.

---

## 6. ILLEGAL TRANSITION HANDLING

If a transition request violates:

- Enumeration
- Transition table
- Guard preconditions
- Terminal immutability

Then:

1. Transition MUST be rejected.
2. lifecycle.current_stage MUST remain unchanged.
3. An error event MUST be appended to lifecycle.history.
4. No partial mutation permitted.

No silent correction allowed.
No auto-adjustment allowed.

---

## 7. TERMINAL STATE RULE

States COMPLETED and TERMINATED are terminal.

Once entered:

- lifecycle.current_stage is immutable.
- No further transitions permitted.
- Any attempted transition MUST trigger illegal transition handling.

---

## 8. STAGE INVARIANTS ALIGNMENT

Each state MUST preserve canonical invariants.

### INIT Invariant
- history length == 1
- first entry == INIT

### ACTIVE Invariant
- system not terminal
- execution permitted

### PAUSED Invariant
- execution halted
- no state mutation except resume or terminate

### COMPLETED Invariant
- execution closed
- immutable

### TERMINATED Invariant
- execution irreversibly stopped
- immutable

Invariants MUST be validated before and after transition.

---

## 9. DETERMINISTIC TRANSITION CONTRACT

The state machine MUST satisfy:

- Determinism (same input → same result)
- No runtime adaptation
- No memory of past transitions beyond history log
- No policy injection
- No advisory influence
- No learning
- No stochastic elements

Transition function is pure:

NextState = f(CurrentState, Event)

Where f is fully defined by this specification.

---

## 10. RELATIONSHIP TO CANONICAL STATE OBJECT

The state machine governs:

state.lifecycle.current_stage  
state.lifecycle.history  

It MUST NOT mutate:

- advisory fields
- guard layer structures
- configuration sections
- external modules

Only lifecycle fields are in scope.

---

## 11. APPEND-ONLY LIFECYCLE HISTORY LOGIC

Every legal transition MUST:

1. Append a new history entry
2. Include:
   - previous_state
   - new_state
   - deterministic event label
   - timestamp (external system-provided)
3. Preserve all prior entries

History is append-only.
No deletion.
No modification.
No compaction.
No summarization.

Illegal transition attempts MUST also append an error entry.

---

## 12. EXCLUDED CONCERNS

This specification does NOT include:

- Advisory logic
- Policy evaluation
- LLM-based decision making
- Runtime optimization
- Production constraints
- Guard layer logic
- Multi-agent behavior

Execution layer only.

---

## 13. LOCK READINESS

This document is LOCK-ready but currently marked:

Status: DRAFT

No extensions permitted without version increment.

---

END OF SPEC
