# HDS INTERACTION FLOW SKELETON v0.1 — INIT

## Status
INIT  
LOCK-ready (v0.1)  
No execution • No autonomy • No decision authority

---

## Purpose

HDS Interaction Flow Skeleton v0.1 definira **minimalni, kanonični potek
interakcije** med SAPIANTA_CHAT in človekom v FAZI F (*Human-in-the-Loop*).

Dokument:
- opisuje **kako** se informacije prikažejo,
- **kje** je Decision Gate,
- **kaj** so dovoljeni odzivi uporabnika,
- **ne** vsebuje izvajanja ali priporočil.

To je **UI/UX semantični okvir**, ne implementacija.

---

## Preconditions

- Izhod je:
  - HOI-interpretiran,
  - HDS Boundary-normaliziran,
  - skladen s HDS Schema v0.1,
  - preverjen skozi HDS Execution Guard v0.1.
- `hds_ready: true`
- `guard_status: PASS | DEGRADED`

---

## Canonical Interaction Flow

### STEP 0 — Entry (Reference Presentation)
SAPIANTA_CHAT prikaže **strukturiran referenčni povzetek**.

**Vsebina:**
- `context`
- `constraints`
- kratka opomba o ne-avtoritativnosti

**Pravilo:**
- brez vprašanj,
- brez pozivov k akciji.

---

### STEP 1 — Options Disclosure
SAPIANTA_CHAT prikaže **vse razpoložljive poti**.

**Vsebina za vsako pot:**
- identifikator poti (A/B/C),
- kratek opis,
- analitične lastnosti (npr. koraki, čas, pravni vpliv),
- brez rangiranja ali priporočil.

**Pravilo:**
- vse poti so prikazane simetrično,
- nobena pot ni privzeta.

---

### STEP 2 — Analytical Detail (On Demand)
Uporabnik LAHKO zahteva:
- dodatno razlago posamezne poti,
- pojasnilo posledic,
- razčlenitev omejitev.

**Pravilo:**
- sistem odgovarja **opisno**,
- brez normativnega jezika.

---

### STEP 3 — Decision Gate (Mandatory)
SAPIANTA_CHAT jasno označi **točko odločitve**.

**Sistemsko sporočilo (kanonično):**
> “Sistem ne izbere poti.  
> Izberi možnost ali zahtevaš dodatno razlago.”

**Pravilo:**
- brez izbire ni napredovanja,
- brez implicitnih nadaljevanj.

---

### STEP 4 — Human Selection
Uporabnik izrecno:
- izbere eno možnost, ali
- zahteva dodatno razlago, ali
- prekine proces.

**Pravilo:**
- izbira je eksplicitna,
- brez časovnih ali logičnih pritiskov.

---

### STEP 5 — Acknowledgement (Non-Executable)
Sistem potrdi **razumevanje izbire**.

**Vsebina:**
- povzetek izbrane poti,
- opozorilo, da izbira **ne sproži izvrševanja** v tej fazi.

---

## Allowed User Actions

- `REQUEST_DETAILS(option_id)`
- `SELECT_OPTION(option_id)`
- `CANCEL_PROCESS`

---

## Forbidden Flow Behaviors

- avtomatsko nadaljevanje,
- predizbrana pot,
- priporočila ali imperativi,
- skrite preference v jeziku ali postavitvi.

---

## Invariants

- Human-in-the-Loop is mandatory
- No execution semantics
- No authority transfer
- Language remains descriptive
- wiring.py remains the sole system entry path

---

## INIT Completion Criteria

INIT v0.1 je zaključen, ko:
- je potek interakcije enolično definiran,
- so Decision Gate točke eksplicitne,
- dokument je zaklenjen (LOCK).

---

END OF DOCUMENT
