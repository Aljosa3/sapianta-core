# SAPIANTA_CHAT v0.1 — Thin Chat Refactor Plan

Status: PLAN (pre-implementation)  
Version: v0.1  
Date: 2026-01-29  
Authority: ADR_SAPIANTA_CHAT_v0.1_ARCHITECTURAL_BOUNDARY  
Canon Alignment: SAPIANTA_CORE_CANON v1.0, CORE_LAWS.md, IPV_CANON_v0.1_LOCK  
Path: governance/plans/SAPIANTA_CHAT_THIN_REFACTOR_PLAN_v0.1.md

---

## 0. Purpose

This document defines the **minimal, compliant refactoring plan** for
`SAPIANTA_CHAT` to align implementation with locked governance.

The goal is to reduce Chat to a **thin interaction shell**:
- no orchestration,
- no reasoning,
- no planning,
- no decision-making.

Chat becomes a **delegator + renderer only**.

---

## 1. Architectural Boundary (Authoritative)

### Chat IS:
- a user-facing interaction shell,
- a request normalizer,
- a delegator to HOI Orchestrator,
- an output renderer (HDS-compatible).

### Chat IS NOT:
- an orchestrator,
- a reasoning engine,
- a planning engine,
- a decision authority,
- an executor,
- a Core proxy.

All intelligence, flow control, and subsystem invocation
**belongs exclusively to the HOI Orchestrator**.

---

## 2. Target Module Shape (Canonical)

After refactor, the module MUST conform to:
```text
sapianta_chat/
├── interface/
│ └── cli.py # User input / output only
├── wiring.py # Delegation to HOI Orchestrator
├── output/
│ └── renderer.py # Render HDS / Orchestrator output
├── README.md # Purpose, scope, boundaries
└── __init__.py
```

No other submodules are permitted.

---

## 3. Explicit Removals (Hard)

The following directories MUST be removed from `sapianta_chat/`:

- `orchestrator/`
- `reasoning/`
- `planning/`
- `routing/`
- any internal strategy selectors
- any internal flow control logic

Rationale:
These violate:
- SAPIANTA_CHAT_v0.1_INIT governance,
- HOI_ORCHESTRATOR_ROLE_CONTRACT,
- CORE_LAWS interaction constraints.

---

## 4. Delegation Model (Required)

### Execution Flow (Mandatory)
Human
↓
SAPIANTA_CHAT (CLI / Interface)
↓ (normalized request)
HOI Orchestrator
↓
[LLM / HDS / Modules]
↓
HOI Orchestrator (final response)
↓
SAPIANTA_CHAT (render only)


Chat:
- does NOT select strategies,
- does NOT branch flows,
- does NOT invoke subsystems directly.

---

## 5. Wiring Contract (Minimal)

`wiring.py` SHALL:
- accept a normalized chat request,
- forward it to the HOI Orchestrator,
- receive a final response object,
- pass it unchanged to the renderer.

No interpretation.
No enrichment.
No inference.

---

## 6. Output Rules

Chat output MUST:
- originate from HOI Orchestrator or HDS,
- preserve structure and meaning,
- never introduce recommendations,
- never rank options,
- never suggest actions.

Rendering only.

---

## 7. Tests (Minimum Viable)

After refactor, the following tests are REQUIRED:

1. **Delegation Test**
   - verifies Chat forwards requests to HOI Orchestrator
   - verifies no internal logic is executed

2. **Non-Decision Test**
   - verifies Chat does not produce ACCEPT/REJECT
   - verifies Chat does not infer outcomes

3. **Render Integrity Test**
   - verifies output is unchanged semantically

No behavioral tests beyond this scope.

---

## 8. Documentation Updates (Linked)

Upon completion of this plan, the following MUST be updated:

- `SAPIANTA_CHAT_v0.1_INIT.md` — aligned with thin chat scope
- `SAPIANTA_CHAT_v0.1_LOCK.md` — issued after refactor
- `SAPIANTA_CHAT_v0.1_COMPLETE.md` — issued after tests pass

---

## 9. Non-Goals (Explicit)

This refactor does NOT:
- add features,
- improve UX,
- optimize performance,
- change governance intent.

It is a **compliance and boundary correction only**.

---

## 10. Completion Criteria

This plan is considered fulfilled when:

- Chat contains no orchestration code,
- Chat delegates exclusively to HOI Orchestrator,
- All governance constraints are met,
- Minimal tests pass,
- LOCK and COMPLETE documents are issued.

---

## 11. Final Statement

SAPIANTA_CHAT is not intelligence.

SAPIANTA_CHAT is not a decision-maker.

SAPIANTA_CHAT is a controlled interface boundary.

That is its strength.


