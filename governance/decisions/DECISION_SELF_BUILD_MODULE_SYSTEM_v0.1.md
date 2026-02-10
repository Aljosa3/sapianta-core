# DECISION_SELF_BUILD_MODULE_SYSTEM_v0.1

**Path:** `governance/decisions/DECISION_SELF_BUILD_MODULE_SYSTEM_v0.1.md`  
**Status:** DECISION — READ-ONLY  
**Phase:** SELF-BUILD MODULE SYSTEM  
**Version:** v0.1  
**Lock:** FINAL (SEE §10)

---

## 1. PURPOSE

This decision establishes the **existence, scope, and intent** of the
**Self-Build Module System** within SAPIANTA.

It answers the question:

> **What does it mean for SAPIANTA to support self-built modules,
> and under which non-negotiable constraints does this occur?**

This is a **decision phase only**.  
No implementation, no schemas, no workflows are defined here.

---

## 2. DECISION STATEMENT

SAPIANTA SHALL support **self-built modules** generated through a governed,
human-oriented process, operating **above a frozen Guard Layer** and **without
modifying guard semantics**.

Self-built modules are treated as **artifacts**, not as autonomous agents.

---

## 3. DEFINITION: MODULE

A **module** is a bounded, declarative artifact that:

- has a clear purpose
- operates within an explicit scope
- exposes a defined interface
- does not alter platform governance
- does not bypass guards
- does not self-modify

A module is **not**:
- a guard
- a policy
- a runtime agent
- a governance authority

---

## 4. DEFINITION: SELF-BUILD

**Self-build** means:

- the system assists in **constructing** a module
- the human remains the **orientation authority**
- the output is **reviewable and bounded**
- the result is an **artifact**, not an execution

Self-build does **not** mean:
- autonomous deployment
- runtime mutation
- self-authorization
- recursive system modification

---

## 5. SYSTEM BOUNDARIES

The Self-Build Module System:

- operates **after HASBT** (authorization to build exists)
- produces artifacts subject to **PBOG** (output release guard)
- does not require new guards
- does not weaken audit posture

Guards remain **frozen and authoritative**.

---

## 6. MODULE LIFECYCLE (ABSTRACT)

At a high level, a module transitions through:

1. **Intent Declaration**  
   Human expresses desired capability.

2. **Structured Construction**  
   System assists in forming the module artifact.

3. **Artifact Finalization**  
   Module exists as a static, reviewable output.

4. **Optional Acceptance**  
   Human accepts or rejects the artifact.

No execution or deployment is implied.

---

## 7. ROLE OF HOI

The **Human Orientation Interface (HOI)**:

- mediates intent
- structures interaction
- enforces clarity
- prevents ambiguity

HOI does **not**:
- authorize governance changes
- bypass guards
- validate compliance on its own

---

## 8. NON-GOALS (EXPLICIT)

The Self-Build Module System does **NOT** aim to:

- auto-deploy modules
- execute modules by default
- create autonomous agents
- generate self-updating code
- manage production pipelines

Those concerns are **out of scope** for this phase.

---

## 9. CONSISTENCY WITH FROZEN LAYERS

This decision is consistent with:

- CANON_GUARD_ARCHITECTURE_v0.1
- Platform Audit Posture
- Global Audit Interpretability Boundary

No frozen layer is reopened or modified.

---

## 10. FINAL LOCK STATEMENT

This decision is hereby declared:

- **READ-ONLY**
- **SCOPE-BOUND**
- **NON-EXECUTABLE**
- **LOCKED**

No reinterpretation or expansion is permitted
without an explicit Decision UNLOCK phase.

**LOCKED — DECISION_SELF_BUILD_MODULE_SYSTEM_v0.1**

---
