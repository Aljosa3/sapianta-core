# F48_MODULE_ADMISSION_RULES.md
Status: ACTIVE · POST-MPL
Vezano na: F47_LOCK, MPL_LOCK
Namen: Določitev pravil za vstop in status modulov v sistem Sapianta

---

## 1. NAMEN FAZE F48

Faza F48 določa pravila, pod katerimi je modul lahko:
- prepoznan kot modul sistema Sapianta
- sprejet v runtime
- udeležen v procesiranju zahtev

F48 ne uvaja novih normativnih pravil.
F48 operacionalizira že zaklenjen Canon.

---

## 2. DEFINICIJA MODULA

Modul je samostojna funkcionalna enota, ki:
- ni del Canona
- ni del MPL
- nima lastne normativne avtoritete
- deluje izključno v okviru dovoljenj, ki jih podeli sistem

Modul:
- ne interpretira Canona
- ne spreminja odločitev Canona
- ne more obiti runtime enforcementa

---

## 3. POGOJI ZA SPREJEM MODULA

Modul je lahko sprejet v sistem samo, če:

1. Ima jasno opredeljen namen (purpose)
2. Ima določeno stopnjo avtoritete (none / advisory / execution)
3. Ima znano lastništvo (system / organization / external)
4. Ima določeno vstopno točko (entry point)
5. Se lahko v celoti podredi F47 runtime enforcementu

Če katerikoli pogoj ni izpolnjen:
→ modul ni sprejet

---

## 4. AVTORITETA MODULA

Moduli so razvrščeni po avtoriteti:

### 4.1 NO_AUTHORITY
- modul ne vpliva na odločanje
- deluje izključno kot transformator ali opazovalec

### 4.2 ADVISORY
- modul lahko predlaga
- sistem ni dolžan upoštevati predloga
- Canon ima vedno prednost

### 4.3 EXECUTION
- modul lahko sproži dejanje
- samo, če je to dejanje izrecno dovoljeno
- vsako dejanje je predmet runtime enforcementa

Če modul zahteva višjo avtoriteto, kot mu je dodeljena:
→ HARD FAIL

---

## 5. OMEJITVE MODULOV

Modul ne sme:

- klicati LLM mimo dovoljenih vstopnih točk
- generirati izhod brez SP-3 preverjanja
- shranjevati ali ohranjati skritega stanja
- vplivati na zaporedje stop-točk
- uvajati lastnih bypass pravil

Vsaka kršitev:
→ modul se zavrne ali odstrani

---

## 6. REGISTRACIJA MODULA

Vsak modul mora biti ob registraciji opremljen z:

- identifikatorjem
- deklariranim namenom
- stopnjo avtoritete
- lastništvom
- verzijo

Registracija ne pomeni avtomatske aktivacije.

---

## 7. AKTIVACIJA MODULA

Aktivacija modula:
- je ločen korak od registracije
- je pogojena z runtime preverjanjem
- je vedno revokabilna

Sistem si pridržuje pravico:
- začasne deaktivacije
- trajne odstranitve modula

---

## 8. ODNOS DO DRUGIH FAZ

F48:
- predhaja F49_CHAT_ENTRY_CONSTRAINTS
- predhaja F50_LLM_INTERFACE_POLICY
- se ne uporablja za validacijo Canona

Vsi moduli:
- so podrejeni F47
- so podvrženi MPL dokazani enforcement logiki

---

## 9. KONČNA IZJAVA

Moduli niso del oblasti.
Moduli so gostje v sistemu.

Sistem Sapianta odloča:
- kdo vstopi
- kaj sme
- in kdaj mora oditi
