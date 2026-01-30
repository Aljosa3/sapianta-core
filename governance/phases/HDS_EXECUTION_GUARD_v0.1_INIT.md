# HDS EXECUTION GUARD v0.1 — INIT

## Status
INIT  
LOCK-ready (v0.1)  
No execution • No autonomy • No decision authority

---

## Purpose

HDS Execution Guard v0.1 definira **zaščitni mehanizem**,
ki zagotavlja, da noben izhod, označen kot *HDS-ready*,
ne preseže pogodbeno dovoljenih meja (HDS Schema / Contract).

Guard:
- **ne izvaja HDS**,
- **ne sprejema odločitev**,
- **ne vpliva na sistemski tok**,  
temveč **blokira, degradira ali zavrne** neveljavne izhode
na podlagi formalnih pravil.

---

## Position in System Architecture

Human
↓
SAPIANTA_CHAT (thin interface)
↓
HOI Orchestrator v0.2 (reference-only)
↓
HDS Boundary v0.1 (passive normalization)
↓
HDS Schema / Contract v0.1 (typed data)
↓
HDS Execution Guard v0.1
↓
[ Guarded, Non-Executable Output ]


HDS Execution Guard:
- nima povratnega vpliva navzgor,
- ne aktivira drugih modulov,
- deluje izključno kot **enostranska zaščita**.

---

## Guard Scope

Guard se uporablja za:
- vse izhode z `hds_ready: true`,
- vse prihodnje HDS integracije,
- vse točke pred potencialnim odločanjem.

Guard se **ne uporablja** za:
- HOI interpretacijo,
- HDS Boundary normalizacijo,
- runtime orkestracijo.

---

## Allowed Guard Actions

HDS Execution Guard v0.1 SME izključno:

### 1. Validate
- preveri skladnost izhoda s HDS Schema v0.1,
- zazna prepovedane elemente (score, priporočila, akcije).

### 2. Degrade
- odstrani ali anonimizira **prepovedane segmente**,
- ohrani dovoljeno strukturo,
- označi izhod kot `guard_degraded: true`.

### 3. Reject
- zavrne izhod, ki ga ni možno varno degradirati,
- vrne **neizvršilen, informativen guard response**.

> Guard **nikoli** ne popravlja semantike,  
> temveč samo **uveljavlja meje**.

---

## Explicit Constraints (NOT ALLOWED)

HDS Execution Guard v0.1 NE SME:

### ❌ Izvajati HDS ali odločanje
- noben ranking,
- nobeno priporočilo,
- nobena optimizacija.

### ❌ Spreminjati sistemski tok
- ne kliče drugih modulov,
- ne sproža ponovitev,
- ne delegira.

### ❌ Uvajati stanje ali spomin
- brez zgodovine,
- brez učenja,
- brez trajnih zapisov.

---

## Invariants

- Guard enforces contracts, not behavior
- Guard has no execution semantics
- Guard introduces no authority
- Guard actions are deterministic
- wiring.py remains the sole system entry path

---

## Guard Outcomes (Abstract)

Dovoljeni izidi Guard-a:

```json
{
  "guard_status": "PASS | DEGRADED | REJECTED",
  "scope": "HDS_EXECUTION_GUARD_v0.1",
  "notes": "informational only"
}
