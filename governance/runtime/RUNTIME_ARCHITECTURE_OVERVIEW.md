# RUNTIME ARCHITECTURE OVERVIEW
## Design-Only — v0.5

## Status
DESIGN-ONLY  
Ta dokument ne uvaja kode, izvajanja ali tehničnih mehanizmov.

---

## Namen dokumenta

Ta dokument opisuje **konceptualno arhitekturo runtime sloja** v sistemu SAPIANTA.
Njegov namen je:
- pojasniti **kako bo runtime strukturiran**, preden obstaja,
- določiti **dovoljene tokove** in **meje odgovornosti**,
- zagotoviti skladnost z:
  - SCF-03 (Module Synergy Constraint),
  - SCF-04 (Guard Lifecycle — Execution Boundary),
  - SCF-05 (Runtime Admission Preconditions).

Dokument:
- NE implementira runtime-a,
- NE dovoljuje izvajanja,
- NE opisuje tehničnih podrobnosti.

---

## Temeljno načelo

> Runtime v SAPIANTA **ni izvršilna inteligenca**,  
> temveč **nadzorovan prehodni sloj**, ki deluje izključno
> v okviru Guard Lifecycle odločitev.

Runtime:
- ne sprejema normativnih odločitev,
- ne koordinira modulov,
- ne optimizira ciljev,
- ne interpretira sinergije.

---

## Arhitekturne plasti (conceptual layers)

### 1. Intent Entry Layer
- Sprejme **deklarativno zahtevo (intent)**.
- Zahteva mora imeti identiteto, namen in kontekst (SCF-05).
- Ta plast:
  - ne validira pravil,
  - ne sproža izvajanja,
  - ne sprejema odločitev.

---

### 2. Guard Evaluation Layer
- Zahteva je posredovana **Guard Lifecycle**.
- Guard:
  - presodi skladnost s SCF,
  - vrne odločitev: ALLOW / DENY / HOLD.
- Guard ne izvaja dejanj in ne ustvari stanja.

---

### 3. Admission Gate (Execution Boundary)
- Konceptualna meja, definirana v SCF-04.
- V v0.5:
  - obstaja **samo kot zasnova**,
  - se **ne prečka**.
- Namen:
  - centralizirana kontrola,
  - preprečevanje implicitnih prehodov.

---

### 4. Execution Slot (Hypothetical)
- Predvidena, a **neimplementirana** komponenta.
- Predstavlja potencialno mesto, kjer bi se execution nekoč zgodil.
- V v0.5:
  - ne obstaja,
  - se ne uporablja,
  - se ne testira.

---

### 5. Audit & Trace Layer
- Konceptualni sloj za sledljivost.
- Vsaka zahteva in odločitev:
  - mora biti zabeležena,
  - mora biti retrospektivno razložljiva.
- Ta plast:
  - ne vpliva na tok,
  - ne spreminja odločitev.

---

## Dovoljeni tokovi (design-level)

Dovoljen je izključno naslednji konceptualni tok:
Intent
→ Guard Evaluation
→ Decision (ALLOW / DENY / HOLD)
→ Admission Gate
→ (STOP v v0.5)


V v0.5 se tok **vedno ustavi** pred kakršnimkoli izvajanjem.

---

## Failure & Denial poti

### DENY
- Kršitev SCF pravil (npr. SCF-03).
- Tok se ustavi.
- Ni stranskih učinkov.

### HOLD
- Zahteva je nepopolna ali brez konteksta.
- Tok se začasno ustavi.
- Ni izvajanja.

### Invalid Intent
- Manjka identiteta ali namen.
- Zahteva se zavrne še pred Guard presojo.

---

## Razmerje do sinergije modulov (SCF-03)

Runtime:
- ne združuje prispevkov modulov,
- ne interpretira sinergije,
- ne sprejema kolektivnih odločitev.

Vsaka zahteva, ki vključuje več modulov:
- mora biti presojena s strani Guard Lifecycle,
- mora biti skladna s SCF-03,
- sicer je zavrnjena.

---

## Izrecne prepovedi (veljajo v v0.5)

V fazi v0.5 je prepovedano:
- implementirati runtime komponente,
- dodajati runtime kodo v repozitorij,
- izvajati ali simulirati execution,
- orkestrirati module,
- uvajati optimizacije ali samodejne tokove.

Vsaka kršitev pomeni:
> prezgoden prehod iz zasnove v implementacijo.

---

## Razmerje do naslednjih korakov

Ta dokument služi kot:
- referenca za **Interaction Registry SPEC**,
- osnova za **Guard ↔ Runtime Interface SPEC**,
- predpogoj za **v0.5 COMPLETE**.

Implementacija je dovoljena šele v prihodnjih fazah
po ločeni avtorizaciji.

---

## Konec dokumenta
