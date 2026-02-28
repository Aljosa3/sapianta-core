# SAPIANTA_GOVERNANCE_MODEL_v1.0

## STATUS
FROZEN

## LAYER
CONSTITUTIONAL

## TYPE
GOVERNANCE_MODEL

## VERSION
1.0

---

# 1. PURPOSE

Ta dokument formalno definira Governance Model sistema SAPIANTA,
vključno z:

- Constitutional Layer
- Domain Governance
- Controlled Optimization
- Authority Structure
- Guardrails
- Latent MetaAuthority Capability

Dokument je replay-verifiable in velja kot ustavni artefakt.

---

# 2. CONSTITUTIONAL LAYER (LAYER 0)

## 2.1 Ontološke invariante

Naslednje invariante so nekršljive:

1. Determinism
2. Hash-bound artifacts
3. Replay verifiability
4. Signature chain integrity
5. Promotion boundary enforcement
6. Human sovereign authority

Sprememba teh invariant zahteva ustavni postopek.

---

## 2.2 Global Sovereignty Root

Sistem vsebuje ustavni vrh (SovereigntyRoot), ki:

- določa obstoj AuthorityPolicy kot governance artefakta
- preprečuje preseganje DomainAuthority preko globalnih invariant
- varuje Layer 0 pred domenskimi posegi

MetaAuthority je arhitekturno predvidena, vendar ni nujno aktivirana.

---

# 3. DOMAIN GOVERNANCE MODEL

## 3.1 Domain Structure

Vsaka domena vsebuje:

- DomainAuthority
- ThresholdPolicy
- ReportingPolicy
- OptimizableScope
- Domain L2 enforcement
- Domain L3 sandbox

Domene so suverene znotraj svojega definiranega Scope.

---

## 3.2 DomainAuthority

DomainAuthority:

- je governance artefakt
- je hash-bound
- je verzioniran
- je podpisno potrjen

Možni načini:

- SINGLE_SIGN
- MULTI_SIGN_M_OF_N

DomainAuthority ne sme:

- razširiti svojega Scope brez višje odobritve
- redefinirati globalnih invariant
- spremeniti lastnega AuthorityModel brez governance postopka

---

## 3.3 Authority Scope Containment (GUARDRAIL 2)

Sprememba domenskega Scope zahteva:

- Global Governance Approval
  ali
- MetaAuthority Approval (če je aktivna)

---

# 4. CONTROLLED OPTIMIZATION MODEL

## 4.1 OptimizableScope

AI lahko avtomatsko optimizira samo parametre, ki:

- ne vplivajo na normativno logiko
- ne vplivajo na legitimnost odločitev
- ne vplivajo na Authority strukturo
- ne vplivajo na replay integriteto

Normativne spremembe so vedno deliberativne.

---

## 4.2 ThresholdPolicy (per domain)

Vsaka domena ima svojo ThresholdPolicy.

ThresholdPolicy:

- je governance artefakt
- je hash-bound
- je podpisno potrjen
- je replay-verifiable

Določa:

- max_change_per_cycle
- max_total_drift
- stability_floor
- cross_metric_guard

L2 enforcement preverja skladnost z veljavno ThresholdPolicy.

---

## 4.3 Drift Integrity Constraint (GUARDRAIL 1)

Vsaka domena mora imeti:

- Baseline Reference Version
- Cumulative Drift Index
- Periodično primerjavo z baseline

Baseline ne sme biti redefiniran brez deliberativne odobritve.

---

## 4.4 Normative Boundary Definition (GUARDRAIL 3)

Sprememba je normativna, če vpliva na:

- odločilno logiko
- legitimnost odločitev
- authority strukturo
- replay integriteto
- validacijska pravila

Vsaka sprememba mora eksplicitno deklarirati svojo kategorijo.

---

# 5. DELIBERATIVE EVOLUTION (LEVEL 3)

LLM:

- generira predloge
- ne legitimira sprememb
- ne uveljavlja pravil

Vsaka normativna sprememba mora:

- postati governance artefakt
- prestati determinism test
- prestati replay test
- prestati promotion gate
- biti podpisno potrjena

Evolution cannot mutate enforcement mid-cycle.
It may only propose a new version for governance review.

---

# 6. META-AUTHORITY (LATENT CAPABILITY)

MetaAuthority:

- potrjuje DomainAuthority definicije
- rešuje meddomenske konflikte
- varuje Layer 0

Formalna aktivacija MetaAuthority je možna ob institucionalni potrebi.

---

# 7. REPORTING & TRANSPARENCY

Vsaka domena ima nastavljivo periodiko poročanja:

- param_changes
- performance_metrics
- drift_summary
- rollback_events
- anomaly_flags

Poročila so:

- hash-bound
- arhivirana
- replay-verifiable

---

# 8. META-INVARIANT

Nobena avtomatska optimizacija ne sme:

- obiti Promotion Gate
- redefinirati AuthorityPolicy
- razširiti Scope
- posegati v Layer 0
- generirati legitimnosti

Suverenost ostaja človeška.

---

END OF DOCUMENT