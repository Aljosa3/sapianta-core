# DECISION_CONTEXT_ENVELOPE_v0.1

STATUS
ACTIVE

TYPE
DECISION_ARTIFACT

VERSION
0.1

---

# 1 PURPOSE

Decision Context Envelope
zajame celoten kontekst odločitve.

Omogoča

- deterministični replay
- audit sled
- hash-chain integriteto.

---

# 2 STRUCTURE

Envelope vsebuje

decision_id  
timestamp  
world_state_hash  
domain_outputs  
orchestration_trace  
final_decision  

---

# 3 DECISION ID

decision_id mora biti
unikaten identifikator.

Primer

decision_id = SHA256(input + timestamp)

---

# 4 WORLD STATE REFERENCE

Envelope mora vsebovati

world_state_hash

To omogoča
rekonstrukcijo konteksta sveta.

---

# 5 DOMAIN OUTPUTS

Zabeleženi morajo biti
izhodni artefakti vseh domen.

Primer

Trading Domain → signal BUY  
Risk Domain → allowed TRUE  
Compliance Domain → allowed TRUE  

---

# 6 ORCHESTRATION TRACE

Trace mora vsebovati

domain_call_sequence  
conflict_resolution  
aggregation_result  

---

# 7 FINAL DECISION

Final decision vsebuje

decision_action  
execution_flag  

Primer

decision_action = EXECUTE_TRADE  

---

# 8 HASH CHAIN

Decision Context Envelope mora
biti povezan v hash-chain.

fields

previous_decision_hash  
current_decision_hash  

---

# 9 REPLAY REQUIREMENT

Replay mora omogočati

- ponovno izvajanje odločitve
- preverjanje determinističnega izida.

---

# 10 META INVARIANTS

Envelope mora vedno vsebovati

- world_state_hash
- domain_outputs
- orchestration_trace.

Brez teh elementov
odločitev ni validna.

---

END OF DOCUMENT