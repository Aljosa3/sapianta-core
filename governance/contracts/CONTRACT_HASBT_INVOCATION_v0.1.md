# CONTRACT_HASBT_INVOCATION_v0.1

Status: LOCKED  
Phase: IMPLEMENTATION  
Applies to: sapianta_chat build pipeline  
Effective from: PHASE_SELF_BUILD_IMPLEMENTATION_INIT_v0.1  

---

## 1. PURPOSE

This contract defines the **canonical and exclusive rules** for invoking
HASBT (Human Authorization Step Before Transformation) during the
SAPIANTA self-build pipeline.

This contract does NOT:
- unlock self-build
- grant execution rights
- modify WRITE-GATE behavior
- introduce new authority

Its sole purpose is to **constrain and freeze** the HASBT invocation surface.

---

## 2. INVOCATION AUTHORITY

HASBT MAY ONLY be invoked by:

- `sapianta_chat.cli.build_flow.run_build_pipeline()`

No other module, CLI command, test harness, or runtime component
is authorized to invoke HASBT.

Any other invocation is INVALID by definition.

---

## 3. INVOCATION POSITION (CANONICAL)

HASBT invocation MUST occur:

1. AFTER:
   - all normative decisions are loaded
   - configuration is resolved

2. BEFORE:
   - any Claude / LLM execution
   - any WRITE-GATE reachable path
   - any artifact generation
   - any transformation logic

This position is LOCKED by:
- DECISION_HASBT_INSERTION_POINT_v0.1

---

## 4. PAYLOAD SOURCE AND SHAPE

The HASBT payload:

- MUST be explicitly provided by the human operator
- MUST conform to the LOCKED HASBT payload schema
- MUST NOT be auto-generated
- MUST NOT be inferred
- MUST NOT be modified by the system

If the payload is missing, malformed, or incomplete:
→ HASBT MUST DENY.

---

## 5. INVOCATION SEMANTICS

### 5.1 PASS

If `evaluate_hasbt(payload)` returns cleanly:

- execution MAY continue
- no state change is implied
- no authorization is persisted
- no unlock is granted

PASS is **local to this execution only**.

---

### 5.2 DENY (FAIL-CLOSED)

If `evaluate_hasbt(payload)` raises `HASBTDeny`:

- execution MUST abort immediately
- the exception MUST propagate
- no retry is allowed
- no fallback is allowed
- no alternative path is permitted

DENY is:
- terminal
- irreversible
- auditable

---

## 6. PROHIBITED BEHAVIOR

The following are STRICTLY FORBIDDEN:

- catching and suppressing `HASBTDeny`
- retrying HASBT evaluation
- auto-confirming authorization
- deriving authorization implicitly
- invoking HASBT conditionally
- invoking HASBT more than once per execution
- invoking HASBT after any WRITE possibility

Any such behavior constitutes a governance violation.

---

## 7. NON-GOALS (EXPLICIT)

HASBT invocation in this phase does NOT perform:

- identity verification
- cryptographic validation
- temporal validation
- permission escalation
- persistence of authorization
- unlocking of self-build

Those concerns are out of scope and remain LOCKED.

---

## 8. FINAL LOCK STATEMENT

This contract LOCKS the HASBT invocation surface.

No code change may alter:
- who invokes HASBT
- where it is invoked
- how DENY is handled
- the absence of side effects

Any deviation requires a new DECISION document.

---

LOCK CONFIRMATION:
Self-build remains LOCKED.
WRITE-GATE remains unchanged.
HASBT invocation is constrained but NOT yet implemented in code.
