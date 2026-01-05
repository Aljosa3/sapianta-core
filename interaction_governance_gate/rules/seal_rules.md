# FILE: interaction_governance_gate/rules/seal_rules.md

## ADMISSIBILITY RULES — SEAL

### Rule S-1
The input structure is valid but incomplete.

### Rule S-2
The input contains opaque metadata not recognized by the gate.

### Rule S-3
The input is syntactically valid but ambiguous at the contract level.

### Outcome
If any SEAL rule is satisfied and no DENY rule applies,
the gate MUST emit decision SEAL.
