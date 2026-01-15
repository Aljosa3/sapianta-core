# F50_LLM_INTERFACE_POLICY.md
Status: ACTIVE · POST-MPL
Vezano na: F47_LOCK, MPL_LOCK, F48, F49
Namen: Določitev edine dovoljene vmesne politike za dostop do LLM v sistemu Sapianta

---

## 1. NAMEN FAZE F50

Faza F50 določa pravila, pod katerimi sistem Sapianta:
- dostopa do LLM
- uporablja izhod LLM
- omejuje avtoriteto LLM

F50 ne uvaja novih normativnih pravil.
F50 operacionalizira že zaklenjen Canon v odnosu do LLM.

---

## 2. POLOŽAJ LLM V SISTEMU

LLM v sistemu Sapianta:
- ni avtoriteta
- ni odločevalec
- ni izvršilni subjekt

LLM je:
- zunanji vir vsebine
- črna škatla
- predmet presoje, ne njen izvajalec

Vsaka druga interpretacija LLM:
→ je neveljavna

---

## 3. EDINA DOVOLJENA VSTOPNA TOČKA DO LLM

Dostop do LLM je dovoljen samo:

- prek sistema
- prek enotne vmesne točke
- po uspešno opravljenem SP-2 preverjanju

Neposreden dostop do LLM:
- iz chata
- iz modula
- iz zunanjega procesa

→ ni dovoljen

---

## 4. OMEJITVE KLICA LLM

Vsak LLM klic mora izpolnjevati:

1. Jasno določen namen klica
2. Dovoljenje po F47 (SP-2)
3. Enkratnost (brez implicitnih retryjev)
4. Sledljivost klica

Če katerikoli pogoj ni izpolnjen:
→ LLM klic se ne izvede

---

## 5. OBRAVNAVA IZHODA LLM

Izhod LLM:
- nima pravice neposrednega izhoda
- ne predstavlja sistemskega odgovora
- ne more sprožiti izvršitve

Vsak izhod LLM:
- je predmet SP-3 preverjanja
- se obravnava kot vhod v sistem
- je lahko zavrnjen brez nadaljevanja

---

## 6. PREPOVEDI V ODNOSU DO LLM

LLM ne sme:

- določati namena obdelave
- zahtevati ponovnega klica
- vplivati na izbiro modulov
- vplivati na avtoriteto sistema
- obiti runtime enforcement

Vsak poskus:
→ se obravnava kot kršitev

---

## 7. ODNOS DO MODULOV IN CHATA

LLM:
- ne komunicira neposredno z moduli
- ne prejema neposrednega chata
- ne pozna notranje strukture sistema

Vse interakcije:
- posreduje sistem
- so enosmerne
- so predmet preverjanja

---

## 8. ZAVRNITVE IN NAPAKE

Če je LLM klic zavrnjen ali neveljaven:
- sistem se ustavi ali nadaljuje brez LLM
- ne izvaja fallback generacije
- ne nadomešča vsebine

Zavrnitev LLM klica:
- ni napaka sistema
- je pravilno delovanje

---

## 9. ODNOS DO NADALJNJIH FAZ

F50:
- zaključuje sklop F48–F50
- definira mejo do zunanjih generativnih sistemov
- ne odpira novih normativnih vprašanj

Vsak LLM:
- je podrejen F47
- je omejen s F50
- je tehnično zamenljiv brez vpliva na Canon

---

## 10. KONČNA IZJAVA

LLM ni možgani sistema.
LLM je vir.

Sistem Sapianta odloča:
- kdaj posluša
- kaj sprejme
- in kaj zavrne
