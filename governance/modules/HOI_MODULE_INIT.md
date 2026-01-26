# HOI_MODULE_INIT — Human Orientation Interface

## Status
INIT

## Version
v1.0

## Module Name
Human Orientation Interface (HOI)

## Type
System Safeguard / Human-in-the-loop Orientation Module

---

## Purpose

Human Orientation Interface (HOI) je samostojen sistemski modul,
katerega namen je zagotavljanje človeške orientacije, razumevanja
in možnosti smiselnega ukrepanja med delovanjem sistema.

HOI obstaja zato, da prepreči stanje človeške nemoči
in ohrani legitimnost nadaljevanja sistemskih procesov.

---

## Canonical Responsibility

HOI je nosilec in izvrševalni varuh
pravila Human Orientation Safeguard (HOS).

HOI zagotavlja, da se sistem ne nadaljuje v stanju,
kjer človeški nadzornik:
- ne razume stanja sistema
- nima možnosti smiselnega ukrepanja

---

## Scope

HOI je odgovoren za:

- zaznavo izgube človeške orientacije (konceptualno)
- razlago stanja sistema v človeku razumljivi obliki
- omogočanje ponovne orientacije
- omogočanje varne preusmeritve toka delovanja

HOI deluje na nivoju orientacije in legitimnosti,
ne na nivoju odločanja ali izvajanja.

---

## Explicit Non-Goals

HOI izrecno NI odgovoren za:

- spreminjanje sistemskih pravil
- spreminjanje vedenja kernela
- učenje ali adaptacijo sistema
- samogradnjo ali samonadgradnjo
- izvajanje commitov ali aktivacijo sprememb
- prevzemanje odgovornosti namesto človeka

HOI ne odloča.
HOI ne izvaja.
HOI ne optimizira.

---

## Relationship to Chat and LLM

HOI ni enakovreden Chat modulu in ni vezan na LLM.

HOI je samostojen sistemski gradnik,
ki lahko sodeluje z različnimi vmesniki,
vključno z (a ne omejeno na):

- Sapianta Chat
- CLI vmesniki
- Poročilnimi ali nadzornimi pogledi

Sapianta Chat je ena možna implementacija
interakcije s HOI, ne njegov nosilec.

---

## Interaction Model (Conceptual)

HOI deluje kot orientacijski sodelavec,
ki:

- prejema signale iz sistema (npr. kernel, observability)
- zaznava potencialno izgubo orientacije
- preusmerja tok v orientacijski način
- ohranja človeški nadzor nad nadaljevanjem

HOI nima lastnega spomina,
ki bi vplival na sistemsko odločanje.

---

## Safety and Governance Alignment

HOI je skladen z:

- Human Orientation Safeguard (HOS)
- načelom človeške odgovornosti
- zahtevami sledljivosti in revizije

HOI obstaja kot varovalni sloj,
ne kot optimizacijski mehanizem.

---

## Canonical Principle

Sistem brez človeške orientacije
in možnosti ukrepanja
ne sme nadaljevati legitimno.

HOI obstaja zato, da to načelo ostane uveljavljeno.
