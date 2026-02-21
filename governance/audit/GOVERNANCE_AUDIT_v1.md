# GOVERNANCE AUDIT v1
Version: v1.0
Status: draft
Lifecycle: active
Scope: Governance inventory, lifecycle coverage, structural risk mapping
Depends-On: governance/model/GOVERNANCE_MODEL_v2.md

---

## 0. Audit Intent

This audit exists to ensure governance remains a structural enabler,
not a structural inhibitor.

This document performs:

- inventory mapping
- lifecycle coverage assessment
- lock/canonical density analysis
- first-pass structural risk triage

This document does NOT:

- modify canonical documents
- reinterpret existing locks
- deprecate artifacts
- archive artifacts

Audit precedes action.

---

## 1. Inventory Snapshot

- Total governance artifacts (md/yaml/yml): 324
- Snapshot source: `/tmp/governance_files.txt`
- Extraction method: filename-based listing (no semantic parsing)

Observation:

Governance volume has reached structural complexity.
Lifecycle coverage is currently near-zero.

---

## 2. Structural Observations

### 2.1 Lock / Canonical Density

High concentration of:

- *_LOCK.md artifacts
- LOCKED status markers
- CANONICAL designations
- Immutable declarations

Risk introduced:

- Duplicate locks
- Lock artifacts without authoritative chain index
- Frozen documents without lifecycle classification
- Potential architectural inertia

This does not imply invalidity.
It implies need for structural ordering.

---

### 2.2 Lifecycle Coverage Gap

Total Lifecycle matches in repository: 16  
Effective lifecycle header usage: ~4 documents

Conclusion:

Governance v2 requirement —
“No governance document without lifecycle classification”
is not yet satisfied.

Lifecycle rollout must be incremental and controlled.

---

## 3. Classification Matrix (Working Model)

Matrix columns:

- Path
- Type (canon/framework/protocol/spec/init/review/lock/checklist/diagram/reference/other)
- Signals (LOCK/INIT/REVIEW/DEMO/CANONICAL/etc.)
- Proposed Lifecycle (draft/active/frozen/deprecated/archived)
- Action (keep/review/deprecate/archive-candidate/merge)
- Risk (low/med/high)
- Notes

This matrix is descriptive — not prescriptive.

---

### 3.1 Seed Rows (Lifecycle Activated)

| Path | Type | Signals | Proposed Lifecycle | Action | Risk | Notes |
|------|------|---------|-------------------|--------|------|-------|
| governance/IPV_CANON_v0.1_LOCK.md | canon | CANONICAL, LOCKED | frozen | keep | low | Lifecycle activated |
| governance/SAPIANTA_SYSTEM_FRAMEWORK.md | framework | LOCKED | frozen | keep | low | Lifecycle activated |
| governance/autonomy/AUTONOMY_INTENT_v1.0.md | intent | INIT history | active | keep | low | Lifecycle activated |
| governance/phases/IPV-1.1_INIT.md | phase | INIT | active | keep | low | Lifecycle activated |

---

### 3.2 High-Signal Frozen Candidates

(First-pass identification via filename triage)

| Path | Type | Signals | Proposed Lifecycle | Action | Risk | Notes |
|------|------|---------|-------------------|--------|------|-------|
| governance/vision/SAPIANTA_INDUSTRIAL_PLATFORM_VISION_LOCK.md | vision | LOCKED | frozen | keep | med | Confirm canonical precedence |
| governance/MODULE_BUILDER_SPEC_v1.0_LOCK.md | spec | LOCKED | frozen | review | med | Check duplicate non-lock spec |
| governance/MODULE_BUILDER_IMPLEMENTATION_SPEC_v1.0_LOCK.md | spec | LOCKED | frozen | review | med | Verify authoritative version |
| governance/locks/HOI_KERNEL_v1_LOCK.md | kernel | LOCKED | frozen | keep | med | Core kernel lock |
| governance/locks/L1_EVENT_REGISTRY_v0.1_LOCK.md | layer1 | LOCKED | frozen | keep | low | Structural invariant |
| governance/locks/L1_EVENT_REFERENCE_v0.1_LOCK.md | layer1 | LOCKED | frozen | keep | low | Structural invariant |
| governance/contracts/LLM_ROLE_CONTRACT_v0.1_LOCK.md | contract | LOCKED | frozen | keep | med | Governance contract |
| governance/contracts/SELF_BUILD_PRECONDITIONS_v0.50_LOCK.md | contract | LOCKED | frozen | review | med | Confirm enforcement surface |
| governance/NORMATIVE_DECISION_EXPLANATION_LOCK.md | protocol | LOCKED | frozen | review | med | Normative enforcement |
| governance/GUARD_LIFECYCLE_LOCK_v0.2.md | protocol | LOCKED | frozen | review | med | Lifecycle constraint |

---

### 3.3 High-Signal Deprecation Candidates

(First-pass identification via INIT/REVIEW/DEMO/SNAPSHOT)

