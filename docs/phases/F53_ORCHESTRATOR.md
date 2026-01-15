# F53_ORCHESTRATOR.md
Status: ACTIVE · EXECUTION ERA
Vezano na: F47_LOCK, MPL_LOCK, F48_50_LOCK, F51_LOCK, F52
Namen: Definicija Orchestratorja kot nevtralnega izvajalca zaporedja na podlagi Execution Contexta

---

## 1. NAMEN FAZE F53

Faza F53 definira Orchestrator kot komponento, ki:
- bere Execution Context
- izvaja zaporedje tehničnih korakov
- nikoli ne odloča o pravilnosti ali dovoljenosti

Orchestrator:
- ne uvaja novih pravil
- ne interpretira Canona
- ne spreminja preteklih odločitev

Njegova naloga je izključno **izvedbena koordinacija**.

---

## 2. POLOŽAJ ORCHESTRATORJA V SISTEMU

Orchestrator se nahaja:
- po uspešno ustvarjenem Execution Contextu
- po zaključenih preverjanjih (SP-1 / SP-2 / SP-3)
- pred dejansko izvedbo modulov ali zunanjih klicev

Orchestrator:
- nikoli ne deluje brez Execution Contexta
- nikoli ne ustvarja novega konteksta
- nikoli ne nadaljuje po FINAL stanju

---

## 3. VHOD IN IZHOD ORCHESTRATORJA

### 3.1 Vhod
- en (1) Execution Context
- stanje mora biti ALLOW
- faza mora biti EXECUTION

Če vhodni pogoji niso izpolnjeni:
→ Orchestrator se ne zažene

### 3.2 Izhod
- posodobljen Execution Context
- dodani zapisi o izvedenih korakih
- morebiten rezultat ali napaka

Orchestrator ne proizvaja neposrednega uporabniškega izhoda.

---

## 4. ODGOVORNOSTI ORCHESTRATORJA

Orchestrator je odgovoren za:

1. Branje trenutnega stanja konteksta
2. Izbor naslednjega tehničnega koraka
3. Klic dovoljenih komponent (modul / LLM / nič)
4. Beleženje poteka v Execution Context
5. Zaključek ali predajo rezultata

Orchestrator ni odgovoren za:
- preverjanje pravil
- interpretacijo vhodov
- odločanje o dovoljenosti

---

## 5. ZAPOREDJE IZVAJANJA

Tipično zaporedje:

1. Preveri stanje konteksta
2. Preveri, ali obstaja nadaljnji korak
3. Izvede korak
4. Zabeleži izid
5. Posodobi fazo ali status
6. Ponovi ali zaključi

Zaporedje je:
- deterministično
- linearno
- brez implicitnih preskokov

---

## 6. OBRAVNAVA NAPAK

Če pride do napake med izvajanjem:
- Orchestrator zabeleži napako
- nastavi status na HALT ali HARD_FAIL
- zaključi izvajanje

Orchestrator:
- ne poskuša samodejnih popravil
- ne izvaja retryjev
- ne nadomešča izhodov

---

## 7. ODNOS DO MODULOV IN LLM

### 7.1 Moduli
Orchestrator:
- kliče samo module, sprejete po F48
- kliče module prek definiranih vmesnikov
- ne posreduje več podatkov, kot je dovoljeno

### 7.2 LLM
Orchestrator:
- kliče LLM samo prek F50 vmesnika
- ne interpretira izhoda LLM
- posreduje izhod kot vhod v nadaljnjo obravnavo

---

## 8. INTEGRITETA IN OMEJITVE

Orchestrator ne sme:
- spreminjati zgodovine konteksta
- ustvarjati stranskih učinkov zunaj konteksta
- vplivati na audit zapise
- obiti runtime enforcement

Vsak tak poskus:
→ je neveljaven

---

## 9. RAZMERJE DO IMPLEMENTACIJE

Ta dokument:
- definira odgovornosti in meje
- ne določa algoritmov
- ne določa tehničnega okolja

Implementacija Orchestratorja:
- mora slediti Execution Contextu
- mora biti zamenljiva
- ne sme razširiti svoje avtoritete

---

## 10. KONČNA IZJAVA

Orchestrator ne misli.
Orchestrator ne presoja.

Orchestrator bere sled
in jo izvaja.
