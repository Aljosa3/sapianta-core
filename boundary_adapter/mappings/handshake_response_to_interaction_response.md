# FILE: boundary_adapter/mappings/handshake_response_to_interaction_response.md

## MAPPING: HANDSHAKE_RESPONSE → INTERACTION_RESPONSE

### Mapping Type
Structural, opaque forwarding

### Source
- handshake_response

### Target
- interaction_response

### Field Mapping
- handshake.request_id → interaction.request_id
- handshake.response_type → interaction.response_type
- handshake.timestamp → interaction.timestamp

### Visibility Rule
- core_visibility is NOT forwarded

### Guarantees
- No interpretation
- No explanation
- No augmentation