| Path | Type | Signals | Proposed Lifecycle | Action | Risk | Notes |
|------|------|---------|-------------------|--------|------|-------|
| governance/DEMO_FLOW_1.md | demo | DEMO_FLOW | deprecated-candidate | review | low | Historical |
| governance/DEMO_FLOW_2.md | demo | DEMO_FLOW | deprecated-candidate | review | low | Historical |
| governance/DEMO_FLOW_3.md | demo | DEMO_FLOW | deprecated-candidate | review | low | Historical |
| governance/GOVERNANCE_SNAPSHOT_v1.md | snapshot | SNAPSHOT | deprecated-candidate | review | low | Snapshot artifact |
| governance/kernel/KERNEL_PUBLIC_SURFACE_SNAPSHOT_v1.0.md | snapshot | SNAPSHOT | deprecated-candidate | review | low | Historical state |
| governance/DECISION_LAYER_REVIEW.md | review | REVIEW | deprecated-candidate | review | low | Superseded? |
| governance/MODULE_SKELETON_REVIEW.md | review | REVIEW | deprecated-candidate | review | low | Superseded? |
| governance/AUDIT_TRACE_DEMO_FLOW.md | demo | DEMO_FLOW | deprecated-candidate | review | low | Trace artifact |
| governance/AUDIT_TRACE_IMPLEMENTATION_INIT.md | init | INIT | deprecated-candidate | review | low | Initialization phase |
| governance/phases/v0.3A_AUDIT_SNAPSHOT_INIT.md | init | INIT | deprecated-candidate | review | low | Early phase artifact |

---

### 3.4 Reference / Non-Normative Candidates

| Path | Type | Signals | Proposed Lifecycle | Action | Risk | Notes |
|------|------|---------|-------------------|--------|------|-------|
| governance/IGL_INDEX.md | index | INDEX | active | keep | low | Navigational |
| governance/runtime/RUNTIME_ARCHITECTURE_OVERVIEW.md | overview | OVERVIEW | active | keep | low | Reference |
| governance/overview/SAPIANTA_SYSTEM_OVERVIEW_v0.42.md | overview | OVERVIEW | active | keep | low | High-level |
| governance/REFERENCE_MODULE_BUILDER_MANIFEST_v1.md | reference | REFERENCE | active | keep | low | Reference |
| governance/REFERENCE_MODULE_INTERACTION_ECHO_V1.md | reference | REFERENCE | active | keep | low | Reference |
| governance/diagrams/DIAGRAM_SELF_BUILD_ENFORCEMENT_ORDER_v0.1.md | diagram | DIAGRAM | active | keep | low | Informational |
| governance/checklists/CHECKLIST_SELF_BUILD_UNLOCK_EVIDENCE_v0.1.md | checklist | CHECKLIST | active | keep | low | Process aid |
| governance/vision/IPV-1_1_TRACEABILITY_ROADMAP.md | roadmap | ROADMAP | active | keep | low | Strategy |
| governance/phases/PHASE_v0.20_IMPLEMENTATION_CHECKLIST.md | checklist | CHECKLIST | active | keep | low | Implementation |
| governance/layer1/L1_EVENT_REFERENCE_ENFORCEMENT_BOUNDARY_v0.1.md | spec | REFERENCE | active | keep | low | Structural reference |

---

## 4. Immediate Structural Questions

1. Where is the authoritative canonical chain registry?
2. Which LOCK artifacts are historical vs operative?
3. Which INIT artifacts are superseded by LOCK versions?
4. Can legacy INIT/REVIEW artifacts move to governance/archive/ without loss?

---

## 5. LOCK Pair Detection (X.md + X_LOCK.md)

Method:
- Derived LOCK bases from `/tmp/governance_files.txt` using `_LOCK.md` suffix stripping.
- Derived MD bases from `/tmp/governance_files.txt` using `.md` suffix stripping.
- Computed intersection to identify pairs where both exist.

Artifacts:
- `/tmp/gov_lock_pairs.txt`
- `/tmp/gov_lock_pairs_report.txt`
- `/tmp/gov_lock_pairs_sizes.txt`

Result:
- Total lock pairs: 7

### 5.1 Pair List

