# DIAGRAM — SELF-BUILD ENFORCEMENT ORDER

**ID:** DIAGRAM_SELF_BUILD_ENFORCEMENT_ORDER_v0.1  
**Status:** DESIGN  
**Phase:** GOVERNANCE  
**Date:** 2026-02-10  
**Scope:** Canonical enforcement order for self-build execution

---

## 1. Purpose

This diagram defines the **authoritative, non-reorderable enforcement order**
for self-build execution in the SAPIANTA system.

It visualizes the enforcement contract and makes the
**governance flow unambiguous**.

No implementation is introduced.

---

## 2. Canonical Enforcement Flow (Authoritative)

```
Human
│
│ (intent, scope, accountability)
▼
HOI — Human Orientation Interface
│
│ - intent shaping
│ - scope clarification
│ - SPEC completeness validation
│
│ ❌ MUST NOT execute
│ ❌ MUST NOT authorize implicitly
▼
HASBT — Human-Authorized Self-Build Trigger
│
│ - explicit human authorization
│ - context integrity validation
│
│ ❌ MUST NOT be implicit
│ ❌ MUST NOT be skipped
▼
Build CLI (Canonical Authority)
│
│ - deterministic execution only
│ - no authorization logic
│
│ ❌ MUST NOT bypass gates
▼
WRITE-GATE (Final Authority)
│
│ - validates all prior approvals
│ - final irreversible decision
│
│ ❌ MUST NOT allow post-write checks
▼
Filesystem Write
│
│ (module materialization)
▼
END
```

---

## 3. Enforcement Rules (Hard)

- Enforcement order is **strict** and **non-reorderable**
- No component may skip or absorb another
- Authorization is **explicit only**
- Validation after write is **invalid as authorization**
- Any violation invalidates the build

---

## 4. Gate Responsibilities (Summary)

| Layer | Role | Authority |
|------|------|-----------|
| Human | Intent & accountability | Origin |
| HOI | Orientation & validation | Preparatory |
| HASBT | Authorization decision | Mandatory |
| Build CLI | Execution | Conditional |
| WRITE-GATE | Final write approval | Absolute |

---

## 5. Prohibited Shortcuts

The following flows are explicitly forbidden:

- Human → Build CLI
- HOI → Build CLI
- Build CLI → Filesystem (without WRITE-GATE)
- HASBT after execution
- WRITE-GATE after write

---

## 6. Relation to Governance Documents

This diagram is binding with:

- `DECISION_SELF_BUILD_LOCK_v0.XX`
- `CONTRACT_SELF_BUILD_UNLOCK_ENFORCEMENT_v0.1`
- `HUMAN_AUTHORIZED_SELF_BUILD_TRIGGER.md`

In case of conflict, **governance contracts prevail**.

---

## 7. Final Statement

Self-build is not a feature.

It is a **governed, auditable, human-authorized process**.

---

**END OF DIAGRAM**
