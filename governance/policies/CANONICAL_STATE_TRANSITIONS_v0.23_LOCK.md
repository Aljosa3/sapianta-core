# CANONICAL STATE TRANSITIONS — v0.23 (LOCK)

Status: LOCKED  
Scope: Canonical state materialization rules  
Implementation: EXCLUDED  
Amendment: Requires new LOCK version  

---

## 0. Purpose

This document defines the **only permitted rules** by which canonical
state may change as a result of a canonical decision.

It establishes a strict, deterministic boundary between
**decision history** and **canonical state**.

---

## 1. Exclusive Transition Authority

**Rule**

Canonical state may change **only** as the direct and explicit result
of a valid Canonical Decision Record (CDR).

**Implications**

- No CDR → no state transition
- No exception
- No alternative mechanisms

---

## 2. Deterministic Mapping

**Rule**

Each canonical decision maps to **at most one** canonical state transition.

- No branching
- No multi-step inference
- No chained transitions

Given the same canonical history,
the resulting canonical state must always be identical.

---

## 3. No Content Mutation

**Rule**

Canonical state transitions **never** modify module content.

**Implications**

- No file overwrites
- No diffs
- No merges
- No in-place edits

State transitions operate on **references and status only**.

---

## 4. Append-Only Canonical History

**Rule**

Canonical history is strictly append-only.

- State transitions do not erase prior states
- Previous canonical entities remain addressable
- Historical state is never rewritten

---

## 5. Single-Target Constraint

**Rule**

A single CDR may affect **only one canonical target**.

**Implications**

- No batch transitions
- No cascading effects
- No fan-out updates

If multiple targets require change,
multiple CDRs are required.

---

## 6. Transition Validity Conditions

A canonical state transition is valid only if:

- The referenced decision type is defined
- The target exists in canonical history
- The transition does not violate prior LOCK rules
- No conflicting active state is created

Invalid transitions are rejected, not repaired.

---

## 7. No Rollback Semantics

**Rule**

Canonical state transitions are irreversible.

- No rollback
- No undo
- No reactivation of past state

Corrections are expressed exclusively
through new canonical decisions.

---

## 8. Emergency Neutrality

**Rule**

Emergency context does not alter transition rules.

Urgency affects timing, not semantics.

---

## 9. Validator Role

The validator:
- computes canonical state from decision history
- verifies transition validity
- rejects non-deterministic or conflicting transitions

The validator does **not**:
- infer missing intent
- optimize transitions
- collapse history
- reinterpret semantics

---

## 10. Canonical State as Derived Truth

**Rule**

Canonical state is a **derived view** of canonical history,
not an independently mutable artifact.

The state reflects what has been decided,
not what is currently preferred.

---

## 11. Final Lock Statement

These state transition rules are absolute for v0.23.

No implementation may introduce additional transitions,
implicit effects, or shortcuts without a new LOCK document.

---

END OF DOCUMENT
