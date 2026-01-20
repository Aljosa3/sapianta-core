# IGL-GR-005 — No Exception-Driven Logic

Status: DRAFT  
Scope: SRS (Implementation Guard Layer)

## Rule
Exceptions MUST NOT be used as a primary control-flow mechanism in
implementation code.

## Rationale
Exception-driven logic obscures execution intent, hides decision points,
and creates implicit behavior that is difficult to statically review.
In a governed system, control flow must be explicit and intentional.

## Enforcement
The following are DISALLOWED in SRS implementation code:
- using `try/except` blocks to select normal execution paths
- suppressing exceptions to infer state or intent
- relying on raised exceptions to trigger alternative logic branches

The following are ALLOWED:
- using exceptions strictly for error signaling
- catching exceptions only to:
  - log
  - rethrow
  - translate into explicit error states handled elsewhere

Exception handling MUST NOT replace explicit condition checks.

## Examples (Non-exhaustive)

### ALLOWED
- Explicit condition checks followed by clear branching
- Exceptions raised to indicate irrecoverable errors

### DISALLOWED
- `try/except` used instead of `if` conditions
- Logic that depends on whether an exception occurred to proceed
