# FILE: core_handshake/rules/allowed_directions.md

## ALLOWED COMMUNICATION DIRECTIONS

### Rule AD-1
Interaction MAY initiate a Handshake Request toward Core.

### Rule AD-2
The Handshake Request MUST conform exactly to the defined
Handshake Request type.

### Rule AD-3
Interaction MAY receive a Handshake Response from Core.

### Rule AD-4
Interaction MAY observe Handshake Status if exposed.

### Rule AD-5
All communication is ONE-WAY per message.
No bidirectional or conversational flow is permitted.

### Rule AD-6
Interaction MUST treat all Core-originated data as opaque.

### Rule AD-7
No retry, escalation, or fallback logic is allowed at this layer.
