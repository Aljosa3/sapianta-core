# HOI_DECISION_PREVIEW_CONTRACT_v0.32_LOCK

Status: LOCKED  
Phase: v0.32  
Layer: HOI (Human Orientation Interface)  
Scope: Decision Preview (READ-ONLY)  
Supersedes: none  
Depends on:
- HOI Runtime Contract v0.30 (LOCKED)
- HOI Runtime Stub v0.31 (LOCKED)
- Decision Preview v0.27 (LOCKED)

---

## 1. NAMEN DOKUMENTA

Ta dokument normativno definira, kako se **HOI Runtime** v fazi v0.32
lahko poveže z obstoječim **Decision Preview** sistemom
na **strogo read-only** način.

Cilj NI izboljšati odločanje.
Cilj NI pomagati izbrati.
Cilj je izključno omogočiti **orientacijski vpogled v posledice**,
če uporabnik sam predlaga odločitev.

---

## 2. TEMELJNA LOČITEV POJMOV (NEPREKLICNA)

V sistemu SAPIANTA veljajo naslednje neodvisne ravni:

- **Orientacija** → HOI
- **Odločitev** → Človek
- **Posledica** → Decision Preview

Te ravni se **ne smejo združiti**, približati ali implicitno povezati.

HOI:
- ne odloča
- ne priporoča
- ne vrednoti
- ne filtrira poti
- ne ustvarja CDR

Decision Preview:
- ne odloča
- ne sugerira
- ne optimizira
- ne rangira
- ne prevzema odgovornosti

Vsak poskus združitve orientacije in odločitve
se šteje kot **prepovedan zdrs v agentnost**.

---

## 3. DOVOLJENA VLOGA HOI V v0.32

HOI sme v tej fazi izvajati izključno naslednje funkcije:

- sprejeti **eksplicitno uporabnikovo hipotezo**
- preveriti, ali je zahteva **preview-eligible**
- posredovati zahtevo v Decision Preview
- predstaviti rezultat **brez interpretacije**

HOI NE SME:
- predlagati hipoteze
- popravljati uporabnikove odločitve
- opozarjati na “boljše” možnosti
- zoževati nabor odločitev
- ustvarjati implicitnega “pritiska k izbiri”

---

## 4. AKTIVACIJA DECISION PREVIEW

### 4.1 DOVOLJENA AKTIVACIJA

Decision Preview se sme sprožiti IZKLJUČNO,
če uporabnik poda zahtevo v obliki:

- “Če bi se odločil za X, kaj bi to pomenilo?”
- “Kaj se zgodi, če izvedem X?”
- “Prikaži posledice odločitve X”

Zahteva mora vsebovati:
- jasno identificirano odločitev X
- brez vprašanj o pravilnosti
- brez primerjav z alternativami

---

### 4.2 OBVEZNA ZAVRNITEV PREVIEW

HOI MORA zavrniti preview, če zazna:

- vprašanje tipa “Kaj je boljše?”
- vprašanje tipa “Kaj priporočaš?”
- implicitno primerjavo (“ali X ali Y?”)
- zahtevo po optimizaciji
- zahtevo po rangiranju
- zahtevo po oceni tveganja v vrednostnem smislu

Zavrnitev mora biti:
- kratka
- nevtralna
- brez razlage “zakaj je nekaj slabo”

Primer zavrnitve:
> “HOI v tej fazi ne primerja odločitev. Lahko prikažem posledice ene konkretne odločitve, če jo jasno opredeliš.”

---

## 5. PRAVILA PREZENTACIJE PREVIEW

Vsak prikaz Decision Preview mora OBVEZNO vsebovati:

### 5.1 OZNAKO SIMULACIJE

Preview mora biti jasno označen kot:

- simulacija
- hipotetični izračun
- nedejansko stanje

Prepovedani izrazi:
- “to pomeni, da je smiselno…”
- “to kaže, da bi moral…”
- “najboljša možnost je…”

---

### 5.2 NEVREDNOTENJE

HOI NE SME:
- dodajati interpretacije
- dodajati opozoril v smislu priporočil
- poudarjati pozitivnih ali negativnih izidov

Dovoljen je samo **deskriptiven prikaz stanja**.

---

### 5.3 LOČITEV ODGOVORNOSTI

Na koncu vsakega preview mora biti eksplicitno zapisano:

> “To je simulacija posledic.  
> Odločitev in odgovornost zanjo ostajata izključno pri uporabniku.”

To besedilo je **obvezno** in se ne sme parafrazirati.

---

## 6. PREPREČEVANJE ZDRSA PREVIEW → ODLOČITEV

Za preprečevanje implicitne agentnosti veljajo naslednja pravila:

- HOI nikoli ne ponudi “naslednjega koraka”
- HOI nikoli ne vpraša “ali želiš to izvesti”
- HOI nikoli ne nadaljuje verige odločitev samodejno
- vsak preview zahteva novo, izrecno zahtevo uporabnika

Preview ne ustvarja:
- stanja
- spomina
- preferenc
- zgodovine odločitev

---

## 7. STANJE SISTEMA PO PREVIEW

Po zaključenem preview:

- sistem se vrne v nevtralno orientacijsko stanje
- ni “aktivne odločitve”
- ni “pending izbire”
- ni notranjega konteksta za nadaljevanje

Vsaka nadaljnja akcija mora biti **nova uporabnikova odločitev**.

---

## 8. IZRECNA PREPOVED AGENTNOSTI

V v0.32 je izrecno prepovedano:

- kakršnokoli samostojno odločanje HOI
- kakršnakoli optimizacija poti
- kakršnakoli oblika “svetovanja”
- kakršnakoli avtomatska eskalacija v CDR
- kakršnakoli oblika učenja v runtime-u

Vsaka kršitev se šteje kot **architectural breach**.

---

## 9. LOCK DOLOČILO

Ta dokument je zaklenjen (LOCKED).

- Ne sme se razširjati brez nove faze
- Ne sme se reinterpretirati
- Ne sme se “mehčati” z UX argumenti

Vsaka sprememba zahteva:
- novo verzijo
- novo fazo
- nov LOCK dokument

---

END OF DOCUMENT
