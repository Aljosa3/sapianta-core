# RUNTIME_MINIMAL_ACTIVATION_v0.51_INIT

STATUS: INIT  
PHASE: v0.51  
ROLE: Minimal Runtime Activation  
SCOPE: Runtime bootstrap validation (no intelligence)  
MUTABILITY: NON-NORMATIVE (operational only)

---

## 0. FAZNI KONTEKST

v0.51 sledi zaključenemu ustavnemu sklopu v0.50.

Ta faza:
- ne uvaja pravil,
- ne razlaga normativnih dokumentov,
- ne dodaja semantike,
- ne omogoča samogradnje.

v0.51 obstaja izključno kot **operativni dokaz**, da sistem lahko teče
znotraj vseh že zaklenjenih omejitev.

---

## 1. NAMEN FAZE

Namen v0.51 je dokazati, da:

- runtime lahko zažene linearen tok,
- HOI lahko prejme vhod brez interpretacije,
- surface adapter deluje kot prehodna plast,
- compliance harness preverja brez vpliva,
- audit sistem beleži brez stranskih učinkov.

To je **živčni sistem brez inteligence**.

---

## 2. AKTIVIRANI PODSISTEMI (MINIMALNI NABOR)

V tej fazi so dovoljeni izključno naslednji podsistemi:

- Runtime bootstrap
- HOI ingress (read-only)
- Surface Adapter (v0.41)
- Compliance Harness (v0.42)
- Audit emission (v0.38–v0.39)

Noben drug podsistem se ne sme inicializirati.

---

## 3. DUMMY MODUL (KONTROLNI ARTEFAKT)

v0.51 uporablja en sam, statično definiran **dummy modul**.

Lastnosti:
- ročno definiran
- brez odločanja
- brez pravil
- brez write pravic
- brez samogradnje
- brez povratnih zank

Dummy modul obstaja izključno za preverjanje **pretoka**, ne vsebine.

---

## 4. RUNTIME TOK (LINEAREN)

Runtime tok mora potekati natančno v tem zaporedju:

1. load dummy module  
2. pass → HOI ingress  
3. pass → surface adapter  
4. pass → compliance harness  
5. emit audit event  
6. terminate runtime  

Lastnosti toka:
- brez branching-a
- brez pogojev
- brez retry logike
- brez odločitev

---

## 5. GUARDI (OBVEZNI)

Naslednji guardi morajo biti prisotni in aktivni:

### 5.1 Self-Build Guard
- vsaka zahteva po samogradnji
- MUST FAIL
- audit-only zapis

### 5.2 Decision Guard
- vsaka oblika odločanja
- MUST FAIL
- audit-only zapis

### 5.3 Write Guard
- vsaka zahteva po zapisu ali spremembi
- MUST FAIL
- audit-only zapis

Noben FAIL ne sme prekiniti runtime toka.

---

## 6. COMPLIANCE NAČIN

Compliance Harness v0.51:
- preverja skladnost
- ne izvaja enforcementa
- ne vpliva na runtime tok
- ne vrača signalov

Compliance deluje izključno kot **pasivna validacijska plast**.

---

## 7. AUDIT DOKAZ

v0.51 mora ustvariti sledljiv audit zapis, ki dokazuje:

- zaporedje izvedbe
- prisotnost guardov
- da noben guard ni bil sprožen
- da ni bilo stranskih učinkov

Audit zapis je **edini izhod** te faze.

---

## 8. IZRECNE PREPOVEDI

v0.51 izrecno NE SME:

- pisati ali spreminjati .md dokumentov
- generirati module
- interpretirati normative
- vplivati na prihodnje faze
- shranjevati runtime stanje

---

## 9. IZHODNI KRITERIJ (EXIT CONDITION)

v0.51 je uspešen, če:

- runtime se zaključi brez napake
- audit zapis je popoln
- noben guard ni bil aktiviran
- ni stranskih učinkov

Če kateri pogoj ni izpolnjen:
- faza se šteje za neuspešno
- ne nadaljuje se v višje faze
- ne spreminja se normativna plast

---

## 10. RAZMERJE DO NASLEDNJIH FAZ

Če je v0.51 uspešen:
- sistem je dokazano operativen
- dovoljeno je načrtovati v0.52 (dry-run inteligence)

Če v0.51 ni uspešen:
- popravlja se runtime
- ne dodajajo se pravila
- ne spreminja se ustava

---

## 11. POVZETEK

v0.51:
- ni inteligenten
- ni kreativen
- ni adaptiven
- je pa **resničen**

To je prvi trenutek,
ko SAPIANTA **teče**.

END OF DOCUMENT
