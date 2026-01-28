
From this point forward, the User Module Template specification is **immutable**.

---

## 2. LOCKED PROPERTIES

The following properties are locked and MUST NOT be changed:

- Definition of User Module as:
  - external
  - passive
  - non-executing
  - non-orchestrating
  - non-inferential
- Exclusive dependency on **API v0.1**
- No access to:
  - runtime
  - HOI
  - HDS internals
  - orchestration
- No use of:
  - LLM
  - inference
  - decision logic
- No mutation of core state
- No API surface changes

---

## 3. PERMITTED EVOLUTION (POST-LOCK)

The following are explicitly allowed **without violating this LOCK**:

- Creation of concrete User Modules that conform to the spec
- Addition of:
  - CLI layers (external, passive)
  - Chat layers (external, non-orchestrating)
  - External adapters (read-only or contract-bound)
- Documentation extensions
- Tooling around validation and admission

All extensions MUST remain compliant with the locked template.

---

## 4. PROHIBITED ACTIONS

The following actions are prohibited and invalidate the LOCK:

- Modifying the definition of a User Module
- Granting execution or decision authority
- Introducing runtime hooks
- Expanding API permissions
- Circumventing semantic mapping
- Backporting user logic into core

---

## 5. GOVERNANCE EFFECT

With this LOCK in place:

- POT B (User Modules) is **formally sealed**
- Core remains untouched
- API v0.1 remains the sole integration boundary
- Future module ecosystems can be built safely

---

## 6. LOCK CONFIRMATION

This specification is locked intentionally and irrevocably unless a future
**formal governance phase** explicitly authorizes a new version.

LOCK EFFECTIVE VERSION: v0.1  
LOCK STATUS: ACTIVE
