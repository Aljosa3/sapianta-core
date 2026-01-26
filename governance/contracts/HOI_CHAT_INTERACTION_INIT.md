# HOI_CHAT_INTERACTION_INIT — Interaction Contract

## Status
INIT

## Version
v1.0

## Parties
- Human Orientation Interface (HOI)
- Sapianta Chat (Interaction / Orchestration Layer)

---

## Purpose

Ta dokument določa interakcijski kontrakt med HOI in Sapianta Chat
z namenom ohranjanja človeške orientacije, legitimnosti nadaljevanja
in skladnosti s Human Orientation Safeguard (HOS).

Kontrakt ne določa implementacije,
temveč meje odgovornosti in prednosti.

---

## Authority and Precedence

- HOI ima prednost pri vseh vprašanjih,
  ki se nanašajo na človeško orientacijo,
  izgubo razumevanja ali nemoč ukrepanja.
- Sapianta Chat mora spoštovati zahteve HOI,
  tudi če to pomeni spremembo ali upočasnitev dialoga.

V primeru konflikta ima HOI prednost pred tekočim dialogom.

---

## Trigger Conditions (Conceptual)

HOI lahko poseže v interakcijo, ko zazna:

- izgubo človeške orientacije glede stanja sistema
- odsotnost možnosti smiselnega ukrepanja
- ponavljajoče se signale nemoči ali zastoja
- nadaljevanje dialoga brez legitimne orientacije

Ti pogoji se obravnavajo kot sistemsko tveganje,
ne kot uporabniška napaka.

---

## Obligations of Sapianta Chat

Ko HOI zazna stanje, ki zahteva orientacijo,
mora Sapianta Chat:

- omogočiti orientacijski način dialoga
- upočasniti ali preusmeriti tekoči pogovor
- zagotoviti jasen povzetek stanja sistema
- ne nadaljevati dialoga, kot da orientacija ni bila izgubljena

Sapianta Chat ne sme obiti ali ignorirati HOI signala.

---

## Limitations

- HOI ne generira vsebine namesto Chata
- HOI ne spreminja sistemskih pravil
- HOI ne izvaja odločitev
- Sapianta Chat ne interpretira HOS samostojno

Vsak modul ohranja svojo avtonomno odgovornost.

---

## Non-Goals

Ta kontrakt ne uvaja:

- samogradnje
- samonadgradnje
- avtomatskih sprememb sistema
- učenja iz dialoga
- eskalacijskih mehanizmov

---

## Governance Alignment

Ta interakcijski kontrakt je skladen z:

- Human Orientation Safeguard (HOS)
- HOI_MODULE_INIT
- SAPIANTA_CHAT_INIT

Vsaka razširitev interakcije mora ohraniti
prednost HOI pri vprašanjih orientacije.

---

## Canonical Principle

Dialog brez človeške orientacije
ni legitimno nadaljevanje sistema.

HOI obstaja zato, da to mejo uveljavlja.
