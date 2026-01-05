# FILE: core_handshake/types/handshake_status.md

## HANDSHAKE TYPE: STATUS

### Purpose
A Handshake Status represents the **non-semantic availability state**
of the Core handshake surface.

### Authority
- Source: Core (implicit)
- Consumer: Interaction

### Properties
- Passive
- Read-only
- Non-contextual

### Allowed States
- AVAILABLE
- UNAVAILABLE
- SEALED

### Forbidden Characteristics
- No cause description
- No duration guarantees
- No recovery hints
- No Canon linkage

### Notes
Status communicates presence only, never capability.
