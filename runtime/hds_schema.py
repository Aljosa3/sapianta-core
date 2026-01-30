# PATH: runtime/hds_schema.py

def hds_schema(boundary_output: dict) -> dict:
    """
    HDS Schema / Contract v0.1 — typing only.
    """

    return {
        "mode": "HDS_SCHEMA_REFERENCE",
        "scope": "HDS_SCHEMA_v0.1",
        "hds_ready": True,
        "data": boundary_output.get("content", {}),
    }
