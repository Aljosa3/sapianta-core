# PATH: runtime/hds_boundary.py

def hds_boundary(hoi_output: dict) -> dict:
    """
    HDS Boundary v0.1 — passive normalization.
    """

    hoi_output["hds_ready"] = True
    return hoi_output
