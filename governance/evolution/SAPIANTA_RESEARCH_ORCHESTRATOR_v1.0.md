# SAPIANTA_RESEARCH_ORCHESTRATOR_v1.0

Status: ARCHITECTURAL SPECIFICATION
Layer: L3 Governance
Scope: Autonomous Research Control
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the architecture of the SAPIANTA
Research Orchestrator.

The Research Orchestrator coordinates the complete
autonomous research pipeline.

It manages:

• idea discovery
• experiment scheduling
• knowledge extraction
• strategy evolution
• artifact registration

The orchestrator ensures that research activities remain:

• deterministic
• traceable
• governance-compliant
• reproducible


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The Research Orchestrator is the central coordination layer
of the SAPIANTA Autonomous Research System.

High level flow:

WORLD INFORMATION
↓
IDEA_DISCOVERY_ENGINE
↓
RESEARCH_ORCHESTRATOR
↓
ASF IMPLEMENTATION
↓
EXPERIMENT_PIPELINE
↓
KNOWLEDGE_ENGINE
↓
STRATEGY_EVOLUTION_ENGINE
↓
STRATEGY_ARTIFACT
↓
PROMOTION_SYSTEM
↓
DOMAIN_MODULES
↓
DECISION_SPINE


------------------------------------------------------------
3. CORE RESPONSIBILITIES
------------------------------------------------------------

The orchestrator performs the following tasks:

1. Idea ingestion
2. Hypothesis creation scheduling
3. Experiment scheduling
4. Artifact registration
5. Knowledge extraction triggering
6. Strategy evolution triggering
7. Promotion candidate tracking


------------------------------------------------------------
4. ORCHESTRATION CYCLE
------------------------------------------------------------

The research loop executed by the orchestrator:

1. discover ideas
2. validate ideas
3. generate experiments
4. run experiments
5. register experiment artifacts
6. extract knowledge
7. evolve strategies
8. register strategy artifacts
9. evaluate promotion candidates

The loop then repeats continuously.


------------------------------------------------------------
5. IDEA MANAGEMENT
------------------------------------------------------------

The orchestrator collects ideas from:

• Idea Discovery Engine
• domain modules
• human input
• knowledge artifacts

Ideas are validated before entering the experiment pipeline.


------------------------------------------------------------
6. EXPERIMENT SCHEDULING
------------------------------------------------------------

The orchestrator schedules experiments using the ASF.

Scheduling inputs:

• experiment priority
• resource availability
• domain constraints
• dataset availability

Experiment execution must remain deterministic.


------------------------------------------------------------
7. ARTIFACT REGISTRATION
------------------------------------------------------------

All artifacts produced during research must be registered
in the Artifact Registry.

Artifacts include:

• idea artifacts
• experiment artifacts
• knowledge artifacts
• strategy artifacts


------------------------------------------------------------
8. KNOWLEDGE EXTRACTION
------------------------------------------------------------

The orchestrator triggers the Knowledge Engine when
new experiment artifacts are available.

Knowledge extraction may produce:

• pattern discoveries
• parameter sensitivities
• regime models


------------------------------------------------------------
9. STRATEGY EVOLUTION
------------------------------------------------------------

The Strategy Evolution Engine uses knowledge artifacts
to generate improved strategies.

Evolution techniques may include:

• parameter mutation
• strategy recombination
• regime specialization


------------------------------------------------------------
10. PROMOTION TRACKING
------------------------------------------------------------

Strategies produced by the research system are evaluated
for promotion.

Promotion conditions include:

• reproducible experiment results
• superior performance metrics
• governance compliance


------------------------------------------------------------
11. DETERMINISTIC ORCHESTRATION
------------------------------------------------------------

All orchestration decisions must be deterministic.

Given identical inputs, the orchestrator must produce
identical research actions.

Requirements:

• deterministic scheduling
• deterministic artifact ordering
• deterministic evaluation triggers


------------------------------------------------------------
12. GOVERNANCE INTEGRATION
------------------------------------------------------------

The Research Orchestrator must respect SAPIANTA governance rules.

All actions must:

• produce artifacts
• maintain lineage traceability
• register artifacts in the Artifact Registry
• support deterministic replay


------------------------------------------------------------
13. SYSTEM ROLE
------------------------------------------------------------

The Research Orchestrator acts as the central intelligence
controller of the SAPIANTA research system.

It ensures that research remains structured,
governance-compliant, and continuously improving.


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------