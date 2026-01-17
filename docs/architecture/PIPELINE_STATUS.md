📌 POVZETEK STANJA RAZVOJA (do F42)
1️⃣ Temelj sistema (zaklenjeno)
✅ Sapianta Core (CANONICAL)

determinističen

brez executiona

brez dialoga

brez feedback loopov

neodvisen od implementacije
➡️ Nedotakljiv temelj sistema

✅ Governance Interface (F31)

vsi vhodi (CLI, API, agenti, SaaS) so enakovredni

enotna vstopna točka v Core

noben vhod nima privilegijev
➡️ Ni bypassov

✅ ROI Interface (F32)

hierarhija: community → organizational

ROI nikoli ne spreminja Core odločitve

ROI lahko samo omeji nadaljnji tok
➡️ Pripravljen za več regulativ (EU AI Act, interne politike, itd.)

✅ Runtime Controller (F33–F34)

zaporedje:

Governance → Core

ROI

Runtime odločitev (HALT / PROCEED)

brez executiona

Execution Gate obstaja, a je NO-OP
➡️ Tok je determinističen in varen

✅ Runtime Trace / Observability (F37)

sledljivost odločitev

brez vpliva na odločitve

nekanonična, implementacijska plast
➡️ Audit-ready brez tveganja vpliva

2️⃣ Modulni pipeline (ključni del)
✅ F40 — Module Registration & Identity

modul mora imeti identiteto

brez implicitnega obstoja modulov

✅ F41 — Module Capability Declaration

modul samo deklarira:

“to znam”

brez dovoljenj

brez konteksta

✅ F42 — Capability Policy Engine (CANONICAL, ZAKLENJENO)

edina avtoriteta, ki odloča:

“ali se capability lahko uporabi v tem kontekstu”

vhodi: identiteta, capability, intent, kontekst, politika

izhodi: ALLOW / DENY / CONDITIONAL

fail-closed (DENY privzeto)

nihče drug ne sme odločati (ne runtime, ne modul, ne LLM)

➡️ To je osrednji varnostni in certifikacijski mehanizem sistema.

🔐 Threat-model F42 → F43 (pregledan)

bypass zaprt

eskalacija zaprta

manjkajoč kontekst = DENY

F43 ne sme odločati
➡️ Arhitektura je varna že po zasnovi

3️⃣ Trenutno stanje repozitorija

normativni dokumenti ločeni od kode

commiti so fazno čisti

git zgodovina je audit / certification ready

Core / Governance / ROI niso bili kršeni