# BUILD ARTIFACT POLICY v0.1

## Status
LOCKED

## Purpose
Define which build artifacts produced by SAPIANTA Chat are:
- canonical (version-controlled),
- ephemeral (runtime-only),
- audit-only,
- forbidden.

This policy prevents repository contamination and enforces deterministic builds.

---

## Artifact Classification

### 1. Canonical Artifacts (MUST be committed)
These artifacts define intent and governance.

- `build_plan.json`
- Governance documents under `governance/**`
- Source modules under `modules/**`
- Runtime wiring code under `runtime/**`
- CLI and validation logic under `sapianta_chat/**`

---

### 2. Ephemeral Artifacts (MUST NOT be committed)
Generated during execution and discarded after use.

- `generated_output/**`
- `claude_raw_output.json`
- `__pycache__/`
- `.pytest_cache/`
- `.coverage`, `htmlcov/`
- Temporary logs and test outputs

These artifacts are excluded via `.gitignore`.

---

### 3. Audit Artifacts (OPTIONAL, external storage)
Artifacts useful for debugging or traceability but not part of source truth.

- Raw LLM outputs
- Execution traces
- Validation reports

If stored, they MUST reside outside the canonical repository
or under explicitly excluded directories.

---

### 4. Forbidden Artifacts (HARD-GATED)
Artifacts that MUST NEVER be produced by a build.

- Markdown files (`*.md`) in generated modules
- Runtime imports (`openai`, `requests`, `subprocess`, etc.)
- Execution logic inside generated modules
- Governance file mutations

Violations trigger HARD-GATE failure.

---

## Enforcement
This policy is enforced by:
- `.gitignore`
- `ModuleWriter`
- `BuildValidator`
- Post-Claude HARD-GATE

No artifact classification may be changed without policy revision.

---
