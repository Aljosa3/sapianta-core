# PATH: sapianta_system/governance/contracts/SAPIANTA_AUTONOMOUS_TESTING_REQUIREMENT_v1.0.md

# SAPIANTA_AUTONOMOUS_TESTING_REQUIREMENT_v1.0

Status: GOVERNANCE CONTRACT
Scope: AI Software Factory (ASF)
Applies to: All autonomously generated or modified code in SAPIANTA

---

# 1. PURPOSE

This contract defines the mandatory testing requirements for any code that is autonomously generated or modified within the SAPIANTA system.

The purpose of this contract is to ensure that autonomous development remains:

- deterministic
- safe
- replay-verifiable
- regression-resistant

This contract is part of the **Governed Autonomous Development (GAD)** framework.

No autonomously generated code may enter the repository without satisfying the requirements defined in this document.

---

# 2. TESTING REQUIREMENT

Every autonomously generated module MUST include associated tests.

These tests must validate:

1. Functional correctness
2. Deterministic behavior
3. Failure handling

Autonomous code without tests MUST be rejected by the Promotion Gate.

---

# 3. REQUIRED TEST TYPES

For each generated module, the following test categories MUST exist.

## 3.1 Unit Tests

Each public function or class must be tested.

Example:

module: runtime/analytics/regime_detector.py
tests: tests/test_regime_detector.py

Unit tests must verify:

- expected outputs
- input handling
- edge cases

---

## 3.2 Determinism Tests

All modules must behave deterministically for identical inputs.

Required property:

f(input) == f(input)

Tests must confirm:

- no hidden randomness
- stable outputs
- reproducible execution

---

## 3.3 Negative Tests

Modules must be tested against invalid inputs.

Examples:

- malformed data
- missing parameters
- boundary conditions

Expected behavior:

- controlled failure
- explicit error handling
- no undefined states

---

# 4. AUTONOMOUS TEST GENERATION

If a module is generated autonomously, the system MUST also generate a corresponding test suite.

Required pipeline:

CodeGenerator
↓
TestGenerator
↓
ModuleTestRunner
↓
MutationValidator
↓
PromotionGate

Generated tests must pass before code can be promoted.

---

# 5. TEST EXECUTION REQUIREMENT

All tests must pass before code promotion.

Required validation steps:

1. Unit test execution
2. Determinism verification
3. Mutation validation

Failure at any stage MUST block promotion.

---

# 6. REGRESSION PROTECTION

Whenever existing code is modified:

- all existing tests must be executed
- mutation validation must run
- regression must be detected

If any previously passing test fails:

PROMOTION: REJECTED

---

# 7. PROMOTION GATE ENFORCEMENT

Promotion Gate must enforce the following rule:

AUTONOMOUS CODE WITHOUT TESTS → REJECT

This rule applies to all structural and parametric changes.

Cosmetic changes are exempt.

---

# 8. TEST COVERAGE TARGET

Autonomous modules should aim for:

minimum coverage target: 80%

Coverage below this threshold should trigger a warning.

Future versions of this contract may enforce stricter thresholds.

---

# 9. REPLAY VERIFICATION

Tests must support replay validation.

This ensures that a historical decision can be reproduced with identical results.

Replay determinism is required for:

- governance validation
- decision audit
- scientific reproducibility

---

# 10. GOVERNANCE CLASSIFICATION

Contract Type:

Governance Contract

Change classification:

STRUCTURAL

Changes to this contract require governance approval.

---

# 11. VERSION HISTORY

v1.0

Initial definition of autonomous testing requirements for the SAPIANTA AI Software Factory.