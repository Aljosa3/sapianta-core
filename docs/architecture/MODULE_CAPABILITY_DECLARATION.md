# Module Capability Declaration

Status: CANONICAL — LOCKED  
Applies from: Phase 41  
Authority: Sapianta Architecture  
Scope: All registered modules  

---

## 0. Canonical Status

This document defines the canonical and normative rules
for declaring module capabilities within the Sapianta system.

If any module, registry, or implementation contradicts this document,
the implementation is invalid.

This document defines **claims of capability**, not trust, permission,
or execution authority.

---

## 1. Definition of a Capability

A capability is a **declarative claim** made by a module
about a specific function, service, or operation it is designed to perform.

Capabilities:
- describe intent,
- are informational,
- are non-authoritative.

A capability does NOT:
- grant permission,
- imply trust,
- enable execution,
- override policy.

---

## 2. Capability Declaration Semantics

Capability declaration is the act of:

- explicitly listing one or more capabilities,
- describing each capability in a structured form,
- associating capabilities with a registered module identity.

Declaring a capability guarantees only that:
- the module claims the capability exists,
- the capability can be referenced and evaluated.

---

## 3. Required Capability Attributes

Each declared capability MUST include the following attributes:

- `capability_id`  
  A unique identifier within the scope of the module.

- `capability_name`  
  A human-readable name describing the capability.

- `capability_description`  
  A concise, declarative description of what the capability claims to do.

- `capability_scope`  
  One of:
  - informational
  - analytical
  - advisory
  - execution_candidate

- `capability_inputs`  
  A high-level description of expected input types
  (no payloads, no schemas).

- `capability_outputs`  
  A high-level description of expected output types.

- `capability_constraints`  
  Declared limitations, assumptions, or boundaries.

If any required attribute is missing,
the capability MUST NOT be considered declared.

---

## 4. Capability Scope Semantics

Capability scope indicates **potential impact**, not permission:

- `informational`  
  Provides static or descriptive information.

- `analytical`  
  Performs analysis or transformation without side effects.

- `advisory`  
  Produces recommendations or opinions.

- `execution_candidate`  
  Claims potential for side effects,
  subject to future policy evaluation and explicit enablement.

Scope does not imply enablement.

---

## 5. Multiple Capabilities

A module MAY declare multiple capabilities.

Each capability:
- MUST be independently identifiable,
- MUST be independently evaluable,
- MUST NOT imply dependency on other capabilities
  unless explicitly declared.

---

## 6. Capability Immutability

Once declared:

- Capability declarations MUST NOT be mutated in-place.
- Changes require:
  - a new capability version, or
  - a new capability_id.

Historical capability declarations MUST remain auditable.

---

## 7. Separation from Authority and Execution

Capability declaration is strictly separated from:

- policy evaluation,
- permission granting,
- execution enablement,
- runtime invocation.

No system component may infer:
- trust,
- safety,
- compliance,
- execution eligibility
from capability declaration alone.

---

## 8. Registry and Audit Requirements

Any capability registry MUST:

- associate capabilities with module identity,
- preserve historical declarations,
- support audit queries by module_id and capability_id.

The registry is a record of claims, not approvals.

---

## 9. Compliance and Governance Rationale

This model enables:

- structured policy evaluation,
- staged certification workflows,
- controlled enablement,
- regulatory traceability.

Capabilities can be reviewed, constrained,
or rejected without executing them.

---

## 10. Canonical Lock

This Module Capability Declaration policy is LOCKED.

Any change requires:
- a new canonical document version,
- a new architectural phase,
- explicit approval.

No capability may be evaluated or enabled
without conforming to this document.
