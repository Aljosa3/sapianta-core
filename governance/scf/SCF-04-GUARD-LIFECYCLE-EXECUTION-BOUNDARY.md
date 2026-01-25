# SCF-04 — GUARD LIFECYCLE: EXECUTION BOUNDARY & DECISION AUTHORITY

## Status
LOCKED — v0.4 CANONICAL  
Spremembe niso dovoljene brez formalne revizije SCF.

---

## ID
SCF-04-GL

## Verzija
v1.0

## Faza
v0.4 — Execution Boundary & Runtime Governance

## Datum
2026-01-25

## Avtor
SAPIANTA — Canonical Governance Layer

---

## 1. NAMEN DOKUMENTA

Ta dokument uvaja **Guard Lifecycle** kot edini dovoljeni
**odločitveni in nadzorni mehanizem** med:

- kanonično normativno plastjo (SCF)
- prihodnjim runtime okoljem
- vsemi potencialnimi oblikami izvajanja ali interakcije modulov

Dokument:
- NE uvaja izvajanja modulov
- NE opisuje runtime arhitekture
- NE dovoljuje aktivacije modulov

Njegov namen je **izključno opredelitev meja odločanja**.

---

## 2. POLOŽAJ GUARD LIFECYCLE V SISTEMU

Guard Lifecycle deluje kot:

> **edini dovoljeni prehodni sloj med deklarativnim in potencialno izvršljivim stanjem**

Nobena oblika:
- izvajanja
- interakcije
- sinergije
- eskalacije

ni dovoljena brez predhodne odločitve Guard Lifecycle.

---

## 3. DEFINICIJA GUARD LIFECYCLE

Guard Lifecycle je:
- formalen,
- determinističen,
- sledljiv
odločitveni proces, ki:

- sprejme zahtevo (intent)
- jo presodi glede na SCF pravila
- vrne normativno odločitev

Guard Lifecycle **ne izvaja dejanj**.
Guard Lifecycle **ne koordinira modulov**.
Guard Lifecycle **ne ustvarja stanja**.

---

## 4. DOVOLJENE ODLOČITVE

Guard Lifecycle lahko vrne izključno eno izmed naslednjih odločitev:

- **ALLOW** — zahteva je normativno dovoljena (brez implicitnega izvajanja)
- **DENY** — zahteva krši SCF in je zavrnjena
- **HOLD** — zahteva je nepopolna ali zahteva kasnejši kontekst

Guard Lifecycle:
- ne sproži dejanj
- ne eskalira
- ne delegira

---

## 5. EXECUTION BOUNDARY (KLJUČNI POJEM v0.4)

Execution Boundary je formalna, še neimplementirana meja, kjer:

- deklarativni sistem *lahko* preide v izvršljivo stanje
- vendar je ta prehod v v0.4 **strogo prepovedan**

Guard Lifecycle:
- zaznava približevanje tej meji
- ne dovoljuje njenega prečkanja

V v0.4:
> **Execution Boundary obstaja samo kot konceptualna meja.**

---

## 6. RAZMERJE DO SCF-03 (MODULE SYNERGY CONSTRAINT)

Guard Lifecycle je **edini normativni organ**, ki lahko presoja,
ali je katerakoli zahteva po sodelovanju modulov
skladna z dokumentom:

> **SCF-03 — MODULE SYNERGY CONSTRAINT**

To pomeni:

- noben modul ne presoja sinergije
- noben runtime sloj ne interpretira sinergije
- nobena sinergijska interakcija ni dovoljena brez Guard presoje

Če zahteva krši katerikoli pogoj SCF-03 → odločitev **DENY**.

---

## 7. PREPOVEDANE FUNKCIJE GUARD LIFECYCLE

Izrecno je prepovedano, da Guard Lifecycle:

- koordinira module
- združuje prispevke modulov
- sprejema končne odločitve namesto sistema
- optimizira cilje
- ustvarja emergentno vedenje
- deluje kot inteligentni agent

Guard Lifecycle ni modul in nikoli ne postane modul.

---

## 8. SLEDLJIVOST IN AUDIT

Vsaka Guard odločitev mora biti:

- eksplicitna
- razložljiva
- retrospektivno sledljiva

Nezabeležena odločitev se šteje kot:
> **nedovoljena odločitev**

---

## 9. RAZMERJE DO PREJŠNJIH FAZ

Ta dokument:
- ne spreminja v0.3 artefaktov
- ne reinterpretira SCF-03
- ne uvaja novih pravic

Deluje izključno kot:
> **odločitvena meja za prihodnje faze (v0.5+)**

---

## 10. ZAKLEP

S tem dokumentom je:

- Guard Lifecycle formalno vzpostavljen kot odločitvena avtoriteta
- Execution Boundary normativno definirana
- vsak prihodnji runtime strogo podrejen SCF

Ta dokument je **kanoničen in zaklenjen**.

---

## KONEC DOKUMENTA
