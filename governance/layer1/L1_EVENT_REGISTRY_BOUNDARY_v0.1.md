# SAPIANTA — Layer 1 Boundary: Event Registry Enforcement (v0.1)

## Status
- Layer 0: SEALED / FROZEN @ v1.2.7
- Layer 1: LOCKED (Closed Event Domain)
- Autonomy Level: A0

---

# 1. Purpose

Layer 1 defines and enforces the closed Event Domain of SAPIANTA.

It guarantees that only explicitly declared events may exist in the system.

---

# 2. Responsibility

Layer 1:

- Owns the authoritative Event Registry
- Enforces closed-domain semantics
- Guarantees fail-closed behavior for unknown events
- Prevents implicit event creation
- Provides deterministic validation via CI

Layer 1 controls event admissibility.

---

# 3. Enforcement Artifacts

1. Registry file:
   governance/registry/EVENT_REGISTRY_v0.1.json

2. Registry validator:
   scripts/validation/validate_event_registry.py

3. Pre-commit enforcement

---

# 4. Out of Scope

Layer 1 does NOT:

- Control how events are referenced in runtime code
- Modify runtime execution
- Introduce event dispatch logic
- Expand autonomy

Event reference discipline is handled by Layer 1.1.

---

# 5. Architectural Position

Hierarchy:

Layer 0 → Deterministic Execution Kernel
Layer 1 → Closed Event Domain

Layer 1 is governance-only and static.

---

END OF DOCUMENT
