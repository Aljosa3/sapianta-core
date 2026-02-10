# DECISION — SELF-BUILD AUTHORITY LOCK

**ID:** DECISION_SELF_BUILD_LOCK_v0.XX  
**Status:** LOCKED  
**Phase:** DESIGN  
**Date:** YYYY-MM-DD  
**Scope:** SAPIANTA canonical self-build execution

---

## 1. Decision Statement

This document formally records the governance decision to **LOCK self-build execution** in the SAPIANTA system.

Although a **single canonical build CLI authority has been identified**, self-build execution is **NOT authorized** at this stage due to missing mandatory governance enforcement mechanisms.

This is a governance decision.  
No code changes are introduced by this document.

---

## 2. Canonical Build Authority (Identified)

The following CLI is the **sole canonical self-build authority** in the current codebase:

- **File:** `sapianta_chat/cli/main.py`
- **Invocation:**
  ```bash
  python3 -m sapianta_chat.cli.main build <plan.json> --workdir out/
```

## Build Path

The canonical build execution path is:

- `sapianta_chat/cli/main.py:main()`
- `sapianta_chat/cli/main.py:_handle_build()`
- `sapianta_chat/cli/build_flow.py:run_build_pipeline()`
- `runtime/raw_module_writer.py:RawModuleWriter.write_from_raw()`

This is the **only code path** that performs filesystem writes for module materialization.

---

## 3. Governance Enforcement Status (Verified)

Static analysis of the canonical build path establishes the following:

### 3.1 HASBT — Human-Authorized Self-Build Trigger

**Specification:**  
`governance/triggers/HUMAN_AUTHORIZED_SELF_BUILD_TRIGGER.md`

**Python implementation:**  
NONE FOUND

**Canonical path enforcement:**  
ABSENT

**Finding:**  
Self-build execution occurs without any HASBT authorization validation.

**Status:** ❌ NOT IMPLEMENTED / NOT ENFORCED

---

### 3.2 WRITE-GATE Enforcement

**Implementation exists:**  
`sapianta_chat/governance/write_gate.py:WriteGate.evaluate()`

**Call-sites found:**  
Test files only (`tests/governance/test_write_gate.py`)

**Canonical build path enforcement:**  
ABSENT

**Filesystem write occurs at:**  
`runtime/raw_module_writer.py:out_path.write_text()` (line ~70)

**Finding:**  
Filesystem writes occur without WRITE-GATE evaluation.

**Status:** ❌ IMPLEMENTED BUT BYPASSED

---

## 4. Governance Violation Declaration

Per HASBT specification:

- Self-build MUST NOT occur without explicit human authorization.
- HASBT MUST be evaluated before any artifact creation.
- WRITE-GATE MUST be enforced prior to filesystem writes.

**Current canonical build behavior violates these requirements.**

---

## 5. LOCK Declaration

Effective immediately:

- 🔒 Self-build execution is **LOCKED**
- 🔒 The canonical build CLI **MUST NOT** be used for active self-building
- 🔒 Any execution of:

```bash
python3 -m sapianta_chat.cli.main build <plan.json> --workdir out/
```
is considered **governance-noncompliant**.

---

## 6. Permitted Activities While LOCKED

The following activities remain allowed:

- DESIGN and architecture work
- Static analysis and audits
- Proposal generation via interactive CLI
- Build plan authoring and validation
- Simulation and dry-run reasoning (no writes)

---

## 7. Unlock Conditions (Non-Binding)

This LOCK may only be lifted when **all** of the following are true:

- HASBT is implemented in executable code
- HASBT is enforced on the canonical build path
- WRITE-GATE is enforced **before any filesystem write**
- Enforcement order is deterministic and auditable

Unlocking requires a **separate governance decision document**.

---

## 8. Final Note

This LOCK preserves the integrity, auditability, and industrial credibility of the SAPIANTA system.

Self-build capability exists —  
**authorization does not.**

---

**END OF DECISION**
