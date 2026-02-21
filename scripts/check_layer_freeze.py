#!/usr/bin/env python3
"""
SAPIANTA — Layer Freeze Enforcement (Layer 0)

Design goals:
- Zero external dependencies (no PyYAML).
- CI-compatible (non-interactive, fail-fast).
- Governance-first: enforce locked_files immutability unless explicit override.

Override mechanism:
- Set env var: SAPIANTA_FREEZE_OVERRIDE=1
  (use only with an explicit governance decision + traceable commit message)
Optional soft tag check:
- By default: warn only (never fail) if current tag doesn't match freeze_version.
- Enforce by setting: SAPIANTA_FREEZE_STRICT_TAG=1

Important:
- Layer 0 freeze tag checks must NOT be affected by non-core tags (e.g., domain tags).
- Therefore, git describe is constrained to core constitutional tags only.
"""

from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from typing import List, Optional, Tuple


MANIFEST_PATH = "governance/phases/LAYER_0_FREEZE.yaml"
CORE_TAG_MATCH = "core_constitutional_*"


@dataclass(frozen=True)
class FreezeManifest:
    layer: str
    freeze_version: str
    freeze_date: str
    execution_model: str
    allowed_cycle_policy: str
    locked_files: List[str]
    notes: str


def _die(msg: str, code: int = 2) -> None:
    print(f"[LAYER_FREEZE] ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def _run(cmd: List[str]) -> Tuple[int, str]:
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return p.returncode, (p.stdout or "").strip()
    except FileNotFoundError:
        return 127, ""


def _strip_quotes(s: str) -> str:
    s = s.strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1].strip()
    return s


def _parse_minimal_yaml(path: str) -> FreezeManifest:
    """
    Minimal YAML parser tailored to this manifest shape:
      key: value
      locked_files:
        - path
        - path
      notes: > (or plain single-line)
        continuation...

    Not a general YAML parser by design (dependency-free).
    """
    if not os.path.exists(path):
        _die(f"Freeze manifest missing: {path}")

    layer = freeze_version = freeze_date = execution_model = allowed_cycle_policy = ""
    locked_files: List[str] = []
    notes_lines: List[str] = []

    in_locked_files = False
    in_notes_block = False

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")

            # Skip comments / empty lines (unless we're in a notes block)
            if not in_notes_block:
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue

            if in_notes_block:
                # notes block continues as long as indentation exists
                if line.startswith("  ") or line.startswith("\t"):
                    notes_lines.append(line.strip())
                    continue
                else:
                    in_notes_block = False
                    # fall-through to parse this line normally

            s = line.strip()

            if s == "locked_files:":
                in_locked_files = True
                continue

            if in_locked_files:
                if s.startswith("- "):
                    locked_files.append(s[2:].strip())
                    continue
                # end of list when we hit a non-item key
                if ":" in s and not s.startswith("- "):
                    in_locked_files = False
                    # fall-through to parse this as key
                else:
                    # ignore malformed lines inside list
                    continue

            if s.startswith("notes:"):
                # notes: >  OR notes: "..."
                _, val = s.split(":", 1)
                val = val.strip()
                if val in (">", "|", ">", "|-", "|-", ">-") or val.startswith(">") or val.startswith("|"):
                    in_notes_block = True
                    continue
                notes_lines.append(_strip_quotes(val))
                continue

            if ":" not in s:
                continue

            key, val = s.split(":", 1)
            key = key.strip()
            val = _strip_quotes(val.strip())

            if key == "layer":
                layer = val
            elif key == "freeze_version":
                freeze_version = val
            elif key == "freeze_date":
                freeze_date = val
            elif key == "execution_model":
                execution_model = val
            elif key == "allowed_cycle_policy":
                allowed_cycle_policy = val

    notes = " ".join([x for x in notes_lines if x]).strip()

    # Basic required-field validation (minimal but enforceable)
    missing = []
    if not layer:
        missing.append("layer")
    if not freeze_version:
        missing.append("freeze_version")
    if not freeze_date:
        missing.append("freeze_date")
    if not execution_model:
        missing.append("execution_model")
    if not allowed_cycle_policy:
        missing.append("allowed_cycle_policy")
    if not locked_files:
        missing.append("locked_files (must be explicit list)")

    if missing:
        _die(f"Manifest incomplete ({path}): missing {', '.join(missing)}")

    return FreezeManifest(
        layer=layer,
        freeze_version=freeze_version,
        freeze_date=freeze_date,
        execution_model=execution_model,
        allowed_cycle_policy=allowed_cycle_policy,
        locked_files=locked_files,
        notes=notes,
    )


