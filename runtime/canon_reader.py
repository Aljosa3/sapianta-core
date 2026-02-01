from pathlib import Path
import re

CANON_FILES = [
    "governance/CORE_LAWS.md",
    "governance/IPV_CANON_v0.1_LOCK.md",
    "governance/phases/RUNTIME_WIRING_COMPLIANCE_v0.1_INIT.md",
]

def extract_rules(text: str) -> dict:
    # Minimalno: pobere eksplicitne prepovedi/dovoljenja/invariante
    rules = {"forbidden": [], "allowed": [], "invariants": []}
    for line in text.splitlines():
        l = line.strip().lower()
        if l.startswith("❌") or "must not" in l or "forbidden" in l:
            rules["forbidden"].append(line.strip())
        if l.startswith("✅") or "may" in l or "allowed" in l:
            rules["allowed"].append(line.strip())
        if "invariant" in l or "must" in l:
            rules["invariants"].append(line.strip())
    return rules

def load_canon() -> dict:
    agg = {"forbidden": [], "allowed": [], "invariants": []}
    for p in CANON_FILES:
        text = Path(p).read_text(encoding="utf-8")
        r = extract_rules(text)
        for k in agg:
            agg[k].extend(r[k])
    return agg
