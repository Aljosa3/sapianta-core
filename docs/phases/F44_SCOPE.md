# F44 — SCOPE
## Dovoljen obseg delovanja sistema SAPIANTA

---

### Status
ACTIVE — NORMATIVE SCOPE DEFINITION

---

## 1. RAZMERJE DO F43

Ta faza neposredno izhaja iz:
- `F43_PURPOSE.md`

F44 ne določa namena sistema, temveč **operativni obseg**, znotraj katerega se namen iz F43 sme udejanjati.

---

## 2. NAMEN FAZE

F44 določa:
> **kaj sistem SAPIANTA sme početi**,  
in s tem posredno tudi,  
> **kaj ni legitimni del njegovega delovanja**.

---

## 3. DOVOLJENI OBSEG (IN-SCOPE)

SAPIANTA sme delovati izključno kot:

1. normativni presojni sistem zahtev
2. posrednik med uporabnikom, AI in izvršilnimi sistemi
3. nadzorni sloj nad inteligentnimi izhodi
4. sistem za zavračanje, omejevanje ali preoblikovanje zahtev
5. sistem za sledljivo beleženje odločitev (intent, trace, policy)

---

## 4. STRUKTURNI OBSEG

SAPIANTA je:
- governance-first sistem
- normativno nadrejen vsem modulom
- odgovoren za *presojo*, ne za *ciljno optimizacijo*
- v osnovi **ne-izvršilni sistem**

Izvršitev je dovoljena **le preko eksplicitno dovoljenih execution modulov**.

---

## 5. IZVEN OBSEGA (OUT-OF-SCOPE)

SAPIANTA ne sodi v področje:

- avtonomnega določanja ciljev
- samostojnega delovanja brez človeka
- spreminjanja normativnih pravil
- prikrite optimizacije rezultatov
- nadomeščanja institucij, zakonodaje ali odgovorne osebe

---

## 6. INTERPRETACIJSKA PREPOVED

Obseg iz F44:
- ni interpretativen
- ni razširljiv brez nove faze
- je zavezujoč za vse module in agente

---

### F44 — ZAKLJUČENA
