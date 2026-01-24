# GUARD LIFECYCLE — CANONICAL PROTOCOL
Version: 1.0
Status: DRAFT (pre-lock)
Scope: Runtime orchestration
Authority: SCF-aligned

---

## 1. Namen dokumenta

Ta dokument definira **kanonični GuardLifecycle protokol** kot
obvezno orkestracijsko plast med katerimkoli vstopom v sistem
in katerokoli obliko izvedbe, odločitve ali izhoda.

GuardLifecycle:
- NI vir normativnih odločitev
- NE vsebuje pravil
- NE interpretira SCF
- JE edina dovoljena vstopna točka za izvedbo

---

## 2. Definicija GuardLifecycle

GuardLifecycle je **determinističen, obvezen orkestracijski tok**, ki:

- sprejme vse zahteve (CLI, API, Chat, Dry-run, internal)
- inicializira ExecutionContext
- zaporedno kliče obstoječe avtoritativne guard/gate komponente
- zagotovi, da ni mogoče:
  - spremeniti Status
  - spremeniti Phase
  - sprožiti execution
  brez tega protokola

GuardLifecycle sam **ne odloča**, temveč uveljavlja zaporedje.

---

## 3. Obvezna vstopna točka (GL-1, GL-2)

Vsaka zahteva MORA vstopiti skozi GuardLifecycle.

Prepovedano je:
- neposredno klicati:
  - runtime orchestratorje
  - execution use-case funkcije
  - dry-run engine
  - chat orchestrator
- ustvarjati alternativne entry-pointe

Vsi tokovi so definirani kot **execution modes**, ne kot ločene poti.

---

## 4. ExecutionContext inicializacija

Ob vstopu GuardLifecycle MORA:

- ustvariti nov ExecutionContext
- nastaviti:
  - source
  - execution_mode
  - raw_input
  - timestamp
- inicialno:
  - Status = PENDING
  - Phase = INIT

Brez obstoječega ExecutionContext ni dovoljeno nadaljevanje.

---

## 5. Zaporedje GuardLifecycle faz

GuardLifecycle MORA izvesti naslednje faze v točno tem vrstnem redu:

### Faza 1 — Structural Admission
- preveri modul / kontekst (če relevantno)
- zavrne nadaljevanje ob neveljavnem stanju

### Faza 2 — Runtime Guards
- kliče avtoritativne runtime guards
- EDINI dovoljeni vir:
  - Status.ALLOW
  - Phase.EXECUTION

### Faza 3 — Normativni SP prehodi
- zaporedno kliče SP-passe (1,2,3,5,8 …)
- ob prvi zavrnitvi se tok ustavi

### Faza 4 — Execution Gate
- preveri execution intent
- preveri zahteve po:
  - human confirmation
  - SEAL statusu
- če ni izpolnjeno → DENY ali HOLD

### Faza 5 — Delegacija izvedbe
- šele po uspešnem prehodu vseh faz
- delegira na ustrezni execution mode handler

### Faza 6 — Finalization & Audit
- nastavi:
  - Phase = FINAL
  - Status = FINAL / DENY / HOLD
- sproži audit trail (ne glede na izid)

---

## 6. Execution Modes (GL-4)

GuardLifecycle razlikuje **načine izvedbe**, ne poti:

- EXECUTION
- DRY_RUN
- CHAT

Razlike med njimi:
- vplivajo na:
  - dovoljene side-effecte
  - vrsto rezultata
- NE vplivajo na:
  - guard zaporedje
  - varnost
  - normativne zahteve

---

## 7. Prepoved normativne avtoritete (GL-3)

GuardLifecycle:
- NE sme:
  - odločati ALLOW / DENY
  - interpretirati pravil
  - spreminjati SCF semantike
- SME:
  - klicati zunanje guard komponente
  - zbirati njihove rezultate
  - ustaviti tok ob zavrnitvi

Vsaka odločitev mora biti sledljiva do zunanjega vira.

---

## 8. Končnost in audit (GL-5)

Brez zaključenega GuardLifecycle:
- ni dovoljeno:
  - vrniti rezultata
  - zaključiti tok
  - skriti zavrnitev

Audit trail je:
- obvezen
- neodvisen od izida
- neblokirajoč

---

## 9. Kršitve protokola

Vsaka izvedba, ki:
- obide GuardLifecycle
- ustvari execution brez Status.ALLOW
- zaključi tok brez audit zapisa

je **neveljavna izvedba** in predstavlja kršitev sistema.

---

## 10. Status dokumenta

Ta protokol:
- služi kot:
  - arhitekturni lock
  - testna osnova
  - SCF razširitev
- mora biti zaklenjen pred implementacijo orchestrator wrapperja
