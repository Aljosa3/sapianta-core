# SAPIANTA — IMPLEMENTATION GUARDRAIL RULE

## ID
IGL-GR-001

## Title
No Semantic Fallbacks

## Status
ACTIVE — SRS GUARDRAIL  
Non-normative, non-decisional, implementation-level rule

## Scope
This guardrail applies to **all SRS-level components**, including but not limited to:
- Chat adapters
- CLI / API adapters
- Module adapters
- Auto-generated modules
- Any code produced by AI-assisted or automated build processes

This rule is enforced during **implementation, review, and automated generation**.

## Rule
No SRS component may generate semantic output, fallback responses, or substitute system decisions under any error, missing dependency, or misconfiguration condition.

## Disallowed Patterns
The following patterns are strictly forbidden at the SRS level:

- Creating or returning synthetic user-facing responses under error conditions  
  (e.g. `"No handler configured"`, `"System not ready"`)
- Translating technical or structural errors into semantic messages
- Generating default `ChatResponse` (or equivalent) objects as substitutes for missing authority
- Handling absence of configuration, authority, or dependency by producing content
- Silent fallback behavior that masks structural or runtime errors

## Allowed Behavior
The following behaviors are explicitly allowed:

- Raising technical exceptions
- Propagating errors unchanged
- Failing hard without semantic mediation
- Delegating all meaning, acceptance, or rejection decisions to authorized decision layers

## Rationale
This rule prevents architectural erosion caused by well-intentioned but unauthorized semantic handling at adapter or interface layers.

It ensures that:
- All meaning originates from authorized decision components
- Adapters remain passive and non-decisional
- Automated module generation does not introduce implicit policy or interpretation

## Enforcement
This guardrail is intended to be:
- Enforced by human review
- Enforced by automated Implementation Guard Layer (IGL) checks
- Applied uniformly to human-written and AI-generated code

Violation of this rule constitutes an **implementation failure**, not a policy exception.

## Canonical Relationship
This guardrail does not modify or extend the SAPIANTA Canon, Core Laws, or SCF.

It operationalizes existing constraints at the SRS implementation level.

---
END OF DOCUMENT
