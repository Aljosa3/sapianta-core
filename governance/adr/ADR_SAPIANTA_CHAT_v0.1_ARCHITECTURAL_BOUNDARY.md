# ADR — SAPIANTA_CHAT v0.1
## Architectural Boundary Decision

---

## Status

- **Status:** ACCEPTED
- **Date:** 2026-01-29
- **Decision Scope:** SAPIANTA_CHAT v0.1
- **Authority:** Sapianta Governance
- **Related Canons:**
  - SAPIANTA_CORE_CANON v1.0
  - CORE_LAWS.md
  - IPV_CANON_v0.1_LOCK.md
  - HOI_ORCHESTRATOR_ROLE_CONTRACT_v0.1.md

---

## Context

Repository introspection (2026-01-29) identified a divergence between
governance definitions of **SAPIANTA_CHAT** and its existing technical
implementation.

Governance documents consistently define SAPIANTA_CHAT as:

- a communication and interaction layer,
- without orchestration authority,
- without reasoning or planning capability,
- without access to LLMs, HDS, or APIs,
- without decision-making responsibility.

However, the current implementation located in `sapianta_chat/`
contains internal orchestration, reasoning, and planning logic,
resulting in an architectural overlap with the HOI Orchestrator role.

This overlap violates explicit governance constraints.

---

## Decision

**SAPIANTA_CHAT v0.1 SHALL NOT perform orchestration, reasoning, or planning.**

The following architectural boundaries are hereby fixed:

1. SAPIANTA_CHAT is a **thin interaction layer only**.
2. SAPIANTA_CHAT SHALL:
   - accept human input,
   - manage conversational phrasing and rendering,
   - delegate all interaction flow control to the HOI Orchestrator.
3. SAPIANTA_CHAT SHALL NOT:
   - contain an orchestrator,
   - contain reasoning or planning strategies,
   - invoke LLMs, HDS modules, APIs, or Core directly,
   - interpret intent or assess acceptability.

All orchestration authority remains exclusively within
the HOI Orchestrator, as defined by
`HOI_ORCHESTRATOR_ROLE_CONTRACT_v0.1.md`.

---

## Consequences

### Immediate

- Existing orchestration, reasoning, and planning logic
  within `sapianta_chat/` is **architecturally invalid** for Chat
  and must be removed or relocated.

### Short-term

- `sapianta_chat/` will be refactored to contain only:
  - interface (CLI / UI),
  - output rendering,
  - delegation wiring to HOI Orchestrator.

### Long-term

- Reasoning and planning logic may be:
  - relocated into the HOI Orchestrator,
  - or extracted into a separate IPV-compliant reasoning module.

Governance documents SHALL NOT be modified to legitimize
the current divergent implementation.

---

## Compliance Statement

This decision:

- preserves strict compliance with SAPIANTA_CORE_CANON v1.0,
- enforces CORE_LAWS.md interaction constraints,
- aligns SAPIANTA_CHAT with IPV_CANON_v0.1_LOCK.md,
- maintains a single authoritative orchestration layer.

---

## Closure

This ADR is binding for **SAPIANTA_CHAT v0.1**.

All future implementation and governance actions
must conform to this boundary decision.

---
