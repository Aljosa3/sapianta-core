# SAPIANTA_STRATEGY_EVOLUTION_ENGINE_v1.0

Status: ARCHITECTURAL SPECIFICATION  
Layer: L3 Governance / Evolution System  
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
• generating new experiments
• ranking strategies through evaluation results
• producing promotion candidates

The engine operates as part of the SAPIANTA Autonomous
Research System.

It ensures that strategy discovery remains:

• deterministic
• reproducible
• governance-compliant
• separated from runtime decision execution.


------------------------------------------------------------
2. POSITION IN AUTONOMOUS RESEARCH ARCHITECTURE
------------------------------------------------------------

The Strategy Evolution Engine is part of the SAPIANTA
Autonomous Research System.

Full research pipeline:

Idea Discovery Engine
↓
Research Orchestrator
↓
Research Runtime
↓
Experiment Engine
↓
Artifact Registry
↓
Evaluation Engine
↓
Strategy Evolution Engine
↓
Promotion Engine
↓
Domain Modules
↓
Decision Spine

The Evolution Engine generates new strategies
based on experiment evaluation results.


------------------------------------------------------------
3. STRATEGY ARTIFACT
------------------------------------------------------------

The Strategy Artifact defines a candidate strategy.

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

Search techniques include:

• grid search
• random search
• adaptive search
• evolutionary parameter search

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

Mutation operators include:

• indicator mutation
• parameter mutation
• logic mutation
• risk parameter mutation

Examples:

mutation_1:
  change RSI period

mutation_2:
  add volatility filter

mutation_3:
  modify stop loss


------------------------------------------------------------
6. STRATEGY RECOMBINATION
------------------------------------------------------------

The recombination engine combines successful strategies
to produce new candidate strategies.

Recombination examples:

• combine indicators from two strategies
• merge entry logic
• combine risk management rules


------------------------------------------------------------
7. EXPERIMENT GENERATION
------------------------------------------------------------

The Evolution Engine generates experiments for
new candidate strategies.

Process:

strategy_candidate
↓
experiment definition
↓
dataset selection
↓
Experiment Engine execution


------------------------------------------------------------
8. EXPERIMENT EVALUATION
------------------------------------------------------------

Experiments are evaluated by the Evaluation Engine.

Metrics evaluated may include:

• Sharpe ratio
• maximum drawdown
• win rate
• profit factor
• stability across datasets


------------------------------------------------------------
9. STRATEGY RANKING
------------------------------------------------------------

Strategies are ranked according to performance.

Example scoring function:

score =

  0.4 * sharpe_ratio
+ 0.3 * profit_factor
+ 0.2 * win_rate
- 0.1 * max_drawdown

Top ranked strategies are selected for
further evolution or promotion review.


------------------------------------------------------------
10. PROMOTION CANDIDATES
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
11. DOMAIN INTEGRATION
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
12. EVOLUTION LOOP
------------------------------------------------------------

The Strategy Evolution Engine executes
the continuous research loop:

evaluate
↓
select
↓
mutate
↓
recombine
↓
generate strategies
↓
generate experiments
↓
experiment execution


------------------------------------------------------------
13. GOVERNANCE CONSTRAINTS
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
14. RELATIONSHIP TO OTHER ARTIFACTS
------------------------------------------------------------

Idea Artifact
→ defines initial concept

Experiment Artifact
→ stores experiment results

Promotion Artifact
→ approves operational deployment

Proposal Artifact
→ used by domains for runtime decisions


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------