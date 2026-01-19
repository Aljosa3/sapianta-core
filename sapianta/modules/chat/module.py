class ChatModule:
    """
    SAPIANTA Chat Module

    Purpose:
    - interact with user
    - structure user input
    - declare INTENT
    - trigger system evaluation flow

    This module:
    - does NOT decide
    - does NOT execute
    - does NOT assess risk
    """

    MODULE_ID = "module.chat"
    VERSION = "1.0.0"

    def __init__(self, config=None):
        self.config = config or {}

    def run(self, raw_input, context=None):
        """
        Allowed:
        - accept raw user input
        - produce structured intent declaration

        Forbidden:
        - interpretation
        - decision
        - execution
        """

        intent = {
            "type": "inquire",
            "source": "user",
            "scope": "informational",
            "payload": {
                "raw_text": raw_input
            }
        }

        return {
            "module_id": self.MODULE_ID,
            "version": self.VERSION,
            "intent": intent
        }
