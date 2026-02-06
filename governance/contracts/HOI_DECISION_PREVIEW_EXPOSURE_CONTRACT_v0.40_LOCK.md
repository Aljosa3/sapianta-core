# HOI_DECISION_PREVIEW_EXPOSURE_CONTRACT_v0.40_LOCK

STATUS: LOCKED  
PHASE: v0.40  
SCOPE: Decision Preview — Exposure / Surface Contract  
MUTABILITY: IMMUTABLE  

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **Exposure / Surface Contract** za *Decision Preview* znotraj HOI.

Namen dokumenta je opredeliti **izključno način izpostavitve (exposure)** že:
- generiranega,
- validiranega,
- runtime-dovoljenega

*Decision Preview* izpisa.

Dokument:
- ne ureja generiranja vsebine
- ne ureja validacije
- ne ureja auditiranja
- ne uvaja novih semantičnih pravil

Velja **enakovredno in identično** za vse izpostavitvene površine (CLI, API, GUI).

---

## 2. NORMATIVNI OBSEG

Ta specifikacija velja za:
- vse HOI komponente, ki izpostavljajo *Decision Preview*
- vse runtime kontekste, kjer je izpis dovoljen s strani v0.35–v0.37
- vse predstavitvene površine brez izjeme

Izven obsega:
- UX oblikovanje
- uporabniški tokovi
- razlage, opisi, pomožna besedila
- kontekstualni ali okoljski vplivi

---

## 3. OSNOVNO NAČELO IZPOSTAVITVE

HOI mora *Decision Preview* izpostaviti:

- identično vsebini, kot je bila validirana
- brez spremembe vrstnega reda
- brez spremembe znakov
- brez dodanih ali odstranjenih elementov
- brez semantičnega ali vizualnega vpliva

Izpostavitev je **mehanska projekcija** validiranega izpisa na površino.

---

## 4. OBVEZNA PRAVILA IZPOSTAVITVE (EXPOSURE RULES)

4.1 HOI mora izpisati *Decision Preview* kot **neprekinjen, celovit niz**, kot definiran v v0.34.

4.2 HOI ne sme:
- dodajati predpone
- dodajati zaključka
- vstavljati ločil
- vstavljati naslovov ali oznak

4.3 HOI mora zagotoviti, da:
- je izpis viden ali dostopen kot celota
- ni razdeljen na semantične segmente

---

## 5. ENOTNOST MED CLI, API IN GUI

5.1 Vsebina izpisa mora biti **bitno enaka** ne glede na površino.

5.2 Razlike med površinami so dovoljene **izključno** na tehnični ravni prenosa, ne pa na ravni vsebine ali strukture.

5.3 Nobena površina ne sme:
- dodajati oznak
- dodajati kontekstnih elementov
- interpretirati izpisa

---

## 6. PREPOVEDANE OBLIKE IZPOSTAVITVE

Izrecno prepovedano je:

- kakršnokoli poudarjanje delov izpisa
- barvno razlikovanje z namenom pomena
- ikone, badge-i, statusni indikatorji
- wrapperji ali okviri, ki nosijo pomen
- sprememba tipografije z namenom interpretacije

---

## 7. PRAVILA FORMATIRANJA (BREZ SEMANTIKE)

7.1 Dovoljene so izključno **strukturno nevtralne** oblike formatiranja, ki ne vplivajo na pomen.

7.2 Formatiranje:
- ne sme dodajati informacij
- ne sme odstranjevati informacij
- ne sme implicitno voditi interpretacije

7.3 Če površina zahteva tehnično kodiranje (npr. escape mehanizmi), mora biti to **reverzibilno brez izgube**.

---

## 8. RAZMERJE MED RUNTIME PASS/FAIL IN IZPOSTAVITVIJO

8.1 HOI ne sme izpostavljati informacije o:
- PASS ali FAIL statusu
- razlogih za dovoljenje ali zavrnitev

8.2 Če runtime ne dovoli izpisa, *Decision Preview* **ne obstaja na površini**.

8.3 Izpostavitev je binarna:
- ali je izpis viden v celoti
- ali ni viden sploh

---

## 9. PREPOVED SURFACE-LEVEL BYPASSA

9.1 Nobena površina ne sme:
- obiti runtime odločitev
- rekonstruirati izpisa iz delnih virov
- prikazati delnega ali nevalidiranega izpisa

9.2 Vsaka izpostavitev mora biti neposredno vezana na runtime dovoljenje.

---

## 10. PRAVILA ZA NO-OUTPUT STANJE

10.1 Če izpis ni dovoljen:
- HOI ne sme izpisati nadomestnega besedila
- HOI ne sme izpisati razlage
- HOI ne sme izpisati placeholderja

10.2 NO-OUTPUT stanje je **tišina na površini**.

---

## 11. MACHINE-CHECKABLE EXPOSURE PRAVILA

11.1 Izpostavitev mora biti preverljiva s strojno primerjavo med:
- validiranim izpisom
- izpostavljenim izpisom

11.2 Dovoljena odstopanja:
- nobena, razen tehnično nujnih transportnih kodiranj

11.3 Vsaka neujemajoča se projekcija pomeni kršitev v0.40.

---

## 12. PHASE BOUNDARY CLAUSE (v0.40)

12.1 Ta faza **izključno** normativno določa pravila izpostavitve (*exposure*) že dovoljenega *Decision Preview* izpisa.

12.2 Faza v0.40:
- ne definira surface adapterjev
- ne definira implementacijskih mehanizmov
- ne določa vedenja posameznih vmesnikov
- ne uvaja tehnoloških ali UX odločitev

12.3 Vsa pravila, ki se nanašajo na:
- definicijo površine,
- obveznosti posameznega vmesnika,
- adapterje med runtime in površino,

so **izrecno izven obsega v0.40** in sodijo v naslednje faze (v0.41+).

12.4 Kakršenkoli poskus razširitve v0.40 preko pravil izpostavitve pomeni kršitev fazne meje.

---

## 13. SKLADNOST IN ZAKLEP

Ta dokument:
- je skladen z v0.34–v0.39
- ne razširja njihove semantike
- ne uvaja novih odločitev

Dokument **HOI_DECISION_PREVIEW_EXPOSURE_CONTRACT_v0.40_LOCK.md** je s tem
**DOKONČNO ZAKLENJEN** in se ne sme več spreminjati.

---
