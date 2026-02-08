from cli.adapters.lifecycle_reader import csip_from_raw_text
from cli.errors import InvalidArgumentsError


def run(args):
    """
    Submit raw human input and display CSIP (read-only).

    Constraints:
    - No persistence
    - No lifecycle transition
    - No execution
    """
    if not args:
        raise InvalidArgumentsError("input requires raw text argument")

    raw_text = " ".join(args).strip()
    if not raw_text:
        raise InvalidArgumentsError("input text must not be empty")

    csip = csip_from_raw_text(raw_text)

    print("CSIP — Structured Intent (read-only)")
    print("----------------------------------")
    print(f"protocol: {csip.get('protocol')}")
    print(f"version: {csip.get('version')}")
    print(f"summary: {csip['intent'].get('summary')}")
    print(f"confidence: {csip['intent'].get('confidence')}")
    print(f"scope: {csip['intent'].get('scope')}")
    print("constraints:")
    for k, v in csip.get("constraints", {}).items():
        print(f"  - {k}: {v}")
