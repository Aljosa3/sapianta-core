# HOI_SURFACE_ADAPTER_COMPLIANCE_HARNESS_v0.42_LOCK

STATUS: LOCKED  
PHASE: v0.42  
SCOPE: HOI Surface Adapter Compliance Harness  
MUTABILITY: IMMUTABLE  

DEPENDENCIES:
- v0.34 — Decision Preview Presentation Schema (LOCKED)
- v0.35 — Validator Enforcement (LOCKED)
- v0.36 — Runtime Integration Contract (LOCKED)
- v0.37 — Failure Propagation & Audit Semantics (LOCKED)
- v0.38 — Audit Event Schema (LOCKED)
- v0.39 — Audit Index & Sanity-Check (LOCKED)
- v0.40 — Decision Preview Exposure / Surface Contract (LOCKED)
- v0.41 — Surface Adapter Contract (LOCKED)

EXPLICIT NON-DEPENDENCIES:
- samogradnja modulov
- runtime odločanje
- enforcement mehanizmi
- surface implementacije
- UX ali razvojna orodja

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **Compliance Harness** za surface adapterje v HOI.

Namen faze v0.42 je:
- zagotoviti **objektivno preverljivost** skladnosti surface adapterjev z v0.40 in v0.41,
- zaznati kršitve brez posega v runtime tok,
- preprečiti, da bi **zaznava skladnosti** postala vir signalov za odločanje ali samogradnjo.

Dokument:
- ne izvaja enforcementa,
- ne uvaja novih semantičnih pravil,
- ne vpliva na odločanje,
- deluje izključno kot **audit-only dokazna plast**.

---

## 2. DEFINICIJA COMPLIANCE HARNESA

Compliance Harness je **opazovalna, pasivna in deterministična plast**, namenjena preverjanju skladnosti surface adapterjev.

Harness:
- ni validator,
- ni runtime komponenta,
- ni surface adapter,
- ni vir resnice.

Njegova vloga je **zaznava**, ne **ukrepanje**.

---

## 3. NORMATIVNI OBSEG

v0.42 normativno ureja:
- vlogo in meje Compliance Harnessa,
- tipologijo kršitev,
- pravila zaznave kršitev,
- prepoved vpliva zaznave na druge faze.

Izrecno izven obsega:
- implementacija preverjanj,
- korekcija adapterjev,
- runtime interakcije,
- samodejno popravljanje,
- gradnja modulov.

---

## 4. TEMELJNA NAČELA HARNESA

Compliance Harness mora delovati skladno z naslednjimi načeli:

- **Pasivnost**  
  Ne posega v tok izvajanja.

- **Ne-intervencija**  
  Ne sproža dejanj ali odločitev.

- **Determinističnost**  
  Enaki vhodni artefakti → enaki zaznavni izidi.

- **Ne-interpretativnost**  
  Ne sklepa o pomenu zaznanih kršitev.

- **Ne-signaliziranje**  
  Ne ustvarja uporabnih signalov za druge faze.

---

## 5. RAZMERJE MED HARNESOM IN SURFACE ADAPTERJEM

5.1 Harness lahko surface adapter **opazuje**, ne sme pa nanj vplivati.  
5.2 Prepovedan je vsak povratni signal proti adapterju.  
5.3 Prepovedana je kakršnakoli korekcija ali prilagoditev adapterja.  
5.4 Harness ne sme spreminjati pogojev izpostavitve.

---

## 6. RAZMERJE MED HARNESOM IN v0.40 / v0.41

6.1 Harness preverja skladnost z v0.40 in v0.41.  
6.2 Harness ne razširja, ne reinterpretira in ne nadomešča pravil teh faz.  
6.3 Zaznava neskladnosti ne spremeni pravil izpostavitve ali vloge adapterja.

---

## 7. TIPOLOGIJA KRŠITEV (CLASS OF VIOLATIONS)

Compliance Harness lahko zazna naslednje razrede kršitev:

- interpretacija izpisa,
- obogatitev ali transformacija izpisa,
- selektivna projekcija,
- povratni signal v runtime,
- surface-only pravila ali stanja,
- kršitev NON-SIGNAL RULE iz v0.41.

Zaznava kršitve ne implicira ukrepanja.

---

## 8. PRAVILA ZAZNAVE KRŠITEV

8.1 Zaznava temelji izključno na **artefaktih**.  
8.2 Prepovedano je:
- časovno sklepanje,
- frekvenčno sklepanje,
- korelacijsko sklepanje,
- kontekstualno sklepanje.

8.3 Harness ne sme rekonstruirati namena ali vzroka kršitve.

---

## 9. SAMOGRADBENI GUARD — HARNESS LEVEL (META NON-SIGNAL RULE)

Compliance Harness **ne sme biti uporabljen kot vir signalov** za:
- gradnjo modulov,
- učenje sistema,
- prilagajanje strategij,
- kakršnokoli odločanje.

Izrecno je prepovedano:
- sklepanje iz števila zaznanih kršitev,
- sklepanje iz zaporedja zaznav,
- sklepanje iz časa zaznave,
- sklepanje iz odsotnosti zaznave,
- uporaba compliance izidov kot vhod v gradbene faze.

Rezultati harnessa so **izključno audit-only artefakti**.

---

## 10. NO-ADAPTER / NO-HARNESS STANJE

10.1 Odsotnost surface adapterja ali harnessa je veljavno stanje.  
10.2 Prepovedano je nadomestno ali kompenzacijsko vedenje.  
10.3 Tišina je normativno pravilno stanje.

---

## 11. MACHINE-CHECKABLE COMPLIANCE KRITERIJI

Skladnost z v0.42 mora biti preverljiva glede:

- pasivnosti delovanja,
- ne-intervencije,
- odsotnosti signaliziranja,
- ločitve od samogradnje,
- spoštovanja faznih mej.

Vsaka ugotovljena kršitev pomeni neskladnost z v0.42.

---

## 12. PHASE BOUNDARY CLAUSE (v0.42)

Ta faza:
- ne uvaja enforcementa,
- ne uvaja implementacij,
- ne posega v runtime tok,
- ne posega v samogradnjo.

Vse navedeno sodi izven obsega v0.42 in mora biti urejeno v kasnejših fazah.

---

## 13. SKLADNOST, ZAKLEP IN NEPOVRATNOST

Ta dokument:
- je skladen z v0.34–v0.41,
- ne razširja njihove semantike,
- ne uvaja novih odločitev.

Dokument **HOI_SURFACE_ADAPTER_COMPLIANCE_HARNESS_v0.42_LOCK.md** je s tem
**DOKONČNO ZAKLENJEN** in se ne sme več spreminjati.

---
