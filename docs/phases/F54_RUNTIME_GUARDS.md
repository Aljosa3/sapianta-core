# F54_RUNTIME_GUARDS.md
Status: ACTIVE · EXECUTION ERA
Vezano na: F47_LOCK, MPL_LOCK, F48_50_LOCK, F51_LOCK, F52, F53
Namen: Tehnična implementacija runtime zaščit (guards), ki uveljavljajo Canon med izvajanjem

---

## 1. NAMEN FAZE F54

Faza F54 definira Runtime Guards kot:
- niz tehničnih zaščit
- trde kontrolne točke
- neposredno uveljavitev Canona med izvajanjem

Runtime Guards:
- ne interpretirajo pravil
- ne odločajo
- ne predlagajo alternativ

Njihova naloga je **zaustavitev**, ne presoja.

---

## 2. POLOŽAJ RUNTIME GUARDS V SISTEMU

Runtime Guards se izvajajo:
- ob vsaki spremembi faze Execution Contexta
- pred vsakim klicem modula
- pred vsakim klicem LLM
- pred vsakim izhodom iz sistema

Runtime Guards:
- berejo Execution Context
- delujejo sinhrono
- nimajo trajnega stanja

---

## 3. VRSTE RUNTIME GUARDS

### 3.1 ASSERTION GUARDS
- preverjajo predpogoje
- preverjajo stanje konteksta
- preverjajo fazo in status

Če assertion pade:
→ HARD_FAIL

---

### 3.2 PERMISSION GUARDS
- preverjajo dovoljenost klica
- preverjajo skladnost s F48, F49, F50
- preverjajo izvor zahteve

Če dovoljenje ni potrjeno:
→ DENY ali HALT

---

### 3.3 BOUNDARY GUARDS
- preprečujejo izhod iz dovoljenega toka
- preprečujejo preskakovanje faz
- preprečujejo rekurzijo ali zanko

Če je meja kršena:
→ HALT

---

## 4. ODGOVORNOSTI RUNTIME GUARDS

Runtime Guards so odgovorni za:
- takojšnjo zaznavo kršitve
- nastavitev ustreznega statusa
- zapis kršitve v Execution Context
- zaustavitev nadaljnjega izvajanja

Runtime Guards niso odgovorni za:
- razlago kršitve (F51)
- popravljanje napak
- nadaljevanje toka

---

## 5. NAČIN IZVAJANJA

Runtime Guards:
- se izvajajo deterministično
- se ne izklapljajo
- se ne obidejo
- nimajo konfiguracijskih zastavic

Vsak poskus obida:
→ je kršitev sama po sebi

---

## 6. OBRAVNAVA KRŠITEV

Ob zaznani kršitvi:

1. Nastavi se status (DENY / HALT / HARD_FAIL)
2. Zabeleži se kršitev
3. Execution Context preide v FINAL
4. Orchestrator se ustavi

Ni fallbacka.
Ni degradacije.
Ni nadaljevanja.

---

## 7. ODNOS DO DRUGIH KOMPONENT

### 7.1 Orchestrator
- Orchestrator ne more preskočiti guards
- Guards se izvajajo pred vsakim korakom

### 7.2 Moduli
- Moduli so podrejeni guards
- Guards preverjajo vsak modul klic

### 7.3 LLM
- Guards se izvajajo pred in po LLM klicu
- Izhod LLM je ponovno preverjen

---

## 8. RAZMERJE DO IMPLEMENTACIJE

Ta dokument:
- definira obvezne kontrolne točke
- ne predpisuje sintakse
- ne predpisuje jezika

Implementacija:
- mora biti centralizirana
- mora biti testabilna
- mora biti neizklopljiva

---

## 9. PREPOVEDI

Runtime Guards ne smejo:
- biti pogojni
- biti izklopljivi
- biti asinhroni
- imeti stranske učinke

Vsaka taka implementacija:
→ je neveljavna

---

## 10. KONČNA IZJAVA

Runtime Guards niso logika.
Runtime Guards so meja.

Če guard pade,
sistem stoji.
