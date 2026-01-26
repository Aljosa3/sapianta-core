# HOI_SIGNAL_HANDLING_MODES_INIT — HOI Signal Handling Modes

## Status
INIT

## Version
v1.0

## Owner
Human Orientation Interface (HOI)

## Related Governance
- governance/core/HUMAN_ORIENTATION_SAFEGUARD.md
- governance/taxonomy/HOI_SIGNAL_TAXONOMY_INIT.md
- governance/contracts/HOI_CHAT_INTERACTION_INIT.md

---

## Purpose

Ta dokument definira dovoljene načine odziva (handling modes),
ki jih HOI lahko uporabi, ko zazna signal v smislu
Human Orientation Safeguard (HOS).

Cilj je omogočiti izhod iz človeške nemoči
brez sprožanja adaptacije, samogradnje ali sprememb sistema.

---

## General Constraints

Vsi HOI handling načini so:

- ne-adaptivni
- brez stranskih učinkov
- brez sprememb stanja sistema
- brez ustvarjanja nove trajne informacije
- brez eskalacije v nadgradnjo

HOI nikoli:
- ne spreminja pravil
- ne spreminja modulov
- ne predlaga nadgradenj kot odziv na signal

---

## Handling Modes

### 1. ORIENT

**Opis:**  
HOI zahteva in omogoči dodatno orientacijo človeka.

**Dovoljena dejanja:**
- zahteva po pojasnitvi v preprostejši obliki
- strukturiranje razlage (koraki, povzetek)
- izpostavitev konteksta in trenutnega stanja

**Prepovedano:**
- dodajanje novih funkcionalnosti
- spreminjanje poteka procesa
- interpretacija signala kot napake

---

### 2. PAUSE

**Opis:**  
HOI zahteva začasno ustavitev nadaljevanja procesa.

**Dovoljena dejanja:**
- eksplicitna ustavitev toka
- potrditev, da se brez orientacije ne nadaljuje
- čakanje na človeško odločitev

**Prepovedano:**
- implicitno nadaljevanje
- avtomatsko preusmerjanje
- eskalacija brez zahteve človeka

---

### 3. REDIRECT

**Opis:**  
HOI omogoči varno preusmeritev toka v bolj orientacijsko pot.

**Dovoljena dejanja:**
- predlaganje alternativnih poti (razlaga, povzetek, zaključek)
- vrnitev na znano stabilno točko
- prehod v pregledni način (read-only)

**Prepovedano:**
- prisilna sprememba cilja
- uvajanje novega procesa
- optimizacija ali razširitev zmožnosti

---

## Mode Selection Principle

Izbira handling načina temelji na:
- vrsti zaznanega signala
- ohranjanju človeške orientacije
- minimalnem posegu v proces

Vedno se izbere najmanj invaziven način,
ki odpravi izgubo orientacije ali nemoč.

---

## Explicit Non-Goals

HOI handling načini niso:
- mehanizem izboljševanja sistema
- diagnostično orodje za arhitekturo
- sprožilec razvoja
- nadomestek za človeško odločanje

---

## Canonical Rule

HOI obstaja zato,
da omogoči človeku nadaljevanje z razumevanjem ali izhod,
ne zato, da sistem postane bolj učinkovit.

Vsak handling način mora ohraniti to mejo.
