# SAPIANTA_CHAT_REVIEW

Status: LOCKED  
Scope: Canonical meaning lock  
Applies to: SAPIANTA_CHAT_MODULE_INIT

---

## 1. NAMEN REVIEWJA

Ta dokument **kanonično zaklepa pomen in vlogo SAPIANTA Chat modula**.

Review ne uvaja nove funkcionalnosti.
Review ne spreminja arhitekture.
Review izključno potrjuje in zaklepa že dogovorjeno semantiko.

---

## 2. KANONIČNA OPREDELITEV CHATA

SAPIANTA Chat je:

> **izključno komunikacijski kanal med človekom in sistemom SAPIANTA.**

Chat je:
- vhodno-izhodni vmesnik
- nosilec uporabniške interakcije
- tehnični adapter za deklaracijo INTENT-a
- prikazovalnik Explain izhodov

Chat **ni**:
- inteligentni agent
- svetovalec
- odločevalec
- interpret jezika
- izvajalec ukazov
- avtoriteta

---

## 3. ARHITEKTURNA MEJA

Chat modul je **strogo omejen na rob sistema**.

Vsa naslednja dejanja so izven njegovega dometa:
- interpretacija namena
- normativna presoja
- tveganjska ocena
- odločanje
- jurisdikcijska presoja
- izvrševanje
- audit

Vse navedeno se mora izvajati **izključno v globljih sistemskih slojih**.

---

## 4. ODNOS DO INTENT LAYERJA

Chat:
- je primarni vir uporabniškega INTENT-a
- INTENT oblikuje deklarativno
- ne dodaja logike ali pomena

Vsak INTENT mora ostati:
- sledljiv do uporabnika
- neinterpretiran
- neobogaten

---

## 5. ODNOS DO EXPLAIN LAYERJA

Chat:
- lahko prikaže Explain izhod
- Explain ne spreminja
- Explain ne interpretira
- Explain ne nadomešča

Če Explain izhod ne obstaja:
- Chat nima pooblastila za ustvarjanje razlage

---

## 6. PREPOVED RAZŠIRITEV

Vsak poskus, da bi Chat:
- predlagal rešitve
- vodil uporabnika
- potrjeval dejanja
- psihološko vplival
- ustvarjal implicitno avtoriteto

predstavlja **kršitev kanona**.

Takšna funkcionalnost zahteva:
- nov modul
- novo fazo
- ločen review
- ločeno odločitev

---

## 7. INVARIANTA

> Če Chat vpliva na odločitev,  
> potem Chat ni več komunikacijski kanal, temveč oblast.

To je sistemsko nesprejemljivo.

---

## 8. ZAKLEP

S tem dokumentom je:

- pomen SAPIANTA Chat modula zaklenjen
- njegova vloga kanonično določena
- vsaka prihodnja sprememba pomena dovoljena samo preko nove faze

Status: **LOCKED**

---

Konec dokumenta.
