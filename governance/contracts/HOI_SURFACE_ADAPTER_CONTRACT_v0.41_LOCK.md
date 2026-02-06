# HOI_SURFACE_ADAPTER_CONTRACT_v0.41_LOCK

STATUS: LOCKED  
PHASE: v0.41  
SCOPE: HOI Surface Adapter Contract  
MUTABILITY: IMMUTABLE  

DEPENDENCIES:
- v0.34 — Decision Preview Presentation Schema (LOCKED)
- v0.35 — Validator Enforcement (LOCKED)
- v0.36 — Runtime Integration Contract (LOCKED)
- v0.37 — Failure Propagation & Audit Semantics (LOCKED)
- v0.38 — Audit Event Schema (LOCKED)
- v0.39 — Audit Index & Sanity-Check (LOCKED)
- v0.40 — Decision Preview Exposure / Surface Contract (LOCKED)

EXPLICIT NON-DEPENDENCIES:
- CLI
- API
- GUI
- UX
- implementacijski mehanizmi

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **Surface Adapter Contract** za HOI.

Namen faze v0.41 je formalno opredeliti:
- kaj *surface adapter* je,
- kakšne so njegove obveznosti,
- katere so njegove absolutne prepovedi.

Dokument:
- ne uvaja novih semantičnih pravil,
- ne uvaja odločevalne logike,
- ne uvaja pravil gradnje modulov,
- ne razširja pravil izpostavitve iz v0.40.

v0.41 je **ustavna faza**, ki loči:
- *izpostavitev* (v0.40)
od
- *obstoja in vloge površine*.

---

## 2. FORMALNA DEFINICIJA SURFACE ADAPTERJA

Surface adapter je **ontološko ločena entiteta**, katere edina vloga je:
- enosmerna projekcija že dovoljenega izpisa na površino.

Surface adapter:
- ni runtime komponenta,
- ni surface instanca,
- ni vir resnice.

Adapter je **projektor**, ne procesor.

---

## 3. NORMATIVNI OBSEG

Ta faza normativno ureja:
- obstoj surface adapterja,
- njegove obveznosti,
- njegove prepovedi.

Izrecno izven obsega so:
- definicija konkretnih površin,
- vedenje posameznih vmesnikov,
- interakcije z uporabnikom,
- implementacije,
- mehanizmi gradnje modulov.

---

## 4. TEMELJNA NAČELA SURFACE ADAPTERJA

Surface adapter mora delovati skladno z naslednjimi načeli:

- **Pasivnost**  
  Adapter ne uvaja dejanj.

- **Enosmernost**  
  Adapter nima povratnega vpliva.

- **Ne-interpretativnost**  
  Adapter ne razume pomena izpisa.

- **Deterministična projekcija**  
  Isti vhod povzroči isti izhod.

- **Ne-učljivost**  
  Adapter se ne spreminja na podlagi uporabe.

---

## 5. OBVEZNOSTI SURFACE ADAPTERJA

Surface adapter je obvezan:

5.1 delovati izključno na podlagi runtime dovoljenja,  
5.2 v celoti spoštovati v0.40 Exposure Contract,  
5.3 projicirati izpis kot nedeljivo celoto,  
5.4 ne izvajati selekcije ali filtriranja,  
5.5 ne izvajati ponovnega izračuna ali transformacije.

---

## 6. ABSOLUTNE PREPOVEDI (NEGATIVE CAPABILITIES)

Surface adapter **ne sme**:

- interpretirati izpisa,
- obogatiti izpisa,
- normalizirati izpisa,
- razčlenjevati izpisa,
- uvajati surface-only pravil,
- ustvarjati surface-only stanj,
- sprejemati surface-only odločitev.

Vsaka taka funkcija predstavlja kršitev v0.41.

---

## 7. RAZMERJE MED SURFACE ADAPTERJEM IN RUNTIME

7.1 Surface adapter je strogo podrejen runtime odločitvam.  
7.2 Adapter ne sme signalizirati nazaj v runtime.  
7.3 Adapter ne sme vplivati na prihodnje odločitve.  
7.4 Adapter ne sme opazovati ali sklepati o procesu odločanja.

---

## 8. RAZMERJE MED SURFACE ADAPTERJEM IN v0.40

Surface adapter:
- izvaja izključno pravila v0.40,
- jih ne razširja,
- jih ne reinterpretira.

NO-OUTPUT stanje iz v0.40 mora biti spoštovano brez nadomestnega vedenja.

---

## 9. SURFACE ADAPTER KOT ZAMENLJIVA KOMPONENTA

9.1 Noben surface adapter ni privilegiran.  
9.2 Ne obstaja referenčna ali kanonična površina.  
9.3 Vsi adapterji so normativno enakovredni.  
9.4 Zamenjava adapterja ne sme vplivati na pomen izpisa.

---

## 10. SAMOGRADBENI GUARD — NON-SIGNAL RULE

Surface adapter **ne sme biti uporabljen kot vir signalov** za:
- gradnjo modulov,
- učenje sistema,
- sprejemanje odločitev.

Izrecno je prepovedano:
- branje zaporedja izpostavitev,
- branje pogostosti izpostavitev,
- sklepanje iz prisotnosti ali odsotnosti adapterja.

Surface adapter je za gradnjo **normativno slepa plast**.

---

## 11. NO-SURFACE STANJE

11.1 Odsotnost surface adapterja je veljavno stanje.  
11.2 Prepovedano je nadomestno ali fallback vedenje.  
11.3 Tišina na površini je legitimna in normativno pravilna.

---

## 12. MACHINE-CHECKABLE PRAVILA SKLADNOSTI

Skladnost z v0.41 mora biti preverljiva glede:

- enosmernosti delovanja,
- pasivnosti adapterja,
- odsotnosti interpretacije,
- spoštovanja NON-SIGNAL RULE.

Vsaka zaznana kršitev pomeni neskladnost faze.

---

## 13. PHASE BOUNDARY CLAUSE (v0.41)

Ta faza:
- ne definira konkretnih adapterjev,
- ne definira tehnologij,
- ne definira implementacij,
- ne definira gradbenih mehanizmov.

Vse navedeno sodi izven obsega v0.41 in mora biti urejeno v kasnejših fazah.

---

## 14. SKLADNOST, ZAKLEP IN NEPOVRATNOST

Ta dokument:
- je skladen z v0.34–v0.40,
- ne razširja njihove semantike,
- ne uvaja novih odločitev.

Dokument **HOI_SURFACE_ADAPTER_CONTRACT_v0.41_LOCK.md** je s tem
**DOKONČNO ZAKLENJEN** in se ne sme več spreminjati.

---
