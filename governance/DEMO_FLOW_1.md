# DEMO_FLOW_1

Status: DEMO  
Scope: Integracijski preizkus toka  
Lock: NO

---

## 1. NAMEN

Ta dokument opisuje **prvi integracijski demo tok v sistemu SAPIANTA**.

Namen demo toka je:
- preveriti pravilno povezavo modulov
- dokazati, da Chat ostaja zgolj komunikacijski kanal
- potrditi ločitev med interakcijo, presojo in razlago
- izvesti tok brez kakršnegakoli izvrševanja

Demo ne uvaja nove funkcionalnosti.
Demo ne spreminja sistema.
Demo nima normativne ali zavezujoče vloge.

---

## 2. OPIS TOKA

Tok poteka v naslednjem zaporedju:

1. Chat Modul
2. INTENT (deklarativen)
3. Risk Assessment Modul
4. Explain (simuliran prikaz)

Execution ni del tega toka.

---

## 3. VKLJUČENI MODULI

### 3.1 Chat Modul
- Vloga: komunikacijski kanal
- Funkcija: sprejem uporabniškega vnosa in deklaracija INTENT-a
- Omejitve:
  - brez interpretacije
  - brez odločanja
  - brez executiona

### 3.2 Risk Assessment Modul
- Vloga: ne-zavezujoča ocena tveganja
- Vhodi:
  - INTENT
  - sistemski context
- Izhodi:
  - signal tipa `risk_assessment`
  - atribut `risk_level`
  - atribut `confidence`

### 3.3 Explain (demo)
- Vloga: informativni prikaz rezultata
- Lastnosti:
  - brez priporočil
  - brez normativnosti
  - brez vpliva na sistem

---

## 4. CONTEXT (DEMO)

V demo toku je bil uporabljen minimalni sistemski context:

- source: demo_flow_1
- jurisdiction: EU
- phase: demo
- execution_allowed: false

Context je ustvarjen izven Chat modula.
Chat nima dostopa do contexta.

---

## 5. OPAZOVANJA

Demo tok je potrdil naslednje:

- Chat modul ostaja popolnoma neodločitven
- INTENT se prenaša brez semantične obogatitve
- Risk modul zahteva sistemski context in deluje neodvisno
- Explain ne ustvarja vpliva ali avtoritete
- Nobeno izvrševanje ni sproženo

---

## 6. KAJ DEMO TOK NI

Ta demo:

- ne predstavlja pravne presoje
- ne predstavlja priporočila
- ne potrjuje skladnosti
- ne sproža dejanj
- ne uvaja odločitev

---

## 7. ZAKLJUČEK

DEMO_FLOW_1 potrjuje, da je osnovni integracijski tok v sistemu SAPIANTA:

- arhitekturno čist
- skladen s kanonom
- varen za nadaljnjo razširitev

Demo tok je zaključen brez potrebe po spremembah obstoječih modulov.

---

Konec dokumenta.
