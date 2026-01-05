# FILE: interaction_governance_gate/contracts/gate_output.interface.md

## INTERFACE: GOVERNANCE GATE → DECISION

### Purpose
Define the only possible output of the Interaction Governance Gate.

### Authority
- Source: Interaction Governance Gate
- Consumer: Interaction layer

### Output Type
- governance_decision

### Allowed Decision Values
- ALLOW
- DENY
- SEAL

### Required Fields
- request_id: string (forwarded, opaque)
- decision: enum (ALLOW | DENY | SEAL)
- timestamp: ISO-8601 string

### Forbidden
- Reason codes
- Explanations
- Severity levels
- Retry instructions
- Escalation hints

### Notes
Decisions are declarative outcomes only and do not imply execution.
