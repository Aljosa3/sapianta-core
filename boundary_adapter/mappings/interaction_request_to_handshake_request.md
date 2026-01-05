# FILE: boundary_adapter/mappings/interaction_request_to_handshake_request.md

## MAPPING: INTERACTION_REQUEST → HANDSHAKE_REQUEST

### Mapping Type
Structural, non-semantic

### Source
- interaction_request

### Target
- handshake_request

### Field Mapping
- interaction.request_id → handshake.request_id
- interaction.timestamp → handshake.timestamp
- interaction.origin_layer → handshake.origin_layer

### Fixed Assignment
- handshake.request_type = DECLARED_INTENT

### Drop Rules
- interaction.payload is NOT forwarded
- Any unknown fields are dropped

### Guarantees
- Deterministic
- Idempotent
- No inference
