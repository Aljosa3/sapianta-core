# FILE: core_handshake/types/handshake_response.md

## HANDSHAKE TYPE: RESPONSE

### Purpose
A Handshake Response represents an **opaque acknowledgment**
originating from Core toward Interaction.

### Authority
- Sender: Core
- Receiver: Interaction
- Core authority is NOT inspectable

### Properties
- Opaque
- Non-explanatory
- Non-interpretable

### Required Fields
- request_id: opaque identifier (string)
- response_type: enum (ACK | NACK | UNAVAILABLE)
- core_visibility: enum (OPAQUE only)
- timestamp: ISO-8601 string

### Forbidden Characteristics
- No reasoning
- No explanations
- No semantic payload
- No Canon exposure

### Notes
The Interaction layer must not infer meaning beyond the declared type.
