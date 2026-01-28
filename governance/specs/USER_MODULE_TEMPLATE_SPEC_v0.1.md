# USER MODULE TEMPLATE SPEC v0.1
## SAPIANTA — External User Modules (Normative, Passive)

STATUS: DRAFT
SCOPE: USER MODULES  
AFFECTS CORE: NO  
API IMPACT: NONE  
LOCK IMPACT: NONE  

---

## 1. DEFINICIJA: USER MODULE (SAPIANTA)

User Module je **zunanji, pasiven, normativni odjemalec**, ki uporablja **izključno API v0.1** za branje ali kasnejšo razširljivo interakcijo, **brez vpliva na runtime, orkestracijo ali odločanje**.

User Module ni del jedra in ne sodeluje v nobenem internem izvajalnem toku sistema SAPIANTA.

### User Module NI:
- del jedra
- del HDS ali HOI
- del orkestracije
- del runtime-a
- izvajalec logike
- interpretator ali agent

### User Module JE:
- pogodbeni odjemalec API v0.1
- semantično vezan na obstoječe LOCK-e
- pasiven nosilec domenske (opisne) logike
- nosilec bodočih razširitev (CLI, Chat, integracije)

---

## 2. UMESTITEV GLEDE NA API v0.1

```
[SAPIANTA CORE]
├─ API v0.1 (LOCKED)
│
└───(contract boundary)────────────────────────
↑
User Module (external client)
```

### Pravila umestitve:
- User Module komunicira izključno prek API v0.1
- nima dostopa do internih struktur
- ne pozna runtime stanja
- ne vpliva na tok obdelave
- ne registrira hookov
- ne generira dogodkov

API v0.1 je edina dovoljena vstopna točka.

---

## 3. NORMATIVNI CONTRACT: USER MODULE

### 3.1 DOVOLJENO

User Module sme:
- klicati read-only API v0.1 endpoint-e
- interpretirati HDS JSON izhod (v0.3 / v0.4)
- hraniti lastno stanje zunaj jedra
- definirati lastne interne semantične modele
- obstajati neodvisno od verzij jedra, dokler je API v0.1 LOCKED

### 3.2 PREPOVEDANO

User Module ne sme:
- spreminjati API v0.1
- zahtevati nove API endpoint-e
- obiti semantic mapper
- izvajati inferenco
- uporabljati LLM
- sprejemati odločitve
- sprožati akcije
- pisati v core
- vplivati na HOI ali HDS tok
- registrirati runtime behaviour

Vsaka kršitev pomeni **INVALID USER MODULE**.

---

## 4. KONCEPTUALNA STRUKTURA USER MODULE

Minimalna, normativna, brez izvajanja.

```
user_modules/
└── example_readonly_module/
├── module.manifest.json
├── contract.md
├── api_client.py
├── models.py
└── README.md
```

Struktura je konceptualna in ne zahteva specifičnega jezika.

---

## 5. MINIMALNA STRUKTURA – DEFINICIJE

### 5.1 module.manifest.json

Namen: identiteta in omejitve modula.

```json
{
  "module_name": "example_readonly_module",
  "type": "user_module",
  "mode": "read_only",
  "api_version": "v0.1",
  "llm": false,
  "runtime": false,
  "orchestration": false,
  "inference": false,
  "permissions": {
    "read": true,
    "write": false,
    "execute": false
  }
}
```

### 5.2 contract.md

Namen: vedenjska pravila modula.

```md
# User Module Contract

This module is an external, passive client of SAPIANTA API v0.1.
Allowed:
- Read-only API access
- Interpretation of HDS JSON output

Forbidden:
- Any form of execution
- Any form of decision making
- Any form of orchestration
- Any interaction beyond API v0.1
```

Violation of this contract invalidates the module.

### 5.3 api_client.py — MINIMALNI READ-ONLY PRIMER

```python
class SapiantaAPIClientV01:
    def __init__(self, api_adapter):
        self.api = api_adapter

    def read_state(self):
        """
        Read-only access.
        No mutation.
        No execution.
        """
        return self.api.get_state()
```


### 5.4 models.py

```python
class SemanticSnapshot:
    def __init__(self, raw_hds_json):
        self.raw = raw_hds_json

    def summary(self):
        return {
            "status": self.raw.get("status"),
            "roles": self.raw.get("roles")
        }
```

Modeli so lokalni in nimajo vpliva izven modula.


## 6. KOMPATIBILNOST IN RAZŠIRLJIVOST

Ta User Module:
je združljiv z vsemi obstoječimi LOCK-i
ne zahteva sprememb jedra
omogoča kasnejši razvoj CLI, Chat in integracij
ohranja pasivnost tudi ob razširitvah
Jedro SAPIANTA ostaja nedotaknjeno.


## 7. STATUS

API v0.1: NESPREMENJEN
LOCK-i: SPOŠTOVANI
POT B: ODPRTA
User Module Template: DEFINIRAN