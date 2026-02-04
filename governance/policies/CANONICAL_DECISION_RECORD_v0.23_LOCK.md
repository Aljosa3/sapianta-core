# CANONICAL DECISION RECORD (CDR) — v0.23 (LOCK)

Status: LOCKED  
Scope: Canonical decision materialization  
Implementation: EXCLUDED  
Amendment: Requires new LOCK version  

---

## 0. Purpose

This document defines the **Canonical Decision Record (CDR)** as the sole
legitimate artifact by which canonical decisions are formally recorded
and later materialized into canonical state.

The CDR enables controlled evolution of the canon without implicit change,
execution, or interpretation.

---

## 1. Definition

A Canonical Decision Record (CDR) is a **formal, immutable record of a
canonical decision**.

A CDR:
- records that a decision was made
- records *what* was decided
- records *why* it was decided

A CDR does **not** perform, trigger, or imply execution.

---

## 2. What a CDR IS

A CDR is:
- an explicit declaration of canonical intent
- a historical record of authority
- an append-only decision artifact
- a prerequisite for any canonical state transition

A CDR exists independently of:
- build artifacts
- module content
- runtime behavior
- implementation mechanisms

---

## 3. What a CDR IS NOT

A CDR is **not**:
- a module
- a patch
- a diff
- a command
- a script
- an instruction to write files
- an execution trigger
- a rollback mechanism

A CDR cannot:
- modify files
- replace content
- merge versions
- infer intent
- correct past decisions

---

## 4. Authority and Exclusivity

Canonical state transitions are valid **only if** backed by a CDR.

- No CDR → no canonical change
- No exception
- No alternative path

All canonical changes must be:
- attributable to exactly one CDR
- traceable in canonical history

---

## 5. Temporal Properties

A CDR is:
- immutable once recorded
- never deleted
- never altered
- never superseded retroactively

Incorrect or outdated decisions remain part of canonical history
and may only be addressed by **new CDRs**.

---

## 6. Decision Semantics (Abstract)

A CDR expresses one and only one canonical decision.

Decision semantics:
- are explicit
- are finite in type
- do not combine implicitly
- do not cascade

A single CDR results in **at most one canonical state transition**.

---

## 7. Separation from Execution

A CDR:
- does not authorize writing
- does not imply WRITE-INTENT
- does not invoke WRITE-GATE
- does not trigger automation

Execution requires separate, explicit mechanisms governed elsewhere.

---

## 8. Validation Boundary

The validator:
- may read CDRs
- may verify their consistency
- may reject invalid or conflicting decisions

The validator may **not**:
- reinterpret decisions
- optimize outcomes
- infer missing intent
- “fix” decisions

---

## 9. Emergency and Error Handling

Emergency context:
- does not alter CDR rules
- does not grant special authority
- does not permit bypass

Erroneous decisions:
- remain recorded
- are not reverted
- are corrected only by new CDRs

---

## 10. Canonical Integrity Guarantee

The CDR guarantees:
- traceability
- accountability
- historical integrity

The CDR does **not** guarantee:
- correctness
- optimality
- best outcomes

The canon reflects **what was decided**, not what should have been decided.

---

## 11. Final Lock Statement

This definition of the Canonical Decision Record is absolute for v0.23.

No implementation, format, storage model, or automation may weaken,
extend, or reinterpret these rules without a new LOCK document.

---

END OF DOCUMENT
