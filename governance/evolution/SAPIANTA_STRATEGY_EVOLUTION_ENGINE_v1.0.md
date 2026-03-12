# SAPIANTA_STRATEGY_EVOLUTION_ENGINE_v1.0

Status: ARCHITECTURAL SPECIFICATION  
Layer: L3 Governance  
Scope: Autonomous Strategy Discovery  
Version: 1.0

------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the architecture for the SAPIANTA
Strategy Evolution Engine.

The Strategy Evolution Engine is responsible for:

• generating candidate strategies
• exploring parameter spaces
• evolving strategies through mutation
• evaluating strategies through experiments
• ranking strategies
• promoting validated strategies into operational domains

The engine operates as part of the SAPIANTA Autonomous
Research System.

It ensures that strategy discovery remains:

• deterministic
• reproducible
• governance-compliant
• separated from runtime decision execution.


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The Strategy Evolution Engine operates within the
Research System and integrates with the Experiment Pipeline.

Architecture flow:

Idea Artifact
↓
ASF implementation
↓
Strategy Candidate
↓
Parameter Search
↓
Mutation Engine
↓
Experiment Pipeline
↓
Artifact Registry
↓
Strategy Ranking
↓
Promotion Candidate
↓
Domain Integration


------------------------------------------------------------
3. STRATEGY ARTIFACT
------------------------------------------------------------

The Strategy Artifact defines a candidate trading strategy.

Example structure:

strategy_artifact:

  strategy_id: "uuid"

  domain:
    domain_id: "trading"
    domain_version: "1.0"

  strategy_type: "momentum"

  indicators:

    - name: "RSI"
      period: 14

    - name: "EMA"
      period: 50

  logic:

    entry_condition:
      "RSI < 30"

    exit_condition:
      "RSI > 60"

  parameters:

    position_size: 0.1
    stop_loss: 0.03
    take_profit: 0.06

  metadata:

    source: "strategy_evolution_engine"
    environment: "research"


------------------------------------------------------------
4. PARAMETER SEARCH ENGINE
------------------------------------------------------------

The Parameter Search Engine explores parameter spaces.

Search techniques:

• grid search
• random search
• adaptive search

Example:

parameter_space:

  RSI_period:
    min: 10
    max: 30

  EMA_period:
    min: 20
    max: 100

  stop_loss:
    min: 0.01
    max: 0.05


------------------------------------------------------------
5. MUTATION ENGINE
------------------------------------------------------------

The Mutation Engine generates new strategy variants.

Mutation operators:

indicator mutation
parameter mutation
logic mutation
risk parameter mutation

Examples:

mutation_1:
  change RSI period

mutation_2:
  add volatility filter

mutation_3:
  modify stop loss


------------------------------------------------------------
6. EXPERIMENT EXECUTION
------------------------------------------------------------

Each strategy candidate is evaluated through the
Experiment Pipeline.

Process:

strategy_candidate
↓
dataset selection
↓
backtest execution
↓
metric evaluation

Metrics evaluated:

• Sharpe ratio
• maximum drawdown
• win rate
• profit factor


------------------------------------------------------------
7. STRATEGY RANKING
------------------------------------------------------------

Strategies are ranked according to performance.

Example scoring function:

score =

  0.4 * sharpe_ratio
+ 0.3 * profit_factor
+ 0.2 * win_rate
- 0.1 * max_drawdown


Top ranked strategies are selected for promotion review.


------------------------------------------------------------
8. PROMOTION CANDIDATE
------------------------------------------------------------

Strategies that pass ranking thresholds become
Promotion Candidates.

Promotion conditions:

• reproducible performance
• performance above baseline
• governance compliance
• deterministic execution


Promotion produces:

PROMOTION_ARTIFACT


------------------------------------------------------------
9. DOMAIN INTEGRATION
------------------------------------------------------------

Promoted strategies are integrated into domain modules.

Example:

Trading Domain

strategy
↓
signal generation
↓
proposal artifact
↓
Decision Spine


------------------------------------------------------------
10. GOVERNANCE CONSTRAINTS
------------------------------------------------------------

The Strategy Evolution Engine must satisfy:

• deterministic experiment execution
• reproducible results
• traceable artifacts
• governance validation before promotion

The engine must never interact directly with execution.

All runtime decisions must go through:

proposal
↓
policy
↓
decision envelope
↓
ledger


------------------------------------------------------------
11. RELATIONSHIP TO OTHER ARTIFACTS
------------------------------------------------------------

Idea Artifact
→ defines initial concept

Experiment Artifact
→ stores experiment results

Promotion Artifact
→ approves operational deployment

Proposal Artifact
→ used by domains for runtime decisions.


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------