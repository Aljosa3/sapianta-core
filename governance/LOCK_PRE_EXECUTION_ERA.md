# LOCK: PRE-EXECUTION ERA (FAZE 17–19)

## Status
ZAKLENJENO — dokončno

## Obseg zaklepa
Ta dokument formalno zaklepa razvojno obdobje sistema SAPIANTA,
imenovano **Pre-Execution Era**, ki zajema naslednje faze:

- FAZA 17 — Chat Module (komunikacijski sloj)
- FAZA 18 — Reasoning Layer (razlagalne strategije)
- FAZA 19 — Planning Layer (konceptualni načrti)

Vse navedene faze so:
- implementirane
- commitane
- tagirane
- uspešno testirane

## Temeljna lastnost Pre-Execution Ere
Sistem v tem obdobju:
- NE izvaja nobenih dejanj
- NE spreminja stanja
- NE upravlja dovoljenj
- NE vsebuje execution logike
- NE vsebuje permission ali security gate-ov

Vse funkcionalnosti so:
- pasivne
- razlagalne
- konceptualne
- deterministične

## Arhitekturni pipeline (zaklenjen)

User Input
↓
Chat Router
↓
Chat Orchestrator
↓
Reasoning Layer (kako razložiti)
↓
Planning Layer (kako bi bilo strukturirano)
↓
Chat Response


Ta pipeline je zaklenjen in se ne spreminja.

## Pravila po zaklepu
Po tem zaklepu velja:

- Nobena FAZA 17–19 se ne spreminja več
- Nobena funkcionalnost se ne dodaja za nazaj
- Vsi prihodnji execution ali permission moduli
  se morajo priklopiti **nad** tem slojem
- Pre-Execution Era služi kot stabilna referenčna osnova

## Dovoljeni posegi
Dovoljeni so izključno:
- bugfixi, ki ne spreminjajo arhitekture
- varnostni popravki brez funkcionalnih sprememb
- dokumentacijski popravki

## Prepovedani posegi
Prepovedano je:
- dodajanje execution logike
- dodajanje permission ali policy logike
- spreminjanje odgovornosti obstoječih slojev
- refaktoriranje pipeline-a

## Namen zaklepa
Namen tega zaklepa je:
- zagotoviti stabilno, nespremenljivo osnovo
- jasno ločiti razmišljanje od delovanja
- omogočiti varen prehod v Execution Era v prihodnjih fazah

---

Zaklep potrjen.

SAPIANTA — Pre-Execution Era je zaključena.
