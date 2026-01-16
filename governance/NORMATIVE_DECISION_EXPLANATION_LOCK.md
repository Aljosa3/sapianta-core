# NORMATIVE DECISION / EXPLANATION LOCK

## Status
LOCKED — CORE GOVERNANCE CONSTRAINT

## Purpose
This document defines a strict and irreversible separation between:
- **Normative Decision**
- **Explanation / Justification**

The purpose of this lock is to preserve the integrity, predictability, and auditability of the Sapianta / Senti core system across all current and future modules.

---

## Core Rule

**Normative decisions MUST be made independently of any explanation.**

Explanation:
- MUST NOT participate in,
- MUST NOT influence,
- MUST NOT condition,
- MUST NOT validate

any normative decision.

---

## Decision First Principle

1. A decision (e.g. allow / restrict / block) SHALL be fully resolved **before** any explanation is generated.
2. The decision process SHALL NOT:
   - read,
   - inspect,
   - depend on,
   - or evaluate

any explanation content.

---

## Explanation as a Derived Artifact

Explanation:
- is a **post-decision artifact**,
- is generated strictly **after** the decision is finalized,
- exists solely to support:
  - transparency,
  - audit,
  - user communication,
  - regulatory reporting.

Explanation has **no authority** and **no feedback path** into the decision layer.

---

## No Reverse Dependency

Under no circumstances may:
- explanation quality,
- explanation completeness,
- explanation clarity,
- explanation feasibility

affect, modify, delay, or invalidate a normative decision.

If an explanation cannot be generated, the decision **remains valid**.

---

## Scope

This lock applies to:
- Core runtime
- Governance adapters
- Audit modules
- Explainability modules
- LLM-based components
- Regulatory interfaces (including EU AI Act compliance)

This rule is global and mandatory.

---

## Lock Level

This document defines a **semantic lock**.
Any implementation, optimization, or extension that violates this rule is invalid by definition.

This lock cannot be overridden by:
- configuration,
- policy layering,
- jurisdictional adapters,
- or future modules.

---
