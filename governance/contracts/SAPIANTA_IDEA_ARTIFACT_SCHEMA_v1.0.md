# SAPIANTA_IDEA_ARTIFACT_SCHEMA_v1.0

Status: CANONICAL SPECIFICATION
Layer: L3 Governance
Scope: Idea Discovery Engine
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the canonical schema for the Idea Artifact
used within the SAPIANTA Idea Discovery Engine.

The Idea Artifact represents a structured description of a
discovered concept, hypothesis, or improvement opportunity
identified by:

- AI research agents
- external information discovery
- domain analysis
- human contribution

The Idea Artifact enables:

• structured idea representation
• cross-domain idea classification
• governance traceability
• deterministic idea evaluation
• integration with the ASF (AI Software Factory)


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The Idea Artifact exists within the Idea Discovery Engine
before hypothesis implementation.

Architecture flow:

information sources
↓
idea discovery
↓
idea artifact
↓
idea registry
↓
idea validation
↓
ASF implementation


------------------------------------------------------------
3. IDEA ARTIFACT STRUCTURE
------------------------------------------------------------

Example Idea Artifact:

idea_artifact:

  idea_id: "uuid"

  source:
    type: "AI_AGENT"
    agent_id: "research_agent_01"

  timestamp: "ISO-8601"

  domain:
    primary_domain: "trading"
    related_domains:
      - "ai"
      - "data_science"

  classification:
    category: "strategy"
    subcategory: "volatility_regime"

  description:
    title: "Regime-switching volatility trading strategy"
    summary: "Use volatility regime detection to switch
              between momentum and mean-reversion strategies."

  rationale:
    motivation: "Volatility regimes strongly influence
                 strategy performance."
    supporting_sources:
      - "research_paper_reference"
      - "github_repository"
      - "blog_post"

  hypothesis:

    description:
      "Strategy performance improves when switching
       trading logic based on volatility regime detection."

  expected_impact:

    metrics:
      - sharpe_ratio
      - max_drawdown
      - win_rate

    potential_improvement: "15% performance improvement"

  feasibility:

    implementation_complexity: "medium"
    data_requirements:
      - "historical volatility"
      - "price time series"

  governance:

    architecture_compatible: true
    policy_risk_level: "low"

  metadata:

    discovery_method: "llm_analysis"
    environment: "research"


------------------------------------------------------------
4. REQUIRED FIELDS
------------------------------------------------------------

The following fields are mandatory:

idea_id
source
timestamp
domain
description
hypothesis
expected_impact

These fields ensure that ideas are:

• traceable
• classifiable
• evaluatable
• reproducible


------------------------------------------------------------
5. IDEA SOURCE TYPES
------------------------------------------------------------

Allowed idea sources:

AI_AGENT
HUMAN
RESEARCH_PAPER
GITHUB
FORUM
NEWS
DATA_ANALYSIS


------------------------------------------------------------
6. DOMAIN CLASSIFICATION
------------------------------------------------------------

Each idea must be assigned to a domain.

Examples:

trading
credit
insurance
energy
infrastructure
ai
data_science

Multiple domains may be referenced.


------------------------------------------------------------
7. IDEA VALIDATION REQUIREMENTS
------------------------------------------------------------

Before an idea can enter the ASF implementation pipeline,
the Idea Validator must verify:

• architectural compatibility
• domain relevance
• feasibility
• governance compliance


------------------------------------------------------------
8. HUMAN IDEA SUPPORT
------------------------------------------------------------

Ideas may originate from human contributors.

Example:

source:

  type: "HUMAN"
  contributor_id: "researcher_01"

Human ideas must follow the same schema
as AI-discovered ideas.


------------------------------------------------------------
9. IDEA REGISTRY STORAGE
------------------------------------------------------------

All Idea Artifacts must be stored in the Idea Registry.

Storage requirements:

• append-only log
• deterministic serialization
• cryptographic integrity verification


------------------------------------------------------------
10. SERIALIZATION REQUIREMENTS
------------------------------------------------------------

Idea artifacts must be serialized deterministically.

Requirements:

• sorted keys
• stable encoding
• canonical representation

Allowed formats:

JSON
canonical JSON
YAML


------------------------------------------------------------
11. GOVERNANCE INTEGRATION
------------------------------------------------------------

Idea Artifacts are not executable instructions.

They must pass through the research pipeline:

idea artifact
↓
idea validation
↓
ASF implementation
↓
experiment pipeline
↓
artifact registry

Only validated experiment results may later influence
domain decisions through the Decision Spine.