# MODULE_BUILDER_SPEC v1.0 — LOCK
## Canonical Phase Lock Record

---

## STATUS

- **Specification:** MODULE_BUILDER_SPEC v1.0
- **Included Amendments:** Amendment A
- **Lock State:** LOCKED
- **Lock Type:** ARCHITECTURAL
- **Lock Scope:** Authoring & Admission Preparation
- **Runtime Impact:** NONE

This lock is final and irreversible.

---

## 1. LOCK INTENT

This lock formally concludes the architectural definition of the ModuleBuilder role.

From this point forward:

- ModuleBuilder is the **only permitted mechanism** for module authoring
- `.module_builder_manifest` is the **only recognized source of truth** for module description
- No alternative authoring paths are valid

---

## 2. LOCKED ELEMENTS

The following elements are now canonically locked:

- Definition of ModuleBuilder role
- Separation between authoring, admission, and execution
- Non-interpretative nature of ModuleBuilder
- Deterministic manifest generation
- Non-normative role of module categories
- Normative authority of capability declarations
- Mandatory declaration of evaluation layer for all manifest statements

These elements MUST NOT be altered without a new major specification version.

---

## 3. EXCLUDED FROM LOCK

This lock explicitly does NOT cover:

- ModuleBuilder implementation details
- CLI or API interfaces
- Internal data formats or schemas
- Validation mechanics beyond presence checks
- Runtime behavior or enforcement logic

These remain open for future phases.

---

## 4. COMPATIBILITY GUARANTEE

This lock is compatible with:

- GuardLifecycle LOCK v0.2
- Module Admission LOCK v0.3
- Existing admitted modules

No retroactive changes are imposed.

---

## 5. ARCHITECTURAL FINALITY STATEMENT

After this lock:

> A module that does not originate from a ModuleBuilder-generated manifest is not considered a module by the system.

This rule is absolute.

---

## 6. CHANGE CONTROL

Any modification to the locked elements requires:

- A new MODULE_BUILDER_SPEC major version
- A separate amendment and lock cycle
- Explicit justification and migration strategy

No silent changes are permitted.

---

## 7. CANONICAL CLOSURE

This document closes the ModuleBuilder architectural phase.

Subsequent work MAY include:
- implementation
- tooling
- examples
- tests

But MUST conform to this locked specification.

---

END OF LOCK
