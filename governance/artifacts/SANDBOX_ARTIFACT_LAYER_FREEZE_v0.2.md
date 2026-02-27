# SANDBOX_ARTIFACT_LAYER_FREEZE_v0.2

STATUS: FROZEN  
LAYER: LEVEL_3  
TYPE: ARTIFACT_BINDING_SPEC  
DATE: 2026-02-27  

---

## 1. PURPOSE

This document formally freezes the deterministic artifact binding layer
used in SAPIANTA Level 3 Sandbox Phase A.

The artifact layer is now considered constitutionally stable.

---

## 2. DETERMINISTIC REQUIREMENTS

The artifact layer SHALL:

1. Use canonical JSON serialization:
   - sort_keys=True
   - separators=(",", ":")
   - ensure_ascii=False
   - UTF-8 encoding explicitly defined

2. Contain no:
   - UUID generation
   - time-based values in binding fields
   - random numbers
   - non-deterministic ordering

3. Derive artifact_id deterministically from binding payload.

4. Derive artifact_hash deterministically from REQUIRED_FIELDS only.

---

## 3. REQUIRED_FIELDS (FROZEN)

The following fields define the binding surface:

- artifact_id
- parent_commit_hash
- prompt_hash
- response_hash
- diff_hash
- validation_report_hash
- sandbox_iteration_count
- declared_scope

No additional fields may enter binding without STRUCTURAL approval.

---

## 4. REPLAY GUARANTEE

Given identical:

- parent_commit_hash
- prompt_text
- response_text
- diff_text
- declared_scope
- iteration

The produced artifact MUST be bit-identical.

---

## 5. GOVERNANCE RULE

Any change to:

- REQUIRED_FIELDS
- canonical serialization rules
- artifact_id derivation logic
- artifact_hash binding logic

is classified as STRUCTURAL.

Promotion Gate approval required.

---

FREEZE CONFIRMED.