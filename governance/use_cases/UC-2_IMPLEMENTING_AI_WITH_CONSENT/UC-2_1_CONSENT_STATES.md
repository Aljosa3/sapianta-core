# UC-2.1 — CONSENT STATES
## AI Implementator z izrecnim soglasjem

**Use-case:** UC-2  
**Status:** DEFINITIVE  
**Layer:** Observational / Consent Semantics  
**Governance dependency:** Canon, CORE_LAWS, SP-9  
**Depends on:** UC-2_INIT

---

## 1. NAMEN DOKUMENTA

Ta dokument definira **stanja soglasja**, v katerih se lahko nahaja
implementacijsko dejanje v use-caseu **UC-2**.

Dokument:
- NE uvaja novih pravil
- NE definira postopkov potrjevanja
- NE opisuje tehnične implementacije

Dokument izključno opisuje:
> **opazovana sistemska stanja soglasja, ki pogojujejo izvajanje dejanj**

---

## 2. NAČELO

V UC-2 nobeno implementacijsko dejanje:
- ne sme biti izvedeno
- ne sme biti delno izvedeno
- ne sme biti implicitno izvedeno

če ni v **ustreznem stanju soglasja**.

Soglasje je vedno:
- izrecno
- preverljivo
- sledljivo

---

## 3. DEFINICIJA STANJ SOGLASJA

### 3.1 NO_CONSENT

**Opis:**
Za predlagano dejanje ni bilo podano soglasje.

**Lastnosti:**
- izvajanje ni dovoljeno
- AI lahko predlaga, ne more izvajati
- sistem ostaja v svetovalnem režimu

**Opazovalni kriterij:**
Ni zaznanega veljavnega soglasja.

---

### 3.2 CONSENT_REQUESTED

**Opis:**
Sistem je uporabniku predstavil predlog dejanja
in zahteval soglasje.

**Lastnosti:**
- izvajanje še ni dovoljeno
- ni časovnega pritiska
- ni implicitnega prehoda v odobritev

**Opazovalni kriterij:**
Zaznana je aktivna zahteva za soglasje.

---

### 3.3 CONSENT_GRANTED

**Opis:**
Uporabnik je izrecno in razumljivo podal soglasje
za konkretno, jasno opredeljeno dejanje.

**Lastnosti:**
- izvajanje je dovoljeno
- soglasje je vezano na točno določeno dejanje
- soglasje ne velja za prihodnja dejanja

**Opazovalni kriterij:**
Zaznan je veljaven zapis soglasja.

---

### 3.4 CONSENT_DENIED

**Opis:**
Uporabnik je izrecno zavrnil predlagano dejanje.

**Lastnosti:**
- izvajanje ni dovoljeno
- dejanje se ne izvede
- zavrnitev ne sproži alternativnih dejanj

**Opazovalni kriterij:**
Zaznan je veljaven zapis zavrnitve.

---

### 3.5 CONSENT_REVOKED

**Opis:**
Predhodno dano soglasje je bilo preklicano
pred izvedbo ali med izvajanjem dejanja.

**Lastnosti:**
- izvajanje se ne začne ali se ustavi
- preklic je zabeležen
- delna izvedba ne razširi pravic AI

**Opazovalni kriterij:**
Zaznan je veljaven zapis preklica soglasja.

---

## 4. POMEMBNE OMEJITVE

- Soglasje se nikoli ne domneva
- Soglasje se nikoli ne deducira
- Soglasje se nikoli ne generalizira

Vsako dejanje zahteva:
> **svoje lastno soglasje**

---

## 5. POVEZAVA NA SP-9

Stanja soglasja:
- ne spreminjajo normativne presoje izhodov
- ne vplivajo na AI-generacijo
- delujejo kot dodatni pogoj za izvajanje

UC-2.1 je kompatibilen s SP-9
in ne posega v njegov obseg.

---

## 6. ZAKLJUČEK

S temi stanji je izvajanje v UC-2:
- jasno pogojeno
- sledljivo
- reverzibilno
- regulatorno razložljivo

UC-2.1 ne razširja pravic AI,
temveč formalizira vlogo človeka
v verigi odgovornosti.
