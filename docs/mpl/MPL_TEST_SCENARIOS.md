# MPL_TEST_SCENARIOS.md
Status: DEFINICIJA · VEZANA NA F47_LOCK
Namen: Deterministična verifikacija runtime enforcementa
Obseg: En zaprt tok · brez razširitev

Priporočena lokacija:
docs/mpl/MPL_TEST_SCENARIOS.md

---

## 0. SPLOŠNA PRAVILA TESTOV (VELJAJO ZA VSE)

- Test ne sme uporabljati bypassov, allowlist, mock Canona ali “testnih izjem”.
- Vsak korak mora vrniti eksplicitno odločitev (ALLOW / DENY / HALT).
- Če se v kateremkoli testu LLM pokliče, ko ne bi smel → FAIL.
- Če se v kateremkoli testu rezultat posreduje brez preverjanja → FAIL.
- Vsi stop-points (SP) so neizklopljivi.

---

## A. INPUT ENFORCEMENT (SP-1)

### TEST A1 — Prepovedan vhod
Input:
- Zahteva, ki neposredno krši kanonsko prepoved.

Pričakovano:
- SP-1 → DENY
- Proces se ne začne
- LLM ni klican
- Izhod: zavrnitev z razlago razloga

Prepovedano:
- Kakršenkoli nadaljnji korak.

---

### TEST A2 — Dovoljen vhod
Input:
- Zahteva, ki je kanonsko dovoljena.

Pričakovano:
- SP-1 → ALLOW
- Proces se začne
- Prehod na SP-2

Prepovedano:
- Implicitni ALLOW brez zapisane odločitve.

---

## B. LLM CALL GATE (SP-2)

### TEST B1 — Nedovoljen LLM klic
Input:
- Zahteva, ki po Canon-u ne dovoljuje LLM klica.

Pričakovano:
- SP-2 → DENY
- LLM ni klican
- Proces se ustavi

Prepovedano:
- “Soft” preskok ali nadomestni odgovor.

---

### TEST B2 — Dovoljen LLM klic
Input:
- Zahteva, ki dovoljuje LLM klic.

Pričakovano:
- SP-2 → ALLOW
- LLM je klican natanko enkrat
- Prehod na SP-3 po prejemu odgovora

Prepovedano:
- Večkratni klic ali retry brez nove presoje.

---

## C. OUTPUT ENFORCEMENT (SP-3)

### TEST C1 — Nedovoljen LLM izhod
LLM Output:
- Vsebina, ki krši Canon.

Pričakovano:
- SP-3 → DENY
- Izhod ni posredovan
- Proces se ustavi
- Dogodek zabeležen kot kršitev

Opomba:
- To je uspeh testa, ne napaka sistema.

---

### TEST C2 — Dovoljen LLM izhod
LLM Output:
- Vsebina v skladu s Canon-om.

Pričakovano:
- SP-3 → ALLOW
- Izhod se posreduje
- Proces se zaključi korektno

Prepovedano:
- Sprememba izhoda brez zapisane odločitve.

---

## D. NO SILENT DEVIATION (GLOBAL)

### TEST D1 — Manjkajoča potrditev
Scenarij:
- En korak se izvede brez eksplicitne odločitve (ALLOW / DENY).

Pričakovano:
- Sistem se ustavi
- Dogodek označen kot FAIL
- Ni nadaljevanja

---

### TEST D2 — Privzeti ALLOW
Scenarij:
- Poskus nadaljevanja brez preverjanja.

Pričakovano:
- Sistem se ustavi
- Dogodek označen kot FAIL

---

## E. HARD-FAIL SCENARIJI

### TEST E1 — Poskus obhoda
Scenarij:
- Poskus preskoka SP-točke ali ročne eskalacije.

Pričakovano:
- HARD-FAIL
- Proces se prekine
- Dogodek označen kot non-recoverable

---

## F. NEGATIVNI META-TESTI (OBVEZNI)

### TEST F1 — Bypass flag
Scenarij:
- Konfiguracija poskuša omogočiti bypass.

Pričakovano:
- FAIL (MPL ni veljaven)

---

### TEST F2 — Mock Canon
Scenarij:
- Uporaba poenostavljenega ali lažnega Canona.

Pričakovano:
- FAIL

---

## G. KRITERIJ USPEHA MPL

MPL je USPEŠEN, če:
- vsi testi A–F PASS
- ni izjem
- ni “za test” bližnjic
- ni interpretacije

Če en sam test pade → MPL FAIL.

---

## KONČNA IZJAVA

MPL ni dokaz pravilnega delovanja.
MPL je dokaz neobidljivosti.
