# Knowledge Anchor Registry

## Status
- Phase: FAZA 23A
- Type: Design-only
- Execution: Forbidden
- Registry state: Authoritative

---

## 1. Purpose

This document defines the **official registry of Knowledge Anchors**
recognized by the SAPIANTA system.

The registry:
- enumerates valid anchors
- defines their authority
- fixes their scope
- prevents implicit or accidental authority

If a document is not listed here,
it is **not** a Knowledge Anchor.

---

## 2. Registry Rules

- Only documents listed in this registry may act as Knowledge Anchors
- Each anchor has a defined authority level
- Conflicts are resolved by authority, then by specificity
- Anchors may only be added by explicit governance action
- Removal or modification requires a new registry version

---

## 3. Anchor List

### KA-001 — SAPIANTA Core Canon

- **Path:** `canon/SAPIANTA_CORE_CANON_v1.0.md`
- **Authority:** Binding
- **Status:** Locked
- **Scope:** Entire system
- **Description:** Fundamental system laws and invariants

---

### KA-002 — Pre-Execution Era Lock

- **Path:** `governance/LOCK_PRE_EXECUTION_ERA.md`
- **Authority:** Binding
- **Status:** Locked
- **Scope:** FAZA 17–19
- **Description:** Permanent lock of non-execution phases

---

### KA-003 — Execution Era Entry Criteria

- **Path:** `governance/EXECUTION_ERA_ENTRY_CRITERIA.md`
- **Authority:** Binding
- **Status:** Active
- **Scope:** Transition into Execution Era
- **Description:** Formal prerequisites for execution capability

---

### KA-004 — Execution Boundary

- **Path:** `governance/EXECUTION_BOUNDARY.md`
- **Authority:** Binding
- **Status:** Active
- **Scope:** All execution-capable modules
- **Description:** Defines what execution may and may not do

---

### KA-005 — Execution Context Definition

- **Path:** `governance/EXECUTION_CONTEXT.md`
- **Authority:** Binding
- **Status:** Active
- **Scope:** Execution environment semantics
- **Description:** Defines execution context structure and limits

---

### KA-006 — Execution Result Definition

- **Path:** `governance/EXECUTION_RESULT.md`
- **Authority:** Binding
- **Status:** Active
- **Scope:** Execution outputs
- **Description:** Defines valid execution result forms

---

### KA-007 — Execution Design Phase Lock

- **Path:** `governance/LOCK_EXECUTION_DESIGN_PHASE.md`
- **Authority:** Binding
- **Status:** Locked
- **Scope:** All execution design artifacts
- **Description:** Locks execution design without implementation

---

### KA-008 — Knowledge Anchor Definition

- **Path:** `governance/KNOWLEDGE_ANCHOR_DEFINITION.md`
- **Authority:** Binding
- **Status:** Active
- **Scope:** Anchor semantics and usage
- **Description:** Defines what Knowledge Anchors are and how they work

---

## 4. Authority Resolution Order

When multiple anchors apply:

1. Binding overrides Guiding
2. More specific scope overrides broader scope
3. Locked overrides Active
4. Newer version overrides older (if explicitly superseding)

No heuristic or model preference is allowed.

---

## 5. Invalid Authority Sources

The following are explicitly NOT Knowledge Anchors:

- model outputs
- reasoning traces
- chat responses
- internal memory
- inferred rules
- undocumented assumptions

---

## 6. Registry Immutability

This registry is:
- normatively binding
- append-only by version
- immutable once locked

Any change requires:
- new registry version
- explicit governance action
- explicit supersession notice

---

## 7. Closing Statement

This registry is the **single source of anchor authority**.

SAPIANTA shall:
- reference anchors by ID
- refuse actions violating binding anchors
- declare absence of anchor when none applies

No anchor. No authority.
