# PHASE 42 — CAPABILITY POLICY ENGINE (CANONICAL)

Status: CANONICAL — LOCKED  
Phase: F42  
Date: 2026-01-14  
Authority: Sapianta Core  
Scope: System-wide normative enforcement  

---

## 0. Canonical Status

This document is the **canonical and normative definition** of the Sapianta Capability Policy Engine (F42).

If any implementation, module, runtime behavior, or explanation contradicts this document,  
**the implementation is wrong**.

This document defines **what must be true**, not how it is implemented.

---

## 1. Purpose of the Capability Policy Engine

The Capability Policy Engine exists to provide a **single, authoritative, normative decision point** for determining whether a declared module capability **may be used in a given context**.

Its sole purpose is to answer the question:

> **“Is the use of this capability allowed in this specific context?”**

The Policy Engine does not execute actions, does not bind capabilities, and does not interact with external systems.

---

## 2. Position in the System Architecture

The Capability Policy Engine operates **between declaration and enablement**.

It is positioned:
- after **Module Identity** (F40),
- after **Capability Declaration** (F41),
- before **Capability Enablement** (F43),
- before any execution attempt.

No system component may bypass this position.

---

## 3. Inputs

The Capability Policy Engine evaluates decisions based on the following inputs:

- Module Identity (as defined in F40)
- Declared Capability (as defined in F41)
- Execution Intent
- Invocation Context (CLI, API, Agent, SaaS, etc.)
- Active Policy Hierarchy (system, community, organizational)

The engine must not accept any additional hidden or inferred inputs.

---

## 4. Outputs

The Capability Policy Engine produces **exactly one** of the following decisions:

- **ALLOW** — capability usage is permitted
- **DENY** — capability usage is forbidden
- **CONDITIONAL** — capability usage is permitted only if additional constraints are satisfied

No other output types are allowed.

The decision is **normative**, **final**, and **non-negotiable**.

---

## 5. Authority and Exclusivity

The Capability Policy Engine is the **only authority** permitted to decide whether a capability may be used.

The following are explicitly forbidden from making or emulating this decision:
- modules,
- execution layers,
- runtime controllers,
- LLMs,
- agents,
- adapters,
- user interfaces.

If any component makes an equivalent decision outside the Policy Engine,  
the system is no longer compliant with Sapianta.

---

## 6. Non-Responsibilities

The Capability Policy Engine **must not**:

- execute actions,
- bind capabilities to runtime hooks,
- allocate resources,
- perform sandboxing,
- perform logging or tracing,
- perform financial, legal, or organizational ROI decisions,
- modify or reinterpret Core decisions.

Its role is strictly **normative evaluation**.

---

## 7. Determinism and Default Denial

The Policy Engine must operate deterministically.

If:
- required information is missing,
- policies conflict without a clear hierarchy resolution,
- context is ambiguous,
- capability is unknown,

the engine **must return DENY**.

Fail-open behavior is strictly forbidden.

---

## 8. Relationship to Other Phases

### Relationship to F41 (Capability Declaration)
- F41 declares **what a module is capable of**.
- F42 decides **whether that capability may be used**.
- Declaration alone never implies permission.

### Relationship to F43 (Capability Enablement)
- F42 authorizes or denies.
- F43 performs technical enablement.
- F43 must never decide independently of F42.

---

## 9. Immutability and Versioning

This document defines **Capability Policy Engine v1.0**.

Any change requires:
- a new canonical document,
- an explicit version increment,
- a declared policy migration.

This version is locked.

---

## 10. Canon Lock

The Capability Policy Engine defined herein is immutable by default.

Any system claiming to be Sapianta-compliant **must implement behavior consistent with this document**.

Violations invalidate compliance.

---