| Base | Non-lock | Lock | Size(non) | Size(lock) | Triage | Notes |
|------|----------|------|-----------|------------|--------|-------|
| governance/vision/SAPIANTA_INDUSTRIAL_PLATFORM_VISION | governance/vision/SAPIANTA_INDUSTRIAL_PLATFORM_VISION.md | governance/vision/SAPIANTA_INDUSTRIAL_PLATFORM_VISION_LOCK.md | 264 | 3044 | lock-dominant | Likely: lock = frozen, non-lock = deprecated-candidate |
| governance/audit/IPV-1_ALIGNMENT_AUDIT | governance/audit/IPV-1_ALIGNMENT_AUDIT.md | governance/audit/IPV-1_ALIGNMENT_AUDIT_LOCK.md | 35741 | 1052 | report+attestation | Likely: report active, lock frozen |
| governance/contracts/LLM_ROLE_CONTRACT_v0.1 | governance/contracts/LLM_ROLE_CONTRACT_v0.1.md | governance/contracts/LLM_ROLE_CONTRACT_v0.1_LOCK.md | 3168 | 620 | lock-wrapper? | Determine which file is referenced as authoritative |
| governance/MODULE_BUILDER_SPEC_v1.0 | governance/MODULE_BUILDER_SPEC_v1.0.md | governance/MODULE_BUILDER_SPEC_v1.0_LOCK.md | 3797 | 2346 | ambiguous | High risk of editing the wrong one; needs authoritative chain rule |
| governance/MODULE_BUILDER_IMPLEMENTATION_SPEC_v1.0 | governance/MODULE_BUILDER_IMPLEMENTATION_SPEC_v1.0.md | governance/MODULE_BUILDER_IMPLEMENTATION_SPEC_v1.0_LOCK.md | 4058 | 2509 | ambiguous | Same as above |
| governance/specs/USER_MODULE_TEMPLATE_SPEC_v0.1 | governance/specs/USER_MODULE_TEMPLATE_SPEC_v0.1.md | governance/specs/USER_MODULE_TEMPLATE_SPEC_v0.1_LOCK.md | 4127 | 1722 | ambiguous | Template may still evolve; lock may be baseline |
| governance/artifacts/v0.7/runtime_wiring_manifest | governance/artifacts/v0.7/runtime_wiring_manifest.md | governance/artifacts/v0.7/runtime_wiring_manifest_LOCK.md | 2519 | 1886 | ambiguous | Determine whether this is historical snapshot or operative reference |

### 5.2 Required Resolution Rule

For each lock pair, governance must define:

- Which file is authoritative (operative)?
- What is the lifecycle of the non-authoritative counterpart?
- If both remain, their relationship must be explicitly documented (e.g., report + attestation model).

### 5.3 Authoritative Chain Resolution (Draft, Evidence-Based)

Evidence sources:
- `/tmp/gov_authoritative_counts.txt` (governance reference counts by filename)
- Header inspection of `_LOCK.md` documents (first ~60 lines)

Resolution rule (v1):
- If `_LOCK.md` explicitly states it applies to / locks / freezes a base document, treat as lock wrapper (attestation) unless it is the canonical lock record for a spec.
- If counts strongly prefer one artifact AND lock text declares the other as reference target, treat as report+attestation pair.
- If counts tie and structure is incomplete, mark as ambiguous (no lifecycle decision yet).

| Base | Authoritative | Evidence | Lifecycle(non) | Lifecycle(lock) | Action | Notes |
|------|---------------|----------|----------------|-----------------|--------|------|
| governance/vision/SAPIANTA_INDUSTRIAL_PLATFORM_VISION | LOCK + base vision (paired) | refs: 3 vs 5; lock “Applies to: SAPIANTA_INDUSTRIAL_PLATFORM_VISION.md” | active | frozen | keep both | Vision doc is content; lock doc freezes it |
| governance/audit/IPV-1_ALIGNMENT_AUDIT | non-lock report | refs: 5 vs 1; lock “Audit Reference: IPV-1_ALIGNMENT_AUDIT.md” and “LOCKS the results” | active | frozen | keep both | report + attestation model |
| governance/artifacts/v0.7/runtime_wiring_manifest | non-lock manifest | refs: 2 vs 1; lock “constraints … defined by: runtime_wiring_manifest.md” | active | frozen | keep both | artifact + lock wrapper |
| governance/contracts/LLM_ROLE_CONTRACT_v0.1 | non-lock contract (for now) | refs: 6 vs 2; lock freezes role scope but is shorter wrapper | active | frozen | keep both | later: consider norm to reference via lock path |
| governance/MODULE_BUILDER_SPEC_v1.0 | LOCK | refs: 1 vs 2; lock is canonical phase lock record (“final and irreversible”) | deprecated-candidate | frozen | review pair | non-lock likely pre-lock spec |
| governance/MODULE_BUILDER_IMPLEMENTATION_SPEC_v1.0 | LOCK | refs: 1 vs 2; lock is canonical phase lock record (“final and irreversible”) | deprecated-candidate | frozen | review pair | non-lock likely pre-lock spec |
| governance/specs/USER_MODULE_TEMPLATE_SPEC_v0.1 | ambiguous | refs tie: 1 vs 1; lock header appears structurally incomplete (missing title/status block) | (no change) | (no change) | hold | requires canonical chain reference or header repair |

---

## 6. Next Governance Steps (Planned)

1. Validate canonical chain integrity.
2. Resolve authoritative file for each lock pair.
3. Introduce lifecycle headers to authoritative artifacts.
4. Propose governance/archive/ structure for deprecated artifacts.
5. Begin controlled lifecycle rollout batch 2.

No changes executed in this audit phase.

---

End of document.
