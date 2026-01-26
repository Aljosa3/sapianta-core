# OBSERVABILITY_TO_HOI_MAPPING_INIT — Observability ↔ HOI Mapping

## Status
INIT

## Version
v1.0

## Owner
Human Orientation Interface (HOI)

## Related Governance
- governance/core/HUMAN_ORIENTATION_SAFEGUARD.md
- governance/taxonomy/HOI_SIGNAL_TAXONOMY_INIT.md
- governance/handling/HOI_SIGNAL_HANDLING_MODES_INIT.md
- governance/contracts/HOI_CHAT_INTERACTION_INIT.md

---

## Purpose

Ta dokument določa izključno dovoljene vire
observability artefaktov, iz katerih HOI
lahko zazna signal v smislu
Human Orientation Safeguard (HOS).

Dokument vzpostavlja strogo, enosmerno in
read-only preslikavo med obstoječimi
observability podatki in HOI signalno zaznavo.

---

## Core Principle

HOI ne ustvarja novih podatkov.
HOI ne interpretira skritih vzorcev.
HOI ne agregira ali sklepa.

HOI lahko zazna signal samo,
če je ta neposredno razviden
iz obstoječega observability artefakta.

---

## Allowed Observability Sources

### 1. Kernel Introspection Probe Outputs

**Vir:**
- KernelIntrospectionProbe decision responses
- outcome (allow / constrain / deny)
- confidence
- guard triggers

**Možna preslikava v signal:**
- ORIENTATION_LOSS
- ACTION_INABILITY

**Omejitve:**
- brez primerjave več runov
- brez trendne analize
- brez statistične inferenčne obdelave

---

### 2. Chat Interaction Structure

**Vir:**
- zaporedje uporabniških odzivov
- eksplicitni izrazi nerazumevanja ali nemoči

**Možna preslikava v signal:**
- ORIENTATION_LOSS
- ORIENTATION_STALL
- EXIT_OBSCURITY

**Omejitve:**
- brez analize tona ali sentimenta
- brez modeliranja uporabnika
- brez psihološke interpretacije

---

### 3. Explicit Human Declarations

**Vir:**
- neposredna človeška izjava o nerazumevanju ali nemoči

**Možna preslikava v signal:**
- ORIENTATION_LOSS
- ACTION_INABILITY
- EXIT_OBSCURITY

**Omejitve:**
- HOI izjave ne reinterpretira
- ni preverjanja verodostojnosti
- ni konflikta z drugimi viri

---

### 4. Audit / Trace Metadata (Limited)

**Vir:**
- trace_id
- event boundary markers
- explicit pause or deny events

**Možna preslikava v signal:**
- ORIENTATION_STALL

**Omejitve:**
- brez vsebinske analize
- brez semantične interpretacije dogodkov
- brez retrospektivne rekonstrukcije

---

## Explicitly Disallowed Sources

HOI NE SME zaznavati signalov iz:

- notranjih stanj LLM
- embeddingov ali latentnih reprezentacij
- metrik uspešnosti ali učinkovitosti
- zgodovine uporabnika
- korelacij ali vzorcev obnašanja
- modelskih napovedi

---

## Mapping Constraints

Preslikava observability → signal mora biti:

- deterministična
- lokalna (en artefakt, en signal)
- razložljiva brez dodatnega konteksta
- reverzibilna (jasno, iz česa izhaja)

Če preslikava ni očitna,
signal ne sme biti zaznan.

---

## Canonical Rule

HOI zazna signal samo,
če je izguba orientacije ali nemoč
neposredno vidna.

Če mora HOI sklepati,
signal ne obstaja.
