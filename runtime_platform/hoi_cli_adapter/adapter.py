from runtime.chat_shell_hds.hoi_guard import HOIGuard


class HOICLIAdapter:
    """
    ZUNANJI ADAPTER ZA HOI
    - ročni ukazi
    - brez avtomatike
    - brez sprememb v HDS Chat Shell
    """

    def __init__(self, hoi: HOIGuard):
        self.hoi = hoi

    def handle(self, raw: str) -> bool:
        """
        Vrne True, če je bil ukaz HOI in je bil obdelan.
        """
        cmd = raw.strip().lower()

        if cmd == ":pause":
            self.hoi.set_state(HOIGuard.PAUSE)
            print("HOI → PAUSE (dialog ustavljen)")
            return True

        if cmd == ":orient":
            self.hoi.set_state(HOIGuard.ORIENT)
            print("HOI → ORIENT (dialog dovoljen)")
            return True

        if cmd == ":redirect":
            self.hoi.set_state(HOIGuard.REDIRECT)
            print("HOI → REDIRECT (preusmeritev)")
            return True

        return False
