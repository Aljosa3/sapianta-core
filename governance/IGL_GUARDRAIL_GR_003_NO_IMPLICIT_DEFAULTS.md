# SAPIANTA — IMPLEMENTATION GUARDRAIL RULE

## ID
IGL-GR-003

## Title
No Implicit Defaults

## Status
ACTIVE — SRS GUARDRAIL  
Non-normative, non-decisional, implementation-level rule

## Scope
This guardrail applies to **all SRS-level components**, including but not limited to:
- Decision runtimes
- Execution components
- Adapters (Chat, CLI, API)
- Configuration loaders
- Auto-generated modules
- Any code produced by AI-assisted or automated build processes

This rule is enforced during **implementation, review, and automated generation**.

## Rule
No SRS component may introduce, assume, or apply **implicit default values** for configuration, behavior, authority, policy, or execution parameters.

All defaults must be **explicitly provided, declared, and traceable**.

## Disallowed Patterns
The following patterns are strictly forbidden at the SRS level:

- Assigning fallback values when configuration is missing
- Inferring behavior from absence of configuration
- Using language-level defaults to mask missing inputs
- Silently normalizing `None`, empty, or missing values into operational parameters
- Auto-filling configuration, policy, or mode values

Examples of forbidden constructs (non-exhaustive):
- `value = value or DEFAULT`
- `timeout = config.timeout if config.timeout else 30`
- `mode = mode or "safe"`
- `policy = policy or DefaultPolicy()`
- Any execution path that proceeds using inferred defaults

## Allowed Behavior
The following behaviors are explicitly allowed:

- Requiring explicit configuration injection
- Raising technical exceptions on missing configuration
- Halting execution deterministically when required values are absent
- Passing configuration responsibility to authorized decision layers
- Treating absence of configuration as an error, not a signal

## Rationale
Implicit defaults introduce **hidden decisions** into the system:
- They alter behavior without explicit intent
- They obscure auditability and traceability
- They enable silent drift in automated systems

All operational values within SAPIANTA must be **intentional, explicit, and reviewable**.

## Enforcement
This guardrail is intended to be:
- Enforced by human review
- Enforced by automated Implementation Guard Layer (IGL) checks
- Applied uniformly to human-written and AI-generated code

Violation of this rule constitutes an **implementation failure**, not a recoverable condition.

## Canonical Relationship
This guardrail does not modify or extend the SAPIANTA Canon, Core Laws, or SCF.

It operationalizes determinism and explicitness requirements at the SRS implementation level.

---
END OF DOCUMENT
