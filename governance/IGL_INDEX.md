# IGL INDEX — IMPLEMENTATION GUARD LAYER

Status: LOCKED  
Version: IGL v1.0  
Applies to: All SAPIANTA SRS code  
Enforced by: `sapianta/igl/igl_init.py`

---

## PURPOSE

This document defines the complete and exhaustive set of Implementation Guard Layer (IGL) rules.

IGL exists to enforce structural, semantic, and architectural constraints on all implementation code.
IGL rules are binding and non-optional.

No guardrail exists outside this index.

---

## CANONICAL GUARDRAILS

The following guardrails constitute the full IGL v1.0 set:

- **IGL-GR-001 — No Semantic Fallbacks**
- **IGL-GR-002 — No Implicit Authority Escalation**
- **IGL-GR-003 — No Implicit Defaults**
- **IGL-GR-004 — No Hidden Control Flow**
- **IGL-GR-005 — No Exception-Driven Logic**
- **IGL-GR-006 — No Global State Mutation**
- **IGL-GR-007 — No Time-Based Behavior**
- **IGL-GR-008 — Explicit Interfaces Only**
- **IGL-GR-009 — No Cross-Layer Imports**

Each guardrail is defined in a dedicated document under `/governance`
and is enforced mechanically by IGL-INIT.

---

## ENFORCEMENT

All implementation code MUST pass `igl_init.py` checks.

Code that violates any guardrail listed above is invalid by definition
and MUST NOT be committed.

---

## SCOPE LOCK

This index is exhaustive.

- No additional IGL guardrails exist outside this list.
- No implicit, hidden, or informal rules are in effect.
- Any future guardrail requires an explicit new index version.

---

## GOVERNANCE AUTHORITY

This document is part of the normative governance layer.

It derives authority from:
- CANON.md
- CORE_LAWS.md
- SAPIANTA Canonical Framework (SCF)

Runtime code has no authority to alter, override, or reinterpret this index.

---

END OF DOCUMENT
