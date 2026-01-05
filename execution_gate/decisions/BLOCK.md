# FILE: execution_gate/decisions/BLOCK.md

## GATE DECISION: BLOCK

### Definition
BLOCK is a declarative gate outcome indicating that a request
is structurally prevented from passing the Execution Gate.

### Nature
- Declarative only
- Non-operational
- Non-authoritative

### Effect
- No execution is enabled
- No permission is granted
- No remediation is provided

### Guarantees
- Deterministic blocking
- No side effects

### Explicit Non-Implications
BLOCK MUST NOT imply:
- Error semantics
- Retry capability
- Escalation
