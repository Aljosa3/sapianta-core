# F49_CHAT_ENTRY_CONSTRAINTS.md
Status: ACTIVE · POST-MPL
Vezano na: F47_LOCK, MPL_LOCK, F48
Namen: Določitev omejitev in pravil za vstop chat interakcij v sistem Sapianta

---

## 1. NAMEN FAZE F49

Faza F49 določa pogoje, pod katerimi je chat interakcija:
- sprejeta v sistem
- obravnavana v runtime toku
- posredovana proti LLM ali modulom

F49 ne uvaja novih normativnih pravil.
F49 operacionalizira že zaklenjen Canon in module, sprejete po F48.

---

## 2. DEFINICIJA CHAT VHODA

Chat vhod je vsak uporabniški ali sistemski vnos, ki:
- vstopa v sistem prek komunikacijskega vmesnika
- lahko sproži procesiranje ali predlog dejanja
- ni del notranje sistemske logike

Chat vhod:
- nima avtoritete
- ne določa namena obdelave
- ne more zahtevati obida pravil

---

## 3. OSNOVNI POGOJI ZA SPREJEM CHAT VHODA

Chat vhod je sprejet v obravnavo samo, če:

1. Ima jasno določljiv izvor (user / system / module)
2. Je tehnično veljaven (format, velikost, kodiranje)
3. Ne vsebuje neposredne kanonske prepovedi
4. Se lahko v celoti podredi F47 runtime enforcementu

Če katerikoli pogoj ni izpolnjen:
→ chat vhod se zavrne

---

## 4. NAMENSKA NEVTRALNOST CHAT VHODA

Chat vhod:
- ne določa namena obdelave
- ne določa cilja sistema
- ne sproži izvršitve sam po sebi

Namen obdelave:
- določi sistem
- v skladu s Canon-om
- ob upoštevanju aktivnih modulov

Vsak poskus, da chat vhod vsili namen:
→ se obravnava kot kršitev

---

## 5. OMEJITVE CHAT VHODA

Chat vhod ne sme:

- zahtevati neposrednega klica LLM
- zahtevati aktivacije modula
- zahtevati spremembe avtoritete
- vsebovati navodil za obid sistema
- določati zaporedja obdelave

Vsaka takšna zahteva:
→ se ignorira ali zavrne

---

## 6. ODNOS CHAT VHODA DO MODULOV

Chat vhod:
- ne komunicira neposredno z moduli
- ne pozna obstoja modulov
- ne usmerja izbire modulov

Izbiro modulov:
- določi sistem
- v skladu s F48
- pod polnim runtime enforcementom

---

## 7. ODNOS CHAT VHODA DO LLM

Chat vhod:
- nima neposrednega dostopa do LLM
- ne more zahtevati LLM klica
- ne določa vsebine prompta

Vsak LLM klic:
- je odločitev sistema
- je predmet SP-2 preverjanja
- je zabeležen in preverjen

---

## 8. OBRAVNAVA ZAVRNITEV

Če je chat vhod zavrnjen:
- sistem lahko vrne razlago
- razlaga ne razkriva notranje logike
- zavrnitev ne sproži nadaljnje obdelave

Zavrnitev je končna za ta vhod.

---

## 9. ODNOS DO NADALJNJIH FAZ

F49:
- predhaja F50_LLM_INTERFACE_POLICY
- se uporablja pred vsakim LLM klicem
- ne spreminja pravil modulov

Vsak chat vhod:
- je podrejen F47
- se obravnava pred aktivacijo modulov in LLM

---

## 10. KONČNA IZJAVA

Chat ni ukaz.
Chat je vhod.

Sistem Sapianta odloča:
- kaj pomeni vhod
- ali se obravnava
- in kako daleč sme iti
