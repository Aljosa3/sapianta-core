# HDS_CHAT_SHELL v0.2 — LOCK

Status: LOCKED  
Datum: 2026-01-26  
Veljavnost: kanonična  
Spremembe: prepovedane brez nove faze

---

## 1. Scope

Ta dokument zaklepa modul **HDS Chat Shell v0.2** kot
razširitev v0.1 z izključno **Explain-on-Demand** funkcionalnostjo.

Razširitev je namenjena:
- dodatni razlagi že predstavljenih možnosti
- izboljšanju razumevanja brez spremembe moči odločanja

Razširitev NI namenjena:
- ustvarjanju novih možnosti
- spreminjanju ali rangiranju obstoječih možnosti
- implicitnemu ali eksplicitnemu usmerjanju odločitev

---

## 2. Hard Constraints (NON-NEGOTIABLE)

Naslednje omejitve so absolutne in ohranjene iz v0.1:

- NO sensing
- NO signal inference
- NO adaptation
- NO memory
- NO state persistence
- NO autonomous decision-making
- NO recommendation authority
- NO optimality claims

Vsaka kršitev pomeni **neveljavno implementacijo**.

---

## 3. Explain-on-Demand Semantics

Dovoljeni so izključno naslednji ukazi:

- `why <n>` — dodatna razlaga razloga
- `expand <n>` — razširjene kvalitativne posledice
- `uncertainty <n>` — poglobljena razlaga negotovosti

Semantika:
- razlaga se nanaša **izključno** na že izpisano možnost
- razlaga ne spreminja vsebine možnosti
- ponavljanje ukazov nima kumulativnega učinka
- razlaga je vedno nezavezujoča

---

## 4. Role Preservation

### HOI — Human Orientation Interface
- absolutna legitimnostna prednost
- PAUSE je terminalen
- brez sprememb glede na v0.1

### HDS — Human Decision Support
- zahteva dodatno razlago
- ne ustvarja novih predlogov
- ne spreminja obstoječih možnosti

### LLM — Language Model
- generira razlago na zahtevo
- brez implicitne avtoritete
- vedno ohranja razkritje negotovosti
- vedno potrdi, da je odločitev na človeku

---

## 5. Forbidden Behaviors

Prepovedano je:

- razlago uporabiti kot prikrito priporočilo
- stopnjevanje razlage v usmerjanje
- ustvarjanje implicitne prioritete z večkratnimi razlagami
- kakršnokoli odločanje namesto človeka

---

## 6. Audit Compatibility

- Explain-on-Demand je popolnoma združljiv z Audit Harness v0.1
- razširitve ne uvajajo novega nadzora ali interpretacije
- vsi izhodi so auditabilni prek stdout zajema

---

## 7. Version Lock

- Ta dokument zaklepa verzijo **v0.2**
- v0.1 ostane nespremenjen in zaklenjen
- nadaljnje razširitve zahtevajo:
  - novo INIT fazo
  - nov LOCK dokument

---

LOCK CONFIRMED.
