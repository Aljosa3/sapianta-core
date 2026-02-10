# CANON_GUARD_ARCHITECTURE_v0.1

**Path:** `governance/canon/CANON_GUARD_ARCHITECTURE_v0.1.md`  
**Status:** CANON — READ-ONLY  
**Scope:** SYSTEM-WIDE (ALL GUARDS)  
**Version:** v0.1  
**Lock:** FINAL (SEE §12)

---

## 1. PURPOSE

This document defines the **canonical architecture for guards** in the SAPIANTA system.

Its purpose is to establish a **binding, system-wide law** governing:
- what a guard is,
- how a guard is introduced,
- how a guard is validated,
- how a guard is closed,
- and how guard-related audits are interpreted.

This canon prevents ad-hoc guards, shortcut enforcement, and post-hoc justification.

---

## 2. DEFINITION: GUARD

A **guard** is a deterministic, FAIL-CLOSED boundary that governs
whether a transition between two system states is permitted.

A guard:
- decides **permission**, not behavior,
- operates at a **boundary**, not within a process,
- authorizes **transition**, not intent.

---

## 3. REQUIRED GUARD LAYERS (NON-OPTIONAL)

Every guard MUST be defined across the following **three layers**:

1. **Enforcement Layer**  
   - Determines ALLOW / DENY
   - FAIL-CLOSED
   - Non-optional
   - Non-mutating

2. **Evidence Layer**  
   - Defines what constitutes proof of invocation
   - Evidence is structural, not observational
   - No artifacts are produced

3. **Audit Interpretability Layer**  
   - Defines what auditors may infer
   - Defines disallowed audit demands
   - Protects against audit overreach

A guard is **incomplete** if any layer is missing.

---

## 4. REQUIRED GUARD PHASES

Every guard MUST pass through the following **phases**, in order:

### 4.1 Decision Phase
- Guard necessity is justified
- Boundary is identified
- Scope is declared
- No code is written

### 4.2 Implementation (Minimal) Phase
- Minimal enforcement implementation (if applicable)
- FAIL-CLOSED semantics enforced
- No optimization
- No side effects

### 4.3 Audit Phase
- Formal audit of enforcement
- Verification of FAIL-CLOSED behavior
- Verification of absence of bypass

### 4.4 Test Phase (READ-ONLY)
- Read-only validation
- No WRITE
- No mutation
- No persistence

### 4.5 Specification Phase
- Evidence capture specification
- Audit interpretability boundary
- Platform consistency verification

Only after Phase 4 may Phase 5 begin.

---

## 5. PROHIBITED GUARD PRACTICES

The following are strictly forbidden:

- ❌ Guards without FAIL-CLOSED semantics
- ❌ Guards without explicit boundaries
- ❌ Guards that emit logs by default
- ❌ Guards that record identities
- ❌ Guards that justify decisions
- ❌ Guards introduced directly in production
- ❌ Guards without evidence and audit specs

Any such guard is **invalid by definition**.

---

## 6. SEPARATION OF CONCERNS

Guards MUST NOT:
- perform authorization
- perform authentication
- execute business logic
- mutate system state
- observe runtime behavior beyond the boundary

Guards exist to **permit or deny transitions only**.

---

## 7. RELATION TO PLATFORM POSTURE

All guards MUST be consistent with:
- Platform Audit Posture
- Global Audit Interpretability Boundary

No guard may weaken platform-level guarantees.

---

## 8. PRIVACY PRINCIPLE

Guard design in SAPIANTA follows:

> **Privacy by non-existence of data**

Guards MUST minimize data by **not producing it**.

---

## 9. EXTENSIBILITY RULE

New guards MAY be introduced only if:
- they fully comply with this canon,
- they do not invalidate existing guards,
- they do not require retroactive changes.

Deviation requires an explicit **Canon UNLOCK**.

---

## 10. COMPLETENESS CRITERIA

A guard is considered **canon-complete** if:

1. Enforcement spec is LOCKED
2. Evidence spec is LOCKED
3. Audit interpretability spec is LOCKED
4. Platform consistency is verified

Anything less is provisional.

---

## 11. PHASE TRANSITION RULE

Completion of this canon marks:

> **Formal closure of Phase 5 (Specification) for the Guard Layer**

No production transition is implied or permitted.

---

## 12. FINAL LOCK STATEMENT

This canon is hereby declared:

- **SYSTEM-CANONICAL**
- **READ-ONLY**
- **NON-NEGOTIABLE**
- **LOCKED**

No amendment, extension, or reinterpretation is permitted
without an explicit **CANON UNLOCK** phase.

**LOCKED — CANON_GUARD_ARCHITECTURE_v0.1**

---
