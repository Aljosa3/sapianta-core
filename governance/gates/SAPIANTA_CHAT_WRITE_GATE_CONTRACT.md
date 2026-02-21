# SAPIANTA CHAT — WRITE-GATE CONTRACT (WGC v0.1)
## Design-only · Non-executing · Governance-enforced

This document defines the **single authority mechanism** that permits or forbids
**any write-producing activity** by SAPIANTA Chat.

WRITE-GATE does not execute writes.
WRITE-GATE does not validate content.
WRITE-GATE only decides **whether writing is permitted at all**.

---

## 0. Fundamental Principle

> **No write is allowed unless the WRITE-GATE is explicitly OPEN.**

If WRITE-GATE state is not explicitly OPEN, it is considered **CLOSED** by default.

---

## 1. Scope of WRITE-GATE

WRITE-GATE governs **all write-producing actions**, including but not limited to:
- file generation
- file modification
- structure creation
- commit preparation
- any artifact intended for persistence

WRITE-GATE does **not** govern:
- reasoning
- specification
- analysis
- validation statements

---

## 2. WRITE-GATE States

WRITE-GATE has exactly **two states**:

### 2.1 CLOSED (Default)
- All write-producing actions are **forbidden**
- BUILD phase is **not permitted**
- Any attempt to write constitutes a **governance violation**

### 2.2 OPEN (Explicit)
- Write-producing actions are **conditionally permitted**
- Permission is **temporary** and **context-bound**
- OPEN does not imply correctness or approval

---

## 3. Preconditions for OPEN

WRITE-GATE may be OPEN **only if all conditions below are met**:

1. **Explicit Human Authorization**
   - The human explicitly requests opening the WRITE-GATE
   - Silence or continuation does not count as authorization

2. **Phase Alignment**
   - Current phase is **BUILD**
   - BUILD phase entry has been explicitly confirmed

3. **Governance Compatibility**
   - Proposed writes do not violate:
     - MMC
     - MMC-EXT-1 NO-GO ZONE
     - Formal Phase Model (FPM)

4. **Scope Declaration**
   - The intended write scope is explicitly declared
   - Anything outside the declared scope remains forbidden

If any condition is unmet → WRITE-GATE remains **CLOSED**.

---

## 4. WRITE-GATE Behavior

### 4.1 Non-Interpretive
WRITE-GATE:
- does not interpret intent
- does not judge quality
- does not infer permission

WRITE-GATE evaluates **conditions only**, not meaning.

---

### 4.2 Non-Persistent
WRITE-GATE:
- holds no memory
- does not persist state across cycles
- resets to **CLOSED** after each cycle

---

### 4.3 Non-Delegable
WRITE-GATE:
- cannot be opened by SAPIANTA Chat itself
- cannot be opened implicitly
- cannot be inherited by subsequent phases

Only explicit human action may open it.

---

## 5. Forbidden WRITE-GATE Transitions

The following are **explicitly forbidden**:

- CLOSED → OPEN without human authorization
- OPEN → OPEN across cycles
- OPEN outside BUILD phase
- OPEN for undefined scope
- OPEN as a result of validation outcome

Any forbidden transition is a **hard governance violation**.

---

## 6. Interaction with Phase Model

WRITE-GATE operates **within** the Formal Phase Model:

- DESIGN phase → WRITE-GATE must be CLOSED
- SPEC phase → WRITE-GATE must be CLOSED
- BUILD phase → WRITE-GATE may be OPEN (if authorized)
- VALIDATE phase → WRITE-GATE must be CLOSED
- CONFIRM phase → WRITE-GATE must be CLOSED

WRITE-GATE never changes phases.

---

## 7. Absolute Compliance Test

WRITE-GATE is violated if **any** of the following is true:

- A write occurs while WRITE-GATE is CLOSED
- WRITE-GATE opens without explicit human authorization
- WRITE-GATE opens outside BUILD phase
- Writes exceed the declared scope
- WRITE-GATE state persists beyond the cycle

If YES → **governance violation**.

---

## 8. Boundary Statement

> WRITE-GATE is the mechanism by which the system proves  
> that writing is a **privilege**, not a default behavior.

---

## 9. Status

- Design-only
- No implementation permission
- No execution authority
- Mandatory prerequisite for self-building
