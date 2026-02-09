# BUILD SCOPE DECLARATION (BSD) — TEMPLATE v0.1
## Design-only · Non-executing · WRITE-GATE Input

This document is the **mandatory scope declaration** required to OPEN the WRITE-GATE.
It defines **what is permitted to be written**, never **how** it is written.

BSD does not authorize execution.
BSD does not validate correctness.
BSD only constrains **write scope**.

---

## 0. Fundamental Rule

> **Anything not explicitly listed in this BSD is forbidden.**

WRITE-GATE permission is **scope-bounded** by this document alone.

---

## 1. Declaration Metadata

- **Requester (Human):** __________________________
- **Date:** __________________________
- **Phase:** BUILD
- **WRITE-GATE Request:** OPEN (scope-bounded)
- **Related Governance References:**
  - MMC
  - MMC-EXT-1 NO-GO ZONE
  - SAPIANTA Chat Formal Phase Model (FPM)
  - SAPIANTA Chat WRITE-GATE Contract (WGC)

---

## 2. Authorized Write Targets

List **only** the exact write targets permitted.

### 2.1 Files (Exact Paths)
- __________________________
- __________________________

### 2.2 Directories (Exact Paths)
- __________________________
- __________________________

Notes:
- Paths must be absolute or repository-root-relative.
- Wildcards are **not allowed**.

---

## 3. Authorized Write Actions

Select **only** the actions explicitly permitted:

- [ ] Create new file(s)
- [ ] Modify existing file(s)
- [ ] Create new directory(ies)
- [ ] Prepare commit commands (no execution)

All unchecked actions are **forbidden**.

---

## 4. Explicit Prohibitions (Scope-Level)

The following are **explicitly forbidden**, even during WRITE-GATE OPEN:

- Writes outside the listed targets
- Changes to governance documents not listed above
- Any execution or runtime triggering
- Any interpretation, recommendation, or decision-making
- Any implicit expansion of scope

---

## 5. Temporal Scope

- **Scope Validity:** Single BUILD cycle only
- **Persistence:** None
- **Carry-over:** Forbidden

Upon completion of the cycle, WRITE-GATE must return to **CLOSED**.

---

## 6. Compliance Assertions

By opening WRITE-GATE under this BSD, it is asserted that:

- The scope does not violate MMC or MMC-EXT-1
- The scope respects the Formal Phase Model
- The scope is sufficient and minimal
- Responsibility remains entirely human

---

## 7. Human Authorization

I explicitly authorize WRITE-GATE to OPEN **only** for the scope declared above.

- **Human Name:** __________________________
- **Signature (Textual):** __________________________
- **Confirmation Phrase:** “OPEN WRITE-GATE FOR THIS SCOPE ONLY”

---

## 8. Absolute Compliance Test

WRITE-GATE usage under this BSD is **invalid** if any of the following occur:

- A write happens outside declared scope
- An undeclared action is performed
- Scope is implicitly expanded
- WRITE-GATE remains OPEN after the cycle

If any condition is true → **governance violation**.

---

## 9. Status

- Template only
- No execution permission
- Mandatory input for WRITE-GATE
- Final authority on write scope
