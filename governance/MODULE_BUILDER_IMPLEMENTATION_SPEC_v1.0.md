# MODULE_BUILDER_IMPLEMENTATION_SPEC v1.0
## Canonical Architecture — Non-Executable Authoring Tool

---

## STATUS

- **Specification:** ModuleBuilder Implementation
- **Version:** 1.0
- **State:** DRAFT (pending lock after review)
- **Scope:** Authoring & Admission Preparation ONLY
- **Runtime Impact:** NONE
- **Depends On:** MODULE_BUILDER_SPEC v1.0 (LOCKED), Amendment A

---

## 1. NAMEN IMPLEMENTACIJSKEGA SPEC-a

Ta dokument definira **kako** je ModuleBuilder implementiran kot orodje,
ne da bi spreminjal ali razširjal **kaj** ModuleBuilder je.

Cilj je zagotoviti:
- deterministično obnašanje
- ne-interpretativno avtorstvo
- popolno ločitev od runtime in admission

---

## 2. VISOKO-NIVOJSKA ARHITEKTURA

ModuleBuilder je **offline, enonamensko orodje** z enim izhodom.

```
[ Author Input ]
        ↓
[ ModuleBuilder Core ]
        ↓
[ .module_builder_manifest ]
```

Ni stranskih poti, ni povratnih zank.

---

## 3. KOMPONENTE MODULEBUILDERJA

### 3.1 Author Input Layer

**Odgovornost:**
- sprejme eksplicitni avtorski opis modula
- ne interpretira, ne dopolnjuje

**Lastnosti:**
- zahteva popolnost (presence-only)
- ne izvaja semantičnih sklepov
- ne bere obstoječih modulov

**Prepovedi:**
- noben default
- noben auto-fill
- nobena inferenca

---

### 3.2 Validation Layer (Structural Only)

**Odgovornost:**
- preveri prisotnost vseh obveznih deklaracij
- preveri enkratnost normativnih trditev (npr. execution capability)
- preveri prisotnost evaluation layerja za vsako deklaracijo

**Lastnosti:**
- binarna validacija (valid / invalid)
- brez “warnings”
- brez popravkov

**Opomba:**
Validacija NE presoja pravilnosti ali skladnosti z locki.

---

### 3.3 Manifest Assembly Layer

**Odgovornost:**
- deterministično sestavi `.module_builder_manifest`
- ohrani vrstni red in vsebino deklaracij

**Lastnosti:**
- isti input → isti output
- brez transformacij pomena
- brez normalizacije vsebine

---

### 3.4 Output Layer

**Odgovornost:**
- izpiše natanko en artefakt: `.module_builder_manifest`
- brez stranskih izhodov
- brez metapodatkov izven manifesta

**Lastnosti:**
- atomic write
- brez delnih rezultatov

---

## 4. DETERMINIZEM IN REPRODUCIBILNOST

ModuleBuilder MORA biti determinističen:

- isti avtorski input → identičen manifest
- brez odvisnosti od:
  - časa
  - okolja
  - sistema
  - stanja projekta

Vsak nedeterminističen element je arhitekturna napaka.

---

## 5. RAZMERJE DO DRUGIH SISTEMOV

### 5.1 Module Admission

- ModuleBuilder ne kliče Admission
- ne pozna admission pravil
- ne ve, ali bo modul admitted

Manifest je **edini stik**.

---

### 5.2 GuardLifecycle

- ModuleBuilder ne bere GuardLifecycle
- ne interpretira guard pravil
- samo označi evaluation layer

---

### 5.3 Runtime

- noben dostop
- noben vpogled
- nobena odvisnost

Runtime ne obstaja v kontekstu ModuleBuilderja.

---

## 6. DOVOLJENI IMPLEMENTACIJSKI OBRAZI

Implementacija ModuleBuilderja JE LAHKO:

- CLI orodje
- API storitev (offline)
- knjižnica
- ročni proces (document-driven)

Implementacija ModuleBuilderja NI LAHKO:

- runtime servis
- samoregistracijski agent
- del execution pipeline-a

---

## 7. NAPAKE IN NEVELJAVNI VHODI

Ob neveljavnem vhodu ModuleBuilder:

- zavrne build
- ne generira manifesta
- ne popravi vhoda
- ne ponuja alternativ

Napaka je **avtorska**, ne sistemska.

---

## 8. VERZIONIRANJE

- Verzija ModuleBuilderja MORA biti zapisana v manifest
- Sprememba implementacije brez spremembe SPEC-a:
  - dovoljena
  - ne vpliva na manifest semantiko
- Sprememba semantike:
  - zahteva nov SPEC

---

## 9. ARHITEKTURNO NAČELO

Ključno implementacijsko načelo:

> **ModuleBuilder je prevajalnik odgovornosti, ne logike.**

Ne sklepa.
Ne pomaga.
Ne optimizira.

---

## 10. ZAKLJUČEK

Ta implementacijski spec zagotavlja:

- da je ModuleBuilder gradljiv
- da ostane arhitekturno čist
- da ne razkraja obstoječih lockov
- da je prihodnja koda omejena z jasnimi mejami

Vsaka implementacija ModuleBuilderja MORA slediti temu dokumentu.

---

END OF IMPLEMENTATION SPEC
