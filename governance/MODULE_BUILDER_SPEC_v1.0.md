# MODULE_BUILDER_SPEC v1.0
## Canonical Specification — Module Authoring & Admission Preparation

---

## STATUS

- **Version:** 1.0
- **State:** CANONICAL
- **Lock:** PENDING (to be locked after review)
- **Scope:** Authoring & Admission Preparation ONLY
- **Runtime Impact:** NONE

---

## 1. NAMEN DOKUMENTA

Ta dokument kanonično definira **ModuleBuilder** kot sistemsko vlogo v SAPIANTA.

ModuleBuilder je edini dovoljeni mehanizem za:
- formalni nastanek modula
- generiranje uradnega opisa modula
- pripravo modula za Module Admission

Brez ModuleBuilderja modul **ne obstaja** v sistemskem smislu.

---

## 2. POZICIJA MODULEBUILDERJA V ARHITEKTURI

ModuleBuilder se nahaja **pred** vsemi naslednjimi sistemi:

- Module Admission
- Interaction Registry
- GuardLifecycle
- Runtime Execution

Arhitekturni tok:

[ Author ]
   ↓
[ ModuleBuilder ]
   ↓
[ .module_builder_manifest ]
   ↓
[ Module Admission ]
   ↓
[ Interaction Registry ]
   ↓
[ Runtime (če admitted) ]

ModuleBuilder nikoli ne sodeluje v runtime.

---

## 3. KANONIČNA VLOGA MODULEBUILDERJA

ModuleBuilder je:

- avtorski mehanizem
- determinističen
- statičen
- ne-interpretativen
- ne-izvajalski

Njegova edina naloga je:
> pretvoriti **avtorski namen** v **formalen, preverljiv opis modula**.

ModuleBuilder ne presoja pravilnosti modula – samo njegovo formalno popolnost.

---

## 4. KAJ MODULEBUILDER SME

ModuleBuilder SME:

1. Sprejeti ekspliciten opis modula
2. Zahtevati popoln nabor obveznih deklaracij
3. Zavrniti nepopolne ali implicitne opise
4. Generirati **.module_builder_manifest**
5. Delovati brez dostopa do runtime
6. Delovati brez vpogleda v admitted module
7. Delovati brez interpretacije GuardLifecycle pravil

---

## 5. KAJ MODULEBUILDER NE SME

ModuleBuilder NE SME:

1. ❌ Izvajati kakršnekoli runtime logike
2. ❌ Nalagati ali klicati module
3. ❌ Samodejno popravljati ali ugibati manjkajoče podatke
4. ❌ Generirati implicitna pravila ali odločitve
5. ❌ Uvajati discovery ali samoregistracijo
6. ❌ Spreminjati ali brati obstoječe locke
7. ❌ Presojati admission ali guard skladnosti

Vsaka kršitev pomeni arhitekturno napako.

---

## 6. .MODULE_BUILDER_MANIFEST — SOURCE OF TRUTH

### 6.1 Status manifesta

`.module_builder_manifest` je:

- edini uradni opis modula
- edini vhod v Module Admission
- statičen artefakt
- immutable po admissionu

Če manifest ne obstaja, modul sistemsko ne obstaja.

---

### 6.2 Vsebinski obseg manifesta

Manifest mora eksplicitno deklarirati:

- identiteto modula
- verzijo
- tip modula
- deklarirani namen
- interaction surface (vhod/izhod)
- deklarirane omejitve
- deklarirane odvisnosti
- avtorstvo
- verzijo ModuleBuilderja

Manifest NE vsebuje:
- kode
- logike
- runtime referenc
- guard pravil
- interpretacij

---

## 7. MINIMALNA IMPLEMENTACIJA MODULEBUILDER v1.0

ModuleBuilder v1.0 je namerno minimalen.

Zna:
- sprejeti popoln opis
- validirati prisotnost obveznih delov
- generirati manifest
- končati

Ne zna:
- migrirati
- optimizirati
- primerjati
- analizirati obstoječih modulov

To ni pomanjkljivost, ampak zavestna omejitev.

---

## 8. RAZMERJE DO OBSTOJEČIH LOCKOV

ModuleBuilder:

- ne bere GuardLifecycle LOCK v0.2
- ne vpliva na Module Admission LOCK v0.3
- ne komunicira z Interaction Registry

S tem je zagotovljena stroga plastnost sistema.

---

## 9. ARHITEKTURNO NAČELO

Ključno načelo ModuleBuilderja:

> **Avtorstvo je ločeno od presoje.**

ModuleBuilder ustvarja objekt presoje.
Presoja se zgodi izključno kasneje.

---

## 10. ZAKLJUČEK

S to specifikacijo je ModuleBuilder:

- formalno definiran
- ločen od runtime
- ločen od admission
- vzpostavljen kot prva faza življenjskega cikla modula

Vsak prihodnji modul mora nastati izključno skozi ModuleBuilder.

---

END OF SPEC
