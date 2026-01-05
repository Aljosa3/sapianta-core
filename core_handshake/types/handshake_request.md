# FILE: core_handshake/types/handshake_request.md

## HANDSHAKE TYPE: REQUEST

### Purpose
A Handshake Request represents a **formal declaration of intent**
from the Interaction layer toward the Core.

### Authority
- Sender: Interaction
- Receiver: Core
- Interaction is NON-AUTHORITATIVE

### Properties
- Declarative only
- Non-executable
- Non-inferential

### Required Fields
- request_id: opaque identifier (string)
- request_type: enum (DECLARED_INTENT only)
- origin_layer: fixed value "interaction"
- timestamp: ISO-8601 string

### Forbidden Characteristics
- No parameters affecting Core behavior
- No execution flags
- No Canon references
- No conditional logic

### Notes
The request does not imply acceptance, processing, or understanding by Core.
