# LOCK — CLOSURE #6a
## Chat → Structured Intent Protocol (CSIP)

**Status:** LOCKED  
**Applies from:** SAPIANTA v0.42+  
**Type:** Governance / Protocol  
**Execution:** NONE  
**Write:** NONE  

---

## 1. PURPOSE

Closure #6a defines a **canonical, deterministic, and non-executive protocol**
for converting conversational human input into a **structured intent object**.

This protocol bridges:

> Human Conversation → Governed System Routing

without introducing interpretation, execution, planning, or write capability.

---

## 2. SCOPE

**Input:** raw human text  
**Output:** structured intent object  

Explicitly excluded:
- build preparation
- module creation
- execution intent
- write operations
- decision preview generation

---

## 3. GOVERNANCE POSITION

CSIP is positioned **before**:
- HOI Runtime
- HDS
- Decision Preview
- ModuleBuilder
- Execution Gates

It is a **pre-routing normalization protocol only**.

---

## 4. ROLE RESPONSIBILITIES

### 4.1 SAPIANTA_CHAT

SAPIANTA_CHAT SHALL:
- accept raw human text
- normalize text into structured intent
- attach non-executive constraints
- forward intent to HOI

SAPIANTA_CHAT SHALL NOT:
- interpret intent semantics
- infer goals or strategies
- orchestrate
- call ModuleBuilder
- generate build plans
- trigger execution
- perform writes

---

### 4.2 HOI

HOI SHALL:
- receive structured intent
- determine routing eligibility
- enforce governance constraints

HOI SHALL NOT:
- treat structured intent as execution intent
- bypass Decision Preview or Human Decision Gates

---

## 5. CANONICAL STRUCTURED INTENT OBJECT


```json
{
  "chat_intent": {
    "intent_class": "inquiry | exploration | execution_request | unknown",
    "subject": "module_creation | inspection | decision_preview | other",
    "confidence": "explicit | implicit | unclear",
    "constraints": {
      "write_allowed": false,
      "execution_allowed": false
    }
  },
  "meta": {
    "source": "SAPIANTA_CHAT",
    "protocol": "CSIP",
    "version": "0.1",
    "trace_id": "<uuid>"
  }
}
```

This object is:
- descriptive only
- non-executable
- non-authoritative
- non-persistent

---

## 6. EXPLICIT PROHIBITIONS

CSIP MUST NOT:
- invoke ModuleBuilder
- create build artifacts
- export build plans
- modify system state
- introduce new intent
- escalate privileges

Any violation constitutes a **governance breach**.

---

## 7. RELATION TO OTHER CLOSURES

- Closure #2 (HALT): unaffected  
- Closure #3 (Mechanical Guard): unaffected  
- Closure #4 (One-time Self-Build Loop-Back): unaffected  
- Closure #5 (ModuleBuilder Activation): unaffected  

Closure #6a introduces **no new execution path**.

---

## 8. LOCK STATEMENT

With this document:
- conversational input normalization is governed
- chat-to-system routing is canonical
- ambiguity around intent handling is eliminated

Closure #6a is hereby **LOCKED**.

---

**End of Closure #6a**
