class AuthoritySnapshot:
    """
    Read-only posnetek avtoritete.
    Ne vsebuje logike ali odločitev.
    """

    def __init__(self, authority_id=None, authority_type=None, status=None, valid_until=None):
        self.authority_id = authority_id
        self.authority_type = authority_type
        self.status = status
        self.valid_until = valid_until


class AuthorityAdapter:
    """
    Read-only adapter za Authority subsystem.
    V FAZI 29 uporablja dummy vir podatkov.
    """

    def resolve(self, authority_reference):
        """
        Vrne read-only snapshot avtoritete.
        """
        # Dummy snapshot (brez interpretacije)
        return AuthoritySnapshot(
            authority_id=authority_reference,
            authority_type=None,
            status=None,
            valid_until=None
        )
