# SAPIANTA — IMPLEMENTATION GUARDRAIL RULE

## ID
IGL-GR-002

## Title
No Silent Authority

## Status
ACTIVE — SRS GUARDRAIL  
Non-normative, non-decisional, implementation-level rule

## Scope
This guardrail applies to **all SRS-level components**, including but not limited to:
- Decision runtimes
- Execution components
- Adapters (Chat, CLI, API)
- Auto-generated modules
- Any code produced by AI-assisted or automated build processes

This rule is enforced during **implementation, review, and automated generation**.

## Rule
No SRS component may execute logic, perform actions, or advance system state **without an explicitly declared and injected authority**.

## Disallowed Patterns
The following patterns are strictly forbidden at the SRS level:

- Proceeding with execution when an authority, handler, or decision source is missing
- Falling back to implicit or default authorities
- Substituting missing authority with placeholder, stub, or inferred handlers
- Using conditional logic that silently bypasses absence of authority
- Executing actions based on assumed or inferred permissions

Examples of forbidden constructs (non-exhaustive):
- `handler = handler or DefaultHandler()`
- `if handler is None: proceed_anyway()`
- `authority = authority or self`
- Any execution path where authority absence does not halt execution

## Allowed Behavior
The following behaviors are explicitly allowed:

- Requiring explicit authority injection
- Raising technical exceptions when authority is missing
- Halting execution deterministically on missing authority
- Delegating all authority resolution to authorized decision layers

## Rationale
This rule prevents implicit assumption of authority, which leads to:
- Loss of auditability
- Undetectable policy drift
- Unauthorized system actions

All authority within SAPIANTA must be explicit, traceable, and intentional.

## Enforcement
This guardrail is intended to be:
- Enforced by human review
- Enforced by automated Implementation Guard Layer (IGL) checks
- Applied uniformly to human-written and AI-generated code

Violation of this rule constitutes an **implementation failure**, not a recoverable condition.

## Canonical Relationship
This guardrail does not modify or extend the SAPIANTA Canon, Core Laws, or SCF.

It operationalizes existing authority and responsibility constraints at the SRS implementation level.

---
END OF DOCUMENT
