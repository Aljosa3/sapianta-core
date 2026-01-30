# HDS BOUNDARY v0.1 — INIT

## Status
INIT  
LOCK-ready (v0.1)  
No execution • No autonomy • No decision authority

---

## Purpose

HDS Boundary v0.1 definira **formalno mejo** med
referenčnim, ne-avtonomnim izhodom HOI Orchestratorja
in potencialnimi prihodnjimi HDS funkcionalnostmi.

V tej fazi HDS Boundary:
- **ne izvaja HDS**,  
- **ne sprejema odločitev**,  
- **ne vpliva na tok sistema**,  
temveč zgolj **validira in normalizira izhodno obliko**, ki je *HDS-ready*.

---

## Position in System Architecture

Human
↓
SAPIANTA_CHAT (thin interface)
↓
HOI Orchestrator v0.2 (reference-only output)
↓
HDS Boundary v0.1
↓
[ Normalized / Passive HDS-Ready Structure ]


HDS Boundary:
- ni aktivni HDS,
- ni odločilni sloj,
- nima povratnega vpliva na HOI ali Chat.

---

## Functional Scope (ALLOWED)

HDS Boundary v0.1 SME:

### 1. Sprejeti izhod HOI Orchestratorja
- izhod je že HOI-konformen,
- brez ponovne interpretacije vsebine.

### 2. Normalizirati strukturo
- preveri skladnost s pričakovano shemo,
- odpravi strukturne nedoslednosti (če obstajajo),
- brez semantičnih sprememb.

### 3. Označiti izhod kot HDS-ready
- dodajanje **metapodatkov** (npr. `hds_ready: true`),
- brez aktivacije HDS logike.

### 4. Delovati povsem pasivno
- brez stranskih učinkov,
- brez sprožitev,
- brez povratnih klicev.

---

## Explicit Constraints (NOT ALLOWED)

HDS Boundary v0.1 NE SME:

### ❌ Izvajati HDS logiko
- nobeno rangiranje možnosti,
- nobeno priporočilo,
- nobena optimizacija.

### ❌ Sprejemati ali sugerirati odločitve
- ne izbira poti,
- ne predlaga “najboljše” rešitve,
- ne ocenjuje pravilnosti.

### ❌ Vplivati na sistemski tok
- ne kliče drugih modulov,
- ne delegira nalog,
- ne spreminja stanja.

### ❌ Uvajati stanje ali spomin
- brez akumulacije konteksta,
- brez učenja,
- brez zgodovine.

---

## Invariants

- HDS Boundary does not execute decisions
- HDS Boundary does not introduce authority
- HDS Boundary output is passive and informational
- wiring.py remains the sole system entry path

---

## Output Contract (v0.1)

Izhod HDS Boundary mora biti:

- **strukturno normaliziran**
- **semantično nespremenjen**
- **brez izvršilne vrednosti**

Primer abstraktne oblike:

```json
{
  "mode": "HDS_READY_REFERENCE",
  "scope": "HDS_BOUNDARY_v0.1",
  "hds_ready": true,
  "content": {
    "...": "..."
  }
}
