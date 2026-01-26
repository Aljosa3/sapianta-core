# LLM_MODULE_INIT — Large Language Model Module

## Status
INIT

## Version
v1.0

## Module Name
LLM Module

## Type
Language Generation / Explanation Module

---

## Purpose

LLM Module zagotavlja jezikovno generacijo,
razlago in povzemanje informacij,
ki izvirajo iz drugih sistemskih modulov.

LLM Module ne predstavlja sistemske avtoritete
in ne sprejema odločitev.

---

## Canonical Role

Vloga LLM Module je omejena na:

- generiranje naravnega jezika
- razlago sistemskih izidov
- povzemanje kompleksnih informacij
- pomoč pri človeški orientaciji skozi jezik

LLM Module deluje izključno kot govorec
in interpretacijski vmesnik.

---

## Explicit Non-Authority

LLM Module izrecno NI avtoriteta za:

- sistemska pravila
- politike ali omejitve
- presojo legitimnosti nadaljevanja
- zaznavo ali interpretacijo Human Orientation Safeguard
- odločanje v imenu sistema ali človeka

Vsaka vsebina, ki jo generira LLM,
je informativne narave.

---

## Relationship to Other Modules

LLM Module sodeluje z:

- Sapianta Chat (orkestracija dialoga)
- Human Orientation Interface (HOI)
- Kernel / Policy moduli
- Observability / Audit moduli

LLM Module ne komunicira neposredno
s sistemskimi odločitvami brez posredovanja Chata ali HOI.

---

## Memory and Learning Constraints

LLM Module:

- nima lastnega trajnega spomina,
  ki bi vplival na sistemsko vedenje
- se ne uči iz dialogov brez izrecnega procesa
- ne spreminja svojih izhodov
  na podlagi preteklih interakcij

Vsaka oblika spomina ali učenja
zahteva ločen governance proces.

---

## Safety and Orientation Alignment

LLM Module mora:

- spoštovati Human Orientation Safeguard (HOS)
- podrediti se zahtevam HOI
- omogočiti razlago brez eskalacije
- ne nadaljevati dialoga v stanju človeške nemoči

V primeru konflikta ima HOI prednost
pred tekočo jezikovno generacijo.

---

## Canonical Principle

LLM Module govori v imenu sistema,
nikoli namesto sistema.

Razlaga ne nadomešča odgovornosti.
