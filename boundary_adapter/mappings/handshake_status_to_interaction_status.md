# FILE: boundary_adapter/mappings/handshake_status_to_interaction_status.md

## MAPPING: HANDSHAKE_STATUS → INTERACTION_STATUS

### Mapping Type
Presence-only forwarding

### Source
- handshake_status

### Target
- interaction_status

### Field Mapping
- handshake.state → interaction.state

### Drop Rules
- Any metadata is dropped

### Guarantees
- No capability inference
- No availability guarantees
