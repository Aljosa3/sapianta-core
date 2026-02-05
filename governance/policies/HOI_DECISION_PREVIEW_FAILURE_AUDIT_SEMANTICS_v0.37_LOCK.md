PATH: governance/policies/HOI_DECISION_PREVIEW_FAILURE_AUDIT_SEMANTICS_v0.37_LOCK.md

# HOI_DECISION_PREVIEW_FAILURE_AUDIT_SEMANTICS_v0.37_LOCK

Status: LOCK-READY
Layer: HOI → Decision Preview
Mode: READ-ONLY
Paraphrase: DISALLOWED
Interpretation: DISALLOWED

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno določa **semantiko FAIL stanj** in **njihovo interno evidentiranje (audit)** za *Decision Preview*.

Dokument:

- dopolnjuje v0.35 (Validator Enforcement Boundary)
- dopolnjuje v0.36 (Runtime Integration Contract)
- formalizira FAIL kot **neuporabniški, interni dogodek**
- določa minimalni audit zapis brez razkritja vsebine

Dokument ne:

- razlaga validacijskih pravil
- opisuje UX ali obnašanje uporabnika
- uvaja retry, fallback ali eskalacijske mehanizme
- razkriva vsebino izpisa ali razloge za FAIL

---

## 2. DEFINICIJA FAIL DOGODKA

2.1. FAIL dogodek nastopi izključno, ko:

- validator (v0.35) vrne rezultat **FAIL**

2.2. FAIL dogodek:

- **NI** runtime napaka
- **NI** exception
- **NI** uporabniški signal

2.3. FAIL dogodek je:

- interni sistemski dogodek
- evidenčni signal
- terminalen za konkreten Decision Preview

---

## 3. RAZMERJE FAIL / ERROR / EXCEPTION

3.1. FAIL:
- pomeni neskladnost z normativnimi pravili
- ne sproži napake v runtime toku
- ne prekine sistema

3.2. ERROR:
- pomeni napako v delovanju sistema
- se obravnava izven področja Decision Preview
- **NI** predmet tega dokumenta

3.3. EXCEPTION:
- pomeni nepričakovano stanje izvajanja
- se obravnava izven področja Decision Preview
- **NI** predmet tega dokumenta

3.4. FAIL **NE SME** biti:
- preoblikovan v ERROR
- eskaliran v EXCEPTION

---

## 4. PROPAGACIJA FAIL DOGODKA

4.1. Ob nastopu FAIL:

- runtime tok *Decision Preview* se zaključi
- izpis se ne prikaže (NO-OUTPUT)

4.2. FAIL se propagira:

- izključno interno
- brez vpliva na uporabniški tok
- brez povratnih informacij uporabniku

4.3. FAIL **NE SME**:

- vplivati na nadaljnje zahteve
- vplivati na stanje uporabnika
- vplivati na druge module

---

## 5. AUDIT DOGODEK

5.1. Vsak FAIL dogodek **MORA** ustvariti en audit dogodek.

5.2. Audit dogodek je:

- minimalen
- strojno berljiv
- vsebinsko nevtralen

5.3. Audit dogodek **NE SME**:

- vsebovati vsebine Decision Preview
- vsebovati razloge za FAIL
- vsebovati uporabniških podatkov

---

## 6. MINIMALNA STRUKTURA AUDIT ZAPISA

Audit zapis **MORA** vsebovati izključno:

- tip dogodka: `DECISION_PREVIEW_VALIDATION_FAIL`
- časovni žig dogodka
- identifikator zahteve (tehnični)
- identifikator verzije pravil (v0.34)

Audit zapis **NE SME** vsebovati:

- besedila izpisa
- prepovedanih ali dovoljenih nizov
- opisnih ali razlagalnih polj

---

## 7. SHRANJEVANJE IN DOSTOP DO AUDITA

7.1. Audit zapis:

- se shrani v interni audit sloj
- ni dostopen HOI v runtime kontekstu
- ni dostopen uporabniku

7.2. Audit zapisi so namenjeni:

- nadzoru skladnosti
- forenzični analizi
- statistični obdelavi

7.3. Audit zapisi **NE SMEJO**:

- vplivati na runtime odločanje
- sprožiti dodatnih akcij
- biti uporabljeni za učenje ali prilagajanje HOI

---

## 8. PREPOVED INTERPRETACIJE FAIL

8.1. HOI **NE SME**:

- interpretirati FAIL dogodka
- sklepati o razlogih FAIL
- prilagajati vedenja na podlagi FAIL

8.2. FAIL je **zaključen dogodek** brez nadaljnjih posledic.

---

## 9. VALIDACIJA AUDIT SEMANTIKE

9.1. Sistem je skladen z v0.37, če in samo če:

- vsak FAIL ustvari en audit zapis
- noben audit zapis ne razkriva vsebine
- FAIL nima uporabniškega učinka

9.2. Kršitev katerega koli pravila pomeni:

- kršitev v0.37
- neveljavno delovanje sistema

---

## 10. KONČNA DOLOČBA

10.1. FAIL v *Decision Preview* obstaja izključno kot:

- interni signal
- audit dogodek
- evidenčna točka

10.2. Za uporabnika FAIL **NE OBSTAJA**.

10.3. Vsak drugačen pomen FAIL pomeni:
- kršitev v0.37
- kršitev verige v0.34 → v0.37

---
