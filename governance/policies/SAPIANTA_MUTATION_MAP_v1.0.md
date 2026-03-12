# SAPIANTA_MUTATION_MAP_v1.0

Status: CANONICAL GOVERNANCE POLICY  
Layer: System Governance  
Scope: Autonomous System Evolution  
Version: 1.0

------------------------------------------------------------
1. PURPOSE
------------------------------------------------------------

This document defines the mutation policy for the SAPIANTA system.

The Mutation Map specifies which parts of the system may be modified
by autonomous development processes and which parts are protected.

The policy ensures:

• system integrity
• deterministic behavior
• governance control
• safe autonomous evolution

This policy is enforced by the Governed Autonomous Development (GAD) system.

------------------------------------------------------------
2. ARCHITECTURAL PRINCIPLE
------------------------------------------------------------

SAPIANTA architecture is divided into layers with different mutation
permissions.

Each layer belongs to one of the following mutation classes:

IMMUTABLE
RESTRICTED
GOVERNED
EVOLVABLE

------------------------------------------------------------
3. MUTATION CLASSES
------------------------------------------------------------

IMMUTABLE

These components must never be modified automatically.

Changes are allowed only through explicit manual governance process.

Examples:

• constitutional architecture
• canonical schemas
• core system guarantees


RESTRICTED

Changes are possible but require strict governance review.

Examples:

• decision runtime pipeline
• policy evaluation logic


GOVERNED

Changes may be proposed by the system but must pass governance validation
and human approval.


EVOLVABLE

These components may be autonomously modified and extended
through the GAD development process.

------------------------------------------------------------
4. LAYER CLASSIFICATION
------------------------------------------------------------

L0 – SYSTEM CONSTITUTION

Mutation Class: IMMUTABLE

Description:

Defines the fundamental architecture principles of SAPIANTA.

Examples:

• architectural constitution
• deterministic guarantees
• system integrity rules

Allowed Mutation:

NONE


------------------------------------------------------------

L1 – CANONICAL ARTIFACT DEFINITIONS

Mutation Class: IMMUTABLE

Description:

Defines canonical artifact schemas used across the system.

Examples:

• STRATEGY_ARTIFACT_SCHEMA
• DECISION_ENVELOPE_SCHEMA
• LEDGER_SCHEMA

Allowed Mutation:

NONE


------------------------------------------------------------

L2 – DECISION SPINE

Mutation Class: RESTRICTED

Description:

The deterministic runtime decision pipeline.

Components include:

proposal
policy validation
advisory
decision envelope
ledger

Allowed Mutation:

Only through governance review and explicit approval.


------------------------------------------------------------

L3 – GOVERNANCE SYSTEM

Mutation Class: GOVERNED

Description:

Governance validation components.

Examples:

• promotion gates
• validation pipelines
• artifact registry

Allowed Mutation:

AI may propose modifications but they must pass:

• governance validation
• human approval


------------------------------------------------------------

L4 – RESEARCH SYSTEM

Mutation Class: EVOLVABLE

Description:

Autonomous research infrastructure.

Examples:

• IdeaEngine
• ExperimentEngine
• EvaluationEngine
• EvolutionEngine
• StrategyMemory
• StrategyPromotionEngine

Allowed Mutation:

Allowed through GAD process.


------------------------------------------------------------

RUNTIME MODULES

Mutation Class: EVOLVABLE

Description:

Domain modules and runtime engines.

Examples:

• trading domain
• market regime engine
• experiment utilities
• research orchestrator

Allowed Mutation:

Allowed through GAD process.


------------------------------------------------------------
5. FORBIDDEN PATHS
------------------------------------------------------------

The following repository paths are strictly protected
and may never be modified automatically.

Protected paths:

governance/constitution/
governance/contracts/

Any change proposed by GAD affecting these paths must be rejected.

------------------------------------------------------------
6. GAD ENFORCEMENT
------------------------------------------------------------

The GAD system must enforce the Mutation Map before any
code generation or repository update.

Validation steps:

1. analyze proposed file changes
2. detect layer of each file
3. check mutation class
4. reject forbidden changes

Example:

If proposed change affects:

governance/contracts/

the system must reject the proposal.


------------------------------------------------------------
7. FUTURE EXTENSIONS
------------------------------------------------------------

The Mutation Map may later include:

• module-level mutation policies
• domain-specific mutation permissions
• safety classification for high-risk modules


------------------------------------------------------------
END OF DOCUMENT
------------------------------------------------------------