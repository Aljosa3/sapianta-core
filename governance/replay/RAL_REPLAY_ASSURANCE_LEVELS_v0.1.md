# RAL_REPLAY_ASSURANCE_LEVELS_v0.1

STATUS
ACTIVE

TYPE
GOVERNANCE_SPEC

LAYER
CROSS_LAYER

VERSION
0.1

---

# 1 PURPOSE

Replay Assurance Levels (RAL) definirajo
stopnjo deterministične reproducibilnosti
odločitev v sistemu SAPIANTA.

RAL določa:

- kako natančno mora biti odločitev ponovljiva
- kateri artefakti morajo biti shranjeni
- kakšna odstopanja so dovoljena.

RAL je ključni element za:

- audit
- regulatorni pregled
- znanstveno validacijo odločitev.

---

# 2 REPLAY PRINCIPLE

Vsaka odločitev mora biti
potencialno reproducibilna.

Reprodukcija pomeni:

ponovno izvajanje odločitve
z identičnimi vhodnimi artefakti.

---

# 3 RAL LEVELS

SAPIANTA definira štiri
Replay Assurance Levels.

RAL0  
RAL1  
RAL2  
RAL3  

---

# 4 RAL0 — NON-REPLAYABLE

Opis

Odločitev ni deterministično reproducibilna.

Primer

- eksperimentalni modeli
- razvojni prototipi
- raziskovalni eksperimenti.

Zahteve

minimal logging.

Uporaba

development environment.

---

# 5 RAL1 — INPUT REPLAY

Opis

Odločitev je reproducibilna,
če se ponovno uporabi isti input.

Zahteve

shrani se

input data  
decision parameters  

Ni zahtev za

model snapshot.

Uporaba

manj kritični sistemi.

---

# 6 RAL2 — MODEL REPLAY

Opis

Odločitev mora biti reproducibilna
z identičnim modelom in inputi.

Zahteve

shrani se

input data  
model version  
parameter configuration  

Možna so manjša numerična odstopanja.

Uporaba

večina produkcijskih domen.

---

# 7 RAL3 — FULL DETERMINISTIC REPLAY

Opis

Odločitev mora biti
bit-level reproducibilna.

Zahteve

shrani se

input data  
world_state_hash  
model snapshot  
parameter snapshot  
execution trace  

Replay mora generirati
identičen rezultat.

Uporaba

- kreditne odločitve
- regulatorni sistemi
- institucionalni audit.

---

# 8 RAL REQUIREMENTS

RAL3 zahteva naslednje artefakte.

world_state_hash  
decision_context_envelope  
domain_outputs  
orchestration_trace  

Brez teh artefaktov
RAL3 ni dosežen.

---

# 9 DOMAIN RAL POLICY

Vsaka domena mora
definirati svoj minimalni RAL.

Primer

Trading Domain

RAL2

Credit Domain

RAL3

Research Domain

RAL1

---

# 10 GOVERNANCE

Sprememba RAL nivoja
za domeno je klasificirana kot

GOVERNANCE_CHANGE.

Zahteva

MetaAuthority approval.

---

# 11 META INVARIANTS

SAPIANTA mora vedno
zagotoviti vsaj

RAL1

za vse odločitve.

RAL0 je dovoljen
samo v development okolju.

---

END OF DOCUMENT