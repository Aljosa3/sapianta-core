# STATUS INITIALIZATION RULE

## Purpose
This document defines the single authoritative point where
ExecutionContext.status may transition from PENDING to ALLOW.

---

## Rule

ExecutionContext.status SHALL transition to Status.ALLOW
exclusively within the runtime guard layer.

No SP pass, orchestrator logic, execution code, or explain/audit
component is permitted to set Status.ALLOW.

---

## Lifecycle

1. ExecutionContext is initialized with:
   - status = PENDING
   - phase = INIT

2. runtime_guards(ctx):
   - performs pre-execution validation
   - MAY set:
     - ctx.status = Status.ALLOW
     - ctx.phase = Phase.EXECUTION

3. Orchestrator execution proceeds ONLY if:
   - status == ALLOW
   - phase == EXECUTION

Any deviation from this lifecycle is invalid.

---

## Lock Level
This rule is a core semantic constraint.
Violations indicate an invalid execution path.
