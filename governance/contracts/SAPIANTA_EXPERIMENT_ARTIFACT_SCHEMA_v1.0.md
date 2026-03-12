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
• deterministic
• traceable
• comparable
• governance-compliant

Experiment artifacts form the bridge between:

Idea Artifacts  
and  
Strategy Artifacts.


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
↓
strategy artifact


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

  hypothesis:

    description:
      "Volatility regime detection improves trading performance."

  experiment_configuration:

    strategy_id: "exp-001"

    parameters:

      lookback_window: 20
      volatility_threshold: 0.03

  dataset:

    dataset_id: "market_dataset_001"

    dataset_hash: "sha256_hash_of_dataset"

    timeframe: "1h"

    asset_universe:

      - BTC
      - ETH

  execution_environment:

    runtime_version: "sapianta_runtime_v0.4"

    execution_node: "research_node_01"

  evaluation_metrics:

    profit: float
    sharpe_ratio: float
    drawdown: float
    volatility: float
    win_rate: float

  evaluation_summary:

    fitness_score: float

    ranking_position: int

  deterministic_replay:

    experiment_hash: "sha256_hash"

    replay_seed: 42

    replay_verified: true

  governance:

    deterministic: true

    reproducible: true

    dataset_integrity_verified: true

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
dataset  
evaluation_metrics  
evaluation_summary  
deterministic_replay  

These fields ensure:

• experiment reproducibility
• deterministic replay
• dataset traceability


------------------------------------------------------------
5. DATASET TRACEABILITY
------------------------------------------------------------

Each experiment must reference the dataset used for evaluation.

The dataset must include:

dataset_id  
dataset_hash  
timeframe  
asset_universe  

dataset_hash ensures:

• dataset immutability
• reproducible experiment results
• protection against data drift


------------------------------------------------------------
6. DETERMINISTIC REPLAY
------------------------------------------------------------

All experiments must support deterministic replay.

Replay requires:

• experiment hash
• dataset hash
• replay seed
• configuration parameters

This guarantees that experiment results can
be reproduced exactly.


------------------------------------------------------------
7. EXPERIMENT SOURCE
------------------------------------------------------------

Experiments may originate from:

ASF_GENERATED  
HUMAN_DEFINED  
DOMAIN_REQUESTED  


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
strategy artifact
↓
domain proposal
↓
decision envelope
↓
ledger entry


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------