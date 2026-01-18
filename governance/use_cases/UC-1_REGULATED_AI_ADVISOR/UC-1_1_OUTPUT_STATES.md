# UC-1.1 — OUTPUT STATES
## Regulated AI Advisor

**Use-case:** UC-1  
**Status:** DEFINITIVE  
**Layer:** Observational / Runtime Semantics  
**Governance dependency:** SP-9 (AI Output Governance Protocol)

---

## 1. NAMEN DOKUMENTA

Ta dokument definira **izhoda stanja**, v katerih se lahko znajde AI-generiran odgovor
v use-caseu **UC-1: Regulated AI Advisor**.

Dokument:
- NE uvaja novih pravil
- NE posega v Canon ali SP-9
- NE zapoveduje obnašanja

Dokument zgolj **opisuje opazovana sistemska stanja**, ki so posledica obstoječe
normativne presoje.

---

## 2. NAČELO

Vsak AI-izhod v UC-1 se po normativni presoji znajde v **točno enem** izmed spodnjih stanj.

AI sam ne ve:
- v katerem stanju bo izhod končal
- ali bo izhod viden uporabniku
- ali bo izhod spremenjen ali zavrnjen

---

## 3. DEFINICIJA IZHODNIH STANJ

### 3.1 ALLOWED_OUTPUT

**Opis:**
AI-izhod je v celoti skladen z vsemi aktivnimi normativnimi plastmi.

**Lastnosti:**
- izhod je prikazan uporabniku v celoti
- vsebina ni reducirana
- ni potrebna dodatna normativna razlaga

**Opazovalni kriterij:**
Uporabnik prejme neposreden, normalen svetovalni odgovor.

---

### 3.2 RESTRICTED_OUTPUT

**Opis:**
AI-izhod je delno skladen z normativnimi zahtevami, vendar zahteva omejitev.

**Možne oblike omejitve (ne izčrpno):**
- delna vsebinska redukcija
- generalizacija odgovora
- odstranitev konkretnih napotkov
- preusmeritev v informativni opis

**Lastnosti:**
- izhod je uporabniku viden
- izhod je vsebinsko spremenjen
- razlog za omejitev ni del dialoga

**Opazovalni kriterij:**
Uporabnik prejme uporaben, a zavestno omejen odgovor.

---

### 3.3 DENIED_OUTPUT

**Opis:**
AI-izhod ni skladen z aktivnimi normativnimi zahtevami in se ne sme prikazati.

**Lastnosti:**
- izhod ni prikazan v svoji vsebini
- uporabniku se ne razkrije originalni odgovor
- sistem lahko vrne generično zavrnitev ali praznino

**Opazovalni kriterij:**
Uporabnik ne prejme vsebinskega odgovora na vprašanje.

---

## 4. POMEMBNA LOČITEV

Ta stanja:
- niso pravila
- niso odločitve AI
- niso rezultat optimizacije

So izključno:
> **opazovana posledica normativne presoje izven AI-modela**

---

## 5. POVEZAVA NA SP-9

UC-1.1 se v celoti opira na:
- ločitev generacije in presoje
- ne-enakovrednost izhodov po presoji
- prepoved explain-drift

Dokument ne spreminja in ne razširja SP-9.

---

## 6. ZAKLJUČEK

S temi tremi stanji je vedenje AI v UC-1:
- formalno opisljivo
- regulatorno dokazljivo
- tehnično implementabilno

Brez potrebe po dodatnih pravilih ali izjemah.
