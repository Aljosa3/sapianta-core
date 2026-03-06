# DOMAIN_ORCHESTRATION_SPEC_v0.1

STATUS
ACTIVE

LAYER
L2.5_DOMAIN_ORCHESTRATION

TYPE
ARCHITECTURE_SPEC

VERSION
0.1

---

# 1 PURPOSE

Domain Orchestration koordinira
izvajanje več domen znotraj
ene odločitve.

Orchestrator:

- kliče domene
- zbira rezultate
- rešuje konflikte
- sestavi Decision Context.

Orchestrator ne vsebuje
domain logic.

---

# 2 ORCHESTRATION PRINCIPLE

Orchestration mora biti:

- deterministična
- replay-verificirana
- hash-traceable.

Execution order mora biti
deterministično definiran.

---

# 3 ORCHESTRATION PIPELINE

Primer pipeline

Market Input
    ↓
Trading Domain
    ↓
Risk Domain
    ↓
Compliance Domain
    ↓
Decision Aggregation

---

# 4 DOMAIN CALL MODEL

Vsaka domena prejme:

- input artifact
- world_state snapshot
- governance parameters.

Vsaka domena vrne:

domain_output artifact.

---

# 5 DOMAIN OUTPUT STRUCTURE

Domain output vsebuje

domain_id  
decision_signal  
confidence_score  
risk_flags  

example

Trading Domain

signal = BUY  
confidence = 0.72  

Risk Domain

risk_allowed = TRUE  

Compliance Domain

asset_allowed = TRUE  

---

# 6 CONFLICT RESOLUTION

Orchestrator mora definirati
pravila konflikta.

Primer

Risk veto > Trading signal  

Compliance veto > Execution  

---

# 7 DETERMINISM

Execution order mora biti
identičen pri replayu.

Orchestration mora biti
hash-traceable.

---

# 8 ORCHESTRATION TRACE

Orchestrator mora generirati
trace artifact.

fields

domain_call_sequence  
domain_outputs  
conflict_resolution  

---

# 9 GOVERNANCE

Spremembe orchestration logike
so klasificirane kot

STRUCTURAL_EXECUTION_CHANGE.

Zahtevajo governance approval.

---

# 10 META INVARIANTS

Orchestrator ne sme

- spreminjati domain logic
- spreminjati World State
- spreminjati governance parametrov.

Orchestrator koordinira samo flow.

---

END OF DOCUMENT