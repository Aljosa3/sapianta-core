# CANONICAL VALIDATOR BOUNDARY — v0.23 (LOCK)

Status: LOCKED  
Scope: Validator authority, limits, and prohibitions  
Implementation: EXCLUDED  
Amendment: Requires new LOCK version  

---

## 0. Purpose

This document defines the **absolute authority boundaries** of the
canonical validator.

Its purpose is to ensure the validator remains a **passive,
deterministic judge**, never an agent of change, interpretation, or optimization.

---

## 1. Validator Role (Read-Only Authority)

**Rule**

The validator is a **read-only authority**.

It may:
- read canonical decision records (CDRs)
- compute canonical state from canonical history
- verify conformance with all LOCK documents
- accept or reject decisions and transitions

It may **not** perform any action beyond validation.

---

## 2. Determinism Requirement

**Rule**

Given the same canonical history, the validator must always
produce the same canonical state and validation outcome.

**Implications**

- No randomness
- No heuristics
- No contextual interpretation
- No time-dependent behavior

---

## 3. Explicit Prohibitions

The validator must **never**:

- modify files or content
- write to any domain
- invoke WRITE-INTENT or WRITE-GATE
- infer missing intent
- reinterpret decisions
- optimize outcomes
- merge, patch, or transform artifacts
- auto-correct invalid decisions
- generate “suggested” fixes
- collapse or rewrite history

Any such behavior constitutes a governance violation.

---

## 4. Rejection Over Repair

**Rule**

Invalid or conflicting canonical decisions are **rejected**, not repaired.

**Implications**

- No best-effort acceptance
- No partial validity
- No silent correction

If a decision is invalid, canonical state remains unchanged.

---

## 5. Closed-World Enforcement

**Rule**

The validator operates under a **closed-world assumption**.

- Only decision types defined by LOCK documents are valid
- Only transitions explicitly permitted are allowed
- Absence of permission equals prohibition

---

## 6. No Escalation of Authority

**Rule**

The validator may not escalate its authority under any circumstance.

This includes:
- emergency context
- human override
- AI confidence
- external signals
- operational pressure

The validator’s authority is fixed and non-negotiable.

---

## 7. Isolation from Runtime and Operations

**Rule**

The validator is isolated from:
- runtime behavior
- operational outcomes
- performance metrics
- success or failure signals

Validation is based solely on canonical artifacts and LOCK rules.

---

## 8. Transparency and Auditability

**Rule**

Validator outcomes must be:
- explainable via LOCK rules
- traceable to specific CDRs
- reproducible independently

The validator must not rely on hidden state or opaque logic.

---

## 9. Canonical Inaction Guarantee

**Rule**

In the absence of a valid canonical decision,
the validator guarantees **canonical inaction**.

No decision → no state change.

---

## 10. Final Lock Statement

These validator boundaries are absolute for v0.23.

No implementation, extension, or tooling may expand, soften,
or reinterpret validator authority without a new LOCK document.

---

END OF DOCUMENT
