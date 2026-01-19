# MODULE_CONTRACT_INIT

Status: INIT  
Odvisnost:
- INTENT_LAYER_INIT = LOCKED
- AUDIT_LAYER_INIT = LOCKED
- EXPLAIN_LAYER_INIT = LOCKED
- DECISION_AUTHORITY_REGISTRY_INIT = LOCKED
- JURISDICTION_LAYER_INIT = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Governance / Module  
Narava: Pogodbena (omejevalna, ne-izvršilna)

---

## 1. NAMEN

Vzpostaviti **MODULE CONTRACT** kot obvezno in enotno pogodbo,
ki definira **meje obnašanja vsakega modula** v sistemu SAPIANTA.

Brez veljavnega Module Contracta:
- modul ne sme obstajati
- modul se ne sme registrirati
- modul se ne sme izvajati

---

## 2. TEMELJNO NAČELO

> Modul je **zmožnost**, ne oblast.

Modul:
- ne odloča
- ne izvršuje
- ne legitimira
- ne razlaga

Modul deluje izključno **znotraj Guard verige**.

---

## 3. OBVEZNI VHODI MODULA

Vsak modul lahko prejme izključno:

- referenco na INTENT (read-only)
- strukturiran CONTEXT (read-only)
- konfiguracijo modula (read-only)

Modul:
- ne spreminja INTENTA
- ne rekonstruira namena
- ne dodaja implicitnih ciljev

---

## 4. DOVOLJENI IZHODI MODULA

Modul lahko vrne izključno:

- evalvacijski signal
- zaznavo (observation)
- priporočilo (non-binding)
- opozorilo (warning)

Izhod modula:
- ni odločitev
- ni dovoljenje
- ni izvršilni ukaz

---

## 5. PREPOVEDANE ZMOŽNOSTI

Modul izrecno NE SME:

- sprožiti Decision Gate
- izbrati Decision Authority
- preverjati jurisdikcije
- pisati v Audit
- izvajati Execution
- komunicirati neposredno z uporabnikom

Vsaka od teh zmožnosti pomeni **kršitev pogodbe**.

---

## 6. ODNOS DO DRUGIH SLOJEV

- INTENT: modul se nanj sklicuje, ga ne interpretira
- AUDIT: modul ne piše, lahko pusti sled prek runtime
- EXPLAIN: modul ne razlaga
- JURISDICTION: modul je slep
- AUTHORITY: modul ni authority

Modul ne pozna **celotnega sistema**, pozna samo svoj kontrakt.

---

## 7. VERZIJE IN RAZŠIRITVE

Module Contract:
- je verzioniran
- se ne spreminja retroaktivno
- se razširja le z novo verzijo

Obstoječi moduli:
- ostanejo vezani na verzijo, s katero so bili registrirani

---

## 8. SANDBOX IN SIMULACIJA

Moduli se lahko izvajajo v:

- sandbox režimu
- simulacijskem režimu

Tudi v sandboxu:
- Contract velja
- prepovedi veljajo
- audit sled je obvezna

---

## 9. KRŠITVE POGODBE

Če modul krši Module Contract:

- se takoj deaktivira
- se označi v auditu
- se ne sme ponovno aktivirati brez pregleda

Ni avtomatskih izjem.

---

## 10. INVARIANTA

> Če modul lahko naredi več,
> kot mu dovoljuje Module Contract,
> sistem ni več upravljan.

Ta invariant je nadrejen implementaciji.

---

## 11. ZAKLEP FAZE

Faza `MODULE_CONTRACT_INIT` se lahko označi kot **LOCKED**, ko velja:

- vsak modul ima contract
- brez contracta ni modula
- contract omejuje moč modula
- ni obvodov ali implicitnih pravic

---

Konec dokumenta.
