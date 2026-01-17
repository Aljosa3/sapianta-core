# SP-12 — INCIDENT RESPONSE PROTOCOL (IRP)

**Status:** INIT  
**Vloga:** governance protokol za zaznavo, klasifikacijo, obravnavo in zapiranje incidentov v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-12 določa **zavezujoč in determinističen postopek** za ravnanje ob incidentih,
ki lahko vplivajo na:
- pravilnost odločitev
- skladnost z normativi
- varnost sistema
- zaupanje uporabnikov ali nadzornih organov

Cilj faze je:
- hitro omejiti vpliv incidenta
- preprečiti verižno škodo
- zagotoviti sledljiv in nadzorovan odziv
- omogočiti korektno poročanje brez razkrivanja jedra

SP-12 **ne določa tehnične implementacije**, temveč **governance odziv**.

---

## 2️⃣ DEFINICIJA INCIDENTA

Incident v smislu SP-12 je vsak dogodek, pri katerem:

- je bila kršena governance politika (SP-9, SP-10, SP-11)
- je bila zaznana nedovoljena razlaga ali razkritje
- je prišlo do nepravilnega logiranja ali hrambe podatkov
- je bil zaznan poskus obhoda varoval
- je sistem deloval izven dovoljenih mej

Incident ≠ napaka v kodi.  
Incident pomeni **potencialno normativno ali varnostno tveganje**.

---

## 3️⃣ KATEGORIJE INCIDENTOV

### 🔹 Kategorija A — Kritični
- vplivajo na odločanje ali skladnost
- možna regulativna posledica
- zahtevajo takojšen odziv

### 🔹 Kategorija B — Resni
- omejen vpliv
- brez takojšnje regulativne posledice
- zahteva prioritetno obravnavo

### 🔹 Kategorija C — Manjši
- lokalni ali prehodni vpliv
- brez vpliva na odločitve
- dokumentiranje brez eskalacije

---

## 4️⃣ SPROŽITEV INCIDENT RESPONSE

Incident response se sproži, ko:
- sistem zazna kršitev politike
- operater prijavi sum
- audit odkrije odstopanje
- regulator zahteva pojasnilo

Vsak sprožen incident mora dobiti:
- enolični identifikator
- časovni žig
- začetno kategorijo

---

## 5️⃣ TAKOJŠNJI UKREPI (CONTAINMENT)

Ob zaznavi incidenta sistem mora:
- omejiti nadaljnje delovanje prizadetega dela
- preprečiti dodatno razkrivanje ali logiranje
- ohraniti minimalne dokaze (v skladu s SP-11)
- preprečiti avtomatsko razlago dogodka

Containment ima prednost pred razlago.

---

## 6️⃣ ANALIZA INCIDENTA

Analiza se izvaja:
- omejeno
- ciljno
- brez retroaktivnega razstavljanja odločitev

Analiza vključuje:
- identifikacijo prizadetih komponent
- preverjanje skladnosti z governance pravili
- oceno obsega in vpliva

Analiza **ne sme** voditi v:
- razkrivanje policy jedra
- generiranje novih razlag
- spremembo že izdanih odločitev

---

## 7️⃣ KOMUNIKACIJA IN POROČANJE

### 🔹 Interna komunikacija
- samo pooblaščene osebe
- minimalni povzetki
- brez tehničnih podrobnosti izven potrebe

### 🔹 Zunanja komunikacija
- samo, če je zahtevana
- omejena na skladnost in dejstva
- brez razkrivanja notranjih razlogov ali trace

Razlaga incidenta **ne sme nadomestiti** odprave.

---

## 8️⃣ ZAPRTJE INCIDENTA

Incident se lahko zapre, ko:
- je vpliv omejen
- so sprejeti korektivni ukrepi
- je dokumentiran povzetek
- je preverjena skladnost po ukrepih

Zaprtje mora biti:
- zabeleženo
- sledljivo
- nepovratno

---

## 9️⃣ POST-INCIDENT REVIEW

Za incidente kategorije A in B se izvede pregled, ki:
- oceni učinkovitost odziva
- identificira sistemske pomanjkljivosti
- predlaga preventivne ukrepe

Pregled **ne odpira** že zaprtih odločitev.

---

## 🔟 RAZMERJE DO DRUGIH FAZ

SP-12:
- temelji na SP-9, SP-10 in SP-11
- ne spreminja Canona ali Core Laws
- ne uvaja runtime sprememb
- deluje izključno kot governance protokol

---

## 1️⃣1️⃣ STATUS FAZE

Ta dokument ima status **INIT**.

Zaklep (LOCK) se lahko izvede po simulaciji incidentov in preverjanju postopkov.

---
