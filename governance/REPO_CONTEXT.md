# REPOSITORY CONTEXT — SAPIANTA

- Branch `main` is the ONLY normative and authoritative branch.
- `main` contains the locked SAPIANTA Canonical Framework (SCF).
- All SRS development MUST be based on `main`.

- Branches under `work/*` are experimental, aborted, or exploratory.
- `work/*` branches MUST NOT be used as architectural or implementation reference.

- SCF is LOCKED.
- Any implementation violating SCF is invalid.

This file is authoritative for repository interpretation.

---

## Governance Scope Clarification

Normative governance for the SAPIANTA system is defined exclusively in the `/governance` directory.

This includes, but is not limited to:
- CANON
- CORE_LAWS
- SAPIANTA Canonical Framework (SCF)
- IGL Guardrails (IGL-GR-001 … IGL-GR-009)

Documents located in `/governance` represent the authoritative and binding rules of the system.

They MUST NOT be redefined, duplicated, overridden, or reinterpreted elsewhere in the repository.

---

## Runtime Governance Disclaimer

The directory `/sapianta/governance` contains runtime-level adapters, interfaces, and technical helpers only.

It has NO normative authority.

No document, code, or configuration located under `/sapianta/` may define, modify, reinterpret, or supersede any rule defined under `/governance`.

---

## Implementation Constraint

All code generated for this repository, whether by humans or automated systems (including AI-assisted tools), MUST comply with the rules defined in `/governance`.

Code that fails IGL-INIT is invalid by definition and MUST NOT be committed.
