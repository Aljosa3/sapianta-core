# CONSTITUTIONAL_CONTRACT_LOCK_v1.0

Status: LOCKED  
Layer: Constitutional Runtime (L1)  
Effective Version: 1.0  

---

## 1. PURPOSE

This document freezes the Constitutional Contract between:

- Domain Layer
- Constitutional Runtime
- Deterministic Core

No breaking semantic changes are allowed without Promotion Gate approval.

---

## 2. PROPOSAL ARTIFACT CONTRACT

A Proposal MUST:

- Be immutable after creation
- Contain a deterministic canonical payload
- Be hash-bound
- Not depend on runtime environment state
- Not contain jurisdiction-specific logic

Proposal creation must be pure and deterministic.

---

## 3. ADVISORY ARTIFACT CONTRACT

An Advisory MUST:

- Reference exactly one Proposal
- Be derived deterministically from Proposal + Policy
- Be replayable
- Not modify Proposal state
- Not embed compliance logic

Advisory is evaluation, not execution.

---

## 4. AUTHORITY DISCIPLINE

Decision finalization requires:

- Explicit authority role
- Valid authority context
- No implicit overrides
- Override reason when required by Governance

Authority validation belongs to Constitutional Runtime.

---

## 5. DECISION ENVELOPE STRUCTURE

The envelope MUST include:

- proposal_hash
- advisory_hash
- policy_hash
- engine_version

Future extensions may include jurisdiction_profile_hash.

Envelope structure is frozen in v1.0.

---

## 6. DETERMINISTIC REPLAY GUARANTEE

Given identical:

- Proposal payload
- Policy definition
- Engine version

The Advisory result MUST be identical.

Any violation is constitutional breach.

---

## 7. DOMAIN RESPONSIBILITIES

Domains:

- Build valid Proposal payloads
- Define domain-specific Policy
- Must not perform authority checks
- Must not alter Constitutional semantics

Domains are subordinate to Spine.

---

## 8. NON-GOALS

This lock does NOT define:

- Jurisdiction behavior
- Promotion Gate rules
- Policy DSL evolution
- Cross-domain arbitration

---

## 9. BREAKING CHANGE DISCIPLINE

Any modification to:

- Proposal structure
- Advisory derivation
- Envelope structure
- Authority model

Requires:

- Promotion Gate classification
- Structural change approval
- Version increment

---

END OF LOCK v1.0