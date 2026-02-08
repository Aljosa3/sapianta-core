# LOCK — CLOSURE #7
## Read-Only Build Preparation (ROBP)

**Status:** LOCKED  
**Applies from:** SAPIANTA v0.42+  
**Type:** Governance / Execution Boundary  
**Execution:** NONE  
**Write:** NONE  

---

## 1. PURPOSE

Closure #7 defines a **strictly read-only execution boundary**
that permits the system to **prepare a build plan** using the existing
ModuleBuilder **without producing artifacts, files, or commits**.

This closure enables:

> Structured build preparation  
> without any form of execution or write side effects.

---

## 2. SCOPE

**Permitted:**
- Invocation of `ModuleBuilder.prepare(...)`
- Generation of in-memory build plans
- Deterministic validation of module structure
- Preview of files, dependencies, and steps

**Explicitly prohibited:**
- File creation
- File modification
- Repository writes
- Commits
- Execution of build steps
- Side effects of any kind

---

## 3. GOVERNANCE POSITION

ROBP is positioned **after**:
- CSIP (Closure #6a)
- HOI routing decision

and **before**:
- Any execution authorization
- Any write gate
- Any artifact binding
- Any commit or persistence step

ROBP is a **non-executive preparatory boundary only**.

---

## 4. ROLE RESPONSIBILITIES

### 4.1 SAPIANTA_CHAT

SAPIANTA_CHAT SHALL:
- forward structured intent (CSIP output)
- display build preparation preview

SAPIANTA_CHAT SHALL NOT:
- call ModuleBuilder directly
- modify build plans
- perform approvals
- perform writes or execution

---

### 4.2 HOI

HOI SHALL:
- determine eligibility for read-only build preparation
- invoke ModuleBuilder in read-only mode
- enforce non-execution constraints

HOI SHALL NOT:
- escalate ROBP output to execution intent
- bypass human approval gates

---

### 4.3 ModuleBuilder

ModuleBuilder SHALL:
- support deterministic `prepare(...)` invocation
- produce a **pure, in-memory build plan**
- expose structure, steps, and dependencies

ModuleBuilder SHALL NOT:
- write files
- modify repository state
- assume execution authorization

---

## 5. CANONICAL READ-ONLY BUILD PLAN OBJECT

The output of ROBP SHALL be a **non-persistent build plan**, for example:

```json
{
  "build_plan": {
    "module_name": "example_module",
    "files": [
      "example_module/__init__.py",
      "example_module/core.py",
      "example_module/README.md"
    ],
    "dependencies": [
      "pydantic",
      "numpy"
    ],
    "steps": [
      "create module skeleton",
      "define core interfaces",
      "attach documentation"
    ]
  },
  "governance": {
    "write_allowed": false,
    "execution_allowed": false,
    "approval_required": true
  },
  "meta": {
    "mode": "READ_ONLY_BUILD_PREPARATION",
    "source": "MODULE_BUILDER",
    "trace_id": "<uuid>"
  }
}
```

---
## 6. EXPLICIT PROHIBITIONS

ROBP MUST NOT:
- create or touch files
- export build plans to disk
- trigger commits
- trigger execution
- mutate ModuleBuilder internal state
- introduce retry or looping behavior

Any violation constitutes a critical governance breach.

## 7. RELATION TO OTHER CLOSURES

- Closure #2 (HALT): unaffected
- Closure #3 (Mechanical Guard): enforced
- Closure #4 (One-time Self-Build Loop-Back): unaffected
- Closure #5 (ModuleBuilder Activation): used in read-only mode
- Closure #6a (CSIP): prerequisite
Closure #7 introduces no write capability.

## 8. LOCK STATEMENT

With this document:

- ModuleBuilder may be invoked in preparation mode
- Build plans may be generated for inspection
- No execution or write path is opened
Closure #7 is hereby LOCKED.
---

End of Closure #7