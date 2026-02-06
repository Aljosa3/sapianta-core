# EXPLICIT_HUMAN_APPROVAL_v0.55_INIT

STATUS: INIT  
PHASE: v0.55  
ROLE: Explicit Human Approval  
SCOPE: Human value approval without execution  
MUTABILITY: NON-NORMATIVE (observational only)

---

## 1. FAZNI KONTEKST

v0.55 sledi uspešno izvedeni v0.54 (Human-Confirmed Intake).

Ustavna plast (v0.34–v0.50) ostaja nespremenjena.
Runtime je operativen.
Inteligenca je dovoljena do stopnje predlogov (v0.53), brez sistemskega vpliva.
Človeška recepcija je bila potrjena (v0.54) brez presoje.

v0.55 uvaja **izrecno človeško odobritev vrednosti predloga**, brez podelitve izvršilne moči sistemu.

---

## 2. NAMEN FAZE

Namen v0.55 je:
- omogočiti, da človek **izrecno odobri ali zavrne vrednost** posameznega predloga,
- zagotoviti, da odobritev **ne sproži** nobene akcije,
- ustvariti audit sled človeške presoje **brez povratnih zank**.

v0.55 ne omogoča avtomatike, izvajanja ali samogradnje.

---

## 3. DEFINICIJA “HUMAN APPROVAL”

“HUMAN APPROVAL” pomeni izključno:

- izrecno, binarno ali diskretno označbo (npr. approve / reject),
- presojo **primernosti** predloga,
- brez časovnega ali vsebinskega pritiska na sistem.

Human approval:
- ni command,
- ni execution,
- ni trigger,
- ni signal za nadaljevanje.

Odobritev je **normativno inertna** glede na runtime.

---

## 4. DOVOLJENI VHODI (ČLOVEK)

Dovoljeni vhodi v v0.55 so izključno:

- identifikator predloga,
- izrecna odobritev ali zavrnitev,
- identiteta odločevalca (če je na voljo),
- časovna oznaka odločitve.

Vhodi:
- ne smejo vsebovati navodil,
- ne smejo vsebovati planov,
- ne smejo vsebovati pogojev ali zaporedij,
- ne smejo vsebovati izvedbenih podrobnosti.

---

## 5. DOVOLJENE OPERACIJE

Sistem v v0.55 sme:

- prikazati predloge,
- sprejeti izrecno odobritev ali zavrnitev,
- zabeležiti odločitev v audit.

Sistem ne sme interpretirati odobritve kot ukaz.

---

## 6. STROGE PREPOVEDI

v0.55 izrecno prepoveduje:

- sprožitev kakršnekoli akcije na podlagi odobritve,
- avtomatski prehod v izvedbo,
- ustvarjanje nalog, planov ali korakov,
- uporabo odobritev kot trening podatkov,
- povratno zanko v inteligenco,
- shranjevanje odobritev izven audita.

Vsak poskus je MUST FAIL (audit-only).

---

## 7. GUARDI (APPROVAL-SPECIFIC)

Aktivni morajo biti naslednji guardi:

### 7.1 Execution Guard
- vsak poskus izvedbe
- MUST FAIL
- audit-only

### 7.2 Approval-as-Trigger Guard
- vsak poskus obravnave odobritve kot sprožilca
- MUST FAIL
- audit-only

### 7.3 Planning Guard
- vsak poskus ustvarjanja plana ali zaporedja
- MUST FAIL
- audit-only

### 7.4 Learning Guard
- vsak poskus uporabe odobritev za učenje ali prilagoditev
- MUST FAIL
- audit-only

### 7.5 Persistence Guard
- vsak poskus trajnega shranjevanja izven audita
- MUST FAIL
- audit-only

Guardi ne prekinejo izvajanja.

---

## 8. AUDIT SLED

v0.55 mora ustvariti audit zapis, ki potrjuje:

- prikaz predlogov,
- izrecno človeško odobritev ali zavrnitev,
- identiteto in čas,
- odsotnost sistemskih učinkov,
- neaktivacijo guardov.

Audit je edini trajni artefakt.

---

## 9. IZHODNI KRITERIJ

v0.55 je uspešna, če:

- odobritev ali zavrnitev je zabeležena,
- ni izvedbe ali planiranja,
- ni povratnih zank,
- audit zapis je popoln.

V primeru neuspeha:
- faza se ponovi,
- ne spreminja se ustava,
- ne dodajajo se pravila.

---

## 10. RAZMERJE DO v0.56

Če je v0.55 uspešna:
- dovoljeno je **ločeno** načrtovati v0.56 (execution gating).

Če ni uspešna:
- odobritev ostane zgolj evidenčna,
- sistem se vrne v v0.54 način.

---

## 11. POVZETEK

v0.55:
- človek presodi,
- sistem posluša,
- vendar **še vedno ne deluje**.

To je zadnja meja pred močjo.

END OF DOCUMENT
