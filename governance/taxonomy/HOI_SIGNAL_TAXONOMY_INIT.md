# HOI_SIGNAL_TAXONOMY_INIT — HOI Signal Taxonomy

## Status
INIT

## Version
v1.0

## Owner
Human Orientation Interface (HOI)

## Related Governance
- HUMAN_ORIENTATION_SAFEGUARD.md (HOS)
- HOI_MODULE_INIT.md
- HOI_CHAT_INTERACTION_INIT.md

---

## Purpose

Ta dokument definira taksonomijo signalov,
ki jih HOI lahko zazna in obravnava
v kontekstu ohranjanja človeške orientacije
in legitimnosti nadaljevanja sistema.

Taksonomija ne določa implementacije,
temveč semantične meje zaznave.

---

## Definition of Signal

Signal je zaznava sistemskega ali interakcijskega stanja,
ki kaže na potencialno izgubo človeške orientacije
ali možnosti smiselnega ukrepanja.

Signal sam po sebi:
- ni zahteva za spremembo sistema
- ni napaka
- ni sprožilec samogradnje
- ne povzroči avtomatskih sprememb

Signal služi orientaciji in varnosti.

---

## Signal Categories

### 1. ORIENTATION_LOSS

**Opis:**  
Človeški nadzornik ne razume trenutnega stanja sistema
ali pomena tekočega procesa.

**Indikativni vzorci (ne izčrpno):**
- ponavljajoče se zahteve po razlagi
- izrazi nerazumevanja ("ne razumem", "kaj se dogaja")
- razhajanje med razlago in zaznano jasnostjo

**Pomen:**  
Ogrožena legitimnost nadaljevanja brez dodatne orientacije.

---

### 2. ACTION_INABILITY

**Opis:**  
Človeški nadzornik razume stanje,
vendar nima možnosti smiselnega ukrepanja
ali vpliva na nadaljevanje procesa.

**Indikativni vzorci:**
- izrazi nemoči ("ne morem nič narediti")
- odsotnost razpoložljivih odločitev
- nadaljevanje procesa brez človeškega vzvoda

**Pomen:**  
Nadaljevanje brez možnosti ukrepanja ni legitimno.

---

### 3. ORIENTATION_STALL

**Opis:**  
Proces se nadaljuje ali ponavlja,
brez napredka v človeški orientaciji.

**Indikativni vzorci:**
- kroženje po istih temah
- ponavljajoče se razlage brez večje jasnosti
- povečanje kompleksnosti brez orientacijskega učinka

**Pomen:**  
Tveganje tihe blokade ali zdrsa.

---

### 4. EXIT_OBSCURITY

**Opis:**  
Ni jasno, kako ali kam se proces lahko varno preusmeri.

**Indikativni vzorci:**
- odsotnost preusmeritvenih možnosti
- nejasen zaključek ali nadaljevanje
- implicitno siljenje v nadaljevanje

**Pomen:**  
Kršitev Human Orientation Safeguard.

---

## Non-Signals (Explicit)

Naslednje NE predstavljajo HOI signalov:

- nezadovoljstvo z izidom
- želja po boljši optimizaciji
- zahteva po novih zmožnostih
- radovednost ali eksperimentiranje
- napake v vsebini brez izgube orientacije

---

## HOI Obligations Upon Signal

Ko je zaznan kateri koli signal iz te taksonomije,
HOI:

- zahteva orientacijski način
- omogoči ponovno orientacijo
- omogoči varno preusmeritev toka
- ne sproži sprememb sistema
- ne interpretira signala kot zahteve za nadgradnjo

---

## Canonical Principle

Signal obstaja zato,
da prepreči nadaljevanje brez orientacije,
ne zato, da bi pospešil spremembe sistema.

HOI uporablja signale za varovanje človeka,
ne za optimizacijo sistema.
