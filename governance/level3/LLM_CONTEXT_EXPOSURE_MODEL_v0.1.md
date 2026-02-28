# LLM_CONTEXT_EXPOSURE_MODEL_v0.1

## STATUS
ACTIVE

## LAYER
LEVEL_3

## TYPE
ARCHITECTURE_SPECIFICATION

## VERSION
0.1

---

# 1. PURPOSE

Ta dokument formalizira ontološki in arhitekturni položaj LLM komponente
znotraj sistema SAPIANTA.

Definira:

- Kaj LLM lahko vidi
- Česa LLM ne sme videti
- Kako je kontekst izpostavljen
- Kako se ohranja deterministična integriteta
- Kako se zagotavlja replay-verifiability

Ta dokument ne spreminja constitutional invariant.

---

# 2. ONTOLOGICAL POSITION

LLM je:

> Snapshot-conditioned, non-authoritative suggestion function.

LLM NI:

- sistemski akter
- izvršilni agent
- authority entiteta
- legitimacijski mehanizem
- runtime participant

LLM je strogo advisory komponenta.

---

# 3. CONTEXT EXPOSURE PRINCIPLE

LLM ne sme imeti neposrednega dostopa do:

- runtime state
- execution memory
- authority payloads
- signature podatkov
- mutable sistemskih struktur
- production filesystem

LLM lahko vidi samo deterministično generiran snapshot.

---

# 4. DETERMINISTIC GOVERNANCE SNAPSHOT

Pred vsakim LLM invocation mora sistem ustvariti:

Governance Snapshot, ki:

- je deterministično generiran
- je hash-bound
- je replay-verifiable
- je read-only
- je minimalno potreben

Snapshot lahko vključuje:

- relevantne governance dokumente
- veljavni OptimizableScope
- veljavni ThresholdPolicy
- deklarirane omejitve
- prejšnje hash-bound artefakte
- scope klasifikacijo

Snapshot ne sme vključevati:

- runtime execution state
- nevalidiranih predlogov
- authority podpisov
- mutable podatkov

---

# 5. INVOCATION BOUNDARY

LLM se kliče izključno preko:

Sandbox Invocation Adapter-ja.

Adapter:

- prejme snapshot
- ustvari prompt
- izvede LLM klic
- vrne surov output
- ne piše v sistem

LLM nima dostopa do filesystem write operacij.

---

# 6. ARTIFACT CONSTRUCTION DISCIPLINE

LLM output ni artefakt.

Deterministic Artifact Builder:

- validira strukturo
- normalizira format
- izračuna hash
- ustvari governance artefakt

LLM nikoli ne generira hash-a.
LLM nikoli ne generira signature request-a.

---

# 7. LOOP INTERACTION MODEL

Loop Engine je determinističen.

LLM:

- ne nadzira števila iteracij
- ne nadzira termination pogojev
- ne nadzira scope eskalacije
- ne nadzira threshold sprememb

Loop Engine nadzira:

- iteration count
- stop conditions
- drift evaluation
- candidate ranking
- escalation logic

LLM je funkcijski klic znotraj deterministične zanke.

---

# 8. REPLAY GUARANTEE

Za vsak LLM invocation mora biti možno reproducirati:

- snapshot hash
- prompt
- LLM output
- artifact construction proces

Replay ne zahteva identičnega LLM output-a,
ampak mora reproducirati:

- snapshot stanje
- klasifikacijski rezultat
- governance odločitev

---

# 9. META-INVARIANT

LLM nikoli ne sme:

- pridobiti authority
- neposredno komunicirati s Promotion Gate
- spremeniti Scope
- redefinirati ThresholdPolicy
- vplivati na Layer 0

LLM je vedno podrejen governance in enforcement sloju.

---

# 10. ARCHITECTURAL IMPLICATION

Execution Isolation mora zagotoviti:

- strogo ločitev med Advisory Plane in Deterministic Core
- enosmeren tok podatkov (Snapshot → LLM → Artifact Builder)
- prepoved stranskih poti
- popolno odstranljivost LLM komponente brez vpliva na sistem

Sistem mora ostati funkcionalen tudi brez LLM.

---

END OF DOCUMENT