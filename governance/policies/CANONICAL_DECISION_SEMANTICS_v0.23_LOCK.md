# CANONICAL DECISION SEMANTICS — v0.23 (LOCK)

Status: LOCKED  
Scope: Canonical decision meaning and limits  
Implementation: EXCLUDED  
Amendment: Requires new LOCK version  

---

## 0. Purpose

This document defines the **closed set of canonical decision types**
and their **strict semantic meaning**.

Its purpose is to eliminate ambiguity, interpretation,
and “helpful” extensions in canonical evolution.

Only decisions defined here may exist.

---

## 1. Closed World Assumption

Canonical decision semantics operate under a **closed world model**.

**Rule**

If a decision type is not explicitly defined in this document,
it does not exist.

**Implications**

- No custom decision types
- No inferred meanings
- No composite or dynamic decisions
- No extensions without a new LOCK

---

## 2. Decision Type: ADD

**Meaning**

Adds a new canonical module or a new canonical version
without affecting existing canonical state.

**Properties**

- Append-only
- Non-destructive
- Does not alter status of existing modules
- Does not imply activation or preference

**Explicitly does NOT**

- Replace existing modules
- Deprecate prior versions
- Change canonical references

---

## 3. Decision Type: REPLACE

**Meaning**

Replaces one canonical reference with another.

**Properties**

- Exactly one target is replaced
- Exactly one replacement is designated
- The replaced entity is not deleted

**Required Effects**

- Previous canonical target transitions out of ACTIVE
- Replacement transitions into ACTIVE

**Explicitly does NOT**

- Delete history
- Merge content
- Imply rollback capability

---

## 4. Decision Type: DEPRECATE

**Meaning**

Marks a canonical module or version as deprecated.

**Properties**

- Status-only decision
- No content change
- No replacement implied

**Explicitly does NOT**

- Remove canonical availability
- Force migration
- Replace or supersede automatically

---

## 5. Decision Type: REVOKE

**Meaning**

Formally withdraws canonical trust from a module or version.

**Properties**

- The module remains historically visible
- The module is no longer considered valid for canonical use

**Explicitly does NOT**

- Delete the module
- Rewrite history
- Remove audit trace

---

## 6. Singular Decision Rule

**Rule**

A single Canonical Decision Record (CDR) may express
**one and only one decision type**.

**Implications**

- No bundled decisions
- No chained semantics
- No implicit follow-ups

If multiple actions are desired,
multiple CDRs are required.

---

## 7. No Implicit Cascades

**Rule**

No canonical decision implies any other canonical decision.

**Implications**

- ADD does not imply ACTIVATE
- REPLACE does not imply DEPRECATE
- DEPRECATE does not imply REVOKE

All consequences must be explicitly decided.

---

## 8. Decision vs Outcome

**Rule**

Canonical decisions define **state transitions**, not outcomes.

Whether a decision results in improved behavior,
performance, or correctness is outside canonical semantics.

---

## 9. Validator Boundary

The validator:
- verifies that the decision type is valid
- verifies semantic consistency
- rejects undefined or ambiguous decision types

The validator does **not**:
- infer intent
- optimize decision choice
- reinterpret semantics

---

## 10. Final Lock Statement

This semantic definition is absolute for v0.23.

No implementation, tooling, or workflow may extend,
reinterpret, or bypass these decision semantics
without a new LOCK document.

---

END OF DOCUMENT
