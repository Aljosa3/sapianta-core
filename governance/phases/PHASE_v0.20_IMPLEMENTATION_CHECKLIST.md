# PHASE v0.20 — IMPLEMENTATION CHECKLIST

Status: IMPLEMENTATION AUTHORITY  
Version: v0.20  
Date: 2026-02-04  
Scope: Validator + Writer (minimal touch)  
Authority: PHASE_v0.20_MULTI_FILE_MODULE_LOCK.md

---

## NAMEN

Ta checklist razbije fazo v0.20 v natančne, mehanske korake.
Vsak korak je:
- determinističen
- neposredno sledljiv LOCK dokumentu
- preverljiv brez interpretacije

Implementacija, ki sledi temu checklistu, se šteje kot skladna z v0.20.

---

## 0. PRE-CONDITIONS (MORAJO DRŽATI)

- v0.19 je zaklenjena faza
- FILE-based output protokol je nespremenjen
- CLI entrypoint ostane nespremenjen
- execution adapter ostane nespremenjen
- RawModuleWriter že obstaja in deluje deterministično

Če katera od teh točk ne drži → implementacija se NE SME začeti.

---

## 1. FILE BLOCK COLLECTION (NO CHANGE)

☐ Sistem še vedno bere FILE bloke identično kot v v0.19  
☐ Podpora za več FILE blokov pride izključno iz ponovitve obstoječega mehanizma  
☐ Nobena nova semantika se ne dodaja v tej fazi  

🚫 Prepovedano:
- združevanje FILE blokov
- implicitna hierarhija
- “main file” privilegiji

---

## 2. VALIDATOR — MODULE BOUNDARY RESOLUTION

☐ Iz poti vseh FILE blokov se določi skupni modul root  
☐ Vsak FILE mora pripadati temu root-u  

HARD FAIL, če:
- FILE poti nimajo skupnega modula
- katerikoli FILE poskuša pisati izven modula  

🚫 Prepovedano:
- runtime preverjanje
- popravljanje poti
- fallback logika

---

## 3. VALIDATOR — FILE INDEX CONSTRUCTION

☐ Zgrajen je kanonični indeks vseh FILE poti  
☐ Poti so obravnavane kot stringi (brez evalvacije)  

HARD FAIL, če:
- obstajata dve FILE poti, ki kažeta na isto datoteko
- katerakoli FILE pot ni veljavna  

🚫 Prepovedano:
- normalizacija z ugibanjem
- prepisovanje datotek

---

## 4. VALIDATOR — IMPORT EXTRACTION

☐ Importi se berejo iz vsebine FILE blokov  
☐ Obravnavajo se samo statični, eksplicitni importi  

HARD FAIL, če:
- import ni statično razpoznaven
- importa ni mogoče mapirati na ime datoteke  

🚫 Prepovedano:
- eval koda
- runtime interpretacija
- implicitni importi

---

## 5. VALIDATOR — MODULE BOUNDARY ENFORCEMENT

☐ Vsak import se preslika v ciljno FILE pot  
☐ Cilj mora obstajati znotraj indeksa modula  

HARD FAIL, če:
- import cilja izven modula
- import cilja na neobstoječo datoteko
- import cilja na runtime ali external namespace  

🚫 Prepovedano:
- dovoljevanje standard library importov
- whitelist logika

---

## 6. VALIDATOR — DEPENDENCY GRAPH CONSTRUCTION

☐ Vozlišče = FILE  
☐ Usmerjen rob = import  

☐ Graf obstaja samo v validatorju  

🚫 Prepovedano:
- optimizacija grafa
- spremembe vrstnega reda
- shranjevanje grafa izven validatorja

---

## 7. VALIDATOR — CYCLE DETECTION

☐ Izvede se aciklični (DAG) check nad grafom  

HARD FAIL, če:
- obstaja katerikoli cikel (katerekoli dolžine)  

🚫 Prepovedano:
- ignoriranje “majhnih” ciklov
- opozorila namesto fail-a

---

## 8. VALIDATOR — PASS / FAIL OUTPUT

☐ Če vse faze PASS → validator vrne PASS  
☐ Če katerakoli faza FAIL → HARD FAIL  

☐ Ob FAIL:
- RawModuleWriter se NE kliče
- nobena datoteka se NE zapiše  

🚫 Prepovedano:
- delni zapisi
- warnings
- retry logika

---

## 9. RAW MODULE WRITER (MINIMAL TOUCH)

☐ Writer sprejme več FILE blokov  
☐ Vsak FILE se zapiše natanko na podano pot  

☐ Writer:
- ne preverja importov
- ne pozna grafa
- ne izvaja validacije  

🚫 Prepovedano:
- preurejanje FILE blokov
- deduplikacija
- popravljanje poti

---

## 10. POST-CONDITIONS (MORAJO DRŽATI)

☐ Veljaven proof module PASS-a  
☐ Vsi negativni scenariji HARD FAIL-ajo  
☐ Vrstni red FILE blokov ne vpliva na rezultat  
☐ Runtime ostane popolnoma neinteligenten  

Če katera točka ne drži → faza v0.20 NI pravilno implementirana.

---

## ZAKLJUČEK

Ta checklist je edini dovoljeni vodnik za implementacijo v0.20.
Vsako odstopanje pomeni kršitev LOCK-a in zahteva novo fazo.

— END OF IMPLEMENTATION CHECKLIST —
