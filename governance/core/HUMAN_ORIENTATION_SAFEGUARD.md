# HUMAN ORIENTATION SAFEGUARD (HOS)

## Status
ACTIVE — Canonical Governance Rule

## Version
v1.0

## Type
Normative / Safety / Human-in-the-loop safeguard

---

## Definition

Human Orientation Safeguard določa, da se sistem ne sme nadaljevati,
dokler človeški nadzornik nima jasne orientacije o stanju sistema
in možnosti smiselnega ukrepanja.

V takem stanju mora sistem omogočiti ponovno orientacijo
ali varno preusmeritev toka.

---

## Purpose

Namen Human Orientation Safeguard je preprečiti stanje človeške nemoči,
v katerem bi sistem nadaljeval delovanje brez legitimnega človeškega nadzora.

Pravilo varuje legitimnost sistema, ne njegovo učinkovitost.

---

## Scope

Pravilo se uporablja za vse sistemske procese,
kjer je prisoten človeški nadzor, odločanje ali odgovornost,
ne glede na stopnjo avtomatizacije.

---

## Trigger Conditions (Conceptual)

Human Orientation Safeguard se sproži, ko so hkrati izpolnjeni naslednji pogoji:

- človeški nadzornik nima jasnega razumevanja stanja sistema
- človeški nadzornik nima možnosti smiselnega ukrepanja
- sistem bi sicer nadaljeval proces brez spremembe režima

To stanje se obravnava kot sistemsko tveganje,
ne kot uporabniška napaka.

---

## System Obligation

Ko je Human Orientation Safeguard sprožen, sistem:

- ne sme nadaljevati obstoječega toka delovanja
- mora omogočiti ponovno orientacijo ali varno preusmeritev procesa
- ne sme samodejno spreminjati svojih pravil ali vedenja

---

## Explicit Non-Goals

Human Orientation Safeguard:

- ne zahteva zaustavitve sistema
- ne pomeni napake ali fail-stanja
- ne zahteva učenja, adaptacije ali samonadgradnje
- ne prenaša odgovornosti s človeka na sistem

---

## Canonical Principle

Brez človeške orientacije in možnosti ukrepanja
nadaljevanje sistema ni legitimno.

---

## Notes

Implementacija pravila ni predpisana.
Način zaznave in izvedbe preusmeritve je odvisen od konteksta sistema,
vendar ne sme kršiti tega pravila.
