# IPV-1.1 — INIT

## Status
INIT
Lifecycle: active

## Scope
Initialize IPV-1.1 as the first governed semantic interpretation layer
between human intent (HOI) and downstream deterministic output (HDS).

IPV does not decide, execute, or act.
IPV interprets, constrains, and classifies intent under explicit invariants.

---

## Purpose

The purpose of IPV-1.1 is to:
- Introduce a formal semantic layer for intent handling
- Prevent uncontrolled interpretation drift
- Enable policy-aware interaction without autonomy
- Prepare the system for regulated, explainable reasoning

IPV is a **meaning gate**, not an agent.

---

## Position in Architecture

Human
 → Interface (Chat / CLI / UI)
   → HOI Orchestrator (deterministic control)
     → IPV Layer (semantic interpretation under invariants)
       → HOI → HDS / API Adapter
         → HDS JSON Output (audit-safe)

The IPV layer never interfaces directly with:
- Execution systems
- Runtime actions
- External services

---

## Core Responsibilities

The IPV layer SHALL:
- Interpret HOI input into constrained semantic categories
- Apply invariant checks before downstream propagation
- Attach semantic annotations to the interaction context
- Enable explainable interpretation paths
- Remain fully deterministic

The IPV layer SHALL NOT:
- Rank options
- Optimize outcomes
- Make decisions
- Trigger actions
- Persist memory
- Adapt based on history
- Introduce probabilistic control flow

---

## Semantic Units (Initial)

IPV-1.1 introduces the following **non-exhaustive** semantic primitives:

- Intent Class (e.g. inquiry, exploration, confirmation)
- Constraint Surface (explicit / implicit)
- Risk Sensitivity (declared, not inferred)
- Policy Relevance (yes / no / unknown)
- Explanation Demand (explicit only)

No inference beyond declared or structurally deducible information is allowed.

---

## Invariants

IPV-1.1 MUST enforce:

1. Human authority invariance  
   → No semantic transformation may override explicit human intent.

2. Non-autonomy invariance  
   → IPV never escalates interpretation into action.

3. Determinism invariance  
   → Same HOI input + same context ⇒ same semantic output.

4. Auditability invariance  
   → All semantic annotations must be observable and replayable.

---

## Explainability

All IPV semantic outputs must:
- Be representable in structured form
- Be explainable on explicit request
- Produce no hidden or implicit rationale

Explain-on-Demand applies identically to IPV as to HDS.

---

## Compatibility

IPV-1.1 is compatible with:
- HOI Orchestrator v0.1
- HDS JSON Output v0.3+
- API v0.1
- Audit Harness v0.1

No backward compatibility guarantees are required (new semantic layer).

---

## Deliverables (for this phase)

- IPV-1.1 semantic contract
- Minimal IPV module structure
- Deterministic semantic mapping logic
- Audit snapshot
- INIT → LOCK → COMPLETE documents

---

## Non-Goals (Explicit)

- No LLM-driven interpretation
- No policy enforcement engine
- No scoring or ranking
- No learning
- No memory
- No autonomy

---

## Version
IPV-1.1

## Next Step
Implement IPV-1.1 semantic contract and minimal module skeleton.

---

INIT CONFIRMED.
