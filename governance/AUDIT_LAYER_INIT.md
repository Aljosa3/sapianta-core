# AUDIT_LAYER_INIT

Status: INIT  
Odvisnost:
- INTENT_LAYER_INIT = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Governance / Evidence  
Narava: Dokazna (ne-narativna)

---

## 1. NAMEN

Vzpostaviti **AUDIT LAYER** kot edini dovoljen sloj za
zbiranje, hrambo in predstavitev **dokazov o delovanju sistema**.

AUDIT LAYER obstaja zato, da je mogoče:
- dokazati, kaj se je zgodilo
- dokazati, kdaj se je zgodilo
- dokazati, kdo je bil nosilec odločitve

Audit **ni razlaga** in **ni komunikacija z uporabnikom**.

---

## 2. TEMELJNO NAČELO

> Audit je **dokaz**, ne zgodba.

Vsak zapis v auditu mora biti:
- faktičen
- preverljiv
- nespremenjen
- brez interpretacije

Če zapis zahteva razlago → ne sodi v audit.

---

## 3. KAJ JE AUDIT ZAPIS

Audit zapis lahko vsebuje izključno:

- identifikator dogodka
- časovni žig
- referenco na INTENT
- referenco na kontekst
- referenco na evalvacijski signal
- referenco na Decision Gate
- referenco na Decision Authority
- izid (allowed / denied / pending / no-decision)

Audit zapis:
- ne vsebuje “zakaj”
- ne vsebuje priporočil
- ne vsebuje povzetkov

---

## 4. KAJ AUDIT NI

AUDIT LAYER izrecno NE SME:

- razlagati odločitev
- povzemati razlogov
- ocenjevati pravilnosti
- prikazovati uporabniških narativov
- skrivati ali olepševati dogodkov

Če je nekaj namenjeno razumevanju → to je Explain Layer.

---

## 5. VIR AUDIT PODATKOV

Audit podatki se lahko zbirajo izključno iz:

- runtime dogodkov
- Decision Gate prehodov
- Decision Authority potrditev
- Execution statusov (če obstajajo)

Moduli:
- ne pišejo neposredno v audit
- ne oblikujejo audit strukture

---

## 6. NE-SPREMENLJIVOST

Audit zapis mora biti:

- append-only
- brez popravkov
- brez brisanja
- brez prepisovanja

Vsak popravek pomeni **nov audit dogodek**, ne spremembe obstoječega.

---

## 7. DOSTOP DO AUDITA

Audit:
- ni namenjen uporabniku
- ni namenjen chatu
- ni namenjen razlagi

Dostop do audita je omejen na:
- nadzorne funkcije
- pravne postopke
- certificirane revizije

Vsaka uporaba audita za razlago pomeni kršitev tega sloja.

---

## 8. INVARIANTA

> Če je mogoče iz audita razbrati namen razlage,
> audit ni več dokazni sloj.

Ta meja je absolutna.

---

## 9. ZAKLEP FAZE

Faza `AUDIT_LAYER_INIT` se lahko označi kot **LOCKED**, ko velja:

- audit vsebuje izključno dokaze
- audit nima narativne oblike
- audit ni neposredno viden uporabniku
- audit je ločen od Explain sloja

---

Konec dokumenta.
