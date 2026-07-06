from agents.language_agent import LanguageAgent


class AIBrain:

    def __init__(self):
        self.language_agent = LanguageAgent()

    def process(self, text: str):

        language = self.language_agent.detect(text)

        return {
            "input": text,
            "language": language
        }   