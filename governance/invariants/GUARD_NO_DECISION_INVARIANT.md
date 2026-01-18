# GUARD_NO_DECISION_INVARIANT

Status: ACTIVE  
Razred: System Invariant  
Veljavnost: Globalna (runtime-wide)  
Uveljavitev: Absolutna

---

## 1. NAMEN INVARIANTE

Ta invarianta zagotavlja, da **Guard nikoli ne sprejema odločitev**  
in da se **nobena odločitev ne more zgoditi brez eksplicitno določene
Decision Authority**.

Invariant varuje:
- arhitekturno ločitev faz
- preprečevanje explain-driven drift
- preprečevanje implicitnega odločanja

---

## 2. PODROČJE UPORABE

Invarianta velja za vse faze in vse poti, kjer sodelujejo:

- Guard
- Evaluation Layer
- Decision Gate
- katerikoli normativni ali izvršilni sloj

Ni izjem.

---

## 3. FORMALNA IZJAVA INVARIANTE

> **Nobena odločitev ne sme biti sprejeta, če:**
>
> - izvira neposredno iz Guarda  
> - izvira iz evalvacijskega sloja  
> - je posledica implicitne logike  
> - Decision Authority ni eksplicitno določena  

Če je kateri koli pogoj izpolnjen → odločitev je **neveljavna**.

---

## 4. DOVOLJEN TOK ODLOČANJA (EDINI)

Veljaven tok mora vedno slediti zaporedju:

1. Guard zazna kontekst (brez presoje)
2. Evaluation Layer izdela evalvacijski signal (brez učinka)
3. Decision Gate pripravi odločitveni zahtevek
4. Decision Authority sprejme ali zavrne odločitev
5. Izvršilni sloj deluje izključno na podlagi te odločitve

Preskok katerega koli koraka pomeni kršitev invariance.

---

## 5. IZRECNO PREPOVEDANI SCENARIJI

Invariant se šteje za kršeno, če:

- Guard sproži dovolitev ali zavrnitev
- Evaluation Layer povzroči spremembo runtime poteka
- Decision Gate samodejno odloči brez nosilca
- obstaja “fallback” odločitev brez Authority
- sistem sklepa “najverjetnejši izid”

Vsak od teh primerov pomeni **kritično arhitekturno napako**.

---

## 6. TESTNI KRITERIJI (ABSTRAKTNI)

Invariant velja za potrjeno, če:

- ni poti, kjer Guard vrača odločitev
- ni poti, kjer evalvacija vpliva na izvršitev
- Decision Gate brez Authority ne sproži dejanja
- vse odločitve imajo sledljivo Decision Authority

Če kateregakoli kriterija ni možno dokazati → invariant ni izpolnjena.

---

## 7. POSLEDICE KRŠITVE

Ob kršitvi te invariance:

- sistem izgubi upravljanost
- normativna skladnost ni več zagotovljena
- vse nadaljnje odločitve so pravno in arhitekturno spornih

Kršitev zahteva:
- takojšnjo zaustavitev nadaljnjega razvoja
- revizijo Guard verige
- ponovno uveljavitev invariance

---

## 8. HIERARHIJA

Ta invarianta je:
- nadrejena implementacijskim odločitvam
- nadrejena optimizacijam
- nadrejena performančnim izboljšavam

Ni preglasljiva.

---

## 9. ZAKLEP

Dokler ta invarianta velja, je zagotovljeno:

- Guard ne odloča
- evalvacija nima stranskih učinkov
- odločanje je centralizirano in odgovorno

Ta dokument je **zavezujoč**.

---

Konec dokumenta.
