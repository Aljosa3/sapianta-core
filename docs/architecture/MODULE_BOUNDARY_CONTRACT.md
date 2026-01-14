# Module Boundary Contract

Status: CANONICAL — LOCKED  
Applies from: Phase 39  
Authority: Sapianta Architecture  
Scope: All external and internal modules  

---

## 0. Canonical Status

This document defines the canonical and binding contract
between the Sapianta system and any module.

If any module violates this contract,
the module is considered non-compliant and invalid.

This contract defines **boundaries**, not implementations.

---

## 1. Definition of a Module

A module is any component that:

- is not part of the Sapianta Core,
- is not part of Governance, ROI, or Runtime,
- provides domain-specific logic or capabilities
  (e.g. finance, legal analysis, marketing, reporting).

Modules are **guests** in the Sapianta system.

---

## 2. Module Authority and Limitations

Modules:

- have no decision authority,
- have no governance authority,
- have no ROI authority,
- have no execution authority.

Modules may only:
- propose information,
- consume authorized outputs,
- perform execution if explicitly allowed
  via the Execution Gate.

---

## 3. Allowed Module Interfaces

Modules may interact with the system **only** through:

- defined module adapters,
- explicitly exposed runtime outputs,
- execution interfaces authorized by policy.

Modules MUST NOT:
- call the Core directly,
- bypass Governance or ROI,
- invoke execution directly,
- alter system state outside execution scope.

---

## 4. Information Access Rules

Modules may access **only**:

- final RuntimeResult (if exposed),
- execution-specific inputs explicitly provided,
- module configuration and local state.

Modules MUST NOT access:

- CoreRequest input,
- user prompts or payloads,
- GovernanceRequest raw input,
- ROIContext internals,
- Trace data,
- explanations or reasoning artifacts.

Modules operate on **results, not meanings**.

---

## 5. Non-Influence Rule

Modules MUST NEVER:

- alter decisions,
- generate new decisions,
- influence Governance or ROI outcomes,
- feed data back into Core or Runtime,
- reinterpret or override system verdicts.

Any attempt to influence upstream layers
is a contract violation.

---

## 6. Execution Constraints

If a module performs execution:

- it must be invoked exclusively via the Execution Gate,
- it must comply with the Execution Policy,
- it must not extend execution scope beyond authorization,
- it must not introduce implicit retries or side effects.

Execution capability does not imply authority.

---

## 7. Isolation and Removability

Modules must be:

- logically isolated,
- removable without affecting system correctness,
- replaceable without changing decisions.

Removing a module MUST NOT change:
- Core decisions,
- Governance behavior,
- ROI enforcement,
- Runtime outcomes.

---

## 8. Compliance and Certification Readiness

This contract enables:

- domain-specific module certification,
- regulatory compliance mapping (e.g. EU AI Act),
- controlled ecosystem growth.

Modules may be certified independently
without modifying the Sapianta Core.

---

## 9. Contract Lock

This Module Boundary Contract is LOCKED.

Any modification requires:
- a new contract version,
- a new architectural phase,
- explicit approval.

No module may be integrated
without conforming to this contract.
