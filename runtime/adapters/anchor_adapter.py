class AnchorSnapshot:
    """
    Read-only posnetek Knowledge Anchorja.
    """

    def __init__(self, anchor_id=None, anchor_type=None, exists=False):
        self.anchor_id = anchor_id
        self.anchor_type = anchor_type
        self.exists = exists


class AnchorAdapter:
    """
    Read-only adapter za Knowledge Anchor lookup.
    V FAZI 29 uporablja dummy vir podatkov.
    """

    def resolve(self, anchor_reference):
        """
        Vrne read-only snapshot anchorja.
        """
        return AnchorSnapshot(
            anchor_id=anchor_reference,
            anchor_type=None,
            exists=False
        )
