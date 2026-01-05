# FILE: controlled_output/rules/output_constraints.md

## CONTROLLED OUTPUT — CONSTRAINTS

### Purpose
Define strict constraints governing controlled output declarations
to ensure output remains inert, non-operational, and non-authoritative.

### Constraints
- Expression Only: output may exist only as an expression
- No Actionability: output MUST NOT enable or suggest actions
- No Intent Coupling: output MUST NOT form, imply, or validate intent
- No Authorization Semantics: output MUST NOT imply permission or approval
- No Targeting: output MUST NOT reference systems, components, or resources
- No State Influence: output MUST NOT alter or depend on system state

### Invariants
- Execution remains forbidden regardless of output
- Output has zero operational effect
- No downstream component may act on output in Phase 15

### Stability
- Constraints are immutable within Phase 15
