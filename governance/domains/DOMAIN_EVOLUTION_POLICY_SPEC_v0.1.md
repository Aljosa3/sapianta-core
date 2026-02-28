# DOMAIN_EVOLUTION_POLICY_SPEC_v0.1

## STATUS
ACTIVE

## LAYER
DOMAIN_GOVERNANCE

## TYPE
EVOLUTION_POLICY_SPECIFICATION

## VERSION
0.1

---

# 1. PURPOSE

Ta dokument formalizira parametrični evolucijski režim domen v sistemu SAPIANTA.

Določa:

- pogoje za prilagoditev uteži
- pogoje za predlaganje novih metrik
- klasifikacijo sprememb
- approval pragove
- replay regresijsko disciplino

Evolution Policy regulira nadzorovano adaptacijo domene
brez kršenja constitutional invariant.

---

# 2. ONTOLOGICAL POSITION

Evolution Policy je:

- Domain Governance artefakt
- hash-bound
- versioned
- replay-verifiable
- Promotion Gate nadzorovan

Execution Engine ne sme samostojno aktivirati sprememb.

---

# 3. CHANGE CLASSIFICATION LEVELS

Domain evolucija je razdeljena v tri tipe:

## 3.1 WEIGHT_ADJUSTMENT

Sprememba uteži obstoječih metrik.

Ontološki vpliv: NIZEK  
Replay vpliv: OMEJEN  
Approval: DomainAuthority

---

## 3.2 THRESHOLD_ADJUSTMENT

Sprememba threshold parametrov ali penalizacijskih pragov.

Ontološki vpliv: SREDNJI  
Replay vpliv: SREDNJI  
Approval: DomainAuthority + GovernanceReview

---

## 3.3 STRUCTURAL_DOMAIN_CHANGE

Dodajanje ali odstranjevanje metrike.

Ontološki vpliv: VISOK  
Replay vpliv: VISOK  
Approval: DomainAuthority + MetaAuthority

Ta režim se aktivira, ko:

- nova metrika razširi model sveta
- spremeni dimenzionalnost scoring funkcije
- vpliva na interpretacijo zgodovinskih rezultatov

---

# 4. PARAMETRIC EVOLUTION CONTROLS

Vsaka domena mora definirati:

## 4.1 evaluation_window_days

Minimalno obdobje analize performansa.

## 4.2 min_statistical_confidence

Minimalna statistična zanesljivost predloga.

## 4.3 min_performance_delta

Minimalno izboljšanje, ki upravičuje spremembo.

## 4.4 max_weight_shift_per_update

Maksimalni dovoljen premik posamezne uteži.

## 4.5 max_total_weight_drift

Maksimalni kumulativni drift od zadnje stabilne verzije.

## 4.6 cooldown_period_days

Minimalno obdobje med zaporednimi spremembami.

---

# 5. EVOLUTION WORKFLOW

## 5.1 Performance Observation

Execution layer generira performance poročila.

## 5.2 Proposal Generation

Evolution Engine lahko ustvari:

- WEIGHT_UPDATE_PROPOSAL
- THRESHOLD_UPDATE_PROPOSAL
- METRIC_PROPOSAL

Vsak predlog mora biti:

- hash-bound
- verzioniran
- dokumentiran

---

## 5.3 Governance Validation

Promotion Gate klasificira spremembo.

Odvisno od tipa spremembe se sproži ustrezni approval režim.

---

## 5.4 Replay Regression Test

Vsaka sprememba mora prestati:

- zgodovinsko simulacijo
- primerjavo rezultatov
- dokumentirano analizo vpliva

---

# 6. METRIC PROPOSAL REQUIREMENTS

STRUCTURAL_DOMAIN_CHANGE zahteva:

1. Matematično definicijo metrike
2. Deterministični izračun
3. Snapshot skladnost
4. Dokaz neodvisnosti od runtime
5. Korelacijsko analizo z obstoječimi metrikami
6. Regresijsko simulacijo
7. Dokumentirano ontološko utemeljitev

Nova metrika ne sme:

- podvajati obstoječih metrik
- uvajati probabilističnih ocen
- kršiti scope discipline

---

# 7. REPLAY DISCIPLINE

Evolution mora ohraniti:

- možnost ponovitve stare verzije
- verzionirano zgodovino ranking konfiguracij
- transparentno primerjavo med verzijami

Sprememba nikoli ne izbriše preteklega stanja.

---

# 8. META-INVARIANT

Evolution Policy ne sme:

- obiti Promotion Gate
- zmanjšati authority discipline
- uvesti implicitne runtime adaptacije
- omogočiti samodejne aktivacije sprememb

Evolution je vedno governance-nadzorovan proces.

---

END OF DOCUMENT