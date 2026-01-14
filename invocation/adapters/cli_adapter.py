"""
CLI Adapter (NON-AUTHORITATIVE)

DEPRECATED:
- Legacy adapter from pre-F31 architecture
- Part of the old `invocation` layer
- Replaced by: `sapianta.interaction.adapters.cli_adapter`
- This adapter MUST NOT be used in the active execution path
- Kept temporarily for reference / migration only

STATUS:
- Read-only
- No new features
- Safe to remove in a future cleanup phase (e.g. F36/F37)
"""

from invocation.types.request import InvocationRequest


def from_cli(raw_input: str) -> InvocationRequest:
    """
    Legacy helper for old invocation flow.
    DO NOT USE in current Sapianta runtime.
    """
    return InvocationRequest(raw_input=raw_input)
