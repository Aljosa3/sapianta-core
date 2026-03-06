# DECISION_EXPERIMENT_PROTOCOL_v0.1

STATUS
ACTIVE

TYPE
GOVERNANCE_SPEC

LAYER
L3_DOMAIN_GOVERNANCE

VERSION
0.1

---

# 1 PURPOSE

Decision Experiment Protocol definira
postopek znanstvenega razvoja
odločitvenih modelov v sistemu SAPIANTA.

Protokol omogoča:

- kontroliran razvoj strategij
- dokazovanje izboljšav
- deterministični replay eksperimentov
- minimalni vpliv na produkcijski sistem.

Eksperimenti se izvajajo v izoliranem okolju.

---

# 2 EXPERIMENT PRINCIPLE

Vsaka sprememba odločitvenega modela
se mora obravnavati kot eksperiment.

Eksperiment mora biti:

- reproducibilen
- dokumentiran
- primerljiv z baseline modelom.

---

# 3 EXPERIMENT STRUCTURE

Vsak eksperiment vsebuje naslednje komponente.

experiment_id  
baseline_model_reference  
candidate_model_reference  
experiment_dataset  
world_state_reference  
evaluation_metrics  

---

# 4 BASELINE MODEL

Baseline model predstavlja
trenutni produkcijski model.

Baseline mora biti:

- verzioniran
- hash-bound
- reproducibilen.

---

# 5 CANDIDATE MODEL

Candidate model predstavlja
novo strategijo ali spremembo.

Primeri sprememb

- nova strategija
- sprememba parametrov
- sprememba modela.

Candidate model mora biti
popolnoma reproducibilen.

---

# 6 EXPERIMENT DATASET

Eksperiment mora uporabljati
definiran dataset.

Dataset mora biti:

- snapshot
- hash-bound
- replayable.

---

# 7 WORLD STATE REFERENCE

Eksperiment mora uporabljati
definiran World State snapshot.

fields

world_state_hash  
world_state_timestamp  

To omogoča reprodukcijo
konteksta eksperimenta.

---

# 8 EVALUATION METRICS

Eksperiment mora definirati
objektivne metrike uspešnosti.

Primeri

Trading

return  
drawdown  
sharpe_ratio  
volatility  

Credit

default_prediction_accuracy  
false_positive_rate  

Risk

stress_resilience_score  

---

# 9 EXPERIMENT EXECUTION

Eksperiment mora biti izveden
v sandbox okolju.

Sandbox mora zagotavljati:

- izolacijo od produkcije
- deterministični replay
- artefaktno sled.

---

# 10 EXPERIMENT ARTIFACTS

Vsak eksperiment mora generirati
artefakte.

experiment_metadata  
execution_trace  
evaluation_results  

Ti artefakti morajo biti
hash-bound.

---

# 11 EXPERIMENT COMPARISON

Candidate model mora biti
primerjan z baseline modelom.

Primerjava mora vključevati:

performance_difference  
risk_difference  
stability_difference  

---

# 12 PROMOTION CRITERIA

Eksperiment lahko vodi
do promocije modela.

Promotion zahteva:

statistically significant improvement  
no increase in systemic risk  
governance approval  

---

# 13 PROMOTION FLOW

Promotion flow

Experiment
    ↓
Evaluation
    ↓
Governance review
    ↓
Promotion Gate
    ↓
Production deployment

---

# 14 RAL REQUIREMENTS

Eksperimenti morajo dosegati
vsaj RAL2.

Kritični sistemi lahko zahtevajo
RAL3.

---

# 15 META INVARIANTS

Eksperimenti ne smejo:

- vplivati na produkcijski execution pipeline
- spreminjati governance pravil
- bypassati Domain Orchestration.

Eksperimenti morajo ostati
popolnoma izolirani.

---

END OF DOCUMENT