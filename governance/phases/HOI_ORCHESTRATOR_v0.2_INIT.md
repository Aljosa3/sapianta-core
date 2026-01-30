# HOI ORCHESTRATOR v0.2 — INIT

## Status
INIT  
LOCK-ready (v0.2)  
No execution • No autonomy • No orchestration authority

---

## Purpose

HOI Orchestrator v0.2 predstavlja **razširjeno, a še vedno ne-avtonomno**
interpretacijsko in odgovor-generirajočo plast sistema SAPIANTA.

Njegova naloga je:
- sprejeti **HOI-validiran vhod** iz SAPIANTA_CHAT,
- oblikovati **strukturiran, determinističen, HDS-pripravljen izhod**,
- brez kakršnekoli izvršilne, usmerjevalne ali odločitvene avtoritete.

HOI Orchestrator **ni možgani sistema**, temveč **legitimen glas sistema**
znotraj strogo omejenega v0.x obsega.

---

## Position in System Architecture

Human
↓
SAPIANTA_CHAT (thin: delegator + renderer only)
↓
HOI Orchestrator v0.2
↓
[ Structured Response / HDS-ready Output ]


HOI Orchestrator:
- NI router
- NI planner
- NI executor
- NI decision engine
- NI state holder

---

## Functional Scope (ALLOWED)

HOI Orchestrator v0.2 SME:

### 1. Interpretirati HOI-konformni vhod
- vhod je že legitimiran (HOI boundary satisfied),
- brez ponovne validacije pravil ali zakonov.

### 2. Oblikovati strukturiran odgovor
- jasna semantična segmentacija (npr. `context`, `options`, `notes`),
- deterministična oblika izhoda,
- brez skritega sklepanja ali predpostavk.

### 3. Pripraviti HDS-ready output
- izhod je **pasiven**, a **pripravljen** za morebitno HDS plast,
- brez aktivnega HDS klica,
- brez odločitev namesto človeka.

### 4. Delovati izključno referenčno
- dovoljeno je:
  - povzemanje stanja,
  - razlaga možnosti,
  - strukturiranje informacij.
- izhod je informativen, ne normativen.

---

## Explicit Constraints (NOT ALLOWED)

HOI Orchestrator v0.2 NE SME:

### ❌ Izvajati kakršnokoli akcijo
- noben klic runtime modulov,
- noben side-effect,
- noben zapis, sprememba ali sprožitev.

### ❌ Sprejemati ali predlagati odločitve
- ne izbira optimalne poti,
- ne rangira možnosti kot “pravilne”,
- ne daje priporočil z avtoriteto.

### ❌ Usmerjati tok sistema
- ne kliče drugih podsistemov,
- ne delegira nalog,
- ne izvaja orkestracije.

### ❌ Uvajati stanje ali spomin
- brez akumulacije konteksta,
- brez dolgoročnih sledi,
- brez implicitnega “učenja”.

---

## Invariants

- HOI Orchestrator does not alter system state
- HOI Orchestrator output has no execution semantics
- wiring.py remains the sole system entry path

---

## Output Contract (v0.2)

Izhod HOI Orchestratorja mora biti:

- **popolnoma strukturiran**
- **determinističen**
- **brez implicitne avtoritete**

Primer abstraktne oblike (ne implementacija):

```json
{
  "mode": "REFERENCE_RESPONSE",
  "scope": "HOI_v0.2",
  "content": {
    "context": "...",
    "available_paths": [
      "...",
      "..."
    ],
    "constraints": [
      "..."
    ],
    "notes": "..."
  }
}
