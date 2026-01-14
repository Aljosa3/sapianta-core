# Execution Policy

Status: CANONICAL — LOCKED  
Applies from: Phase 38  
Scope: Execution layer only  
Authority: Sapianta Architecture  

---

## 0. Canonical Status

This document defines the **canonical and normative rules**
governing execution within the Sapianta system.

If any implementation, module, or adapter contradicts this policy,
the implementation is invalid.

This document defines **what execution is allowed to be**,
not how execution is implemented.

---

## 1. Definition of Execution

Execution is the act of performing **side effects** outside the Sapianta Core,
including but not limited to:

- system actions,
- external API calls,
- data mutation,
- message dispatch,
- infrastructure interaction.

Execution is **never part of decision-making**.

---

## 2. Preconditions for Execution Eligibility

Execution is permitted **only if all of the following conditions hold**:

1. The Core decision is `ACCEPTED`.
2. Governance evaluation has completed without rejection.
3. ROI evaluation has returned `allowed = true`.
4. RuntimeController has returned `RuntimeDecision.PROCEED`.
5. Execution is invoked exclusively via the Execution Gate.

If any condition is not met, execution MUST NOT occur.

---

## 3. Execution Gate Authority

The Execution Gate is the **sole authorized entry point** for execution.

- No module may execute actions directly.
- No adapter may bypass the Execution Gate.
- No execution path may originate from Core, Governance, ROI, or Trace.

If the Execution Gate is disabled or returns `NO_OP`,
execution is considered prohibited.

---

## 4. Information доступ Execution

Execution is allowed to access **only**:

- the final `RuntimeResult`,
- immutable metadata explicitly exposed by runtime,
- execution-specific configuration.

Execution MUST NOT access:

- CoreRequest input,
- user prompts or payloads,
- GovernanceRequest raw input,
- ROIContext internal content,
- Trace records,
- explanations or reasoning artifacts.

Execution operates on **decisions, not meanings**.

---

## 5. Non-Influence Rule

Execution MUST NEVER:

- alter Core decisions,
- alter Governance or ROI outcomes,
- alter Runtime decisions,
- generate new decisions,
- feed information back into the decision pipeline.

Execution is strictly downstream and irreversible.

---

## 6. Failure Handling

If execution fails:

- the failure MUST NOT propagate upstream,
- no retry logic may influence decisions,
- no automatic compensation is allowed by default.

Failure handling may be observed or logged,
but never interpreted as a new decision.

---

## 7. Trace Separation

Execution MUST NOT:

- emit trace records into Runtime Trace,
- consume Runtime Trace,
- extend trace scope.

Execution observability, if implemented,
must be handled via a separate, execution-scoped mechanism.

---

## 8. Removability

The entire execution subsystem may be removed
without affecting:

- Core correctness,
- Governance integrity,
- ROI enforcement,
- Runtime decisions.

If execution is removed,
system behavior MUST remain decision-identical.

---

## 9. Compliance Rationale

This policy enforces:

- strict separation of decision and action,
- non-influence guarantees,
- auditability without side effects,
- compatibility with regulated AI requirements
  (e.g. EU AI Act, ISO-style governance).

Execution is capability, not authority.

---

## 10. Policy Lock

This Execution Policy is LOCKED.

Any change requires:
- a new policy version,
- an explicit architectural decision,
- and a dedicated phase.

No execution capability may be introduced
without conforming to this policy.
