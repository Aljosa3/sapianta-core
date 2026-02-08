# MODULE PROMOTION RULES — v1.0 (LOCK)

## Status
LOCKED — normative, canonical, non-negotiable

## Scope
These rules govern the promotion of a generated module
from the staging domain (`out/`) into the canonical repository domain.

They apply to:
- all SAPIANTA-generated modules
- all human-assisted module builds
- all future automated promotion pipelines

---

## 1. Promotion Domains

### 1.1 Staging Domain
- Path: `out/modules/<module_name>`
- Purpose: materialization, inspection, validation
- Status: non-canonical, mutable, disposable

### 1.2 Canonical Domain
- Path: `modules/<module_name>`
- Purpose: stable, auditable, reusable modules
- Status: canonical, versioned, protected

---

## 2. Mandatory Preconditions for Promotion

A module MAY be promoted only if:

1. The module exists fully under:
   `out/modules/<module_name>/`

2. The module has passed:
   - `ValidatorPipelineV020`
   - with ZERO warnings
   - with ZERO auto-fixes
   - with ZERO runtime interpretation

3. The validator output is considered the sole authority.
   Human judgement MAY NOT override validator failure.

---

## 3. Promotion Mechanics

Promotion is defined as:

- a byte-for-byte copy
- preserving internal structure
- without transformation
- without reformatting
- without content mutation

Allowed operation:
- `cp -r out/modules/<module_name> modules/<module_name>`

Any other operation constitutes a violation.

---

## 4. Forbidden Artifacts in Canonical Modules

The following MUST NOT exist in `modules/<module_name>`:

- `__pycache__/`
- `*.pyc`
- runtime-generated files
- execution logs
- temporary or sandbox artefacts
- implicit or accidental entrypoints (e.g. `main.py` unless explicitly specified)

Canonical modules MUST be source-only.

---

## 5. Structural Integrity

- All internal imports MUST be intra-module
- Cross-module imports are forbidden unless explicitly governed
- Circular imports are forbidden
- The module MUST be internally coherent as a closed unit

---

## 6. Promotion Authority

- Promotion is a governance action, not a runtime action
- Promotion MAY be manual or automated
- Automation MUST strictly replicate the rules defined here
- Any deviation requires a new LOCK document

---

## 7. Auditability

Each promotion MUST be traceable via:
- a dedicated git commit
- a clear commit message indicating promotion
- a clean diff limited to the promoted module

---

## 8. Irreversibility Principle

Once promoted:
- the module becomes part of the canonical system
- it MUST NOT be mutated without versioned change
- rollback requires explicit governance action

---

## 9. Enforcement

Violation of these rules constitutes:
- a governance breach
- a canonical integrity failure
- an invalid build state

No silent recovery is permitted.

---

## END OF DOCUMENT
