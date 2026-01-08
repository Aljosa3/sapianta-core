from runtime.adapters.authority_adapter import AuthorityAdapter
from runtime.adapters.anchor_adapter import AnchorAdapter


class RuntimeContext:
    """
    Združuje runtime read-only vire:
    - authority
    - knowledge anchors
    """

    def __init__(self):
        self.authority_adapter = AuthorityAdapter()
        self.anchor_adapter = AnchorAdapter()

    def resolve_authority(self, authority_reference):
        return self.authority_adapter.resolve(authority_reference)

    def resolve_anchor(self, anchor_reference):
        return self.anchor_adapter.resolve(anchor_reference)
