# CONTRACT — SELF-BUILD UNLOCK ENFORCEMENT

**ID:** CONTRACT_SELF_BUILD_UNLOCK_ENFORCEMENT_v0.1  
**Status:** DESIGN  
**Phase:** GOVERNANCE  
**Date:** YYYY-MM-DD  
**Scope:** Conditions and enforcement order for unlocking self-build execution

---

## 1. Purpose

This document defines the **mandatory enforcement contract** that MUST be satisfied
before the self-build LOCK can be lifted in the SAPIANTA system.

This contract does NOT introduce implementation.
It defines **roles, order, and non-negotiable conditions** for self-build authorization.

---

## 2. Governing Principle

Self-build execution is permitted **only if and only if**:

- explicit human authorization is validated,
- governance gates are enforced deterministically,
- filesystem writes are protected by a final authority gate.

Any deviation invalidates authorization.

---

## 3. Canonical Enforcement Order (Authoritative)

The enforcement order below is **strict and non-reorderable**:

1. **SPEC Completeness Validation**
2. **HASBT — Human-Authorized Self-Build Trigger**
3. **WRITE-GATE Evaluation**
4. **Filesystem Write Execution**

No step may be skipped, merged, or implicitly assumed.

---

## 4. Role Responsibilities

### 4.1 Human Operator
- provides intent and authorization context,
- explicitly confirms self-build execution,
- remains accountable for authorization decision.

---

### 4.2 HOI — Human Orientation Interface

HOI is responsible for:

- orienting the human operator,
- validating intent clarity and scope,
- ensuring SPEC completeness,
- preparing the authorization context for HASBT.

HOI **does not**:
- execute builds,
- write artifacts,
- authorize implicitly.

HOI output is **preparatory**, not executable.

---

### 4.3 HASBT — Human-Authorized Self-Build Trigger

HASBT is responsible for:

- validating explicit human authorization,
- verifying authorization context integrity,
- refusing authorization if context is incomplete or ambiguous.

HASBT operates:

- after SPEC validation,
- before any execution,
- before any filesystem write.

Without HASBT approval, self-build **MUST NOT** proceed.

---

### 4.4 Build CLI (Canonical Authority)

The canonical build CLI:

- receives execution permission only after HASBT approval,
- performs build execution deterministically,
- MUST NOT bypass governance gates.

The build CLI is an **executor**, not an authorizer.

---

### 4.5 WRITE-GATE

WRITE-GATE is responsible for:

- final authorization of filesystem writes,
- verifying that all prior gates passed,
- denying writes on any violation.

WRITE-GATE operates:

- immediately before filesystem writes,
- as the last irreversible control point.

---

## 5. Negative Rules (Hard Constraints)

The following are strictly prohibited:

- implicit authorization of self-build,
- HOI triggering execution directly,
- build execution without HASBT,
- filesystem writes without WRITE-GATE,
- post-write validation used as authorization.

Any of the above constitutes a governance violation.

---

## 6. Evidence Required for UNLOCK

The self-build LOCK may be lifted only when **all** of the following are demonstrably true:

- HASBT exists as executable enforcement logic,
- HASBT is enforced on the canonical build path,
- WRITE-GATE is enforced before any filesystem write,
- enforcement order matches Section 3 exactly,
- enforcement is auditable and deterministic.

Evidence must be technical and verifiable.

---

## 7. Unlock Authority

Unlocking self-build execution requires:

- a **separate governance decision document**,
- explicit reference to this contract,
- confirmation that all evidence requirements are met.

No implicit or partial unlock is permitted.

---

## 8. Final Statement

Self-build capability is conditional.

Execution is a privilege, not a default.

Governance precedes automation.

---

**END OF CONTRACT**
