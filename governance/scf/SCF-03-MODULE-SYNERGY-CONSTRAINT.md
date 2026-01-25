# SCF-03 — MODULE SYNERGY CONSTRAINT

## Status
LOCKED — v03 CANONICAL  
Spremembe niso dovoljene brez formalne revizije SCF.

---

## ID
SCF-03-MSC

## Verzija
v1.0

## Faza
v03 — Normativna opredelitev dovoljenih interakcij

## Datum
2026-01-25

## Avtor
SAPIANTA — Canonical Governance Layer

---

## Namen dokumenta

Ta dokument določa **stroga normativna pravila**, pod katerimi je v sistemu SAPIANTA dovoljena
**sinergijska interakcija med moduli**.

Dokument:
- NE uvaja tehničnih mehanizmov
- NE opisuje izvedbe
- NE dovoljuje samostojnega delovanja modulov izven svoje domene

Njegov namen je **zgolj omejitev in opredelitev** pojma sinergije na kanonični ravni.

---

## Temeljno načelo

> Sinergija v SAPIANTA sistemu ni emergentno vedenje,  
> temveč **vnaprej normativno dovoljena oblika sodelovanja**,  
> omejena z vlogami, kontekstom in sledljivostjo.

---

## Definicije

### Modul
Samostojna funkcionalna enota sistema, omejena na:
- lastno domeno znanja
- lastne odgovornosti
- lastne izhodne tipe

Modul nima avtoritete nad drugimi moduli.

---

### Sinergijska interakcija
Formalizirana situacija, kjer:
- več modulov prispeva **ločene, omejene in sledljive prispevke**
- noben modul ne združuje ali interpretira celote
- končni rezultat NI v lasti nobenega modula

---

## Dovoljeni obseg sinergije

Sinergija je dovoljena izključno, kadar so izpolnjeni vsi pogoji:

1. Vsak modul deluje **znotraj svoje kanonično definirane vloge**
2. Prispevek vsakega modula je:
   - omejen
   - ločljiv
   - sledljiv
3. Moduli:
   - ne delijo notranjega stanja
   - ne spreminjajo stanja drugih modulov
4. Noben modul:
   - ne koordinira sinergije
   - ne sprejema končne odločitve
5. Sinergija se lahko zgodi **le znotraj formalno definiranega konteksta**

---

## Prepovedane oblike vedenja

Izrecno prepovedano je:

- samodejno ali spontano povezovanje modulov
- neposredno klicanje enega modula iz drugega
- delitev notranjih struktur ali delovnega stanja
- skupno optimiziranje ciljev
- kolektivno odločanje brez nadzornega konteksta
- kakršnakoli oblika “emergentne inteligence”

Vsaka od zgornjih oblik predstavlja **sistemski zdrs**.

---

## Avtoriteta in odločanje

- Moduli nimajo avtoritete nad rezultatom sinergije
- Moduli ne interpretirajo prispevkov drugih modulov
- Končna odločitev je **izven modula** (runtime / nadzorni sloj)

Ta dokument **ne določa**, kdo ali kaj sprejema odločitev — to je predmet kasnejših faz.

---

## Sledljivost

Vsaka sinergijska interakcija mora biti:
- zaznavna
- ločljiva
- retrospektivno razložljiva

Če sinergije ni mogoče slediti, **ni dovoljena**.

---

## Razmerje do drugih SCF pravil

Ta dokument:
- ne spreminja obstoječih kanoničnih pravil
- ne uvaja novih pravic modulom
- deluje izključno kot **omejevalni zakon**

---

## Zaklep

S tem dokumentom je pojem **sinergije modulov normativno zaklenjen**.

Kakršnakoli izvedba, ki ni skladna s tem dokumentom, se šteje za:
**kršitev SCF in nedovoljeno vedenje sistema.**

---

## KONEC DOKUMENTA
