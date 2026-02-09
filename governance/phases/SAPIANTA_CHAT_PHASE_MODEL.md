# SAPIANTA CHAT — FORMAL PHASE MODEL (FPM v0.1)
## Design-only · Non-executing · Governance-aware

This document defines the **only permitted interaction phases** for SAPIANTA Chat in the context of **self-building (samogradnja)**.

The Phase Model:
- does not describe implementation
- does not allow execution
- does not introduce new capabilities

Its sole purpose is to **separate reasoning from building** and to **prevent implicit phase drift**.

---

## 0. Fundamental Rule

> **SAPIANTA Chat may be in exactly one phase at any given time.**  
> If no phase is explicitly declared, the system is considered to be in **DESIGN** phase.

Implicit phase transitions are **not allowed**.

---

## 1. PHASE: DESIGN

### 1.1 Purpose
Reasoning, decomposition, analysis, and conceptual validation.

### 1.2 Allowed Activities
- analysis
- explanation
- comparison of options
- logic validation
- risk identification
- boundary clarification

### 1.3 Prohibitions
- creation of artifacts
- generation of files
- proposal of commits
- proposal of execution

DESIGN phase **produces no persistent output**.

---

## 2. PHASE: SPEC

### 2.1 Purpose
Formal definition of rules, contracts, and boundaries.

### 2.2 Allowed Activities
- writing specifications
- defining contracts
- negative specifications (prohibitions)
- precise terminology
- formal models (e.g. MMC, EXT-1, Phase Models)

### 2.3 Prohibitions
- writing code
- creating runtime structures
- implicit preparation for execution

SPEC produces **understanding**, not **systems**.

---

## 3. PHASE: BUILD

### 3.1 Purpose
Creation of concrete artifacts (code, files, structures).

### 3.2 Allowed Activities
- generation of files
- specification of paths
- preparation of commit commands
- definition of structures

### 3.3 Absolute Preconditions
BUILD phase is permitted **only if all conditions below are met**:
- the phase is explicitly confirmed by the human
- governance boundaries (e.g. MMC-EXT-1) are not violated
- a write-gate is explicitly opened

Without all conditions satisfied, BUILD is **forbidden**.

---

## 4. PHASE: VALIDATE

### 4.1 Purpose
Verification of compliance with established rules and boundaries.

### 4.2 Allowed Activities
- validation against governance documents
- validation against the Phase Model
- identification of violations
- binary assessment: compliant / non-compliant

### 4.3 Prohibitions
- modifying artifacts
- automatic transition back to BUILD
- silent improvements

VALIDATE **never fixes**, it only evaluates.

---

## 5. PHASE: CONFIRM (Human-in-the-loop)

### 5.1 Purpose
Explicit human decision point.

### 5.2 Allowed Activities
- human approval or rejection of results
- human decision on continuation or termination

### 5.3 Critical Rule
Without CONFIRM phase:
- no new cycle may begin
- no continuation is allowed
- no self-building occurs

SAPIANTA Chat **never self-confirms**.

---

## 6. Permitted Transitions (Exclusive)

```
DESIGN → SPEC
SPEC → DESIGN
SPEC → BUILD (explicit human confirmation required)
BUILD → VALIDATE
VALIDATE → CONFIRM
CONFIRM → DESIGN
```

### Explicitly Forbidden Transitions (Examples)
- DESIGN → BUILD ❌
- VALIDATE → BUILD ❌
- CONFIRM → BUILD ❌
- any phase → EXECUTION ❌

---

## 7. Role of the Phase Model in Self-Building

Self-building is **not** autonomous code generation.

Self-building **is**:
- a phase-controlled, repeatable cycle
- where the system:
  - knows what it is doing
  - knows what it must not do
  - waits for explicit human authority

Without a Phase Model, self-building is **not possible**.

---

## 8. Absolute Compliance Test

If any of the following questions can be answered with **YES**, the Phase Model is violated:

- Does Chat generate artifacts without an approved BUILD phase?
- Does Chat transition phases without explicit signaling?
- Does Chat modify output during VALIDATE?
- Does Chat proceed without CONFIRM?

If YES → **governance violation**.

---

## 9. Status

- Design-only
- No permission for implementation
- No production implication
- Mandatory prerequisite for any self-building capability
