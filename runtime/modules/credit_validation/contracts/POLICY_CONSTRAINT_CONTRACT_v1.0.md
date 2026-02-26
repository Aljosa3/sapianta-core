# SAPIANTA
# Policy Constraint Contract v1.0
# Development Module – Credit Validation

---

## 1. Purpose

Defines the deterministic structure of a single credit policy constraint
used during validation.

This document is a development artifact.

---

## 2. Constraint Structure

Each constraint MUST include:

- constraint_id (unique string)
- description (non-interpretative text)
- severity (HARD | SOFT)
- expression (deterministic boolean expression)
- referenced_fields (list of Decision Envelope fields)
- policy_version

---

## 3. Constraint Principles

A constraint MUST:

- Be deterministic
- Produce binary output (PASS | FAIL)
- Reference only Decision Envelope fields
- Be independent
- Be version-bound

---

## 4. Severity Semantics

HARD:
- Failure results in INVALID decision.

SOFT:
- Failure is recorded in audit but does not invalidate decision.

v1.0 may restrict implementation to HARD only.

---

## 5. Evaluation Rules

All constraints MUST be evaluated.

Validation result MUST include:

- List of all failed constraints
- PASS if no HARD constraint fails
- INVALID if at least one HARD constraint fails

Short-circuit evaluation is not allowed.

---

## 6. Determinism Guarantee

Given:

- Identical Decision Envelope
- Identical Policy Version

The validation output MUST be identical.

---

## 7. Scope v1.0

Supports:

- Rating-based exposure limits
- Collateral coverage thresholds
- Client concentration checks
- Sector exposure checks

Does not support:

- Behavioral scoring
- Probabilistic models
- Override logic