def _git_current_tag_soft() -> Optional[str]:
    """
    Layer 0 freeze must compare against core constitutional tags only.
    Domain tags (e.g., trading_domain_v0.1) must not influence the result.
    """
    # exact tag if HEAD is tagged (core constitutional tags only)
    code, out = _run(["git", "describe", "--tags", "--match", CORE_TAG_MATCH, "--exact-match"])
    if code == 0 and out:
        return out

    # fallback: describe (may include distance/hash) but still core tags only
    code, out = _run(["git", "describe", "--tags", "--match", CORE_TAG_MATCH, "--always"])
    if code == 0 and out:
        return out

    return None


def _git_changed_files(targets: List[str]) -> List[str]:
    """
    Detect changes in locked files:
    - staged changes
    - unstaged changes
    relative to HEAD

    This is CI-safe and local-dev safe.
    """
    changed: set[str] = set()

    # staged
    code, out = _run(["git", "diff", "--name-only", "--cached", "HEAD", "--"] + targets)
    if code == 0 and out:
        for p in out.splitlines():
            p = p.strip()
            if p:
                changed.add(p)

    # unstaged
    code, out = _run(["git", "diff", "--name-only", "HEAD", "--"] + targets)
    if code == 0 and out:
        for p in out.splitlines():
            p = p.strip()
            if p:
                changed.add(p)

    return sorted(changed)


def main() -> int:
    manifest = _parse_minimal_yaml(MANIFEST_PATH)

    # 1) Verify listed files exist
    missing_files = [p for p in manifest.locked_files if not os.path.exists(p)]
    if missing_files:
        _die(
            "Locked files listed in manifest do not exist:\n"
            + "\n".join(f"  - {p}" for p in missing_files)
        )

    # 2) Optional tag check (soft by default)
    current_tag = _git_current_tag_soft()
    strict_tag = os.getenv("SAPIANTA_FREEZE_STRICT_TAG", "0") == "1"

    if current_tag is None:
        print(
            "[LAYER_FREEZE] WARN: Unable to determine core constitutional git tag "
            "(git describe unavailable or no core_constitutional_* tags reachable)."
        )
    else:
        if manifest.freeze_version not in current_tag:
            msg = (
                f"[LAYER_FREEZE] WARN: freeze_version={manifest.freeze_version} "
                f"does not match current core git tag/describe='{current_tag}'."
            )
            if strict_tag:
                _die(msg.replace("WARN", "ERROR"))
            else:
                print(msg)

    # 3) Fail if locked files modified without explicit override
    override = os.getenv("SAPIANTA_FREEZE_OVERRIDE", "0") == "1"
    changed = _git_changed_files(manifest.locked_files)

    if changed and not override:
        _die(
            "Locked Layer 0 files modified without explicit override.\n"
            "Set SAPIANTA_FREEZE_OVERRIDE=1 ONLY with an explicit governance decision.\n"
            "Modified locked files:\n" + "\n".join(f"  - {p}" for p in changed),
            code=3,
        )

    if changed and override:
        print("[LAYER_FREEZE] OVERRIDE ACTIVE: locked file modifications allowed (governance decision required).")
        for p in changed:
            print(f"[LAYER_FREEZE]   modified: {p}")

    print("[LAYER_FREEZE] PASS: Layer 0 freeze manifest present and enforced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())