# FILE: execution_intent/rules/intent_constraints.md

## EXECUTION INTENT — CONSTRAINTS

### Purpose
Define strict constraints governing the declaration of execution intent
to ensure it remains non-operational and non-authoritative.

### Constraints
- Declaration Only: intent may exist only as a declaration
- No Parameters: intent MUST NOT include inputs, arguments, or payloads
- No Targets: intent MUST NOT reference systems, resources, or components
- No Conditions: intent MUST NOT include conditions or prerequisites
- No Timing: intent MUST NOT include scheduling or temporal markers
- No Scope Expansion: intent MUST NOT imply authorization or readiness

### Invariants
- Execution remains forbidden regardless of intent declaration
- Intent declaration has zero operational effect
- No downstream component may act on intent in Phase 13

### Stability
- Constraints are immutable within Phase 13
