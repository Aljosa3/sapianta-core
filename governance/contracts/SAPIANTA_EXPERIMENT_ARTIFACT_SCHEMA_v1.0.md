# SAPIANTA_EXPERIMENT_ARTIFACT_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION
Layer: L3 Governance
Scope: Research System
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the canonical schema for the Experiment Artifact
used within the SAPIANTA Autonomous Research System.

The Experiment Artifact represents the structured output of an
experimental evaluation performed by the AI Software Factory (ASF).

The artifact ensures that experiments are:

• reproducible
• traceable
• comparable
• governance-compliant


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The Experiment Artifact exists within the research pipeline
between hypothesis implementation and knowledge extraction.

Architecture flow:

idea artifact
↓
ASF hypothesis generation
↓
experiment execution
↓
experiment artifact
↓
knowledge extraction
↓
promotion evaluation


------------------------------------------------------------
3. EXPERIMENT ARTIFACT STRUCTURE
------------------------------------------------------------

Example:

experiment_artifact:

  experiment_id: "uuid"

  source_idea:
    idea_id: "uuid"

  timestamp: "ISO-8601"

  domain:

    primary_domain: "trading"

  experiment_configuration:

    strategy_id: "exp-001"

    parameters:

      lookback_window: 20
      volatility_threshold: 0.03

    dataset:

      dataset_id: "market_dataset_001"
      timeframe: "1h"

  evaluation_metrics:

    profit: float
    sharpe_ratio: float
    drawdown: float
    volatility: float
    win_rate: float

  evaluation_summary:

    fitness_score: float
    ranking_position: int

  governance:

    deterministic: true
    reproducible: true

  metadata:

    execution_environment: "ASF"
    evaluation_engine: "regime_strategy_evaluator"


------------------------------------------------------------
4. REQUIRED FIELDS
------------------------------------------------------------

The following fields are mandatory:

experiment_id
source_idea
timestamp
experiment_configuration
evaluation_metrics
evaluation_summary

These fields ensure experiment reproducibility.


------------------------------------------------------------
5. EXPERIMENT SOURCE
------------------------------------------------------------

Experiments may originate from:

ASF_GENERATED
HUMAN_DEFINED
DOMAIN_REQUESTED


------------------------------------------------------------
6. DATASET TRACEABILITY
------------------------------------------------------------

Each experiment must reference the dataset used for evaluation.

Example:

dataset_reference:

  dataset_id: "market_data_2026"
  timeframe: "1h"
  asset_universe:

    - BTC
    - ETH


------------------------------------------------------------
7. REPRODUCIBILITY REQUIREMENT
------------------------------------------------------------

All experiments must be reproducible.

Reproducibility requires:

• deterministic dataset
• deterministic configuration
• deterministic evaluation


------------------------------------------------------------
8. ARTIFACT IMMUTABILITY
------------------------------------------------------------

Experiment artifacts must be immutable once stored in the
Artifact Registry.

Any modification requires creation of a new artifact.


------------------------------------------------------------
9. KNOWLEDGE INTEGRATION
------------------------------------------------------------

The Knowledge Engine consumes Experiment Artifacts to generate:

• strategy rankings
• performance distributions
• parameter sensitivity analysis

Knowledge outputs may generate new Idea Artifacts.


------------------------------------------------------------
10. PROMOTION ELIGIBILITY
------------------------------------------------------------

An experiment artifact may qualify for promotion if:

• evaluation metrics exceed baseline
• results are reproducible
• governance constraints are satisfied

Promotion creates a Promotion Artifact.


------------------------------------------------------------
11. TRACEABILITY CHAIN
------------------------------------------------------------

Experiment artifacts are part of the global SAPIANTA traceability chain.

idea artifact
↓
experiment artifact
↓
knowledge artifact
↓
promotion artifact
↓
domain proposal
↓
decision envelope
↓
ledger entry


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------