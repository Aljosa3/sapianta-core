#!/usr/bin/env python3
"""
Kernel Execution Graph Check (STATIC + STRUCTURAL)
- Zero external dependencies (stdlib only)
- Deterministic output ordering
- CI-safe: nonzero exit on violation

Governance mode: C (requires ALL_STATES registry)

Validates:
1) Closure
2) Reachability
3) Determinism (structural)
4) Dead-ends (reported; not necessarily fail unless unreachable or outside ALL_STATES)
5) Cycles (fail by default)
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
        violations.append("Missing required export: ALL_STATES (governance mode C)")

    if violations:
        _fail(["FAIL: missing required exports:"] + [f"- {v}" for v in violations])

    transitions = getattr(mod, "TRANSITIONS")
    all_states = getattr(mod, "ALL_STATES")

    initial_state = getattr(mod, "INITIAL_STATE", "INITIAL")
    if not isinstance(initial_state, str) or not initial_state:
        _fail(["FAIL: INITIAL_STATE must be a non-empty str (or omitted to use default 'INITIAL')."])

    # Normalize ALL_STATES to set[str]
    if isinstance(all_states, (set, frozenset)):
        all_states_set = set(all_states)
    elif isinstance(all_states, (list, tuple)):
        all_states_set = set(all_states)
    else:
        _fail(
            [
                "FAIL: ALL_STATES must be a set/frozenset (preferred) or list/tuple of strings.",
                f"Got type: {type(all_states).__name__}",
            ]
        )

    # Ensure all_states are str
    bad_states = [s for s in all_states_set if not isinstance(s, str) or not s]
    if bad_states:
        _fail(
            [
                "FAIL: ALL_STATES contains non-string or empty entries:",
            ]
            + [f"- {repr(s)}" for s in sorted(map(repr, bad_states))]
        )

    # Ensure TRANSITIONS is mapping
    if not isinstance(transitions, Mapping):
        _fail(
            [
                "FAIL: TRANSITIONS must be a mapping (dict-like).",
                f"Got type: {type(transitions).__name__}",
            ]
        )

    # Convert transitions to a concrete dict deterministically
    # (preserves semantics; ensures stable iteration in our checks)
    transitions_dict: Dict[Tuple[str, str], str] = dict(transitions)

    return all_states_set, transitions_dict, initial_state


def _validate_structure(
    all_states: Set[str],
    transitions: Dict[Tuple[str, str], str],
    initial_state: str,
) -> Tuple[List[str], Dict[str, Set[str]], Set[str], Set[str], Set[str]]:
    """
    Returns:
      violations (list[str])
      adjacency (dict[from_state] -> set[to_state])
      source_states (set)
      target_states (set)
      event_set (set)
    """
    violations: List[str] = []

    adjacency: Dict[str, Set[str]] = defaultdict(set)
    source_states: Set[str] = set()
    target_states: Set[str] = set()
    event_set: Set[str] = set()

    # Structural type checks + closure
    for k, v in transitions.items():
        if (
            not isinstance(k, tuple)
            or len(k) != 2
            or not isinstance(k[0], str)
            or not isinstance(k[1], str)
            or not k[0]
            or not k[1]
        ):
            violations.append(f"Invalid transition key (must be (str, str) non-empty): {repr(k)}")
            continue

        from_state, event_type = k

        if not isinstance(v, str) or not v:
            violations.append(f"Invalid transition value (must be non-empty str next_state) for {repr(k)}: {repr(v)}")
            continue

        to_state = v

        # Closure vs ALL_STATES (mode C)
        if from_state not in all_states:
            violations.append(f"Closure violation: from_state not in ALL_STATES: {from_state}")
        if to_state not in all_states:
            violations.append(f"Closure violation: next_state not in ALL_STATES: {to_state}")

        source_states.add(from_state)
        target_states.add(to_state)
        event_set.add(event_type)

        adjacency[from_state].add(to_state)

    # Initial state existence
    if initial_state not in all_states:
        violations.append(f"Initial state '{initial_state}' not in ALL_STATES")

    # Ensure ALL_STATES matches observed state space (strict mode)
    observed_states = set(source_states) | set(target_states)
    extra_declared = all_states - observed_states
    missing_declared = observed_states - all_states  # should be empty due to closure checks

    # In strict C, we allow declared states that are not referenced only if governance decides so.
    # Here we FAIL if there are extra declared states because reachability must be total and explicit.
    # If you later want "declared but unused" to be allowed, change this policy in governance doc.
    if extra_declared:
        for s in sorted(extra_declared):
            violations.append(f"ALL_STATES contains state not referenced by TRANSITIONS (extra declared): {s}")

    if missing_declared:
        for s in sorted(missing_declared):
            violations.append(f"Observed state missing from ALL_STATES: {s}")

    return violations, dict(adjacency), source_states, target_states, event_set


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
    """
    Returns list of cycles (each as list of states) deterministically.
    Policy v1.0: any cycle is a violation.
    """
    visited: Set[str] = set()
    stack: Set[str] = set()
    parent: Dict[str, str] = {}

    cycles: List[List[str]] = []

    def dfs(node: str) -> None:
        visited.add(node)
        stack.add(node)

        for nxt in sorted(adjacency.get(node, set())):
            if nxt not in visited:
                parent[nxt] = node
                dfs(nxt)
            elif nxt in stack:
                # Found a back-edge -> cycle
                # Reconstruct cycle path node -> ... -> nxt
                cycle = [nxt]
                cur = node
                while cur != nxt and cur in parent:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(nxt)
                cycle.reverse()

                # Normalize cycle representation to be deterministic (rotate to smallest)
                # Remove duplicate closing node for comparison, then re-close it.
                core = cycle[:-1]
                if core:
                    min_state = min(core)
                    idx = core.index(min_state)
                    rotated = core[idx:] + core[:idx]
                    rotated_closed = rotated + [rotated[0]]
                    cycles.append(rotated_closed)

        stack.remove(node)

    for start in sorted(adjacency.keys()):
        if start not in visited:
            dfs(start)

    # Deduplicate cycles deterministically
    unique = []
    seen = set()
    for c in cycles:
        key = tuple(c)
        if key not in seen:
            seen.add(key)
            unique.append(c)

    unique.sort(key=lambda x: tuple(x))
    return unique


def main() -> None:
    mod = _import_transitions_module()
    all_states, transitions, initial_state = _extract_required(mod)

    violations, adjacency, source_states, target_states, event_set = _validate_structure(
        all_states=all_states,
        transitions=transitions,
        initial_state=initial_state,
    )

    # Reachability (must cover ALL_STATES)
    if initial_state in all_states:
        reachable = _reachable_states(adjacency, initial_state)
        unreachable = all_states - reachable
        if unreachable:
            for s in sorted(unreachable):
                violations.append(f"Reachability violation: unreachable state from initial '{initial_state}': {s}")
    else:
        reachable = set()

    # Dead-ends (report)
    dead_ends = sorted(all_states - set(adjacency.keys()))

    # Cycle detection (fail on any cycle)
    cycles = _detect_cycles(adjacency)
    if cycles:
        for c in cycles:
            violations.append("Cycle violation: " + " -> ".join(c))

    # Report (deterministic)
    print("KERNEL EXECUTION GRAPH CHECK")
    print(f"MODULE: {TARGET_MODULE}")
    print(f"INITIAL_STATE: {initial_state}")
    print(f"ALL_STATES: {', '.join(sorted(all_states)) if all_states else '<empty>'}")
    print(f"EVENTS: {', '.join(sorted(event_set)) if event_set else '<none>'}")
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
