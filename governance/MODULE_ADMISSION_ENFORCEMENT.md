# MODULE_ADMISSION_ENFORCEMENT

## Status
LOCKED — ENFORCED AT RUNTIME

---

## Purpose

This document defines the **mandatory runtime enforcement rules** for admitting
modules into the SAPIANTA system.

Its role is to ensure that **no module can exist, load, or execute**
unless it has been **provably created via the Module Builder**.

This is an enforcement document, not a guideline.

---

## Core Rule

**A module SHALL be admitted into the runtime if and only if:**

- It resides under the canonical `/modules/` directory
- It contains a valid `.module_builder_manifest` file at its root

Any deviation from this rule results in **hard rejection**.

---

## Enforcement Point

Enforcement MUST occur at **module discovery / load time**, before:

- wiring
- capability exposure
- execution intent evaluation
- runtime orchestration

No module may reach any execution-related layer prior to admission validation.

---

## Admission Algorithm (Normative)

For each directory under `/modules/`:

1. Check for existence of `.module_builder_manifest`
2. If the manifest is missing:
   - Immediately BLOCK the module
   - Do not load
   - Do not warn
   - Do not attempt fallback
3. If the manifest exists:
   - Module is considered **structurally admissible**
   - Further validation may occur in later stages

---

## Explicit Prohibitions

The runtime MUST NOT:

- auto-admit modules without a manifest
- infer legitimacy from directory names
- support "legacy compatibility"
- provide soft warnings instead of blocking
- allow bypass flags or development overrides

---

## Legacy Module Policy

Modules located outside `/modules/`, including but not limited to:

- /history/legacy_modules_pre_builder/


are considered **historical artifacts only**.

They MUST NOT be:

- reloaded
- re-registered
- migrated automatically
- conditionally activated

There is **no re-entry path** for legacy modules.

---

## Security Rationale

This enforcement guarantees:

- single point of module provenance
- elimination of silent module injection
- deterministic system growth
- compatibility with IGL guardrails
- long-term governance stability

Without this rule, Module Builder authority is non-binding.

---

## Relationship to Other Locks

This document enforces and operationalizes:

- `srs/module_builder/PURPOSE_AND_BOUNDARIES.md`
- `srs/module_builder/MODULE_LIFECYCLE_LOCK.md`
- IGL principles (explicit provenance, no implicit authority)

---

## Final Statement

If a module was not built by the Module Builder,  
**it does not exist** for the SAPIANTA runtime.

This rule is absolute.
