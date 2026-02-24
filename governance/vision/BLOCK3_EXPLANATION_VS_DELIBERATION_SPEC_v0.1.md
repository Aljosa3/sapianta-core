# /home/pisarna/sapianta_system/governance/vision/BLOCK3_EXPLANATION_VS_DELIBERATION_SPEC_v0.1.md

# SAPIANTA · BLOCK 3
## Explanation vs Deliberation · Boundary Specification v0.1

Status: DRAFT (intended for governance integration)  
Scope: Defines hard boundary between deterministic Explanation (constitutional/audit) and cognitive Deliberation (optional extension).

---

## 0. Definitions

### 0.1 Explanation
**Explanation** is a deterministic, reproducible account of *why* a given Decision outcome was produced by the Engine under a specific Policy, using the Proposal inputs.

Explanation is **proof-oriented**:
- derived from deterministic trace / rule evaluation
- reproducible under replay
- consistent with canonical hashing discipline

Explanation MUST NOT contain normative judgment, recommendations, or context speculation.

### 0.2 Deliberation
**Deliberation** is a non-constitutional, optional cognitive analysis that may:
- discuss context
- explore scenarios
- provide recommendations
- state assumptions and uncertainties

Deliberation is **judgment-oriented**:
- not required to be reproducible
- not used in deterministic replay validation
- MUST NOT influence canonical decision outcome or hashing

---

## 1. Constitutional Boundary

### 1.1 Layer allocation
- Explanation belongs to **Block 1/2** (Deterministic Constitutional Spine + Authority Enforcement) as an audit-grade artifact derived from deterministic execution.
- Deliberation belongs to **Block 3** (Deliberation Layer) as an optional cognitive artifact.

### 1.2 Determinism isolation
- Explanation MUST be reproducible under replay.
- Deliberation MAY be non-reproducible and MUST remain isolated from replay outcome.

---

## 2. Rules

### 2.1 Explanation rules (EXPL_*)

**EXPL_RULE_01 — Trace-derivable**
Explanation MUST be derivable from deterministic evaluation trace (rule hits, comparisons, thresholds, explicit computations allowed by the deterministic engine).

**EXPL_RULE_02 — No normative content**
Explanation MUST NOT contain recommendations, advice, or normative language (e.g., “I recommend”, “it would be better”, “should”, “probably”).

**EXPL_RULE_03 — No external context**
Explanation MUST NOT depend on external knowledge sources, market narratives, macro context, or speculation. It is strictly bound to Proposal + Policy + Engine evaluation.

**EXPL_RULE_04 — Audit alignment**
Explanation MUST reference the exact identifiers enabling audit and reproduction:
- proposal_hash
- policy_hash
- engine_version
- decision_result (APPROVED/REJECTED/…)
- triggered_rules / trace summary (minimum)

### 2.2 Deliberation rules (DL_*)

**DL_RULE_04 — May recommend**
Deliberation MAY contain recommendations, scenario analysis, and contextual reasoning.

**DL_RULE_05 — No deterministic causality claims**
Deliberation MUST NOT claim deterministic causality in a way that impersonates proof.
Forbidden patterns:
- “Rule R-07 triggered therefore X” (unless explicitly and verifiably quoting a deterministic trace reference)
- “Engine decided because…” (without linking to Explanation / trace)

Allowed patterns:
- “Given the outcome and available context, consider…”
- “Assumption: …”
- “Scenario: …”

**DL_RULE_06 — Must not affect replay**
Deliberation MUST NOT be included in canonical decision hash and MUST NOT influence replay determinism outcome.

**DL_RULE_07 — Optional integration only**
Any linkage from Decision to Deliberation MUST be optional and governance-configurable, and MUST be implemented via a non-canonical extension field (see §4).

---

## 3. Minimal Content Requirements

### 3.1 Minimal Explanation payload (audit-grade)
Explanation MUST minimally include:
- decision_result
- triggered_rules (identifiers)
- key comparisons / thresholds used (e.g., DTI=0.51 > 0.45)
- references: proposal_hash, policy_hash, engine_version

### 3.2 Minimal Deliberation payload (cognitive)
Deliberation SHOULD minimally include:
- recommendation (APPROVED/REJECTED/NEUTRAL/REQUEST_MORE_INFO)
- reasoning_text
- assumptions (explicitly marked)
- scenarios (optional)
- integrity_hash for tamper-evidence (non-constitutional)

---

## 4. Optional Decision Extension for Deliberation Acknowledgement

### 4.1 Non-canonical extension field
If an institution requires acknowledgement, Decision MAY contain:

- extensions.deliberation_reviewed: true/false

Constraints:
- extensions MUST NOT be part of canonical decision hash.
- replay MUST ignore extensions.

This preserves:
- determinism
- replay stability
- constitutional purity

---

## 5. Examples (normative)

### 5.1 Explanation (valid)
Result: REJECTED  
Triggered rules: R-07, R-12  
Inputs: DTI=0.51 (>0.45), CreditScore=590 (<600)  
Refs: proposal_hash=…, policy_hash=…, engine_version=…

### 5.2 Deliberation (valid)
Recommendation: REQUEST_MORE_INFO  
Assumptions: sector volatility elevated; revenue concentration risk unknown  
Scenario notes: request updated contracts / pipeline before final approval

### 5.3 Invalid cross-contamination examples

Invalid Explanation:
- “I recommend rejection due to macro uncertainty.”  (normative + external context)

Invalid Deliberation:
- “Rule R-07 proves the applicant is risky.” (claims proof / deterministic causality without trace linkage)

---

## 6. Non-goals (v0.1)

- No multi-agent debate protocol
- No policy auto-modification from deliberation
- No decision auto-trigger from deliberation
- No inclusion of deliberation hashes into canonical decision hashing

---

## 7. Acceptance Criteria (v0.1)

- A reviewer can unambiguously classify any text artifact as Explanation or Deliberation by applying the rules above.
- Replay determinism is unaffected by presence/absence of deliberation artifacts.
- Explanation remains fully reproducible from deterministic trace.

---