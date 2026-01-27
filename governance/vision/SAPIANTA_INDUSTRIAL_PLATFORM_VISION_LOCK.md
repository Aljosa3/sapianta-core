# SAPIANTA INDUSTRIAL PLATFORM VISION  
## FORMAL LOCK DOCUMENT (IPV-1-LOCK)

Document ID: IPV-1-LOCK  
Applies to: SAPIANTA_INDUSTRIAL_PLATFORM_VISION.md (IPV-1)  
Status: LOCKED  
Effective date: 2026-01-27  
Owner: SAPIANTA Governance  
Change policy: Restricted  

---

## 1. NAMEN LOCK DOKUMENTA

Ta dokument formalno zaklepa vizijo SAPIANTA Industrial Platform (IPV-1) in jo razglaša za:

**nadrejeni normativni okvir**  
za vse nadaljnje faze razvoja, arhitekturne odločitve, module in produkte sistema SAPIANTA.

Z dnem uveljavitve tega LOCK dokumenta:
- vizija ni več implicitna,
- vizija ni več predmet interpretacije,
- vizija postane zavezujoč razvojni constraint.

---

## 2. OBSEG ZAKLEPA

LOCK velja za:
- celotno platformo SAPIANTA,
- vse obstoječe in prihodnje komponente,
- vse produkte, ki se sklicujejo na ime SAPIANTA.

LOCK ni časovno omejen in velja do izrecnega formalnega odklepa.

---

## 3. ZAKLENJENE POSTAVKE

### 3.1 Namen platforme
SAPIANTA je zaklenjena kot industrijska AI platforma za decision-support.

Ni:
- avtonomni sistem odločanja,
- black-box AI rešitev.

---

### 3.2 Ciljni položaj platforme
Zaklenjena je orientacija proti:
- nadzorovani uporabi AI,
- razložljivosti,
- sledljivosti,
- odgovornosti človeka.

Vsak razvoj, ki bi platformo usmerjal proti:
- avtonomnemu odločanju,
- nepovratnemu izvrševanju brez človeške potrditve,
- netransparentnemu obnašanju,

se šteje za kršitev tega zaklepa.

---

### 3.3 Industrijski standardi
Zaklenjeni so vsi industrijski nefukcionalni standardi:
- reliability,
- security,
- auditability,
- explainability,
- predictability,
- change control,
- observability.

Ti standardi imajo prednost pred funkcionalnimi zahtevami.

---

### 3.4 Nepogajalski principi
Vsi nepogajalski principi (IP-01 → IP-08) so hard constraints.

Niso predmet:
- izjem,
- optimizacij,
- tržnih kompromisov.

---

### 3.5 Negativna definicija
Seznam »Kaj SAPIANTA ni« je zaklenjen kot zaščita pred scope driftom.

---

## 4. POSLEDICE ZAKLEPA ZA RAZVOJ

Z uveljavitvijo LOCK dokumenta:
1. Noben nov modul ne sme biti sprejet brez skladnosti z IPV-1.
2. Nobena funkcionalnost ne sme implicitno širiti obsega platforme.
3. Nobena tehnična odločitev ne sme preglasiti zaklenjenih principov.

LOCK ima prednost pred faznimi cilji v primeru konflikta.

---

## 5. INDUSTRIAL GATE

Industrial Gate Checklist iz IPV-1 je obvezna kontrolna točka
za prehod iz INIT v LOCK pri modulih in funkcionalnostih.

---

## 6. SPREMEMBE IN ODKLEP

### 6.1 Spremembe
Spremembe vizije niso dovoljene brez:
- nove verzije (IPV-2),
- ločenega REVISION dokumenta,
- novega LOCK dokumenta.

### 6.2 Odklep
Odklep je dovoljen izključno z formalno dokumentirano odločitvijo.

Implicitni odklon od vizije se šteje kot kršitev governance pravil.

---

## 7. STATUS

Ta dokument je aktiven, veljaven in nima nadomestnega dokumenta.

---

LOCK CONFIRMATION

Vizija SAPIANTA Industrial Platform (IPV-1) je s tem dokumentom
formalno zaklenjena in zavezujoča.

---

KONEC DOKUMENTA
