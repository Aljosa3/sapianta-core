# SAPIANTA_CHAT v0.1 — INIT

Status: INIT  
Version: v0.1  
Date: 2026-01-29  
Authority: Sapianta Governance  
Alignment:
- ADR_SAPIANTA_CHAT_v0.1_ARCHITECTURAL_BOUNDARY (LOCKED)
- SAPIANTA_CHAT_THIN_REFACTOR_PLAN_v0.1 (PLAN)
- SAPIANTA_CORE_CANON v1.0 (LOCKED)
- CORE_LAWS.md (CANON-COMPLIANT)
- IPV_CANON_v0.1_LOCK (LOCKED)

---

## 0. Purpose

This document defines the **authoritative initiation scope** for
`SAPIANTA_CHAT v0.1`.

It establishes SAPIANTA_CHAT as a **thin interaction layer** whose sole role
is to mediate between a human user and the HOI Orchestrator **without
performing any reasoning, orchestration, or decision-making**.

This INIT supersedes all prior interpretations of “Chat” as an intelligent
or autonomous subsystem.

---

## 1. Canonical Position in the System

SAPIANTA_CHAT is an **external interaction layer**.

It is:
- subordinate to SAPIANTA_CORE_CANON,
- constrained by CORE_LAWS,
- architecturally bounded by the locked ADR.

SAPIANTA_CHAT has **no authority** over meaning, decisions, or execution.

---

## 2. Role Definition (Normative)

### SAPIANTA_CHAT SHALL:

- accept human input,
- normalize input into a request form suitable for delegation,
- delegate requests exclusively to the HOI Orchestrator,
- receive final responses from the HOI Orchestrator,
- render responses faithfully to the user.

### SAPIANTA_CHAT SHALL NOT:

- interpret user intent,
- perform semantic analysis,
- perform orchestration or flow control,
- select strategies or subsystems,
- invoke LLMs directly,
- invoke HDS or APIs directly,
- perform planning, reasoning, or optimization,
- make or simulate decisions,
- rank options or recommend actions,
- execute commands or cause side effects.

Any such behavior constitutes a **governance violation**.

---

## 3. Architectural Boundary (Binding)

All intelligence, reasoning, heuristics, and control flow belong
**exclusively** to the HOI Orchestrator.

The mandatory execution flow is:

Human
  ↓
SAPIANTA_CHAT (interface only)
  ↓
HOI Orchestrator
  ↓
[LLM / HDS / Subsystems]
  ↓
HOI Orchestrator (final response)
  ↓
SAPIANTA_CHAT (render only)

SAPIANTA_CHAT may not bypass or replace the HOI Orchestrator.

---

## 4. Relationship to the Core

SAPIANTA_CHAT:

- does not submit requests directly to the SAPIANTA Core,
- does not receive ChatResponse or ExplainResponse directly,
- never alters or interprets Core outputs.

Any Core interaction occurs **only through the HOI Orchestrator**.

This preserves:
- Core isolation,
- determinism,
- canonical authority.

---

## 5. Output Constraints

All user-visible output produced by SAPIANTA_CHAT MUST:

- originate from the HOI Orchestrator or HDS,
- preserve original semantic meaning,
- be rendered without enrichment or interpretation.

SAPIANTA_CHAT output is **presentational only**.

---

## 6. Module Scope (v0.1)

The scope of SAPIANTA_CHAT v0.1 is intentionally minimal.

Included:
- CLI or equivalent interface,
- request normalization,
- delegation wiring,
- output rendering.

Excluded:
- orchestration logic,
- reasoning or planning logic,
- strategy selection,
- persistence,
- audit generation,
- learning or adaptation.

---

## 7. Compliance with CORE_LAWS

SAPIANTA_CHAT complies with CORE_LAWS by:

- never deciding acceptability,
- never overriding or simulating Core decisions,
- never executing actions,
- deferring all authority upstream.

SAPIANTA_CHAT is a **non-authoritative interaction surface**.

---

## 8. Compliance with IPV_CANON

SAPIANTA_CHAT performs **no analytical, heuristic, or normative reasoning**.

It does not:
- evaluate options,
- generate proposals,
- assess likelihoods,
- infer optimal actions.

All such activity, if any, belongs outside Chat.

---

## 9. Refactoring Reference

This INIT is implemented through:

- `SAPIANTA_CHAT_THIN_REFACTOR_PLAN_v0.1.md`

That plan is **binding for implementation** and must be completed
before LOCK or COMPLETE status may be issued.

---

## 10. Exit Criteria

This INIT phase may advance to LOCK only when:

- SAPIANTA_CHAT implementation conforms to this document,
- the Thin Chat Refactor Plan is fulfilled,
- minimal delegation and render tests pass,
- no prohibited logic remains in the module.

---

## 11. Final Statement

SAPIANTA_CHAT is not intelligence.

SAPIANTA_CHAT is not a decision-maker.

SAPIANTA_CHAT is a controlled interface boundary.

This limitation is intentional and canonical.
