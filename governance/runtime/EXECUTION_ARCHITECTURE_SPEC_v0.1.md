# EXECUTION_ARCHITECTURE_SPEC_v0.1

## STATUS
ACTIVE

## LAYER
RUNTIME_ARCHITECTURE

## TYPE
EXECUTION_SPECIFICATION

## VERSION
0.1

---

# 1. PURPOSE

Ta dokument formalizira deterministično Execution Architecture plast sistema SAPIANTA.

Definira:

- Loop Engine
- Multi-candidate model
- Deterministic Ranking Engine
- Invocation Adapter
- Governance Snapshot Builder
- Promotion Gate Interface
- Authority Interface
- Runtime Boundary Guard
- Execution State Machine

Ta dokument ne redefinira constitutional invariant.
Izvaja jih na implementacijski ravni.

---

# 2. ARCHITECTURAL POSITION

Execution Layer je:

- determinističen
- replay-verifiable
- authority-neutral
- governance-bound

Execution Layer mora ostati funkcionalen tudi brez LLM komponente.

LLM je advisory input generator, ne execution komponenta.

---

# 3. CORE COMPONENTS

## 3.1 Loop Engine

Loop Engine je deterministična komponenta, ki:

- upravlja iteracije
- nadzira termination pogoje
- sproži LLM invocation
- sproži artifact construction
- sproži ranking
- sproži Promotion Gate

Loop Engine nikoli ne delegira nadzora LLM.

---

## 3.2 Governance Snapshot Builder

Pred vsakim LLM invocation:

- deterministično ustvari Governance Snapshot
- snapshot je hash-bound
- snapshot je replay-verifiable
- snapshot je read-only

Snapshot vključuje samo dovoljene governance elemente.

---

## 3.3 Invocation Adapter

Invocation Adapter:

- prejme snapshot
- generira prompt
- izvede LLM klic
- vrne surov output

Adapter ne:

- piše v sistem
- modificira runtime state
- komunicira z Promotion Gate
- komunicira z Authority

---

## 3.4 Multi-Candidate Model

LLM generira K kandidatov.

Artifact Builder:

- normalizira vsak kandidat
- validira strukturo
- izračuna hash
- ustvari deterministične artefakte

Vsak kandidat je hash-bound.

LLM output sam po sebi ni artefakt.

---

## 3.5 Deterministic Ranking Engine

Ranking Engine:

- prejme strukturirane artefakte
- izračuna score za vsak kandidat
- uporabi Domain Ranking Configuration
- vrne deterministično urejen seznam

Ranking mora biti:

- popolnoma determinističen
- brez runtime podatkov
- brez LLM vpliva
- reproducibilen

---

# 4. DOMAIN RANKING CONFIGURATION

Ranking konfiguracija je Domain Governance artefakt.

Vključuje:

- metrike
- uteži
- penalizacije
- prioritetne faktorje

Sprememba ranking konfiguracije je normativna sprememba.

Execution Engine samo izvaja formulo.

---

# 5. PROMOTION GATE INTERFACE

Promotion Gate:

- prejme izbran kandidat
- klasificira spremembo
- določi potrebo po Authority approval

Gate ne ve, ali je kandidat generiral LLM ali človek.

Gate je edina klasifikacijska instanca.

---

# 6. AUTHORITY INTERFACE

Authority:

- podpisuje artefakte
- legitimira spremembe
- nikoli ne prejema inputa neposredno od LLM

LLM nima signature sposobnosti.

---

# 7. RUNTIME BOUNDARY GUARD

Runtime Guard zagotavlja:

- LLM nima filesystem write pravic
- LLM nima runtime memory dostopa
- LLM nima neposrednega Gate dostopa
- LLM nima Authority dostopa
- Snapshot je obvezen

Podatkovni tok je enosmeren:

Snapshot → LLM → Artifact Builder → Ranking → Gate

Ni stranskih poti.

---

# 8. EXECUTION STATE MACHINE

Stanja:

- INIT
- SNAPSHOT_BUILT
- LLM_INVOKED
- CANDIDATES_NORMALIZED
- SCORED
- RANKED
- SELECTED
- CLASSIFIED
- APPROVED / REJECTED
- EXECUTED / TERMINATED

LLM ne more sprožiti stanja.

Prehodi so deterministični.

---

# 9. SCOPE ENGINE

Execution Architecture podpira:

- FILE_SCOPE (aktiviran)
- MODULE_SCOPE (neaktiviran)
- SYSTEM_SCOPE (neaktiviran)

Scope eskalacija zahteva governance override.

Arhitektura je scope-agnostična, aktivacija pa governance-nadzorovana.

---

# 10. REPLAY GUARANTEE

Za vsak execution cikel mora biti možno reproducirati:

- Governance Snapshot hash
- Ranking configuration verzijo
- Candidate artefakte
- Ranking rezultat
- Promotion klasifikacijo
- Authority odločitev

Replay ne zahteva identičnega LLM outputa,
ampak mora reproducirati governance odločitev.

---

# 11. META-INVARIANT

Execution Layer nikoli ne sme:

- redefinirati governance pravil
- razširiti Scope
- spremeniti Authority strukture
- obiti Promotion Gate
- generirati legitimnosti

Execution Layer je implementacijski sloj pod governance nadzorom.

---

END OF DOCUMENT