FILE PATH:
sapianta_system/governance/architecture/SAPIANTA_GLOBAL_KNOWLEDGE_GRAPH_SPEC_v1.0.md

Status: ARCHITECTURAL SPECIFICATION
Layer: L3 Governance
Scope: Knowledge System
Version: 1.0


------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the architecture of the Global Knowledge Graph
(GKG) used within the SAPIANTA system.

The Global Knowledge Graph represents the structured knowledge base
of the autonomous research system.

The graph connects research artifacts produced by the system,
including:

- ideas
- experiments
- strategies
- datasets
- domains
- results

The purpose of the knowledge graph is to enable:

• cross-domain reasoning
• knowledge generalization
• research prioritization
• discovery of patterns across experiments
• long-horizon research planning
• recursive system improvement


------------------------------------------------------------
2. ARCHITECTURAL POSITION
------------------------------------------------------------

The Global Knowledge Graph operates inside the Knowledge Engine.

High level architecture flow:

information space
↓
idea discovery engine
↓
idea artifact
↓
idea registry
↓
idea validation
↓
AI Software Factory (ASF)
↓
experiment pipeline
↓
artifact registry
↓
knowledge engine
↓
GLOBAL KNOWLEDGE GRAPH
↓
research planning
↓
new ideas


------------------------------------------------------------
3. CORE CONCEPT
------------------------------------------------------------

The Global Knowledge Graph is a structured graph representation of
the entire research history of the system.

Nodes represent research entities.

Edges represent relationships between those entities.

This allows the system to understand how knowledge evolves over time.

Core node types:

IDEA
EXPERIMENT
STRATEGY
DOMAIN
DATASET
RESULT


------------------------------------------------------------
4. NODE TYPES
------------------------------------------------------------

4.1 IDEA NODE

Represents a discovered concept or hypothesis.

Source: Idea Artifact.

Fields:

node_type: IDEA

idea_id
source
timestamp
domain
classification
description
hypothesis
expected_impact


------------------------------------------------------------

4.2 EXPERIMENT NODE

Represents an executed experiment.

Fields:

node_type: EXPERIMENT

experiment_id
experiment_configuration
dataset_reference
execution_environment
timestamp


------------------------------------------------------------

4.3 STRATEGY NODE

Represents a strategy discovered through experiments.

Source: Strategy Artifact.

Fields:

node_type: STRATEGY

strategy_id
domain_scope
strategy_logic
parameters
performance_metrics
robustness_metrics
origin_experiment


------------------------------------------------------------

4.4 DOMAIN NODE

Represents an operational domain supported by SAPIANTA.

Examples:

trading
credit
energy
robotics
logistics

Fields:

node_type: DOMAIN

domain_id
domain_version
domain_type
supported_datasets
compatible_strategies


------------------------------------------------------------

4.5 DATASET NODE

Represents datasets used during experiments.

Fields:

node_type: DATASET

dataset_id
source
domain
time_range
feature_list


------------------------------------------------------------

4.6 RESULT NODE

Represents the outcome of an experiment.

Fields:

node_type: RESULT

result_id
experiment_reference
metrics
evaluation_summary
timestamp


------------------------------------------------------------
5. RELATIONSHIP TYPES
------------------------------------------------------------

The Knowledge Graph uses explicit relationships between nodes.

Allowed relationships include:

GENERATED_EXPERIMENT
EXPERIMENT_TESTED_IDEA
EXPERIMENT_PRODUCED_STRATEGY
STRATEGY_APPLIES_TO_DOMAIN
STRATEGY_TESTED_ON_DATASET
STRATEGY_IMPROVES_STRATEGY
RESULT_EVALUATES_STRATEGY

Example relationship chain:

idea_001
  ↓ GENERATED_EXPERIMENT
experiment_042
  ↓ PRODUCED_STRATEGY
strategy_015
  ↓ APPLIES_TO_DOMAIN
trading_domain


------------------------------------------------------------
6. KNOWLEDGE ENGINE FUNCTIONS
------------------------------------------------------------

The Knowledge Engine performs analysis on the knowledge graph.

Key functions include:

Pattern discovery

• detect correlations between parameters and performance
• identify regime-dependent strategy behaviour
• identify parameter sensitivity

Cross-domain transfer

Example:

volatility regime detection
trading → energy grid optimization

Research prioritization

• identify high-impact ideas
• identify unexplored research areas
• identify promising strategy families


------------------------------------------------------------
7. GOVERNANCE REQUIREMENTS
------------------------------------------------------------

The knowledge graph must satisfy the following requirements:

deterministic
versioned
append-traceable
reproducible

Each node must reference the artifact that created it.

Required metadata:

artifact_hash
artifact_origin
timestamp
creation_process


------------------------------------------------------------
8. DATA STORAGE MODEL
------------------------------------------------------------

Possible implementations:

graph database
knowledge graph engine
distributed research index

The storage must support:

• fast traversal of relationships
• deterministic query results
• reproducible graph reconstruction


------------------------------------------------------------
9. FUTURE EXTENSIONS
------------------------------------------------------------

Possible extensions include:

causal knowledge graphs
probabilistic knowledge graphs
domain ontologies
scientific discovery modules
meta-learning systems