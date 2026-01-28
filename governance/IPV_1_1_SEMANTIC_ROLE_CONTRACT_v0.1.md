# IPV-1.1 SEMANTIC ROLE CONTRACT v0.1

## Status
LOCKED

## Purpose
Define the exact semantic responsibility, output shape, and invariants
of the IPV-1.1 layer.

IPV-1.1 performs deterministic semantic interpretation of HOI input
under explicit invariants. It does not decide, reason, or act.

---

## Role Definition

The IPV-1.1 layer is a **semantic classifier and annotator**.

Its sole function is to transform raw HOI input into a constrained,
structured semantic representation suitable for downstream deterministic
processing.

---

## Authority Boundaries

IPV-1.1 MAY:
- Classify declared human intent into predefined semantic classes
- Attach explicit semantic annotations
- Apply invariant checks
- Reject non-conforming HOI input
- Produce explainable semantic metadata

IPV-1.1 MAY NOT:
- Infer unstated intent
- Rank options
- Optimize outcomes
- Trigger actions
- Invoke APIs
- Invoke LLMs
- Persist memory
- Modify downstream logic

---

## Input Contract

Input to IPV-1.1 MUST be:
- Explicitly human-provided (HOI)
- Context-bounded
- Free of hidden state
- Provided by the HOI Orchestrator only

---

## Output Contract (Canonical Shape)

IPV-1.1 output MUST be fully serializable and deterministic.

```json
{
  "semantic": {
    "intent_class": "inquiry | exploration | confirmation | execution_request | unknown",
    "policy_relevance": "yes | no | unknown",
    "risk_sensitivity": "declared_low | declared_medium | declared_high | unspecified",
    "explanation_requested": true | false
  },
  "meta": {
    "ipv_version": "1.1",
    "trace_id": "<uuid>",
    "source": "ipv",
    "audit_hint": "stdout-only"
  }
}
```
No additional fields are permitted unless explicitly versioned.

## Determinism Guarantees

- Identical HOI input + identical context ⇒ identical IPV output
- No stochastic behavior
- No adaptive rules
- No historical dependency

## Invariants

### Human Intent Preservation
Declared intent must not be altered or overridden.

### Non-Autonomy
Semantic interpretation must never escalate into action.

### No Hidden Reasoning
All semantic assignments must be explainable.

### Auditability
Output must be replayable via stdout capture.

## Explain-on-Demand
- IPV-1.1 MUST support explicit explanation requests
- Explanations MUST reference only:
  - declared intent
  - mapping rules
  - invariant checks
- No speculative reasoning is allowed

## Architectural Position
Human
→ Interface (Chat / CLI / UI)
→ HOI Orchestrator
→ IPV-1.1 (this module)
→ HOI → HDS / API Adapter
→ HDS JSON Output

## Compatibility
HOI Orchestrator v0.1
HDS JSON Output v0.3+
API v0.1
Audit Harness v0.1

## Version
v0.1

## Lock

This contract is immutable unless superseded by a higher-versioned,
explicitly LOCKED governance document.