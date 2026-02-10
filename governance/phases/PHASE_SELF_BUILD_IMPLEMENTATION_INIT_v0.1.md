# PHASE — SELF-BUILD IMPLEMENTATION INIT

**ID:** PHASE_SELF_BUILD_IMPLEMENTATION_INIT_v0.1  
**Status:** INIT  
**Phase:** IMPLEMENTATION  
**Date:** YYYY-MM-DD  
**Scope:** Controlled initiation of self-build governance implementation

---

## 1. Purpose

This document formally initiates the **IMPLEMENTATION PHASE**
for self-build governance in the SAPIANTA system.

The purpose of this phase is to **implement previously LOCKED governance designs**
without altering their intent, scope, or authority.

This document does NOT unlock self-build execution.

---

## 2. Preconditions (Already Satisfied)

The following DESIGN artifacts are completed and LOCKED:

- `DECISION_SELF_BUILD_LOCK_v0.XX`
- `CONTRACT_SELF_BUILD_UNLOCK_ENFORCEMENT_v0.1`
- `DIAGRAM_SELF_BUILD_ENFORCEMENT_ORDER_v0.1`
- `HASBT_AUTHORIZATION_PAYLOAD_v0.1`
- `CHECKLIST_SELF_BUILD_UNLOCK_EVIDENCE_v0.1`

These documents are **authoritative** for this phase.

---

## 3. Phase Boundary (Hard)

This phase permits **implementation only** of:

- HASBT enforcement logic
- HASBT payload validation
- WRITE-GATE enforcement on canonical build path

This phase explicitly forbids:

- unlocking self-build execution
- changing governance rules
- bypassing any LOCKed constraint
- introducing new authorization semantics
- enabling filesystem writes without WRITE-GATE

---

## 4. Implementation Order (Mandatory)

Implementation MUST follow this exact order:

1. **HASBT Implementation**
   - payload parsing
   - validation logic
   - explicit denial behavior

2. **HASBT Enforcement**
   - integration into canonical build path
   - denial halts execution deterministically

3. **WRITE-GATE Enforcement**
   - invocation immediately before filesystem writes
   - denial prevents any write operation

No reordering is permitted.

---

## 5. Canonical Modification Scope

Code changes are permitted **only** in the following areas:

- HASBT implementation module(s)
- Canonical build path enforcement points
- WRITE-GATE invocation wiring
- Test coverage validating enforcement

All other areas are **out of scope**.

---

## 6. Verification Requirements

Each implementation step MUST include:

- static code analysis proof
- negative test cases (deny scenarios)
- explicit confirmation of enforcement order

Implementation without verification is invalid.

---

## 7. Self-Build Status During Implementation

During this phase:

- self-build execution remains **LOCKED**
- filesystem writes remain **forbidden**
- any attempt to bypass governance is a violation

Implementation success does NOT imply unlock.

---

## 8. Exit Criteria (For Next Phase)

This phase is considered complete when:

- HASBT is fully implemented and enforced
- WRITE-GATE is fully enforced
- all items in `CHECKLIST_SELF_BUILD_UNLOCK_EVIDENCE_v0.1`
  are demonstrably satisfied

Completion enables — but does NOT perform — UNLOCK.

---

## 9. Unlock Authority (Explicit)

Unlocking self-build execution requires:

- completion of this phase
- completion of the UNLOCK Evidence Checklist
- a **separate governance decision document**

No implicit unlock is permitted.

---

## 10. Final Statement

Implementation serves governance.

Execution serves authorization.

No code outranks governance.

---

**END OF PHASE INIT**
