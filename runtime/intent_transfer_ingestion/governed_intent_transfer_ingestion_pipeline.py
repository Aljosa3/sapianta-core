"""Preview-ready governed intake construction."""


def build_preview_ready_governance_intake(*, transfer_package: dict) -> dict:
    return {
        "downstream_runtime_target": transfer_package["downstream_runtime_target"],
        "normalized_governed_request": transfer_package["normalized_governed_request"],
        "governance_mode": transfer_package["governance_mode"],
        "preview_required": True,
        "confirmation_required": True,
        "authority_granted": False,
    }
