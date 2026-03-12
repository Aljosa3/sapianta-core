# SAPIANTA_KNOWLEDGE_ARTIFACT_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION
Layer: L3 Governance
Scope: Knowledge Engine / Research System
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the canonical schema for the Knowledge Artifact
within the SAPIANTA Autonomous Research System.

A Knowledge Artifact represents structured insight discovered
from one or more experiment artifacts.

The artifact captures patterns, relationships, and principles
identified during research analysis.

Knowledge artifacts enable:

• cross-experiment learning
• strategy improvement
• parameter sensitivity discovery
• regime pattern recognition
• cross-domain knowledge reuse


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

Knowledge artifacts are produced by the Knowledge Engine.

Research pipeline:

IDEA_ARTIFACT
↓
ASF IMPLEMENTATION
↓
EXPERIMENT
↓
EXPERIMENT_ARTIFACT
↓
KNOWLEDGE_ENGINE
↓
KNOWLEDGE_ARTIFACT
↓
STRATEGY_EVOLUTION
↓
STRATEGY_ARTIFACT


------------------------------------------------------------
3. KNOWLEDGE ARTIFACT STRUCTURE
------------------------------------------------------------

knowledge_artifact:

  metadata:

    knowledge_id: "uuid"

    knowledge_hash: "sha256"

    created_at: "ISO8601 timestamp"

    created_by: "knowledge_engine"

    artifact_type: "knowledge_artifact"

    artifact_schema_version: "1.0"

  source_experiments:

    experiment_ids:

      - "exp_uuid_1"
      - "exp_uuid_2"
      - "exp_uuid_3"

    experiment_hashes:

      - "sha256_exp1"
      - "sha256_exp2"

  knowledge_type:

    category: "pattern"

    subtype: "volatility_regime_effect"

  description:

    title: "Volatility regime strongly influences strategy profitability"

    summary: >
      Analysis of experiments shows that momentum strategies
      outperform mean reversion strategies during high volatility
      regimes.

  discovered_pattern:

    variables:

      - volatility
      - momentum_return

    relationship:

      volatility_high → momentum_outperforms

  statistical_evidence:

    confidence_score: 0.92

    sample_size: 3500

    validation_method: "cross_validation"

  applicability:

    domains:

      - trading
      - energy_optimization

  governance:

    deterministic_analysis: true

    reproducible: true

    experiment_traceable: true


------------------------------------------------------------
4. REQUIRED FIELDS
------------------------------------------------------------

The following fields are mandatory:

knowledge_id
knowledge_hash
source_experiments
knowledge_type
description
governance


------------------------------------------------------------
5. KNOWLEDGE TYPES
------------------------------------------------------------

Possible knowledge categories include:

pattern
parameter_sensitivity
strategy_dominance
regime_behavior
risk_pattern
cross_domain_pattern


------------------------------------------------------------
6. TRACEABILITY
------------------------------------------------------------

Every knowledge artifact must reference the experiments
from which the insight was derived.

This ensures that knowledge claims remain verifiable
and reproducible.


------------------------------------------------------------
7. DETERMINISTIC ANALYSIS
------------------------------------------------------------

Knowledge extraction must be deterministic.

The Knowledge Engine must produce identical
knowledge artifacts when executed on identical
experiment artifact sets.


------------------------------------------------------------
8. KNOWLEDGE REUSE
------------------------------------------------------------

Knowledge artifacts may influence:

• strategy generation
• strategy mutation
• parameter search space definition
• domain decision heuristics


------------------------------------------------------------
9. ARTIFACT LINEAGE
------------------------------------------------------------

Knowledge artifacts extend the artifact lineage:

IDEA_ARTIFACT
↓
EXPERIMENT_ARTIFACT
↓
KNOWLEDGE_ARTIFACT
↓
STRATEGY_ARTIFACT
↓
PROPOSAL_ARTIFACT
↓
DECISION_ENVELOPE
↓
LEDGER_ENTRY


------------------------------------------------------------
10. DESIGN PRINCIPLES
------------------------------------------------------------

Knowledge artifacts must guarantee:

• deterministic generation
• experiment traceability
• reproducibility
• governance compatibility
• cross-domain interpretability


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------