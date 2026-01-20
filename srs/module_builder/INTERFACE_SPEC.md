# SRS: MODULE BUILDER — INTERFACE SPECIFICATION

Status: PROPOSED  
Layer: SRS  
Scope: Function signatures only  
Normativity: NONE  
Bindings: IGL v2 (GR-001–GR-009)

---

## 1. MODUL: srs.module_builder.schema

```python
from typing import TypedDict, Dict

class ModuleSpec(TypedDict):
    module_id: str
    module_name: str
    module_version: str
    layer: str
    files: Dict[str, str]
