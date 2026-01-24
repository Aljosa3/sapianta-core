# MODULE_BUILDER_SPEC v1.0 — AMENDMENT A
## Canonical Clarifications (Non-Structural)

---

## STATUS

- **Amends:** MODULE_BUILDER_SPEC v1.0
- **Amendment ID:** A
- **Scope:** Clarification ONLY
- **Structural Impact:** NONE
- **Version Change:** NONE (remains v1.0)

This amendment introduces no new capabilities and does not alter system layering.

---

## 1. CLARIFICATION: MODULE CATEGORY VS. CAPABILITIES

### 1.1 Module Category

Module Category is defined as:

- a descriptive classification
- a semantic label for human and analytical reference
- **non-normative**

Module Category has **no enforcement authority** and MUST NOT be used as a decision input for:

- Module Admission
- GuardLifecycle
- Runtime execution control

---

### 1.2 Capability Declarations

Capabilities declared in a module manifest are:

- explicit
- normative
- authoritative inputs for Module Admission

If both a category and a capability declaration exist, **capability declarations take precedence**.

---

## 2. CLARIFICATION: EXECUTION CAPABILITY DECLARATION

Execution capability MUST adhere to the following rules:

1. Execution capability MUST be declared **explicitly and exactly once**
2. Execution capability MUST be unambiguous
3. Execution capability MUST NOT be inferred from module category or purpose

Any manifest containing multiple or conflicting execution declarations is invalid.

---

## 3. CLARIFICATION: DECLARATION EVALUATION LAYER

Every declarative statement in a `.module_builder_manifest` MUST specify its intended evaluation layer.

Allowed evaluation layers are:

- **Module Admission**
- **GuardLifecycle**
- **Runtime**

Declarative statements without a specified evaluation layer are considered incomplete.

ModuleBuilder is responsible only for enforcing the presence of this specification, not its correctness.

---

## 4. ARCHITECTURAL SAFETY STATEMENT

This amendment:

- does not grant ModuleBuilder any interpretative authority
- does not shift responsibility between system layers
- does not introduce runtime logic into authoring
- preserves strict separation between authoring, admission, and execution

---

## 5. CANONICAL NOTE

This amendment exists solely to:

- eliminate implicit interpretation
- close semantic gaps revealed by reference manifests
- ensure that MODULE_BUILDER_SPEC v1.0 is fully self-sufficient

---

END OF AMENDMENT A
