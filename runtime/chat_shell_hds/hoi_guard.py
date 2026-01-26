class HOIGuard:
    """
    HUMAN ORIENTATION INTERFACE
    - absolutna prioriteta
    - ročni nadzor
    """

    ORIENT = "ORIENT"
    PAUSE = "PAUSE"
    REDIRECT = "REDIRECT"

    def __init__(self):
        self.state = self.ORIENT

    def set_state(self, state: str):
        if state not in (self.ORIENT, self.PAUSE, self.REDIRECT):
            raise ValueError("Invalid HOI state")
        self.state = state

    def ensure_legitimacy(self):
        if self.state == self.PAUSE:
            raise RuntimeError("HOI: PAUSE active – dialog halted")

        if self.state == self.REDIRECT:
            return False

        return True
