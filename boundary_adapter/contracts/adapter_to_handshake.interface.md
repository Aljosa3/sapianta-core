# FILE: boundary_adapter/contracts/adapter_to_handshake.interface.md

## INTERFACE: ADAPTER → HANDSHAKE

### Purpose
Define the only allowed output surface from Boundary Adapter toward Core Handshake.

### Authority
- Sender: Boundary Adapter
- Receiver: Core Handshake
- Adapter is NON-AUTHORITATIVE

### Emitted Type
- handshake_request (Phase 07)

### Required Fields
- request_id: string (forwarded, opaque)
- request_type: fixed enum value DECLARED_INTENT
- origin_layer: fixed value "interaction"
- timestamp: ISO-8601 string

### Mapping Rule
- Fields MUST be mapped 1:1 where names overlap
- Fields without a target MUST be dropped
- No new fields may be introduced

### Forbidden
- Field enrichment
- Semantic transformation
- Canon linkage
