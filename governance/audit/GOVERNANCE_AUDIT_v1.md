# GOVERNANCE AUDIT v1
Version: v1.0
Status: draft
Lifecycle: active
Scope: Governance inventory, lifecycle coverage, lock/canonical hotspots, and deprecation candidates
Depends-On: governance/model/GOVERNANCE_MODEL_v2.md

---

## 0. Audit Intent

This audit prevents governance artifacts from becoming structural drag.

Rules:
- No deletions.
- No silent deprecation.
- No retroactive reinterpretation of canonical documents.
- Audit first, actions later.

---

## 1. Current Inventory Snapshot

- Total governance artifacts (md/yaml/yml): 324
- Snapshot file: /tmp/governance_files.txt

---

## 2. Observations (Hotspots)

### 2.1 LOCK / CANONICAL / IMMUTABLE signal density

A non-trivial portion of governance contains LOCK/CANONICAL/IMMUTABLE signals.
This increases the risk of:
- duplicated locks
- obsolete “locked” documents remaining in active paths
- governance becoming a development bottleneck

Initial sample (grep head) shows hotspots across:
- module builder specs (LOCK)
- vision lock documents
- audit lock documents
- execution gate / lifecycle locks
- canonical principles

---

### 2.2 Lifecycle coverage is effectively missing

Lifecycle keyword occurrences (all matches): 16
However, most matches are not lifecycle classification headers but “Guard Lifecycle” content.

Conclusion:
- Lifecycle classification is effectively absent across governance.
- Governance v2 requirement (“no document without lifecycle classification”) is not yet satisfied.
- Next step is incremental lifecycle rollout guided by the classification matrix.

---

## 3. Classification Matrix (Draft)

Columns:
- Path
- Type (canon/framework/protocol/spec/init/review/lock/checklist/diagram/other)
- Signals (LOCKED/CANONICAL/INIT/REVIEW/etc.)
- Proposed Lifecycle (draft/active/frozen/deprecated/archived)
- Action (keep/deprecate/archive/merge/rename/move)
- Risk (low/med/high)
- Notes

### 3.1 Seed rows (already lifecycle-activated)

| Path | Type | Signals | Proposed Lifecycle | Action | Risk | Notes |
|------|------|---------|-------------------|--------|------|-------|
| governance/IPV_CANON_v0.1_LOCK.md | canon | CANONICAL, LOCKED, immutable | frozen | keep | low | Lifecycle activated |
| governance/SAPIANTA_SYSTEM_FRAMEWORK.md | framework | LOCKED | frozen | keep | low | Lifecycle activated |
| governance/autonomy/AUTONOMY_INTENT_v1.0.md | intent | non-enforced | active | keep | low | Lifecycle activated |
| governance/phases/IPV-1.1_INIT.md | init | INIT | active | keep | low | Lifecycle activated |

### 3.2 High-signal candidates (first-pass)

| Path | Type | Signals | Proposed Lifecycle | Action | Risk | Notes |
|------|------|---------|-------------------|--------|------|-------|
| governance/vision/SAPIANTA_INDUSTRIAL_PLATFORM_VISION_LOCK.md | vision | LOCKED | frozen | keep | med | Core strategic lock; confirm canonical chain |
| governance/MODULE_BUILDER_SPEC_v1.0_LOCK.md | spec | LOCKED | frozen | keep | med | Likely core; check duplicates vs non-lock version |
| governance/MODULE_BUILDER_IMPLEMENTATION_SPEC_v1.0_LOCK.md | spec | LOCKED | frozen | keep | med | Check relation to implementation spec non-lock |
| governance/audit/AUDIT_HASBT_ENFORCEMENT_v0.1.md | audit | AUDITED/LOCKED | frozen | keep | low | Audit lock document |
| governance/audit/IPV-1_ALIGNMENT_AUDIT_LOCK.md | audit | LOCKED | frozen | keep | low | Audit lock document |
| governance/GUARD_LIFECYCLE_LOCK_v0.2.md | protocol | LOCKED | frozen | keep | med | Confirm if operative constraint |
| governance/EXECUTION_GATE_REVIEW.md | gate | LOCKED | frozen | keep | med | Confirm enforcement binding |

---

## 4. Immediate Audit Questions

1) Where is the authoritative “canonical chain” index that states which locks are operative?
2) Which pairs exist as (spec) + (spec_LOCK) and are both still necessary?
3) Which INIT/REVIEW/DEMO_FLOW documents should become deprecated → archived?
4) Which documents are pure references vs normative constraints?

---

## 5. Next Actions (Not executed in this commit)

Planned next steps:
- Create an automated candidate list for:
  - *_LOCK.md, *LOCK*.md (likely frozen)
  - *INIT*.md, *REVIEW*.md, *DEMO_FLOW*.md (likely deprecated candidates)
- Expand the matrix in controlled batches (no moves yet).
- Propose an archive strategy (governance/archive/...) and a sandbox namespace (governance/experimental/).

End of document.
