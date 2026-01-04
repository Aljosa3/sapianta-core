# SAPIANTA INTERACTION LAYER

## Canon Compliance Specification v0.1

Status: DRAFT — CANON-COMPLIANT  
Version: v0.1  
Date: 2026-01-03  
Authority: Sapianta Interaction Layer  
Dependency: SAPIANTA_CORE_CANON v1.0  

This document defines how an interactive layer may exist
above the Sapianta Core without violating the Canon.

---

## 0. Canon Dependency

This specification is subordinate to SAPIANTA_CORE_CANON v1.0.

If any interaction behavior conflicts with the Core Canon,
the interaction behavior is invalid.

This document defines interaction constraints, not decision logic.

---

## 1. Purpose of the Interaction Layer

The Interaction Layer exists to:

- accept human input,
- manage conversational context,
- produce natural language responses,
- mediate between humans and system modules.

The Interaction Layer does not decide meaning.

---

## 2. Non-Responsibilities (Hard Limits)

The Interaction Layer MUST NOT:

- decide whether a request is acceptable,
- reinterpret or override ChatResponse,
- generate its own ACCEPTED / REJECTED outcomes,
- soften, harden, negotiate, or contextualize Core decisions,
- execute actions based on its own judgment,
- simulate Core behavior.

If any of the above occurs, the layer is non-compliant.

---

## 3. Relationship to the Core

The Interaction Layer:

- may submit requests to the Core,
- must wait for a ChatResponse,
- may only express the Core decision,
- may not modify decision semantics.

The Core is treated as a black-box authority.

---

## 4. Allowed Interaction Capabilities

The Interaction Layer MAY:

- guide the user in expressing intent,
- clarify phrasing before Core submission,
- rephrase Core outputs into human language,
- provide explanations derived from ExplainResponse,
- maintain conversational memory outside the Core,
- suggest next steps without deciding.

All suggestions are non-binding.

---

## 5. Output Rules

Every user-visible output must fall into one of the following categories:

1. Expression of Core Decision  
   - faithful rendering of ChatResponse  
   - no reinterpretation  

2. Explanation  
   - derived only from ExplainResponse  
   - neutral and descriptive  

3. Non-decisional Assistance  
   - wording help  
   - navigation  
   - education  
   - clarification  

No other output categories are permitted.

---

## 6. LLM Usage Constraints

LLMs may be used by the Interaction Layer only as:

- language generators,
- paraphrasing tools,
- structuring assistants,
- explanatory narrators.

LLMs MUST NOT:

- infer acceptability,
- guess Core outcomes,
- preempt Core decisions,
- simulate rejection or approval logic.

LLMs operate strictly in user space.

---

## 7. Failure and Ambiguity Handling

If the Core returns ambiguity or rejection,
the Interaction Layer may:

- explain why,
- ask the user to rephrase,
- offer educational context.

The Interaction Layer MUST NOT:

- resolve ambiguity itself,
- override the outcome,
- escalate without explicit user action.

---

## 8. Audit and Transparency

The Interaction Layer:

- may display audit confirmation,
- may reference that a decision was recorded,
- may not expose audit internals.

Audit presence does not alter interaction behavior.

---

## 9. Replaceability

Any Interaction Layer implementation:

- is fully replaceable,
- may be rewritten in another language,
- may use different LLMs or UIs,

provided it remains compliant with:

- this specification,
- and SAPIANTA_CORE_CANON v1.0.

---

## 10. Compliance Statement

An Interaction Layer is Sapianta-compliant if and only if:

- it never decides,
- it never overrides,
- it never simulates the Core,
- it always defers authority.

---

## 11. Minimal Conclusion

The Interaction Layer does not know what is right.

It knows how to talk about what the Core has decided.

That is its power.
