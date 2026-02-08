from cli.adapters.lifecycle_reader import (
    get_current_lifecycle,
    csip_from_raw_text,
    robp_from_csip,
    hcbpf_from_robp,
)
from cli.errors import InvalidArgumentsError

# Procesno-lokalni, read-only stub zadnjega inputa
# (dokler ne beremo iz core lifecycle-a)
_LAST_RAW_INPUT = "testni stavek"


def run(args):
    """
    Read-only consolidated views of system state.

    Supported:
    - show status
    - show robp
    - show plan
    """
    if not args:
        raise InvalidArgumentsError("usage: show <status|robp|plan>")

    target = args[0]

    # ------------------------
    # SHOW STATUS
    # ------------------------
    if target == "status":
        lifecycle = get_current_lifecycle()

        print("Lifecycle status")
        print("----------------")

        if lifecycle is None:
            print("Active lifecycle: NONE")
        else:
            print(f"Active lifecycle: {lifecycle.get('lifecycle_id')}")
            print(f"Lifecycle state: {lifecycle.get('status')}")

        print("CSIP: AVAILABLE (read-only)")
        print("ROBP: AVAILABLE (read-only)")
        print("HCBPF: PREVIEW ONLY")
        return

    # ------------------------
    # SHOW ROBP
    # ------------------------
    if target == "robp":
        csip = csip_from_raw_text(_LAST_RAW_INPUT)
        robp = robp_from_csip(csip)

        print("ROBP — Read-Only Build Preparation")
        print("--------------------------------")
        print(f"module_type: {robp.get('module_type')}")
        print(f"write_required: {robp.get('write_required')}")
        print(f"execution_required: {robp.get('execution_required')}")
        print(f"notes: {robp.get('notes')}")
        return

    # ------------------------
    # SHOW PLAN (HCBPF PREVIEW)
    # ------------------------
    if target == "plan":
        csip = csip_from_raw_text(_LAST_RAW_INPUT)
        robp = robp_from_csip(csip)
        plan = hcbpf_from_robp(robp)

        print("HCBPF — Frozen Build Plan (preview)")
        print("----------------------------------")
        print(f"status: {plan.get('status')}")
        print("plan:")
        for k, v in plan.get("plan", {}).items():
            print(f"  - {k}: {v}")
        print("constraints:")
        for k, v in plan.get("constraints", {}).items():
            print(f"  - {k}: {v}")
        print(f"notes: {plan.get('notes')}")
        return

    # ------------------------
    # INVALID
    # ------------------------
    raise InvalidArgumentsError("usage: show <status|robp|plan>")
