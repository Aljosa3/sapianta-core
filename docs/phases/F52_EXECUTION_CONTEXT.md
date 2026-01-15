# F52_EXECUTION_CONTEXT.md
Status: ACTIVE · EXECUTION ERA
Vezano na: F47_LOCK, MPL_LOCK, F48_50_LOCK, F51_LOCK
Namen: Definicija Execution Context kot edinega nosilca stanja med izvajanjem

---

## 1. NAMEN FAZE F52

Faza F52 definira Execution Context kot:
- edini nosilec stanja zahteve
- edini objekt, ki se premika skozi sistem
- edini vir resnice o poteku izvajanja

Execution Context:
- ne odloča
- ne interpretira pravil
- ne vsebuje poslovne logike

Njegova vloga je izključno nosilna in sledljiva.

---

## 2. DEFINICIJA EXECUTION CONTEXT

Execution Context je strukturiran objekt, ki:
- nastane ob vstopu zahteve v sistem
- spremlja zahtevo skozi vse faze
- se zaključi z enim končnim izidom

Vsaka zahteva ima točno en Execution Context.
Execution Context nikoli ne obstaja brez zahteve.

---

## 3. OBVEZNA POLJA EXECUTION CONTEXTA

Execution Context mora vsebovati najmanj naslednja polja:

### 3.1 Identiteta
- `context_id` – enolični identifikator
- `created_at` – čas nastanka
- `source` – izvor zahteve (chat / module / system)

### 3.2 Stanje
- `status` – trenutno stanje (PENDING / ALLOW / DENY / HALT / HARD_FAIL)
- `phase` – zadnja dosežena faza (SP-1, SP-2, SP-3, EXECUTION, FINAL)

### 3.3 Vsebina
- `input` – originalni vhod (nespremenjen)
- `normalized_input` – tehnično normaliziran vhod

### 3.4 Odločitveni zapisi
- `decisions` – seznam sprejetih odločitev (časovno urejen)
- `violations` – zaznane kršitve (če obstajajo)

### 3.5 Rezultat
- `result` – končni rezultat (če obstaja)
- `error` – napaka ali razlog prekinitve (če obstaja)

---

## 4. ŽIVLJENJSKI CIKEL EXECUTION CONTEXTA

Execution Context ima naslednji življenjski cikel:

1. Ustvarjanje (PENDING)
2. Preverjanje (SP-1 / SP-2 / SP-3)
3. Izvajanje ali zaustavitev
4. Zaključek (FINAL)

Ko Execution Context doseže stanje FINAL:
- se ne sme več spreminjati
- se lahko samo bere
- se lahko audita

---

## 5. NEPREMENSKOST IN INTEGRITETA

Execution Context:
- se ne briše
- se ne prepisuje
- se ne resetira

Vsaka sprememba:
- mora biti dodajanje
- mora biti časovno sledljiva
- mora biti deterministična

Retroaktivne spremembe:
→ niso dovoljene

---

## 6. ODNOS DO OSTALEGA SISTEMA

### 6.1 Runtime Enforcement
Runtime enforcement (F47):
- bere Execution Context
- posodablja status in fazo
- nikoli ne ustvari novega konteksta

### 6.2 Orchestrator
Orchestrator:
- prejme Execution Context
- deluje izključno na podlagi njegovega stanja
- ne spreminja preteklih zapisov

### 6.3 Audit / Explain Layer
Audit sloj:
- bere Execution Context
- ne vpliva na njegovo stanje
- ne sodeluje v runtime toku

---

## 7. PREPOVEDI

Execution Context ne sme:
- vsebovati normativnih pravil
- vsebovati logike odločanja
- vplivati na zaporedje faz
- sprožiti izvajanja sam po sebi

Vsak poskus take uporabe:
→ je neveljaven

---

## 8. RAZMERJE DO IMPLEMENTACIJE

Ta dokument:
- definira strukturo in odgovornost
- ne predpisuje jezika ali podatkovnega formata
- ne določa fizične implementacije

Vsaka implementacija:
- mora biti skladna s to definicijo
- ne sme razširiti avtoritete Execution Contexta

---

## 9. KONČNA IZJAVA

Če se sistem premika,
se premika Execution Context.

Če se Execution Context ustavi,
se sistem ustavi.

Execution Context je sled.
Sled je resnica.
