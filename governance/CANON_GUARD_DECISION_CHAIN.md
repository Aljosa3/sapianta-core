# CANON_GUARD_DECISION_CHAIN

Status: CANONICAL  
Veljavnost: Trajna  
Razred: System Canon  
Področje: Guard / Decision Architecture

---

## 1. IZJAVA CANONA

**Odločitvena veriga Guarda je nespremenljiva.**

Guard v sistemu SAPIANTA:
- nikoli ne sprejema odločitev
- nikoli ne dovoljuje ali zavrača dejanj
- nikoli ne izvaja normativnih pravil

To velja za vse verzije, vse runtime konfiguracije in vse prihodnje razširitve.

---

## 2. KANONIČNA VERIGA

Edini dovoljen tok je:

1. **Context Surface**  
   Guard zazna kontekst brez interpretacije.

2. **Evaluation Layer**  
   Guard izvede neizvršilno presojo brez stranskih učinkov.

3. **Decision Gate**  
   Sistem pripravi odločitveni zahtevek brez samostojne odločitve.

4. **Decision Authority**  
   Zunanji nosilec (normativni modul ali človek) sprejme odločitev.

Če kateri koli korak manjka ali je preskočen → odločitev se ne zgodi.

---

## 3. ABSOLUTNE MEJE

Naslednje je trajno prepovedano:

- implicitno odločanje
- avtomatsko dovoljevanje ali zavračanje
- fallback logika brez nosilca
- “pametne” optimizacije, ki obidejo Decision Authority

Vsak poskus predstavlja kršitev Canona.

---

## 4. RAZLOG OBSTOJA

Ta Canon obstaja zato, da:

- prepreči explain-driven drift
- ohrani sledljivost in odgovornost
- omogoči pravno in normativno skladnost
- zagotovi, da sistem ostane upravljan

Učinkovitost ali priročnost nikoli ne preglasita tega Canona.

---

## 5. SKLICEVANJE

Ta Canon je podprt z:

- `GUARD_CONTEXT_SURFACE_INIT`
- `GUARD_EVALUATION_LAYER_INIT`
- `GUARD_DECISION_GATE_INIT`
- `GUARD_NO_DECISION_INVARIANT`

V primeru konflikta ima **Canon prednost**.

---

## 6. ZAKLEP

Ta dokument ni priporočilo.  
Ta dokument ni smernica.

**Ta dokument je temeljna resnica sistema.**

---

Konec dokumenta.
