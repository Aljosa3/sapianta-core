# INTERACTION REGISTRY SPEC
## Design-Only — v0.5

## Status
DESIGN-ONLY  
Ta dokument ne uvaja kode, izvajanja ali tehničnih mehanizmov.

---

## 1. NAMEN REGISTRYJA

Interaction Registry je **konceptualni normativni mehanizem**, ki določa:
- katere interakcije med moduli so **dovoljene**,
- katere so **prepovedane**,
- pod kakšnimi pogoji se interakcija lahko sploh obravnava.

Registry:
- NE orkestrira modulov,
- NE sproža izvajanja,
- NE združuje prispevkov,
- NE sprejema odločitev.

Njegov edini namen je:
> zagotoviti, da je vsaka interakcija **vnaprej omejena, sledljiva in presojljiva**.

---

## 2. POLOŽAJ V SISTEMU

Interaction Registry deluje:
- **pred runtime izvajanjem**,
- **znotraj Guard presoje**,
- kot referenčni okvir za dovoljene odnose.

Registry:
- nima avtonomije,
- ne deluje samostojno,
- nima vpliva brez Guard Lifecycle.

Brez Registryja:
> runtime ne sme delovati.

---

## 3. DEFINICIJA INTERAKCIJE

### Interakcija (v smislu SAPIANTA)

Interakcija pomeni:
- formalno zaznano situacijo,
- kjer več kot en modul prispeva izhod
- v okviru iste zahteve ali konteksta.

Interakcija:
- NI neposreden klic modula iz modula,
- NI delitev stanja,
- NI koordinacija.

Vsaka interakcija mora biti:
- eksplicitna,
- deklarirana,
- presojena.

---

## 4. DOVOLJENE VRSTE INTERAKCIJ

V v0.5 so **konceptualno dovoljene** naslednje vrste:

### 4.1 Vzporedni prispevki
- več modulov poda **ločene izhode**,
- brez združevanja,
- brez interpretacije.

### 4.2 Sekvenčni prispevki brez odvisnosti
- moduli delujejo zaporedno,
- brez prenosa notranjega stanja,
- vsak modul vidi le vhodni kontekst.

### 4.3 Kontekstualna soprisotnost
- več modulov deluje v istem kontekstu,
- brez medsebojnega zavedanja.

Vse zgoraj je dovoljeno **le, če je skladno s SCF-03**.

---

## 5. IZRECNO PREPOVEDANE INTERAKCIJE

V skladu s SCF-03 je prepovedano:

- neposredno klicanje modulov
- delitev notranjega stanja
- kolektivno odločanje
- koordinacija ciljev
- emergentno vedenje
- implicitne povezave

Vsaka taka zaznava pomeni:
> **DENY brez možnosti prehoda.**

---

## 6. RAZMERJE DO GUARD LIFECYCLE

Interaction Registry:
- NE odloča,
- NE validira samostojno.

Guard Lifecycle:
- uporablja Registry kot **omejevalno referenco**,
- presodi skladnost interakcije,
- izda odločitev (ALLOW / DENY / HOLD).

Registry je:
> pasivna normativna struktura, ne aktivni mehanizem.

---

## 7. RAZMERJE DO RUNTIME-A

Runtime:
- ne obide Registryja,
- ne ustvarja interakcij,
- ne sklepa novih povezav.

Vsak runtime tok, ki vključuje več modulov:
- mora biti predhodno presojan preko Guard + Registry,
- sicer se ustavi na Admission Gate (SCF-04).

---

## 8. SLEDLJIVOST

Vsaka zaznana interakcija mora imeti:
- referenco na kontekst zahteve,
- seznam vključenih modulov,
- tip interakcije,
- rezultat Guard presoje.

Interakcija brez sledljivosti:
> ni dovoljena.

---

## 9. IZRECNE PREPOVEDI (v0.5)

V fazi v0.5 je prepovedano:
- implementirati registry kot kodo,
- ustvarjati dinamične povezave,
- testirati interakcije,
- uporabljati registry kot orkestrator.

Vsaka kršitev pomeni:
> prezgoden prehod iz zasnove v implementacijo.

---

## 10. RAZMERJE DO NASLEDNJIH KORAKOV

Ta dokument je:
- obvezen predpogoj za Guard ↔ Runtime Interface SPEC,
- del zaključnega sklopa v0.5,
- nujen za prihodnjo implementacijo.

Implementacija registryja je dovoljena
šele po:
- v0.5 COMPLETE
- formalni avtorizaciji v0.6.

---

## KONEC DOKUMENTA
