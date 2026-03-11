# SAPIANTA_PROMOTION_ARTIFACT_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION
Layer: L3 Governance
Scope: Research → Production Promotion
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the canonical schema for the Promotion Artifact
used in the SAPIANTA Autonomous Research System.

A Promotion Artifact records the transition of a research artifact
into an operational domain artifact.

The artifact ensures that the transition from research results
to operational deployment is:

• controlled
• auditable
• policy-compliant
• reversible


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

Promotion artifacts exist between the research pipeline and
domain runtime modules.

Architecture flow:

idea artifact
↓
experiment artifact
↓
knowledge analysis
↓
promotion artifact
↓
domain integration
↓
proposal artifact
↓
decision envelope


------------------------------------------------------------
3. PROMOTION ARTIFACT STRUCTURE
------------------------------------------------------------

Example:

promotion_artifact:

  promotion_id: "uuid"

  source_experiment:
    experiment_id: "uuid"

  timestamp: "ISO-8601"

  promoted_artifact:

    type: "strategy"

    artifact_reference:
      artifact_id: "strategy_001"

  evaluation_summary:

    performance_metrics:

      sharpe_ratio: float
      drawdown: float
      profit: float

  promotion_decision:

    decision: "APPROVED"

    justification:
      "performance exceeds baseline threshold"

  governance:

    policy_compliant: true
    deterministic: true

  metadata:

    promotion_source: "knowledge_engine"
    environment: "research"


------------------------------------------------------------
4. REQUIRED FIELDS
------------------------------------------------------------

Mandatory fields:

promotion_id
source_experiment
timestamp
promoted_artifact
promotion_decision


------------------------------------------------------------
5. PROMOTION CRITERIA
------------------------------------------------------------

Artifacts may be promoted when:

• experiment metrics exceed baseline
• results are reproducible
• policy constraints are satisfied
• domain compatibility verified


------------------------------------------------------------
6. DOMAIN INTEGRATION
------------------------------------------------------------

After promotion, artifacts may be integrated into domains.

Example:

trading domain → new strategy candidate

credit domain → new risk model

integration produces Proposal Artifacts.


------------------------------------------------------------
7. TRACEABILITY CHAIN
------------------------------------------------------------

Promotion artifacts maintain full traceability:

idea artifact
↓
experiment artifact
↓
promotion artifact
↓
proposal artifact
↓
decision envelope
↓
ledger entry


------------------------------------------------------------
8. SAFETY PRINCIPLE
------------------------------------------------------------

Promotion does not automatically trigger execution.

All promoted artifacts must still pass:

policy validation
decision envelope
ledger recording


------------------------------------------------------------
9. REVERSIBILITY
------------------------------------------------------------

Promotion must support rollback.

If a promoted artifact causes undesirable outcomes,
the artifact may be disabled by governance intervention.


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------