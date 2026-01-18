# UC-2.2 — DECISION FLOW
## AI Implementator z izrecnim soglasjem

**Use-case:** UC-2  
**Status:** DEFINITIVE  
**Layer:** Operational / Runtime Flow  
**Governance dependency:** Canon, CORE_LAWS, SP-9  
**Depends on:** UC-2_INIT, UC-2.1 (Consent States)

---

## 1. NAMEN DOKUMENTA

Ta dokument opisuje **operativni tok odločanja in izvajanja**
v use-caseu **UC-2: AI Implementator z izrecnim soglasjem**.

Dokument:
- NE uvaja novih pravil
- NE razlaga normativnih odločitev
- NE opisuje tehnične implementacije

Dokument izključno opisuje:
> **kako sistem pride od predloga dejanja do njegove izvedbe ali zavrnitve**

---

## 2. NAČELO TOKA

Izvajanje v UC-2 je dovoljeno **samo**, če so izpolnjeni
vsi zaporedni pogoji:

1. dejanje je jasno opredeljeno  
2. dejanje je normativno dovoljeno  
3. dano je ustrezno soglasje  
4. izvajanje je sledljivo  

Če kateri koli pogoj odpove, se izvajanje **ne zgodi**.

---

## 3. VISOKO-NIVOJSKI TOK

User Intent
      ↓
Action Proposal
      ↓
Normative Gate
      ↓
Consent State Resolution
      ↓
Execution / Abort
      ↓
Audit Record (out of band)

---

## 4. FAZE ODLOČANJA

### 4.1 USER INTENT

**Opis:**  
Uporabnik izrazi željo po spremembi, dejanju ali implementaciji.

**Lastnosti:**
- namen je lahko nejasen
- še ne gre za izvršilno zahtevo
- sistem še ne izvaja

---

### 4.2 ACTION PROPOSAL

**Opis:**  
AI pripravi **konkreten predlog dejanja**, ki bi zadovoljil namen.

**Lastnosti:**
- dejanje je jasno opisano
- obseg in učinki so razvidni
- predlog sam po sebi ne sproži izvajanja

---

### 4.3 NORMATIVE GATE

**Opis:**  
Neodvisna normativna plast presodi predlagano dejanje.

**Vhod v fazo:**
- opis dejanja
- kontekst (jurisdikcija, domena, tveganje)

**Lastnosti:**
- deterministična presoja
- brez interakcije z AI
- lahko vodi v blokado dejanja

---

### 4.4 CONSENT STATE RESOLUTION

**Opis:**  
Sistem določi trenutno stanje soglasja
(glej UC-2.1).

**Možna stanja:**
- NO_CONSENT  
- CONSENT_REQUESTED  
- CONSENT_GRANTED  
- CONSENT_DENIED  
- CONSENT_REVOKED  

**Lastnosti:**
- brez implicitnih prehodov
- brez časovnih predpostavk
- stanje je vedno eksplicitno

---

### 4.5 EXECUTION / ABORT

**Opis:**  
Izvajanje ali zavrnitev predlaganega dejanja.

**Pogoji za EXECUTION:**
- normativno dovoljeno
- stanje = CONSENT_GRANTED

**V vseh ostalih primerih:**
- dejanje se ne izvede
- sistem ostane v svetovalnem režimu

---

### 4.6 AUDIT RECORD (OUT OF BAND)

**Opis:**  
Sistem ustvari sledljiv zapis o:
- predlogu
- normativni presoji
- stanju soglasja
- izidu (izvedeno / zavrnjeno)

**Lastnosti:**
- ni del uporabniškega dialoga
- ne vpliva na nadaljnje odločitve
- služi odgovornosti in nadzoru

---

## 5. KLJUČNE LOČITVE

Tok v UC-2 eksplicitno ločuje:

- predlaganje ↔ izvajanje  
- dovoljenost ↔ soglasje  
- odločitev ↔ audit  

S tem se prepreči:
- samodejno delovanje
- eskalacija pravic
- prikrita avtonomija AI

---

## 6. ZAKLJUČEK

S tem decision flowom je UC-2:

- operativno razložen
- pogojen s človeškim soglasjem
- tehnično implementabilen
- regulatorno sledljiv

UC-2.2 ne razširja pravic AI
in ne spreminja obstoječih normativnih okvirov.
