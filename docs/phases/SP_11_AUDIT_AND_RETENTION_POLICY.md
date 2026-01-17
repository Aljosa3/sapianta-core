# SP-11 — AUDIT & RETENTION POLICY (ARP)

**Status:** INIT  
**Vloga:** governance politika za določanje obsega, hrambe in upravljanja audit evidence, execution trace in explain artefaktov v sistemu SAPIANTA

---

## 1️⃣ NAMEN FAZE

SP-11 določa **zavezujoča pravila**, ki urejajo:
- kateri podatki se beležijo za namen audita
- koliko časa se posamezni tipi podatkov hranijo
- kdo ima dostop do katerih dokazov
- kdaj in kako se podatki izbrišejo ali anonimizirajo

Cilj faze je:
- preprečiti prekomerno logiranje
- preprečiti tiho širjenje audita v trace
- zagotoviti dokazljivost brez razkrivanja jedra
- omogočiti skladnost z regulativnimi zahtevami (npr. EU AI Act)

SP-11 **ne določa tehnične implementacije**, temveč normativne meje.

---

## 2️⃣ RAZMERJE DO PREJŠNJIH FAZ

SP-11:
- temelji na SP-10 (Explainability Boundary Protocol)
- dopolnjuje SP-9 (AI Output Governance)
- ne spreminja Canona ali Core Laws

Audit in retention sta **governance odgovornost**, ne runtime lastnost.

---

## 3️⃣ KATEGORIJE PODATKOV

Sistem SAPIANTA ločuje naslednje kategorije:

### 🔹 EXPLAIN ARTEFAKTI
- uporabniško vidne razlage
- povzetki odločitev
- interpretativni opisi

### 🔹 AUDIT EVIDENCE
- dokazila skladnosti
- reference na politike
- časovne oznake
- identifikatorji odločitev

### 🔹 EXECUTION TRACE
- tehnični zapisi izvajanja
- zaporedje korakov
- notranji identifikatorji

---

## 4️⃣ NAČELO MINIMALNE HRAMBE

> Sistem sme hraniti **le minimalni nabor podatkov**, ki je potreben za dokazovanje skladnosti.

To pomeni:
- audit evidence ≠ celoten trace
- trace se ne hrani privzeto
- explain artefakti nimajo dokazne teže

---

## 5️⃣ RETENTION POLITIKE (PRIVZETE)

Privzeti roki hrambe, če ni drugače določeno:

| Kategorija | Privzeta hramba |
|----------|-----------------|
| Explain artefakti | do zaključka interakcije |
| Audit evidence | časovno omejeno (politika) |
| Execution trace | ne hrani se privzeto |

Vsako odstopanje mora biti:
- izrecno konfigurirano
- časovno omejeno
- utemeljeno

---

## 6️⃣ IZJEME IN INCIDENTI

Execution trace se lahko hrani **izključno**, če:
- je zaznan incident
- je sprožen interni audit
- to zahteva regulatorni organ

V takem primeru:
- se hramba označi kot **izjema**
- določi se časovni rok
- dostop je strogo omejen

---

## 7️⃣ DOSTOPNE PRAVICE

- Explain artefakti → uporabnik
- Audit evidence → pooblaščeni auditor
- Execution trace → sistem (izjemoma auditor v agregirani obliki)

Neprepoznan dostop pomeni **kršitev politike**.

---

## 8️⃣ BRISANJE IN ANONIMIZACIJA

Po poteku retention roka:
- audit evidence se izbriše ali anonimizira
- trace se izbriše brez izjeme
- explain artefakti se ne arhivirajo

Brisanje mora biti:
- avtomatizirano
- sledljivo
- nepovratno

---

## 9️⃣ RAZMERJE DO EU AI ACT

SP-11 podpira skladnost, ker:
- omogoča dokazljivost brez razkritja
- uvaja načelo sorazmernosti
- ločuje obvezno hrambo od tehnične sledljivosti
- preprečuje prekomerno zbiranje podatkov

---

## 1️⃣0️⃣ STATUS FAZE

Ta dokument ima status **INIT**.

Zaklep (LOCK) se lahko izvede po preverjanju implementacijskih vplivov.

---
