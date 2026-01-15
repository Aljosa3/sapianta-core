F47_RUNTIME_ENFORCEMENT.md

Status: FINAL · LOCKED
Vloga: Runtime izvršilna zapora Canona
Hierarhija: Podrejen Canonu · Nadrejen vsem izvedbenim modulom

1. NAMEN FAZE

Ta dokument določa neobidljiv mehanizem uveljavljanja Canona v runtime-u.

F47 ne določa:

novih pravil

novih dovoljenj

novih izjem

F47 določa izključno:

kako se Canon prisilno uveljavlja

kdaj se sistem mora ustaviti

kdaj izvedba ni dovoljena, tudi če je tehnično mogoča

2. TEMELJNO NAČELO (NEPREKLICNO)

Če je Canon kršen, se sistem ne sme nadaljevati.

Ni:

“fallback”

“best effort”

“soft fail”

“interpretacije v runtime-u”

Kršitev Canona ni stanje, temveč dogodek zaustavitve.

3. RUNTIME KATEGORIJE KRŠITEV
3.1 Assertion Breach (AB)

Assertion Breach nastopi, ko:

vhodni zahtevek krši kanonsko prepoved

izhodni odgovor preseže dovoljeno mejo

modul poskuša izvesti nedovoljen prehod stanja

Posledica:

takojšnja zaustavitev toka

brez klica naslednje faze

brez posredovanja LLM

3.2 Hard-Fail Condition (HF)

Hard-Fail nastopi, ko:

sistem zazna poskus obhoda Canona

zazna nedovoljeno eskalacijo odgovornosti

zazna neavtorizirano izvedbo

Posledica:

takojšnja prekinitev procesa

zavrnitev zahteve

označitev dogodka kot non-recoverable

3.3 Silent Deviation (SD)

Silent Deviation je najstrožje prepovedano stanje:

Canon je kršen brez eksplicitne zaznave

runtime nadaljuje brez potrditve skladnosti

Načelo:

Silent Deviation ne sme obstajati.

Vsak korak runtime-a mora imeti preverljivo potrditev skladnosti.

4. TOČKE ZAUSTAVITVE (STOP POINTS)

Runtime mora imeti fiksne, neizbrisljive točke zaustavitve:

SP-1: Pred obdelavo vhoda

preveri skladnost zahteve s Canon-om

brez potrditve → proces se ne začne

SP-2: Pred vsakim klicem LLM

preveri, ali je klic sploh dovoljen

če ne → klic je prepovedan

SP-3: Po prejemu LLM odgovora

preveri skladnost izhoda

nedovoljen izhod se ne sme posredovati

SP-4: Pred izvedbo dejanja (execution)

preveri, ali je odgovornost prenesena pravilno

če ne → izvedba ni dovoljena

Te točke ne smejo biti izklopljive.

5. RUNTIME ODGOVORNOST

Runtime:

ni interpret

ni svetovalec

ni optimizator

Runtime je:

mehanični izvrševalec kanonskih omejitev

Če pride do dvoma:

runtime ne nadaljuje

runtime ne razlaga

runtime ne improvizira

6. PREPOVEDANI MEHANIZMI

V runtime-u so izrecno prepovedani:

dinamična omilitev pravil

“temporary allow” mehanizmi

konfiguracije, ki spreminjajo kanonsko logiko

fallback poti, ki preskočijo preverjanje

Če mehanizem obstaja, ki:

omogoča obhod F47
je to kršitev Canona.

7. ODNOS DO PRIHODNJIH FAZ

F48–F50 ne smejo spreminjati F47

noben modul ne sme redefinirati enforcementa

vsak prihodnji sistem mora dokazati, da spoštuje F47

F47 je nadrejena izvršilna plast.

8. STATUS ZAKLEPA

S tem dokumentom je:

runtime enforcement zaključen

kanonska prisila določena

interpretacija prepovedana

Ta dokument je:

zaklenjen

nespremenljiv

referenčna osnova za vse prihodnje faze

9. KONČNA IZJAVA

Canon brez enforcementa je deklaracija.
Enforcement brez izjem je sistem.

S F47 Sapianta ni več zgolj normativna konstrukcija,
temveč neobidljiv okvir delovanja.