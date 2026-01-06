# EXECUTION ERA — ENTRY CRITERIA

## Status
DESIGN-ONLY — execution ni dovoljen

## Namen dokumenta
Ta dokument definira **vstopne pogoje** za začetek Execution Ere v sistemu SAPIANTA.
Dokler vsi kriteriji niso izpolnjeni ali načrtovani, je **vsak execution prepovedan**.

Dokument se eksplicitno sklicuje na:
- LOCK_PRE_EXECUTION_ERA

---

## 1. Arhitekturni kriteriji

- [x] Pre-Execution Era (FAZE 17–19) je zaklenjena
- [x] Chat / Reasoning / Planning pipeline ostaja nespremenjen
- [ ] Execution sloj je jasno definiran kot *nadrejeni potrošnik*
- [ ] Noben execution modul nima dostopa do notranjosti Orchestratorja
- [ ] Execution se ne more priklopiti med obstoječe sloje

Status: ⬜ NAČRTOVANO

---

## 2. Semantični kriteriji

- [x] Razlika med Intent in Action je jasno definirana
- [x] Razlika med Plan (konceptualen) in Task (izvedljiv) je jasno ločena
- [ ] Execution prejema izključno strukturirane objekte
- [ ] Naravni jezik se nikoli ne interpretira neposredno v executionu

Status: ⬜ NAČRTOVANO

---

## 3. Varnostni kriteriji

- [ ] Obstaja Execution Boundary dokument (kaj je načeloma dovoljeno)
- [ ] Fail-Closed politika je definirana (nejasno → ne izvrši)
- [ ] Audit-first logika je obvezna
- [ ] Human-in-the-loop točka je definirana

Status: ⬜ NAČRTOVANO

---

## 4. Operativni kriteriji

- [ ] Definiran je Execution Context (čas, vir, namen)
- [ ] Definiran je Execution Result model (success / fail / partial)
- [ ] Obstaja rollback koncept (tudi če še ni implementiran)
- [ ] Idempotence je jasno opredeljena

Status: ⬜ NAČRTOVANO

---

## 5. Governance kriteriji

- [x] Obstaja LOCK_PRE_EXECUTION_ERA
- [ ] Execution Era ima lasten lock dokument
- [ ] Vsi execution moduli se sklicujejo na governance
- [ ] Vsaka execution faza je verzionirana in tagirana

Status: ⬜ NAČRTOVANO

---

## 6. Prepovedi do izpolnitve kriterijev

Dokler ta dokument ni potrjen kot IZPOLNJEN:

- [x] Prepovedano je pisati execution kodo
- [x] Prepovedano je dodajati permission sisteme
- [x] Prepovedano je avtomatizirati dejanja
- [x] Prepovedano je povezovanje zunanjih sistemov

---

## 7. Formalni signal za začetek Execution Ere

Execution Era se lahko začne šele, ko:

- ta dokument doseže status **IZPOLNJENO**
- obstaja commit, ki potrjuje izpolnitev
- obstaja tag, ki označuje začetek Execution Ere

Do takrat sistem ostaja v **Pre-Execution + Design-only načinu**.

---

Dokument potrjen kot referenca.
Execution Era še NI aktivna.
