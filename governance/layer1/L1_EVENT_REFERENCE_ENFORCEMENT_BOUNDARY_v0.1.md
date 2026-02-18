# SAPIANTA — Layer 1.1 Boundary: Event Reference Enforcement (v0.1)

## Status
- Layer 0: SEALED @ v1.2.7
- Layer 1: LOCKED (Closed Event Domain)
- Layer 1.1: INTRODUCED
- Autonomy Level: A0

---

# 1. Purpose

Layer 1.1 enforces discipline over how events are referenced in runtime code.

Layer 1 defines which events may exist.
Layer 1.1 defines how they may be referenced.

---

# 2. Problem Addressed

Without reference enforcement:

- Hard-coded event literals may appear
- Registry may diverge from runtime usage
- Governance procedures may be bypassed

Layer 1.1 prevents these risks.

---

# 3. Enforcement Model

A deterministic static validator:

    scripts/validation/validate_event_references.py

Validator responsibilities:

1. Read official registry
2. Extract allowed event IDs
3. Scan Python runtime source
4. Detect string literals starting with "EVT_"
5. Fail if literal not declared in registry

---

# 4. Scope

Applies to:

- Runtime Python source files

Excludes:

- governance/
- tests/
- scripts/validation/
- registry JSON

No runtime behavior changes.
Static enforcement only.

---

# 5. Violation Definition

A violation occurs if:

- A string literal matches pattern "EVT_*"
- AND is not declared in registry

Validation must fail closed.

---

# 6. Architectural Position

Hierarchy:

Layer 0 → Execution
Layer 1 → Event Domain
Layer 1.1 → Event Reference Discipline

Layer 1.1 strengthens Layer 1.

---

# 7. Out of Scope

Layer 1.1 does NOT:

- Modify registry content
- Introduce event factories
- Change runtime semantics
- Expand autonomy

---

END OF DOCUMENT
