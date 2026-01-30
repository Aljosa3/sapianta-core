# HDS INTERACTION SEMANTICS v0.1 — INIT

## Status
INIT  
LOCK-ready (v0.1)  
No execution • No autonomy • No decision authority

---

## Purpose

HDS Interaction Semantics v0.1 definira **dovoljeno semantiko interakcije**
med sistemom SAPIANTA in človekom v fazi *Human-in-the-Loop*.

Cilj dokumenta je:
- omogočiti **analitično razkritje lastnosti poti** (vključno z optimalnostjo),
- izrecno **ločiti analizo od odločitve**,
- zagotoviti, da sistem **ne izvaja normativnega vpliva**.

Ta dokument ureja **jezik in pomen**, ne izvajanja.

---

## Position in System Architecture

Human
↓
SAPIANTA_CHAT (interaction UI)
↓
wiring.py
↓
HOI Orchestrator v0.2 (reference analysis)
↓
HDS Boundary v0.1 (normalization)
↓
HDS Schema / Contract v0.1 (typed data)
↓
HDS Execution Guard v0.1 (contract enforcement)
↓
HDS Interaction Semantics v0.1
↓
[ Human Decision Gate — explicit choice required ]


HDS Interaction Semantics:
- ne spreminja toka,
- ne sprejema odločitev,
- ne izvaja dejanj.

---

## Core Principle

**System may analyze.  
Human decides.**

Sistem lahko razkrije analitične lastnosti možnosti,
vendar **nikoli** ne prevzame avtoritete nad izbiro.

---

## Allowed Semantics (PERMITTED)

HDS Interaction Semantics v0.1 DOVOLJUJE:

### 1. Deskriptivno analitiko poti
Sistem SME opisati:
- število korakov,
- pravne zahteve,
- časovne posledice,
- zaznana tveganja,
- omejitve in predpogoje.

Primer (dovoljeno):
> “Možnost B zahteva najmanj pravnih korakov.”  
> “Možnost C podaljša postopek zaradi dodatnih preverjanj.”

---

### 2. Analitično razkritje optimalnosti (nenormativno)
Sistem SME navesti **analitično ugotovljene lastnosti**, ki so
pogosto povezane z optimalnostjo, **brez priporočila**.

Primer (dovoljeno):
> “Na podlagi znanih omejitev ima možnost B manj zaznanih zapletov v nadaljnjih fazah.”

Opomba:
- izraz “optimalno” je dovoljen **le deskriptivno**, nikoli kot ukaz.

---

### 3. Razlago posledic izbire
Sistem SME razložiti:
- kaj sledi po vsaki izbiri,
- kateri dodatni podatki so potrebni,
- kje se proces zaključi ali nadaljuje.

---

### 4. Eksplicitni Decision Gate
Sistem MORA jasno označiti točko, kjer:
- je potrebna **človeška izbira**,
- brez izbire **ni napredovanja**.

Primer:
> “Sistem ne izbere poti. Izberi možnost ali zahtevaj dodatno razlago.”

---

## Forbidden Semantics (STRICTLY NOT ALLOWED)

HDS Interaction Semantics v0.1 STROGO PREPOVEDUJE:

### ❌ Normativno priporočanje
- “priporočamo”,
- “najboljša izbira”,
- “izberi” (brez človekove pobude),
- kakršenkoli imperativni ton.

---

### ❌ Rangiranje z avtoriteto
- score, uteži, točke,
- verjetnosti uspeha,
- implicitno vrednotenje (“boljše/slabše”) kot zaključek.

---

### ❌ Skrita odločitev
- avtomatsko nadaljevanje brez izbire,
- predizbrana pot,
- privzeta odločitev brez potrditve.

---

## Language Constraints

Dovoljen je **opisni jezik**.  
Prepovedan je **normativni jezik**.

| Tip jezika | Status |
|-----------|--------|
| Opis posledic | DOVOLJEN |
| Analitični vpogled | DOVOLJEN |
| Priporočilo | PREPOVEDANO |
| Ukaz | PREPOVEDANO |

---

## Invariants

- System analyzes; human decides
- No execution semantics introduced
- No authority or autonomy added
- All interaction remains auditable
- wiring.py remains the sole system entry path

---

## INIT Completion Criteria

INIT v0.1 je zaključen, ko:
- je semantična meja jasno definirana,
- je normativni jezik izrecno prepovedan,
- je dokument zaklenjen (LOCK).

---

END OF DOCUMENT
