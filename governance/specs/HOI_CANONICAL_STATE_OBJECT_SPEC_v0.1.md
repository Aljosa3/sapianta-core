# HOI_CANONICAL_STATE_OBJECT_SPEC_v0.1
Status: DRAFT
Layer: Execution Layer
Scope: Deterministic Core
Related: HOI_BUILD_FLOW_SPEC_v0.1_LOCK, MODULE_FORMAT_SPEC_v0.1_LOCK

---

## 1. PURPOSE

This document defines the canonical state object used by the HOI (Human Orientation Interface) execution layer.

The canonical state object is:

- The single source of truth for module construction state
- Deterministic
- Serializable
- Audit-replayable
- Independent of conversational history
- Immutable per transition (versioned on mutation)

This specification introduces no learning, no adaptation, and no runtime intelligence.

---

## 2. DESIGN PRINCIPLES

The canonical state object must satisfy:

1. Determinism  
   Identical input sequence ⇒ identical state.

2. Explicitness  
   No inferred fields. All fields must be explicit.

3. Separation  
   No conversational artifacts (chat turns, wording, prompts).

4. Isolation  
   No LLM dependency.

5. Serializability  
   Must be JSON-serializable.

6. Transition Safety  
   State changes allowed only through validated transitions.

---

## 3. STATE OBJECT STRUCTURE

CanonicalStateObject v0.1:

```json
{
  "version": "v0.1",
  "program": {
    "name": "",
    "description": ""
  },
  "module": {
    "name": "",
    "type": "",
    "description": ""
  },
  "intent": {
    "statement": "",
    "normalized_form": "",
    "status": "PENDING | CONFIRMED"
  },
  "scope": {
    "in_scope": [],
    "out_of_scope": [],
    "status": "PENDING | CONFIRMED"
  },
  "constraints": {
    "acknowledged": false,
    "list": []
  },
  "structure": {
    "definition": "",
    "status": "PENDING | CONFIRMED"
  },
  "lifecycle": {
    "current_stage": "ENTRY | INTENT | SCOPE | CONSTRAINTS | STRUCTURE | AUTHORIZATION | ARTIFACT | EXIT",
    "history": []
  },
  "authorization": {
    "approved": false,
    "timestamp": null
  },
  "metadata": {
    "created_at": "",
    "last_modified": "",
    "state_hash": ""
  }
}
```

## 4. STATE INVARIANTS

The following invariants MUST hold:

1. `authorization.approved == true`  
   ⇒ `lifecycle.current_stage == AUTHORIZATION`

2. `lifecycle.current_stage == ARTIFACT`  
   ⇒ `intent.status == CONFIRMED`  
   AND `scope.status == CONFIRMED`  
   AND `constraints.acknowledged == true`  
   AND `structure.status == CONFIRMED`

3. `constraints.acknowledged == true`  
   ⇒ `constraints.list` must be non-empty

4. No stage skipping allowed.

5. `lifecycle.history` must be append-only.


---

## 5. MUTATION RULES

State mutation is allowed only through:

1. Explicit transition functions  
2. Validation guards  
3. Immutable update (new object version)

Direct field mutation is forbidden.


---

## 6. RELATION TO CONVERSATION

Conversation:

- May inform state creation  
- Must not be stored inside canonical object  
- Must not influence behavior outside validated transitions  

Canonical state must be reconstructible without chat logs.


---

## 7. EXPORT CONTRACT

When:

`authorization.approved == true`

State becomes eligible for:

- Deterministic export  
- Prompt payload generation  
- Artifact construction  

Exporter must use canonical state only.

No conversational memory permitted.


---

## 8. VERSIONING

Future changes to structure require:

- New version identifier  
- Migration path  
- Explicit LOCK  


END OF SPEC
