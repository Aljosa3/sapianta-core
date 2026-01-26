# HDS_CHAT_SHELL v0.1 — LOCK

Status: LOCKED  
Datum: 2026-01-26  
Veljavnost: kanonična  
Spremembe: prepovedane brez nove faze

---

## 1. Scope

Ta dokument zaklepa modul **HDS-enabled Chat Shell** kot
referenčni primer **READ-ONLY dialoga brez avtoritete**.

Modul je namenjen:
- podpori človeku pri razumevanju odločitev
- strukturiranju možnosti in posledic
- razkritju negotovosti

Modul NI namenjen:
- sprejemanju odločitev
- zaznavanju ali interpretaciji signalov
- adaptaciji ali učenju
- vzpostavljanju stanja ali spomina

---

## 2. Hard Constraints (NON-NEGOTIABLE)

Naslednje omejitve so absolutne in neodpravljive v tej verziji:

- NO signal detection
- NO signal inference
- NO adaptation
- NO memory
- NO state persistence
- NO autonomous decision-making
- NO recommendation authority
- NO optimization claims

Vsaka kršitev pomeni **neveljavno implementacijo**.

---

## 3. Role Separation

### HOI — Human Orientation Interface
- vedno prisoten
- ima absolutno legitimnostno prednost
- ročno sprožljiv:
  - ORIENT
  - PAUSE
  - REDIRECT
- stanje PAUSE je terminalno (dialog se ne nadaljuje)

### HDS — Human Decision Support
- strukturira razumevanje
- zahteva od LLM:
  - predloge (ne navodila)
  - razloge
  - kvalitativne posledice
  - razkritje negotovosti
- nikoli ne sprejema odločitev

### LLM — Language Model
- podrejeni jezikovni izvajalec
- brez avtoritete
- brez optimalnosti
- brez implicitnega odločanja
- vedno jasno označi negotovost
- vedno potrdi, da je odločitev na človeku

---

## 4. Allowed Outputs

Dovoljeni so izključno naslednji tipi izhoda:

- seznam možnosti (proposals)
- opis razlogov
- kvalitativne posledice
- razkritje negotovosti

Vse formulacije morajo biti:
- neobvezujoče
- neinstruktivne
- brez pritiska

---

## 5. Forbidden Behaviors

Prepovedano je:

- trditi ali namigovati na optimalno odločitev
- uporabljati imperativni ali usmerjevalni jezik
- prikrito rangiranje brez razkritja
- ustvarjanje občutka nujnosti ali avtoritete
- nadaljevanje dialoga ob HOI:PAUSE

---

## 6. Pause Semantics

- HOI:PAUSE takoj ustavi dialog
- ni samodejnega nadaljevanja
- nadaljevanje je možno izključno z eksplicitnim HOI:ORIENT

---

## 7. Version Lock

- Ta dokument zaklepa verzijo **v0.1**
- Razširitve zahtevajo:
  - novo fazo
  - nov dokument INIT
  - novo LOCK potrditev
- Neposredne spremembe tega modula niso dovoljene

---

LOCK CONFIRMED.
