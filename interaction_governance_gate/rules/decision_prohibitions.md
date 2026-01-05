# FILE: interaction_governance_gate/rules/decision_prohibitions.md

## DECISION-LEVEL PROHIBITIONS

### DP-1
The Governance Gate MUST NOT emit any decision other than:
ALLOW, DENY, or SEAL.

### DP-2
The Governance Gate MUST NOT attach reasoning, metadata,
severity, or explanation to any decision.

### DP-3
The Governance Gate MUST NOT condition decisions on
external state, history, or timing.

### DP-4
The Governance Gate MUST NOT revise, override, or revoke
a decision once emitted.

### DP-5
Decisions MUST NOT trigger execution, retries, or escalation.
