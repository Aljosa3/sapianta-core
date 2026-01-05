# FILE: interaction_governance_gate/contracts/interaction_input.interface.md

## INTERFACE: INTERACTION → GOVERNANCE GATE

### Purpose
Define the only admissible input surface from the Interaction layer into
the Interaction Governance Gate.

### Authority
- Sender: Interaction
- Receiver: Interaction Governance Gate
- Interaction is NON-AUTHORITATIVE

### Accepted Type
- interaction_request (as defined in Interaction layer)

### Required Fields
- request_id: string (opaque)
- origin_layer: fixed value "interaction"
- timestamp: ISO-8601 string

### Optional Fields
- metadata: opaque structure (ignored by default)

### Gate Guarantees
- No field interpretation
- No field mutation
- No validation beyond structural presence

### Forbidden
- Execution intent
- Canon references
- Adapter or Handshake references
- State indicators or flags
