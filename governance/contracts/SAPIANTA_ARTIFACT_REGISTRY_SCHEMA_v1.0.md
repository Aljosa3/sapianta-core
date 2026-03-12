# SAPIANTA_ARTIFACT_REGISTRY_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION
Layer: L3 Governance
Scope: Global Artifact Registry
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the canonical schema for the Artifact Registry
used within the SAPIANTA system.

The Artifact Registry is the canonical index of all artifacts produced
by the SAPIANTA ecosystem.

It enables:

• artifact traceability
• artifact lineage tracking
• cross-domain knowledge reuse
• governance verification
• promotion control
• deterministic artifact verification

The registry ensures that all artifacts in the system are:

• uniquely identifiable
• immutable
• verifiable
• traceable across the full decision lifecycle.


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The Artifact Registry connects the research system with the
operational decision system.

Architecture flow:

IDEA_ARTIFACT
↓
EXPERIMENT_ARTIFACT
↓
STRATEGY_ARTIFACT
↓
PROPOSAL_ARTIFACT
↓
DECISION_ENVELOPE
↓
LEDGER_ENTRY

Each artifact generated in this chain must be registered in the
Artifact Registry.

The registry therefore represents the canonical map of
artifact lineage across the entire SAPIANTA system.


------------------------------------------------------------
3. ARTIFACT REGISTRY STRUCTURE
------------------------------------------------------------

Example entry:

artifact_registry_entry:

  artifact_id: "uuid"

  artifact_type: "EXPERIMENT_ARTIFACT"

  artifact_hash: "sha256_hash"

  artifact_schema:

    schema_name: "SAPIANTA_EXPERIMENT_ARTIFACT_SCHEMA"
    schema_version: "1.0"

  parent_artifact:

    artifact_id: "uuid"

    relation: "derived_from"

  domain:

    primary_domain: "trading"

  creation_timestamp: "ISO-8601"

  origin:

    system_component: "ASF"
    execution_node: "research_node_01"

  artifact_location:

    storage_system: "artifact_store"
    storage_path: "/artifacts/experiments/exp_001.json"

  dataset_reference:

    dataset_hash: "sha256"

  governance:

    immutable: true
    verified: true
    deterministic_serialization: true

  lifecycle:

    status: "ACTIVE"

    promotion_stage: "RESEARCH"

    eligible_for_promotion: true


------------------------------------------------------------
4. REQUIRED FIELDS
------------------------------------------------------------

The following fields are mandatory:

artifact_id
artifact_type
artifact_hash
artifact_schema
creation_timestamp
origin
governance

These fields ensure artifact traceability and integrity.


------------------------------------------------------------
5. ARTIFACT TYPES
------------------------------------------------------------

Supported artifact types include:

IDEA_ARTIFACT
EXPERIMENT_ARTIFACT
KNOWLEDGE_ARTIFACT
STRATEGY_ARTIFACT
PROMOTION_ARTIFACT
PROPOSAL_ARTIFACT
DECISION_ENVELOPE
LEDGER_ENTRY


------------------------------------------------------------
6. ARTIFACT LINEAGE
------------------------------------------------------------

Artifacts form a lineage graph.

Example lineage chain:

IDEA_ARTIFACT
↓
EXPERIMENT_ARTIFACT
↓
STRATEGY_ARTIFACT
↓
PROPOSAL_ARTIFACT
↓
DECISION_ENVELOPE
↓
LEDGER_ENTRY

The registry stores parent-child relationships between artifacts.

This lineage graph enables:

• strategy evolution tracking
• research reproducibility
• artifact provenance analysis
• governance audits


------------------------------------------------------------
7. IMMUTABILITY REQUIREMENT
------------------------------------------------------------

Artifacts must be immutable once registered.

Modifications require creation of a new artifact entry
with a new artifact_id and artifact_hash.

The original artifact remains preserved.


------------------------------------------------------------
8. ARTIFACT INTEGRITY
------------------------------------------------------------

Each artifact must include a SHA256 hash.

The hash ensures:

• artifact integrity
• tamper detection
• deterministic verification

Artifact hashes must be generated from
deterministically serialized artifacts.


------------------------------------------------------------
9. PROMOTION TRACKING
------------------------------------------------------------

Artifacts progress through lifecycle stages:

RESEARCH
↓
CANDIDATE
↓
VALIDATED
↓
DEPLOYED

The Artifact Registry tracks promotion eligibility and state.


------------------------------------------------------------
10. GOVERNANCE INTEGRATION
------------------------------------------------------------

The Artifact Registry supports governance validation.

Governance checks include:

• artifact immutability
• artifact lineage verification
• artifact hash validation
• promotion eligibility verification
• schema compatibility verification


------------------------------------------------------------
11. SYSTEM ROLE
------------------------------------------------------------

The Artifact Registry acts as the canonical index of
all knowledge and decision artifacts produced by SAPIANTA.

It provides the foundation for:

• knowledge engines
• research reproducibility
• cross-domain learning
• artifact promotion systems
• deterministic experiment verification
• full decision traceability.


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------