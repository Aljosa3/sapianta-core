# DECISION — HASBT INSERTION POINT

**ID:** DECISION_HASBT_INSERTION_POINT_v0.1  
**Status:** DESIGN  
**Phase:** IMPLEMENTATION  
**Date:** YYYY-MM-DD  
**Scope:** Canonical HASBT enforcement insertion point

---

## 1. Purpose

This document defines the **single authoritative insertion point**
for HASBT (Human-Authorized Self-Build Trigger) enforcement.

The goal is to ensure that HASBT is evaluated:
- exactly once,
- deterministically,
- before any build execution or filesystem write.

This document introduces **no implementation**.

---

## 2. Canonical Build Path (Authoritative)

The canonical build execution path is:

1. `sapianta_chat/cli/main.py:main()`
2. `sapianta_chat/cli/main.py:_handle_build()`
3. `sapianta_chat/cli/build_flow.py:run_build_pipeline()`
4. `runtime/raw_module_writer.py:RawModuleWriter.write_from_raw()`

No other path performs self-build execution or filesystem writes.

---

## 3. HASBT Enforcement Boundary (Decision)

### 3.1 Insertion Location (Exact)

HASBT MUST be evaluated **inside**:
```
sapianta_chat/cli/build_flow.py
```


**Function:**
```
run_build_pipeline(...)
```


**Position:**
- AFTER: SPEC completeness validation
- BEFORE: any build execution (ClaudeExecutor)
- BEFORE: any filesystem write
- BEFORE: WRITE-GATE evaluation

This is the **only permitted location** for HASBT enforcement.

---

## 4. Enforcement Semantics (Hard)

At the HASBT insertion point:

- HASBT validation MUST execute exactly once
- HASBT DENY MUST:
  - immediately halt execution
  - prevent any further processing
  - prevent any filesystem write
- HASBT PASS allows execution to proceed
- HASBT MUST NOT:
  - perform writes
  - invoke WRITE-GATE
  - alter build artifacts

HASBT is a **gate**, not a processor.

---

## 5. Prohibited Insertion Points

HASBT MUST NOT be implemented in:

- `sapianta_chat/interface/cli.py` (interactive layer)
- `sapianta_chat/cli/main.py` (argument parsing layer)
- `runtime/claude_executor.py` (execution backend)
- `runtime/raw_module_writer.py` (write layer)
- any HOI or HDS component

Multiple HASBT checks are forbidden.

---

## 6. Relation to Governance Artifacts

This decision is binding with:

- `PHASE_SELF_BUILD_IMPLEMENTATION_INIT_v0.1`
- `DIAGRAM_SELF_BUILD_ENFORCEMENT_ORDER_v0.1`
- `HASBT_AUTHORIZATION_PAYLOAD_v0.1`
- `CHECKLIST_SELF_BUILD_UNLOCK_EVIDENCE_v0.1`

In case of conflict, governance decisions prevail.

---

## 7. Final Statement

HASBT exists to stop execution — not to decorate it.

There is exactly one place where authorization becomes executable.

That place is now defined.

---

**END OF DECISION**

