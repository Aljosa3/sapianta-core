# SAPIANTA — Layer 1 Event Registry Specification (v0.1)

## Status
- Layer 0: SEALED @ v1.2.7
- Layer 1: ACTIVE (structural enforcement layer)
- Autonomy level: A0 (no expansion)

This document institutionalizes the Layer 1 Event Registry as a normative governance artifact.

---

# 1. Normative Authority

The Event Registry defined in:

    governance/registry/EVENT_REGISTRY_v0.1.json

is the **single authoritative source of truth** for all admissible events in the SAPIANTA system.

No event may exist outside this registry.

Any event not declared in the registry is invalid by definition.

Unknown event handling policy:
    FAIL_CLOSED (mandatory)

---

# 2. Closed Domain Principle

The Event Domain is explicitly closed.

Implications:

- No dynamic event creation.
- No implicit event inference.
- No fallback event names.
- No auto-generation based on runtime behavior.
- No event materialization from logs, prompts, or external input.

The registry must explicitly enumerate every allowed event.

---

# 3. Enforcement Model

Layer 1 enforcement is structural and deterministic.

Enforcement mechanisms:

1. Registry JSON (authoritative declaration)
2. Deterministic validator:
       scripts/validation/validate_event_registry.py
3. CI / pre-commit integration

Failure conditions:

- Missing registry file
- Invalid JSON
- Invariant violation
- Duplicate event IDs
- Policy violation
- Closed-domain breach

All failures must terminate pipeline execution with non-zero exit.

No recovery path exists at Layer 1.

---

# 4. Relationship to Layer 0

Layer 1:

- DOES NOT modify kernel logic
- DOES NOT alter state transitions
- DOES NOT change execution semantics
- DOES NOT introduce new runtime control flow

Layer 0 remains the deterministic execution authority.

Layer 1 only constrains the admissible event domain.

---

# 5. Relationship to HOI_EVENT_MODEL_SPEC_v0.1.md

Hierarchy:

Layer 1 Event Registry
    ↓ (declares allowed events)

HOI_EVENT_MODEL_SPEC_v0.1.md
    ↓ (defines runtime semantics of those events)

Interpretation:

- Layer 1 defines *which* events may exist.
- HOI_EVENT_MODEL_SPEC defines *how* those events behave.

If an event is not declared in the Layer 1 registry,
it cannot be referenced in HOI_EVENT_MODEL_SPEC.

The registry precedes semantic modeling.

---

# 6. Event Addition Procedure (Governance Controlled)

New events may only be introduced through:

1. Governance decision record
2. Registry version increment
3. Invariant re-validation
4. Commit + tag

Procedure:

Step 1 — Create governance decision document
Step 2 — Modify registry JSON
Step 3 — Increment registry_version
Step 4 — Run validator
Step 5 — Commit with explicit version tag

No event may be added without version increment.

---

# 7. Versioning Rules

Registry is versioned independently of Layer 0.

Version format:
    vX.Y

Rules:

- Minor increment (v0.1 → v0.2):
    Additive event extension only.

- Major increment (v0.x → v1.0):
    Structural invariant change.

Removal of events requires major version increment.

Version history must remain immutable.

---

# 8. Backward Compatibility

Backward compatibility rules:

- Existing event IDs must never change.
- Event ID renaming is forbidden.
- Event removal requires major version bump.
- Event semantic reinterpretation requires HOI spec update.

Layer 1 guarantees stable identity of events.

---

# 9. Migration Protocol (Future Growth)

If registry grows significantly:

- Introduce EVENT_REGISTRY_vX.Y.json
- Maintain previous version for audit traceability
- Provide migration note document
- Never overwrite historical registry files

Historical registry versions are immutable artifacts.

---

# 10. Autonomy Constraint

Layer 1 does NOT:

- Introduce event-driven autonomy
- Introduce event-based self-generation
- Introduce runtime learning

Autonomy remains A0.

---

# 11. Scope Limitation

Layer 1 governs only:

- Event identity
- Event admissibility
- Event domain closure

It does NOT govern:

- State semantics
- Transition guards
- Runtime behavior
- Decision authority
- Module composition

---

# 12. Institutional Seal

With this specification:

Layer 1 is formally institutionalized
as a governance-level enforcement layer.

No event may exist outside the declared registry.

Closed-domain enforcement is mandatory.

