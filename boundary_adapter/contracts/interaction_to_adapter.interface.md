# FILE: boundary_adapter/contracts/interaction_to_adapter.interface.md

## INTERFACE: INTERACTION → ADAPTER

### Purpose
Define the only allowed input surface from Interaction into the Boundary Adapter.

### Authority
- Sender: Interaction
- Receiver: Boundary Adapter
- Interaction is NON-AUTHORITATIVE

### Accepted Type
- interaction_request (as defined in Interaction layer)

### Required Fields
- request_id: string (opaque)
- origin_layer: fixed value "interaction"
- timestamp: ISO-8601 string
- payload: opaque structure

### Adapter Guarantees
- No field interpretation
- No field mutation
- No validation beyond structural presence

### Forbidden
- Execution intent
- Canon references
- Conditional flags
- State indicators
