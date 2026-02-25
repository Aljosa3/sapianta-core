# PROMOTION_GATE_v0.2_SPEC
Status: DRAFT  
Layer: Governance Enforcement Layer  
Supersedes: Promotion Gate v0.1.x  
Principle: Stability Over Flexibility  

---

# 1. PURPOSE

Promotion Gate v0.2 introduces a deterministic, rule-based Change Classification Engine.

The engine SHALL:

1. Automatically classify a change into:
   - COSMETIC
   - PARAMETRIC
   - STRUCTURAL

2. Ignore any user-provided change_type argument.

3. Require explicit approval artifact ONLY IF classification = STRUCTURAL.

4. Always execute:
   - Determinism enforcement
   - Freeze enforcement

---

# 2. DESIGN PRINCIPLES

## 2.1 Stability First

If uncertainty exists, the system SHALL escalate severity.

Severity ordering (strict):

STRUCTURAL > PARAMETRIC > COSMETIC

Final classification SHALL be the maximum detected severity.

---

## 2.2 Determinism

Classification MUST be:

- Fully reproducible
- Based solely on Git diff
- Independent of runtime state
- Independent of heuristics or AI inference

---

## 2.3 Fail-Closed

If diff parsing fails:

→ classification SHALL default to STRUCTURAL.

---

# 3. INPUT DEFINITION

The engine SHALL evaluate:

## 3.1 Changed File Set

git diff --name-only <range>

## 3.2 Unified Diff (Zero Context)

git diff --unified=0 <range>

No contextual lines SHALL be used.

---

# 4. RULE SYSTEM

Rules SHALL be evaluated in the following order:

1. STRUCTURAL rules
2. PARAMETRIC rules
3. COSMETIC rules

All matched rules SHALL be recorded as evidence.

Final classification SHALL be the maximum severity detected.

---

# 5. STRUCTURAL RULES

## 5.1 S1 – Core Tripwire Rule

If any changed file path matches:

sapianta_core/**
runtime/layers/**
runtime/validation/**
governance/constitution/**
governance/phases/**
scripts/check_layer_freeze.py

→ classification SHALL include STRUCTURAL

Reason format:

Detected structural change: core/lifecycle surface modified (<path>)

---

## 5.2 S2 – Public API Signature Rule

If unified diff contains modifications to lines starting with:

def 
class 

AND file is within:

sapianta_core/**

→ classification SHALL include STRUCTURAL

Reason:

Detected structural change: public API modified (<file>)

---

## 5.3 S3 – Export Surface Rule

If unified diff modifies:

__all__ =
__init__.py (any change inside sapianta_core)

→ classification SHALL include STRUCTURAL

Reason:

Detected structural change: export surface modified

---

# 6. PARAMETRIC RULES

Evaluated ONLY if no STRUCTURAL rule triggered.

## 6.1 P1 – Configuration Value Change

File extensions:

.yml
.yaml
.json
.toml

If value changed but key unchanged:

- max_dti: 0.35
+ max_dti: 0.40

→ classification SHALL include PARAMETRIC

Reason:

Detected parametric change: configuration value modified (<file>)

---

## 6.2 P2 – Numeric Literal Change (Non-Core Code)

If:

- Numeric literal replaced
- No def/class/import/from modified
- File NOT under STRUCTURAL tripwire

→ classification SHALL include PARAMETRIC

Reason:

Detected parametric change: numeric literal modified (<file>)

---

# 7. COSMETIC RULES

Applies ONLY IF no STRUCTURAL and no PARAMETRIC rules triggered.

## 7.1 C1 – Documentation Only

If all changed files match:

*.md
docs/**
*.rst

→ classification SHALL be COSMETIC

Reason:

Detected cosmetic change: documentation only

---

## 7.2 C2 – Comment / Whitespace Only

If unified diff contains only:

- Lines starting with #
- Blank lines
- Whitespace changes

→ classification SHALL be COSMETIC

Reason:

Detected cosmetic change: comment/whitespace only

---

# 8. EVIDENCE MODEL

Engine SHALL collect:

[
  { rule_id: "S1", file: "...", severity: STRUCTURAL },
  { rule_id: "P1", file: "...", severity: PARAMETRIC }
]

Final classification:

max(severity(evidence))

Severity mapping:

COSMETIC = 1
PARAMETRIC = 2
STRUCTURAL = 3

---

# 9. APPROVAL ENFORCEMENT

If classification = STRUCTURAL:

- Approval artifact MUST exist
- --approve-structural flag MUST be present

If classification != STRUCTURAL:

- Approval artifact NOT required

---

# 10. OUTPUT FORMAT

Promotion Gate v0.2
Change Classification: STRUCTURAL

Evidence:
 - S2: public API modified (sapianta_core/validator.py)
 - S3: export surface modified

Approval Required: YES

Output SHALL be deterministic in ordering.

---

# 11. CONSTITUTIONAL GUARANTEE

Promotion Gate v0.2 SHALL ensure:

1. No structural change may pass without explicit approval.
2. No parametric change may be misclassified as cosmetic.
3. Any ambiguity SHALL escalate severity.
4. Classification SHALL be explainable.

---

# 12. NON-GOALS (v0.2)

Out of scope:

- AST parsing
- AI semantic reasoning
- Behavioral impact analysis
- Cross-file semantic coupling detection

---

# 13. VERSIONING

Promotion Gate v0.2:

- Replaces manual change_type argument
- Maintains determinism + freeze enforcement
- Preserves v0.1.x structural approval semantics