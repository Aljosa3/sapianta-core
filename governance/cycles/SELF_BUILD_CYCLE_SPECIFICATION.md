# SAPIANTA CHAT — SELF-BUILD CYCLE SPECIFICATION (SBC v0.1)
## Design-only · Non-executing · Governance-controlled

This document defines the **single, unified self-build cycle** for SAPIANTA Chat.
It specifies **how phases relate as one controlled process**, not how anything is implemented.

This specification:
- does not enable execution
- does not grant new capabilities
- does not authorize autonomy

Its purpose is to ensure that **self-building is a governed process**, not an emergent behavior.

---

## 0. Fundamental Definition

> **Self-building is a closed, phase-governed cycle that can only progress
> through explicit human authority and governance compliance.**

Self-building is **not**:
- autonomous generation
- continuous improvement
- self-directed evolution

Self-building **is**:
- a bounded process
- with explicit checkpoints
- and enforced human responsibility

---

## 1. Cycle Overview

The Self-Build Cycle consists of exactly **five phases**, executed in strict order:
```
DESIGN → SPEC → BUILD → VALIDATE → CONFIRM
```

No phase may be skipped.
No phase may be repeated implicitly.
No phase may transition out of order.

---

## 2. Phase Roles within the Cycle

### 2.1 DESIGN — Reasoning Phase
**Role in Cycle:**
- Explore the problem space
- Identify constraints, risks, and unknowns
- Prepare conceptual readiness for specification

**Cycle Constraints:**
- No artifacts are produced
- No commitments are made
- No transition to BUILD is possible

---

### 2.2 SPEC — Formalization Phase
**Role in Cycle:**
- Translate reasoning into formal definitions
- Define rules, contracts, and boundaries
- Produce precise, reviewable specifications

**Cycle Constraints:**
- No code or runtime structures
- No implicit preparation for execution
- SPEC must be complete before BUILD is possible

---

### 2.3 BUILD — Artifact Creation Phase
**Role in Cycle:**
- Create only the artifacts explicitly authorized
- Operate strictly within declared scope

**Cycle Constraints (All Mandatory):**
- BUILD phase explicitly confirmed by human
- WRITE-GATE explicitly OPEN
- Valid Build Scope Declaration (BSD) present
- No violation of MMC or MMC-EXT-1

Without all constraints satisfied, BUILD **cannot occur**.

---

### 2.4 VALIDATE — Compliance Phase
**Role in Cycle:**
- Assess artifacts against:
  - specifications
  - governance boundaries
  - phase rules

**Cycle Constraints:**
- Validation is read-only
- No fixes, improvements, or changes
- Output is strictly binary: compliant / non-compliant

VALIDATE cannot transition back to BUILD.

---

### 2.5 CONFIRM — Human Authority Phase
**Role in Cycle:**
- Final human decision point
- Accept or reject the cycle outcome

**Cycle Constraints:**
- Only a human may confirm
- No automatic acceptance
- Rejection terminates the cycle

Without CONFIRM, the cycle **cannot complete**.

---

## 3. Permitted Cycle Transitions

The only valid transitions within a self-build cycle are:
```
DESIGN → SPEC
SPEC → BUILD
BUILD → VALIDATE
VALIDATE → CONFIRM
```

Any deviation constitutes a **governance violation**.

---

## 4. Cycle Termination Rules

A self-build cycle terminates when:

- CONFIRM is completed (accept or reject), or
- A governance violation is detected, or
- The human explicitly aborts the cycle

There is **no automatic restart**.

A new cycle requires:
- a new DESIGN phase
- fresh human intent
- fresh authorization

---

## 5. Relationship to Governance Components

The Self-Build Cycle is constrained by:

- **Formal Phase Model (FPM)**  
  → defines phase semantics and prohibitions

- **WRITE-GATE Contract (WGC)**  
  → controls permission to write during BUILD

- **Build Scope Declaration (BSD)**  
  → defines exact write scope

- **MMC-EXT-1 NO-GO ZONE**  
  → enforces absolute semantic limits

The cycle **cannot override** any of these components.

---

## 6. Responsibility Model

### Human
- Owns intent
- Grants authority
- Confirms or rejects outcomes
- Bears full responsibility

### SAPIANTA Chat
- Executes the cycle mechanically
- Enforces phase discipline
- Refuses progression when rules are violated
- Never assumes authority

---

## 7. Absolute Compliance Test

The Self-Build Cycle is violated if **any** of the following occur:

- BUILD occurs without explicit human authorization
- WRITE-GATE opens implicitly
- Scope is exceeded
- VALIDATE modifies artifacts
- CONFIRM is bypassed
- A new cycle starts without a new DESIGN phase

If any condition is true → **governance violation**.

---

## 8. Boundary Statement

> Self-building in SAPIANTA is not freedom to act,
> but discipline to wait.

---

## 9. Status

- Design-only
- No implementation permission
- No autonomy implied
- Final structural prerequisite for governed self-building

