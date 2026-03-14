from sapianta_factory.llm.llm_bridge import ask_llm


class DiscussionEngine:
    """
    Handles discussion loop between human and LLM.
    Keeps conversation history.
    """

    def __init__(self):

        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are SAPIANTA architecture advisor. "
                    "Help design improvements for the SAPIANTA system."
                ),
            }
        ]

    def ask(self, text):

        self.messages.append(
            {
                "role": "user",
                "content": text
            }
        )

        response = ask_llm(self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        return response