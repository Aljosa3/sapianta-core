# CHECKLIST — SELF-BUILD UNLOCK EVIDENCE

**ID:** CHECKLIST_SELF_BUILD_UNLOCK_EVIDENCE_v0.1  
**Status:** DESIGN  
**Phase:** GOVERNANCE  
**Date:** 2026-02-10  
**Scope:** Verifiable evidence required to unlock self-build execution

---

## 1. Purpose

This checklist defines the **mandatory, verifiable evidence** required
to unlock self-build execution in the SAPIANTA system.

Unlock is permitted **only if all checklist items pass**.
This document introduces **no implementation**.

---

## 2. Governing Rule

Self-build execution MUST remain LOCKED unless **every item**
in Sections 3–6 is satisfied with concrete evidence.

Partial compliance is insufficient.

---

## 3. HASBT — Authorization Evidence (Mandatory)

### 3.1 Implementation Presence
- [ ] Executable HASBT logic exists in codebase
- [ ] HASBT logic is reachable from canonical build path

**Evidence required:**
- File path(s)
- Entry function/class reference

---

### 3.2 Payload Validation
- [ ] HASBT validates all required payload fields
- [ ] HASBT rejects missing or ambiguous authorization
- [ ] HASBT rejects expired authorization
- [ ] HASBT binds authorization to specific build plan

**Evidence required:**
- Validation rules reference
- Negative test cases (deny scenarios)

---

### 3.3 Explicit Human Authorization
- [ ] Authorization requires explicit affirmative human action
- [ ] Authorization is attributable to a specific human
- [ ] Authorization cannot be inferred or auto-generated

**Evidence required:**
- Input boundary definition
- Audit trace description

---

## 4. Enforcement Order Evidence (Mandatory)

### 4.1 Order Integrity
- [ ] SPEC completeness validation occurs before HASBT
- [ ] HASBT executes before any build execution
- [ ] WRITE-GATE executes before any filesystem write

**Evidence required:**
- Call graph or static analysis trace
- Function order confirmation

---

### 4.2 Non-Reorderability
- [ ] No code path allows bypassing HASBT
- [ ] No code path allows bypassing WRITE-GATE
- [ ] No post-write validation is used as authorization

**Evidence required:**
- Negative path analysis
- Explicit denial cases

---

## 5. WRITE-GATE — Filesystem Protection Evidence (Mandatory)

### 5.1 Enforcement Placement
- [ ] WRITE-GATE is invoked immediately before filesystem writes
- [ ] WRITE-GATE denies writes on any missing prior approval

**Evidence required:**
- Exact invocation location
- Deny behavior description

---

### 5.2 Authority and Finality
- [ ] WRITE-GATE validates HASBT approval
- [ ] WRITE-GATE validates SPEC completeness
- [ ] WRITE-GATE acts as final irreversible gate

**Evidence required:**
- Input signals list
- Failure handling behavior

---

## 6. Auditability Evidence (Mandatory)

### 6.1 Traceability
- [ ] Each build execution is traceable to a HASBT payload
- [ ] Payload is immutably recorded
- [ ] Payload is retrievable for post-hoc audit

**Evidence required:**
- Storage description
- Retrieval mechanism

---

### 6.2 Determinism
- [ ] Enforcement behavior is deterministic
- [ ] Same inputs yield same authorization outcome

**Evidence required:**
- Determinism statement
- Test confirmation

---

## 7. Prohibited Conditions (Hard Fail)

UNLOCK MUST be denied if any of the following are true:

- [ ] HASBT is design-only
- [ ] WRITE-GATE exists but is bypassed
- [ ] Authorization is implicit
- [ ] Authorization is global or perpetual
- [ ] Filesystem writes occur without WRITE-GATE
- [ ] Enforcement order differs from governance contract

Any checked item here blocks UNLOCK.

---

## 8. UNLOCK Decision Requirements

UNLOCK requires:
- this checklist completed with all mandatory items passing,
- attached evidence references,
- a **separate governance decision document** explicitly authorizing unlock.

No implicit unlock is permitted.

---

## 9. Final Statement

Self-build unlock is an evidence-based decision.

Governance unlocks execution — not intent.

---

**END OF CHECKLIST**
