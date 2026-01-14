# Module Registration & Identity

Status: CANONICAL — LOCKED  
Applies from: Phase 40  
Authority: Sapianta Architecture  
Scope: All modules  

---

## 0. Canonical Status

This document defines the canonical and normative rules
for module registration and identity within the Sapianta system.

If any module, registry, or implementation contradicts this document,
the implementation is invalid.

This document defines **existence and identity**, not authority or capability.

---

## 1. Definition of Module Identity

A module identity is the minimal, immutable description
by which a module is uniquely recognized by the system.

Module identity establishes:
- existence,
- referencability,
- auditability.

Module identity does **not** establish:
- trust,
- permission,
- capability,
- execution rights.

---

## 2. Required Identity Attributes

Every module MUST declare the following identity attributes
in order to be registered:

- `module_id`  
  A globally unique identifier within the Sapianta ecosystem.

- `module_name`  
  A human-readable name for reference purposes.

- `module_version`  
  A semantic or canonical version identifier.

- `module_owner`  
  The legal or organizational entity responsible for the module.

- `module_type`  
  One of:
  - internal
  - external
  - third-party

- `module_description`  
  A brief declarative description of module intent.

If any required attribute is missing,
the module MUST NOT be registered.

---

## 3. Registration Semantics

Module registration is the act of:

- declaring module identity,
- recording the identity in a registry,
- assigning a registration status.

Registration guarantees only that:
- the module exists as a known entity,
- the module can be referenced by identity.

Registration does not guarantee:
- activation,
- permission,
- correctness,
- safety,
- compliance.

---

## 4. Registration States

A registered module MUST be in exactly one of the following states:

- `REGISTERED`  
  The module identity is known to the system.

- `DISABLED`  
  The module identity is retained,
  but the module is not eligible for interaction.

- `REVOKED`  
  The module identity is invalidated
  and must not be used.

State transitions MUST be explicit and auditable.

---

## 5. Identity Immutability

Once registered:

- `module_id` MUST NEVER change.
- Identity attributes MUST NOT be mutated in-place.

If identity attributes change,
a new module identity MUST be registered.

---

## 6. Separation from Capability and Authority

Module identity is strictly separated from:

- capability declaration,
- permission granting,
- policy evaluation,
- execution eligibility.

No downstream system component
may infer authority or capability from identity alone.

---

## 7. Registry Constraints

Any module registry implementation MUST:

- treat identity records as immutable,
- preserve historical identity states,
- support audit queries by module_id.

The registry is a record of existence,
not a trust store.

---

## 8. Compliance and Audit Rationale

This identity model supports:

- independent module certification,
- regulatory traceability,
- lifecycle governance,
- separation of responsibility.

A module can be audited by identity
without inspecting its implementation.

---

## 9. Canonical Lock

This Module Registration & Identity policy is LOCKED.

Any change requires:
- a new canonical version,
- a new architectural phase,
- explicit approval.

No module may participate in the Sapianta system
without conforming to this document.
