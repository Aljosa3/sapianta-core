# FILE: execution_intent/rules/forbidden_intent.md

## EXECUTION INTENT — FORBIDDEN FORMS

### Purpose
Explicitly enumerate forms of intent declaration that are prohibited
to prevent implicit execution or authorization semantics.

### Forbidden Forms
An execution intent declaration MUST NOT:
- Include executable code or pseudo-code
- Include commands, actions, or verbs implying execution
- Reference execution gates, authorization mechanisms, or approvals
- Reference Core, Handshake, Adapter, Governance Gate, or System Flow
- Encode state transitions or lifecycle changes
- Embed implicit consent, permission, or readiness signals

### Enforcement Note
- No enforcement mechanism is defined in Phase 13
- Presence of forbidden forms constitutes a Phase 13 breach

### Stability
- Forbidden forms are immutable within Phase 13
