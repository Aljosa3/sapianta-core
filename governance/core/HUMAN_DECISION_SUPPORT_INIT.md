# HUMAN_DECISION_SUPPORT_INIT — Human Decision Support (HDS)

## Status
INIT

## Version
v1.0

## Owner
Sapianta Core

## Related Governance
- governance/core/HUMAN_ORIENTATION_SAFEGUARD.md
- governance/modules/HOI_MODULE_INIT.md
- governance/contracts/HOI_CHAT_INTERACTION_INIT.md
- governance/modules/LLM_MODULE_INIT.md

---

## Purpose

Human Decision Support (HDS) je namenski sloj sistema Sapianta,
katerega naloga je pomagati človeku razumeti posledice odločitev,
ki jih sistem od njega zahteva ali omogoča.

HDS ne sprejema odločitev.
HDS ne deluje avtoritativno.
HDS ne nadomešča človeške presoje.

Njegov namen je zmanjšati nelagodje in tveganje odločanja
v pogojih nepopolnega razumevanja.

---

## Core Principle

Če sistem od človeka zahteva izbiro,
mora človeku omogočiti dovolj razumevanja,
da je izbira legitimna.

Predlog brez razlage je nedopusten.
Razlaga brez razkritja negotovosti je nelegitimna.

---

## Role Definition

HDS je ločen od:

- **HOI (Human Orientation Interface)**  
  HOI varuje orientacijo in legitimnost nadaljevanja.

- **Chat Orchestration**  
  Chat vodi dialog, ne vrednoti odločitev.

- **LLM**  
  LLM generira razlage in predloge,
  vendar brez avtoritete in brez odločanja.

HDS deluje kot posredniški sloj,
ki strukturira razlago odločitev,
ne da bi posegal v njihovo izvršitev.

---

## Allowed Capabilities

HDS SME:

- predlagati eno ali več možnosti,
  ki jih sistem ocenjuje kot smiselne
- izpostaviti razloge za vsak predlog
- opisati možne posledice odločitev
  (kvalitativno, ne deterministično)
- jasno označiti stopnjo negotovosti
- ponuditi dodatno razlago na zahtevo človeka
- predstaviti alternative brez preferenčnega pritiska

---

## Explicit Prohibitions

HDS NE SME:

- odločati namesto človeka
- trditi, da je neka možnost pravilna ali optimalna
- prikriti negotovosti ali omejitve
- uveljavljati priporočil kot navodil
- obiti ali preglasiti HOI
- sprožiti akcije ali spremembe sistema

---

## Relationship with HOI

- HOI ima prednost pri zaščiti legitimnosti.
- Če je HOI v načinu PAUSE,
  HDS ne sme spodbujati nadaljevanja.
- HDS ne more razveljaviti HOI odločitve.

HOI in HDS se dopolnjujeta,
vendar ne prekrivata.

---

## Transparency Requirements

Vsak HDS predlog mora jasno vsebovati:

- da gre za predlog, ne odločitev
- razloge za predlagano možnost
- znane omejitve in negotovosti
- da končna odločitev ostaja pri človeku

---

## Canonical Rule

Sistem ne sme zahtevati odločitve,
če hkrati ne omogoča razumevanja posledic.

HDS obstaja zato,
da je človeška odločitev informirana,
ne zato, da je avtomatizirana.
