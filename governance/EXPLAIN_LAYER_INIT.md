# EXPLAIN_LAYER_INIT

Status: INIT  
Odvisnost:
- AUDIT_LAYER_INIT = LOCKED
- INTENT_LAYER_INIT = LOCKED
- CANON_GUARD_DECISION_CHAIN = ACTIVE

Razred: Interaction / Narrative  
Narava: Razlagalna (ne-dokazna)

---

## 1. NAMEN

Vzpostaviti **EXPLAIN LAYER** kot edini dovoljeni sloj za
razlago delovanja sistema **uporabniku ali operaterju**.

EXPLAIN LAYER:
- pojasnjuje
- povzame
- kontekstualizira

Ne dokazuje in ne legitimira odločitev.

---

## 2. TEMELJNO NAČELO

> Explain je **narativ**, ne dokaz.

Vsaka razlaga:
- je namenjena razumevanju
- ni pravno zavezujoča
- ne more nadomestiti audita

Če je razlaga uporabljena kot dokaz → sloja nista ločena.

---

## 3. VIRI ZA RAZLAGO

Explain LAYER lahko uporablja izključno:

- referenco na INTENT
- povzetek konteksta (ne surove podatke)
- povzetek evalvacijskih signalov
- povzetek odločitvenega izida
- jurisdikcijski okvir (če je dovoljen)

Explain:
- ne dostopa do surovega audit zapisa
- ne spreminja audit podatkov
- ne filtrira dokazov

---

## 4. KAJ JE DOVOLJENA RAZLAGA

Explain lahko:

- povzame *kaj* se je zgodilo
- pojasni *kako* je sistem obravnaval zahtevo
- navede *kateri sloji* so sodelovali
- opozori na omejitve ali zavrnitve

Explain ne sme:

- rekonstruirati razlogov odločanja
- navajati pravil ali tehtanj
- ustvarjati vtisa legitimacije

---

## 5. KAJ EXPLAIN NI

EXPLAIN LAYER izrecno NE SME:

- nadomestiti audita
- opravičevati odločitev
- prikazovati notranjih pravil
- ustvarjati “dokaznega videza”
- zagotavljati pravne varnosti

Če je potrebna dokazljivost → uporabi se Audit Layer.

---

## 6. NASLOVNIKI RAZLAGE

Explain je lahko namenjen:

- končnemu uporabniku
- operaterju sistema
- nadzornemu vmesniku

Explain **ni** namenjen:
- pravnim postopkom
- revizijam
- certificiranju

---

## 7. LOČITEV OD DRUGIH SLOJEV

- Explain nikoli ne piše v Audit
- Explain nikoli ne sproža Decision Gate
- Explain nikoli ne vpliva na Execution

Explain je **posledica**, nikoli vzrok.

---

## 8. INVARIANTA

> Če Explain vpliva na odločitev ali izvršitev,
> ni več razlagalni sloj, temveč prikrita oblast.

Ta meja je absolutna.

---

## 9. ZAKLEP FAZE

Faza `EXPLAIN_LAYER_INIT` se lahko označi kot **LOCKED**, ko velja:

- Explain je ločen od audita
- Explain je ne-zavezujoč
- Explain je uporabniško usmerjen
- Explain nima izvršilne moči

---

Konec dokumenta.
