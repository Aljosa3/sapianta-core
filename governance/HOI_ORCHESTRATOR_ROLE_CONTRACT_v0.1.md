# HOI ORCHESTRATOR ROLE CONTRACT v0.1

## Status
LOCKED

## Purpose
Define the deterministic control role of the HOI Orchestrator within the Sapianta system.

The HOI Orchestrator is the sole component responsible for coordinating the interaction flow between:
- Human-facing interfaces (Chat, CLI, UI)
- Advisory modules (LLM)
- Deterministic output layers (HDS / API adapters)

---

## Core Responsibility

The HOI Orchestrator:
- Controls interaction flow deterministically
- Decides which subsystem is invoked and when
- Enforces governance constraints
- Preserves human authority

The HOI Orchestrator is **not** an advisor, reasoner, or executor.

---

## Authority and Constraints

The HOI Orchestrator MAY:
- Accept structured HOI input from Chat / CLI / UI
- Invoke LLM modules as advisory-only components
- Invoke HDS / API adapters for output generation
- Enforce ordering and gating of calls
- Attach execution context metadata
- Reject invalid or non-conforming requests

The HOI Orchestrator MAY NOT:
- Generate free-form reasoning
- Modify system state
- Execute commands
- Perform autonomous decisions
- Persist memory
- Bypass governance layers
- Delegate control to LLMs or UIs

---

## Position in Architecture

Human
 → Interface Layer (Chat / CLI / UI)
   → HOI Orchestrator (deterministic control)
     ├─ LLM Adapter (optional, advisory-only)
     └─ HOI → HDS / API Adapter
         → HDS JSON Output (audit-safe)

The HOI Orchestrator is the **only** component permitted to:
- Invoke LLM modules
- Invoke HDS / API adapters

---

## Interaction Semantics

- All interactions are human-initiated
- All LLM invocations are explicit and contextual
- LLM output is treated as untrusted input
- Final output is always produced via HDS
- The Orchestrator never infers intent autonomously

---

## Determinism Guarantees

- Identical HOI input + identical context ⇒ identical downstream calls
- No hidden state
- No adaptive behavior
- No stochastic control paths

---

## Audit and Traceability

The HOI Orchestrator MUST:
- Preserve traceability metadata
- Maintain correlation identifiers
- Enable stdout-only audit capture
- Ensure replayability of interaction flows

---

## Invariants

- Human authority is absolute
- LLM authority is zero
- Orchestration is deterministic
- Execution is externalized
- Auditability is mandatory

---

## Version
v0.1

## Lock
This contract is immutable unless superseded by a higher-versioned, locked governance document.
