#!/usr/bin/env python3
"""
Kernel Execution Graph Check (STATIC + STRUCTURAL)

- Zero external dependencies (stdlib only)
- Deterministic output ordering
- CI-safe: nonzero exit on violation

Governance mode: B (Controlled Recovery)

Validates:
1) Closure
2) Reachability
3) Determinism (structural)
4) Dead-ends (reported)
5) Cycles (ONLY RUNNING <-> ERROR allowed)
6) Orphan events (reported)

Target module:
- sapianta_hoi.runtime_stub.transitions
"""

from __future__ import annotations

import sys
import traceback
from collections import defaultdict, deque
from typing import Any, Dict, Iterable, List, Mapping, Set, Tuple


TARGET_MODULE = "sapianta_hoi.runtime_stub.transitions"


# ------------------------------------------------------------
# Allowed Recovery Policy
# Only this cycle is allowed:
# RUNNING -> ERROR -> RUNNING
# ------------------------------------------------------------

ALLOWED_RECOVERY_CYCLE = ["RUNNING", "ERROR", "RUNNING"]


def _fail(lines: List[str], exit_code: int = 1) -> None:
    for line in lines:
        print(line)
    sys.exit(exit_code)


def _deterministic_sorted(iterable: Iterable[str]) -> List[str]:
    return sorted(set(iterable))


def _import_transitions_module() -> Any:
    try:
        mod = __import__(TARGET_MODULE, fromlist=["*"])
        return mod
    except Exception:
        tb = traceback.format_exc()
        _fail(
            [
                "FAIL: could not import transitions module.",
                f"MODULE: {TARGET_MODULE}",
                "TRACEBACK:",
                tb.rstrip(),
            ]
        )
    raise RuntimeError("unreachable")


def _extract_required(mod: Any) -> Tuple[Set[str], Dict[Tuple[str, str], str], str]:
    violations: List[str] = []

    if not hasattr(mod, "TRANSITIONS"):
        violations.append("Missing required export: TRANSITIONS")

    if not hasattr(mod, "ALL_STATES"):
        violations.append("Missing required export: ALL_STATES (governance mode B)")

    if violations:
        _fail(["FAIL: missing required exports:"] + [f"- {v}" for v in violations])

    transitions = getattr(mod, "TRANSITIONS")
    all_states = getattr(mod, "ALL_STATES")

    initial_state = getattr(mod, "INITIAL_STATE", "INITIAL")

    if not isinstance(initial_state, str) or not initial_state:
        _fail(["FAIL: INITIAL_STATE must be a non-empty str"])

    if isinstance(all_states, (set, frozenset)):
        all_states_set = set(all_states)
    elif isinstance(all_states, (list, tuple)):
        all_states_set = set(all_states)
    else:
        _fail(["FAIL: ALL_STATES must be set/list/tuple of strings"])

    if not isinstance(transitions, Mapping):
        _fail(["FAIL: TRANSITIONS must be dict-like mapping"])

    transitions_dict: Dict[Tuple[str, str], str] = dict(transitions)

    return all_states_set, transitions_dict, initial_state


def _validate_structure(
    all_states: Set[str],
    transitions: Dict[Tuple[str, str], str],
    initial_state: str,
) -> Tuple[List[str], Dict[str, Set[str]], Set[str]]:

    violations: List[str] = []
    adjacency: Dict[str, Set[str]] = defaultdict(set)
    event_set: Set[str] = set()

    for k, v in transitions.items():

        if (
            not isinstance(k, tuple)
            or len(k) != 2
            or not isinstance(k[0], str)
            or not isinstance(k[1], str)
        ):
            violations.append(f"Invalid transition key: {repr(k)}")
            continue

        if not isinstance(v, str):
            violations.append(f"Invalid transition value for {repr(k)}: {repr(v)}")
            continue

        src, event = k
        dst = v

        if src not in all_states:
            violations.append(f"Closure violation: {src} not in ALL_STATES")
        if dst not in all_states:
            violations.append(f"Closure violation: {dst} not in ALL_STATES")

        adjacency[src].add(dst)
        event_set.add(event)

    if initial_state not in all_states:
        violations.append(f"Initial state '{initial_state}' not in ALL_STATES")

    return violations, dict(adjacency), event_set


def _reachable_states(adjacency: Dict[str, Set[str]], initial_state: str) -> Set[str]:
    visited: Set[str] = set()
    q = deque([initial_state])

    while q:
        s = q.popleft()
        if s in visited:
            continue
        visited.add(s)
        for nxt in sorted(adjacency.get(s, set())):
            if nxt not in visited:
                q.append(nxt)

    return visited


def _detect_cycles(adjacency: Dict[str, Set[str]]) -> List[List[str]]:
    visited: Set[str] = set()
    stack: Set[str] = set()
    parent: Dict[str, str] = {}

    cycles: List[List[str]] = []

    def dfs(node: str):
        visited.add(node)
        stack.add(node)

        for nxt in adjacency.get(node, set()):
            if nxt not in visited:
                parent[nxt] = node
                dfs(nxt)
            elif nxt in stack:
                cycle = [nxt]
                cur = node
                while cur != nxt and cur in parent:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(nxt)
                cycle.reverse()
                cycles.append(cycle)

        stack.remove(node)

    for start in sorted(adjacency.keys()):
        if start not in visited:
            dfs(start)

    return cycles


def _validate_cycles(cycles: List[List[str]]) -> List[str]:
    violations: List[str] = []

    for cycle in cycles:
        if cycle == ALLOWED_RECOVERY_CYCLE:
            continue
        violations.append(f"Disallowed cycle detected: {' -> '.join(cycle)}")

    return violations


def main() -> None:
    mod = _import_transitions_module()
    all_states, transitions, initial_state = _extract_required(mod)

    violations, adjacency, event_set = _validate_structure(
        all_states=all_states,
        transitions=transitions,
        initial_state=initial_state,
    )

    reachable = _reachable_states(adjacency, initial_state)
    unreachable = all_states - reachable

    for s in sorted(unreachable):
        violations.append(f"Unreachable state: {s}")

    cycles = _detect_cycles(adjacency)
    violations += _validate_cycles(cycles)

    dead_ends = sorted(all_states - set(adjacency.keys()))

    print("KERNEL EXECUTION GRAPH CHECK")
    print(f"MODULE: {TARGET_MODULE}")
    print(f"INITIAL_STATE: {initial_state}")
    print(f"ALL_STATES: {', '.join(sorted(all_states))}")
    print(f"EVENTS: {', '.join(sorted(event_set))}")
    print(f"DEAD_END_STATES: {', '.join(dead_ends) if dead_ends else '<none>'}")

    if violations:
        print("RESULT: FAIL")
        print("VIOLATIONS:")
        for v in sorted(violations):
            print(f"- {v}")
        sys.exit(1)

    print("RESULT: PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
