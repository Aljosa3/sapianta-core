# SAPIANTA_PROMOTION_ENGINE_v1.0

Status: ARCHITECTURAL SPECIFICATION  
Layer: L3 Governance / Evolution System  
Scope: Strategy Promotion Control  
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

The Promotion Engine determines when a research strategy
is allowed to move from the research environment into
operational domain modules.

The Promotion Engine acts as a governance gate between:

RESEARCH SYSTEM
and
OPERATIONAL DECISION SYSTEM


------------------------------------------------------------
2. POSITION IN RESEARCH PIPELINE
------------------------------------------------------------

Full architecture flow:

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


------------------------------------------------------------
3. PROMOTION PURPOSE
------------------------------------------------------------

Promotion ensures that only strategies that meet
strict governance requirements become operational.

Promotion validates:

• reproducible performance
• stability across datasets
• governance compliance
• deterministic execution


------------------------------------------------------------
4. PROMOTION INPUT ARTIFACTS
------------------------------------------------------------

Promotion candidates originate from:

Strategy Artifacts

and

Evaluation Artifacts


Example input:

strategy_artifact
evaluation_artifact
ranking_result


------------------------------------------------------------
5. PROMOTION CONDITIONS
------------------------------------------------------------

A strategy can be promoted only if:

• evaluation metrics exceed baseline
• results are reproducible
• strategy is deterministic
• artifact lineage is complete


------------------------------------------------------------
6. PROMOTION VALIDATION
------------------------------------------------------------

Validation includes:

Performance Validation

• Sharpe ratio threshold
• drawdown limits
• stability across regimes

Reproducibility Validation

• deterministic replay
• dataset consistency

Governance Validation

• artifact lineage
• schema compliance


------------------------------------------------------------
7. PROMOTION ARTIFACT
------------------------------------------------------------

Promotion produces a Promotion Artifact.

Example:

promotion_artifact:

  promotion_id: "uuid"

  strategy_id: "uuid"

  domain: "trading"

  validation:

    performance_pass: true
    reproducibility_pass: true
    governance_pass: true

  timestamp: "ISO8601"


------------------------------------------------------------
8. DOMAIN DEPLOYMENT
------------------------------------------------------------

Promoted strategies are deployed into domain modules.

Example:

Trading Domain

strategy
↓
signal generator
↓
proposal artifact
↓
Decision Spine


------------------------------------------------------------
9. SAFETY CONSTRAINT
------------------------------------------------------------

The Promotion Engine ensures that the research system
cannot directly affect runtime decisions.

All operational usage must go through:

proposal
↓
policy
↓
decision envelope
↓
ledger


------------------------------------------------------------
10. SYSTEM ROLE
------------------------------------------------------------

The Promotion Engine converts the SAPIANTA research system
into an operational intelligence system.

Without promotion:

SAPIANTA = research laboratory

With promotion:

SAPIANTA = operational decision engine


------------------------------------------------------------
END OF DOCUMENT