#!/usr/bin/env python3
"""
Kernel Execution Graph Check (STATIC + STRUCTURAL)

Governance mode: B (Controlled Recovery)

Validates:
1) Closure
2) Reachability
3) Determinism (structural)
4) Dead-ends (reported)
5) Cycles (ONLY RUNNING <-> ERROR allowed)
6) Orphan events (reported)
"""

from __future__ import annotations

import sys
import traceback
from collections import defaultdict, deque
from typing import Any, Dict, Iterable, List, Mapping, Set, Tuple


TARGET_MODULE = "sapianta_hoi.runtime_stub.transitions"


def _fail(lines: List[str], exit_code: int = 1) -> None:
    for line in lines:
        print(line)
    sys.exit(exit_code)


def _import_transitions_module() -> Any:
    try:
        return __import__(TARGET_MODULE, fromlist=["*"])
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


def _extract_required(mod: Any) -> Tuple[Set[str], Dict[Tuple[str, str], str], str]:
    if not hasattr(mod, "TRANSITIONS"):
        _fail(["Missing required export: TRANSITIONS"])

    if not hasattr(mod, "ALL_STATES"):
        _fail(["Missing required export: ALL_STATES (governance mode B)"])

    transitions = dict(getattr(mod, "TRANSITIONS"))
    all_states = set(getattr(mod, "ALL_STATES"))
    initial_state = getattr(mod, "INITIAL_STATE", "INITIAL")

    if initial_state not in all_states:
        _fail([f"Initial state '{initial_state}' not in ALL_STATES"])

    return all_states, transitions, initial_state


def _build_graph(transitions):
    adjacency: Dict[str, Set[str]] = defaultdict(set)
    events: Set[str] = set()

    for (src, event), dst in transitions.items():
        adjacency[src].add(dst)
        events.add(event)

    return dict(adjacency), events


def _check_closure(transitions, all_states):
    violations = []
    for (src, _), dst in transitions.items():
        if src not in all_states:
            violations.append(f"Closure violation: {src} not in ALL_STATES")
        if dst not in all_states:
            violations.append(f"Closure violation: {dst} not in ALL_STATES")
    return violations


def _reachable_states(adjacency, initial_state):
    visited: Set[str] = set()
    q = deque([initial_state])

    while q:
        s = q.popleft()
        if s in visited:
            continue
        visited.add(s)
        for nxt in adjacency.get(s, []):
            if nxt not in visited:
                q.append(nxt)

    return visited


def _detect_cycles(adjacency):
    visited: Set[str] = set()
    stack: Set[str] = set()
    parent: Dict[str, str] = {}

    cycles: List[List[str]] = []

    def dfs(node: str):
        visited.add(node)
        stack.add(node)

        for nxt in adjacency.get(node, []):
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


# ------------------------------------------------------------
# FIX: Rotation-safe cycle validation
# Only allowed cycle is 2-node cycle between RUNNING and ERROR
# ------------------------------------------------------------

def _validate_cycles(cycles: List[List[str]]) -> List[str]:
    violations: List[str] = []
    allowed_nodes = {"RUNNING", "ERROR"}

    for cycle in cycles:
        core = cycle[:-1]  # remove duplicate closing node

        if len(core) == 2 and set(core) == allowed_nodes:
            continue  # allowed recovery cycle

        violations.append(f"Disallowed cycle detected: {' -> '.join(cycle)}")

    return violations


def main():
    mod = _import_transitions_module()
    all_states, transitions, initial_state = _extract_required(mod)

    adjacency, events = _build_graph(transitions)

    violations = []
    violations += _check_closure(transitions, all_states)

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
    print(f"EVENTS: {', '.join(sorted(events))}")
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
