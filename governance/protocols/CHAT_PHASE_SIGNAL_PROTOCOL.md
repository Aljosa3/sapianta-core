# SAPIANTA CHAT — CHAT ↔ PHASE SIGNAL PROTOCOL (CPSP v0.1)
## Design-only · Non-executing · Governance-aligned

This document defines the **explicit signaling protocol** by which SAPIANTA Chat
knows **which phase is active**.  
It prevents **implicit phase drift** and does **not** enable execution.

CPSP:
- does not authorize writing
- does not open WRITE-GATE
- does not introduce autonomy

Its sole purpose is **phase clarity**.

---

## 0. Fundamental Rule

> **A phase is active only if it is explicitly signaled.**  
> If no valid signal is present, the active phase is **DESIGN**.

Implicit phase inference is **forbidden**.

---

## 1. Valid Phase Signals

The following signals are the **only valid phase declarations**:

- `PHASE: DESIGN`
- `PHASE: SPEC`
- `PHASE: BUILD`
- `PHASE: VALIDATE`
- `PHASE: CONFIRM`

Signals are **case-sensitive** and must match exactly.

---

## 2. Signal Placement and Scope

### 2.1 Placement
- A phase signal must appear **at the start** of a human message.
- Any content before the signal invalidates the signal.

### 2.2 Scope
- A phase signal applies **only to the current interaction scope**.
- Signals do **not persist** across cycles or sessions.

---

## 3. Default Behavior

If:
- no phase signal is provided, or
- the signal is malformed, or
- multiple signals are provided,

then:
- the system must assume `PHASE: DESIGN`.

---

## 4. Forbidden Signals and Patterns

The following are **explicitly forbidden**:

- Multiple phase signals in one message
- Implicit phrases (e.g. “now build”, “let’s validate”)
- Conditional signals (e.g. “if valid then BUILD”)
- System-generated phase signals
- Phase changes without a new explicit signal

Any forbidden pattern results in **DESIGN**.

---

## 5. Phase Transition Rules

- Phase transitions require a **new human message** with a valid signal.
- The system must **not infer** transitions from context.
- The system must **reject** transitions that violate the Formal Phase Model.

CPSP **never** performs transitions; it only **recognizes** them.

---

## 6. Interaction with Governance Components

CPSP operates alongside:

- **Formal Phase Model (FPM)**  
  → defines what each phase allows or forbids

- **WRITE-GATE Contract (WGC)**  
  → governs permission to write (independent of CPSP)

- **Build Scope Declaration (BSD)**  
  → constrains write scope during BUILD

CPSP does **not** override any governance component.

---

## 7. Error Handling

On invalid or forbidden signals:
- the system must remain in **DESIGN**
- no corrective action is taken
- no clarification questions are asked

Silence is treated as **DESIGN**.

---

## 8. Absolute Compliance Test

CPSP is violated if **any** of the following occur:

- A phase other than DESIGN is assumed without a valid signal
- The system infers a phase from context
- The system emits a phase signal
- A phase persists without explicit re-signaling

If any condition is true → **governance violation**.

---

## 9. Boundary Statement

> Phase awareness is explicit, never inferred.

---

## 10. Status

- Design-only
- No execution permission
- No write authorization
- Mandatory for determinist phase control
