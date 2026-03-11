FILE PATH:
sapianta_system/governance/contracts/SAPIANTA_STRATEGY_ARTIFACT_SCHEMA_v1.0.md


# SAPIANTA_STRATEGY_ARTIFACT_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION  
Layer: L3 Governance  
Scope: Research Artifacts / Strategy Evolution  
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the canonical schema for the Strategy Artifact
used within the SAPIANTA Autonomous Research System.

The Strategy Artifact represents a structured description of a
validated strategy produced by the research pipeline.

Strategies may apply across multiple domains including:

• trading
• credit decision models
• medical treatment policies
• infrastructure control
• energy optimization
• insurance risk models

The Strategy Artifact ensures:

• deterministic representation
• governance traceability
• reproducible experiments
• strategy evolution tracking
• domain-independent logic


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The Strategy Artifact exists inside the SAPIANTA research pipeline.

Architecture flow:

idea artifact
↓
ASF implementation
↓
experiment execution
↓
evaluation
↓
STRATEGY_ARTIFACT
↓
ranking
↓
promotion
↓
domain integration
↓
proposal artifact
↓
decision spine
↓
execution

This ensures that research remains separated from
runtime execution decisions.


------------------------------------------------------------
3. CANONICAL STRATEGY ARTIFACT STRUCTURE
------------------------------------------------------------

Example Strategy Artifact:

strategy_artifact:

  strategy_id: "uuid"

  version: "1.0"

  origin:

    idea_reference:
      idea_id: "uuid"
      idea_hash: "sha256"

    experiment_reference:
      experiment_id: "uuid"
      experiment_hash: "sha256"

  domain_scope:

    primary_domain: "trading"

    compatible_domains:
      - "credit"
      - "energy"
      - "infrastructure"

  classification:

    category: "decision_strategy"
    subtype: "momentum_breakout"

  description:

    title: "Momentum Breakout Strategy"

    summary: >
      Strategy detects breakout conditions using moving averages
      and volatility expansion.

  strategy_logic:

    inputs:
      - price_series
      - volatility
      - volume

    signals:

      entry_condition: "EMA20 > EMA50 AND RSI > 60"

      exit_condition: "RSI < 50"

    action_mapping:

      signal_buy: "OPEN_POSITION"

      signal_sell: "CLOSE_POSITION"


------------------------------------------------------------
4. PARAMETERS
------------------------------------------------------------

Strategies must expose parameters that allow controlled mutation.

parameters:

  EMA_FAST:

    type: integer
    value: 20

    mutation_range:
      min: 10
      max: 50

  EMA_SLOW:

    type: integer
    value: 50

    mutation_range:
      min: 30
      max: 100

  RSI_THRESHOLD:

    type: float
    value: 60

    mutation_range:
      min: 55
      max: 70


------------------------------------------------------------
5. PARAMETER MUTATION
------------------------------------------------------------

Strategies support evolutionary search through mutation.

parameter_mutation:

  allowed: true

  mutation_method: "genetic_search"

  mutation_constraints:

    max_step: 10

    parameter_lock: false

Allowed mutation methods:

• grid_search
• genetic_algorithm
• bayesian_optimization
• adaptive_search


------------------------------------------------------------
6. PERFORMANCE EVALUATION
------------------------------------------------------------

Evaluation results must reference the experiment artifact.

evaluation:

  dataset_reference: "dataset_hash"

  metrics:

    sharpe_ratio: 1.35
    max_drawdown: 0.12
    win_rate: 0.58
    profit_factor: 1.70

  robustness_tests:

    walk_forward_periods: 5
    regime_stability: "pass"
    parameter_stability: "pass"


------------------------------------------------------------
7. PERFORMANCE SUMMARY
------------------------------------------------------------

performance_summary:

  ranking_score: 0.84

  baseline_comparison: "+18%"


------------------------------------------------------------
8. GOVERNANCE COMPATIBILITY
------------------------------------------------------------

governance:

  architecture_compatible: true

  policy_risk_level: "medium"

  reproducible: true

  deterministic: true


------------------------------------------------------------
9. STRATEGY LINEAGE
------------------------------------------------------------

Strategies evolve through generations.

lifecycle:

  generation: 3

  parent_strategies:
    - "strategy_uuid_1"
    - "strategy_uuid_2"

  mutation_history:

    - mutation_id: "mut_001"

      changed_parameter: "EMA_FAST"

      old_value: 15

      new_value: 20


------------------------------------------------------------
10. DOMAIN INDEPENDENCE
------------------------------------------------------------

Strategy artifacts must remain domain-independent.

They define:

• signals
• conditions
• decision logic

Execution is defined by domain modules.

Example:

Trading domain
→ OPEN_POSITION

Credit domain
→ APPROVE_LOAN

Infrastructure domain
→ ACTIVATE_CONTROL_POLICY


------------------------------------------------------------
11. DETERMINISTIC SERIALIZATION
------------------------------------------------------------

Strategy artifacts must be serialized deterministically.

Requirements:

• canonical JSON or YAML
• sorted keys
• stable encoding
• no runtime randomness

Hash calculation:

strategy_hash = sha256(canonical_serialization)


------------------------------------------------------------
12. PROMOTION CONDITIONS
------------------------------------------------------------

A strategy may be promoted when:

• reproducible == true
• ranking_score above threshold
• robustness tests passed
• governance compatibility confirmed

Promotion generates a:

PROMOTION_ARTIFACT


------------------------------------------------------------
13. STRATEGY LIFECYCLE
------------------------------------------------------------

The lifecycle of a strategy within SAPIANTA:

IDEA
↓
IDEA_ARTIFACT
↓
ASF IMPLEMENTATION
↓
EXPERIMENT
↓
EXPERIMENT_ARTIFACT
↓
STRATEGY_ARTIFACT
↓
RANKING
↓
PROMOTION
↓
DOMAIN INTEGRATION
↓
PROPOSAL_ARTIFACT
↓
DECISION_SPINE
↓
DECISION_ENVELOPE
↓
LEDGER
↓
EXECUTION


------------------------------------------------------------
14. DESIGN PRINCIPLES
------------------------------------------------------------

The Strategy Artifact must guarantee:

• deterministic evaluation
• reproducibility
• governance traceability
• evolutionary search compatibility
• domain-independent strategy definition