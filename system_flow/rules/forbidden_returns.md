# FILE: system_flow/rules/forbidden_returns.md

## FORBIDDEN RETURNS

### FR-1
No responses may propagate backward beyond their immediate upstream layer.

### FR-2
No status or response may alter upstream behavior.

### FR-3
No retries, loops, or replays are permitted.

### FR-4
No escalation or fallback paths are permitted.
