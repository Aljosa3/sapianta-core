# CANONICAL UPDATE GOVERNANCE — v0.22 (LOCK)

Status: LOCKED  
Scope: Governance only  
Implementation: EXCLUDED  
Amendment: Requires new LOCK version  

---

## 0. Purpose

This document defines the **non-negotiable governance rules** for updating,
replacing, or deprecating canonical modules in SAPIANTA.

The goal of v0.22 is to enable **controlled canonical evolution**
without compromising trust, auditability, or historical integrity.

---

## 1. Canonical Change Requires Explicit Decision (LOCK-01)

**Rule**

A canonical module MAY change state **only** through an explicit,
formally recorded canonical decision.

**Implications**

- No implicit updates
- No side effects
- No inferred state transitions
- No “helpful” or “obvious” changes

If no explicit decision exists, the canon **has not changed**.

---

## 2. Decision Is Not Execution (LOCK-02)

**Rule**

Canonical decisions and technical execution are strictly separated concerns.

- UPDATE-INTENT expresses intent or decision
- WRITE-INTENT expresses permission to write
- Neither implies the other

**Implications**

- No automatic execution after approval
- No escalation from UPDATE to WRITE
- No silent materialization of decisions

A decision alone **never modifies files or content**.

---

## 3. Canonical History Is Append-Only (LOCK-03)

**Rule**

Canonical history is immutable and append-only.

- No rollbacks
- No deletions
- No rewriting past decisions
- No “undo” of canonical changes

Corrections are expressed **only** as new decisions.

**Implications**

- Incorrect decisions remain visible
- Trust is preserved through honesty, not perfection
- The past is never altered

---

## 4. Emergency Has No Canonical Privileges (LOCK-04)

**Rule**

“Emergency” affects urgency, not authority.

Canonical rules apply identically under normal and emergency conditions.

**Implications**

- No emergency bypass
- No temporary exceptions
- No crisis-driven shortcuts

Operational fixes may exist outside the canon,
but canonical change still requires formal decision.

---

## 5. Canonical Truth Over Canonical Correctness (LOCK-05)

**Rule**

The canon guarantees **truthfulness and traceability**, not correctness.

A canonical state may be later judged incorrect,
but it must always reflect what was officially decided at the time.

**Implications**

- Mistakes are not erased
- Accountability is preserved
- Learning remains possible

The canon records reality, not ideal outcomes.

---

## 6. Normative Scenario A — “Helpful Update”

A minor improvement is identified in an active canonical module.

- UPDATE-INTENT is allowed
- New versions may exist in non-canonical domains
- Without an explicit canonical decision:
  - The existing canonical module remains unchanged
  - No overwrite, merge, or silent update is permitted

Result: **Helpful intent alone never alters the canon.**

---

## 7. Normative Scenario B — Emergency Decision Error

An emergency-driven replacement decision is later found incorrect.

- The original decision remains in canonical history
- No rollback is permitted
- A new canonical decision may supersede the incorrect one

Result: **Errors are corrected forward, never erased backward.**

---

## 8. Final Lock Statement

These rules are absolute within v0.22.

No implementation, automation, or optimization may weaken,
reinterpret, or bypass them without a new governance LOCK.

---

END OF DOCUMENT
