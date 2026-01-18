# CERT-TRACK-1 — REGULATORY CERTIFICATION TRACK
## CERT-TRACK-1_SURFACE_MAPPING

### Status
**ACTIVE — CERTIFICATION SURFACE MAPPING**

---

## 1. NAMEN DOKUMENTA

Ta dokument izvede **preslikavo (mapping)** med:
- **produktnimi certifikacijskimi površinami** PRODUCT-1
- in **regulatornimi stiki (regulatory touchpoints)**

Dokument:
- ne navaja zakonov
- ne interpretira pravnih besedil
- ne ugotavlja skladnosti
- ne predlaga ukrepov

Njegov namen je izključno:
> **identificirati, kje PRODUCT-1 lahko postane predmet regulatorne presoje.**

---

## 2. IZHODIŠČA PRESLIKAVE

Preslikava temelji na naslednjih že definiranih dokumentih:

- PRODUCT-1_CERTIFICATION_SURFACE
- PRODUCT-1_SCOPE
- PRODUCT-1_DEPLOYMENT_MODEL
- PRODUCT-1_GOVERNANCE_INHERITANCE

Ti dokumenti predstavljajo **edino dovoljeno osnovo** za preslikavo.

---

## 3. KONCEPT REGULATORNEGA STIKA

Regulatorni stik pomeni:
> **točko, kjer lastnost produkta ali njegova uporaba lahko sproži regulatorno zanimanje, presojo ali zahtevo.**

Stik ni nujno:
- pravna obveznost
- zahteva za certifikat
- dokaz neskladnosti

Je zgolj **potencialna vstopna točka** za regulacijo.

---

## 4. PRIMARNE PRESLIKAVE

### 4.1 Odločitvena vloga → Regulatorni interes

**Produktna površina:**
- vloga sistema v odločanju (svetovalna, podporna, nadzorna)

**Regulatorni stik:**
- presoja vpliva sistema na končne odločitve
- vprašanje razdelitve odgovornosti
- zahteva po razmejitvi človek / sistem

---

### 4.2 Stopnja avtonomije → Regulatorni interes

**Produktna površina:**
- pogojenost izhodov
- zahteva po soglasju
- blokade ali omejitve

**Regulatorni stik:**
- presoja dovoljenih stopenj avtonomije
- zahteve po nadzoru
- pogoji za uporabo v reguliranih procesih

---

### 4.3 Upravljanje izhodov → Regulatorni interes

**Produktna površina:**
- normativno omejeni izhodi
- kontekstualna veljavnost rezultatov
- omejitve nadaljnje uporabe

**Regulatorni stik:**
- vprašanja glede zanesljivosti izhodov
- zahteve po razložljivosti
- omejitve glede uporabe ali distribucije rezultatov

---

### 4.4 Sledljivost in revizija → Regulatorni interes

**Produktna površina:**
- možnost rekonstrukcije odločitev
- revizijski zapisi
- ločitev explain in audit slojev

**Regulatorni stik:**
- zahteve po dokazljivosti procesa
- možnost nadzora
- presoja ustreznosti sledljivosti

---

## 5. SEKUNDARNE PRESLIKAVE

### 5.1 Deployment model → Regulatorni interes

**Produktna površina:**
- SaaS, on-prem, hibridni modeli

**Regulatorni stik:**
- lokacija izvajanja
- nadzor nad spremembami
- razmejitev odgovornosti med ponudnikom in uporabnikom

---

### 5.2 Market interface → Regulatorni interes

**Produktna površina:**
- oblike dostopa
- organizacijska raba
- integracijski dostop

**Regulatorni stik:**
- upravljanje dostopov
- identifikacija uporabnikov
- nadzor nad uporabo v različnih kontekstih

---

## 6. NE-PRESLIKAVE (ZAVESTNE IZKLJUČITVE)

Naslednje produktne lastnosti **niso preslikane** v regulatorne stike:

- notranja arhitektura jedra
- implementacijski detajli
- algoritmične optimizacije
- tehnične izbire modelov

Te lastnosti so:
> **izven regulatornega interesa na produktni ravni**  
> dokler ne vplivajo na odločitveno ali operativno vlogo sistema.

---

## 7. REZULTAT PRESLIKAVE

Rezultat tega dokumenta je:
- strukturiran seznam regulatornih stikov
- jasna ločitev med produktnimi lastnostmi in regulatornim interesom
- stabilna podlaga za nadaljnje regulatorne faze

Preslikava:
- ne ocenjuje tveganja
- ne razvršča produktov
- ne določa obveznosti

---

### CERT-TRACK-1_SURFACE_MAPPING — ZAKLJUČENO

Ta dokument opredeljuje, **kje** PRODUCT-1 lahko vstopi v regulatorno presojo.

Ne določa, *kako* se presoja izvaja  
in ne določa, *kakšen* je izid.
