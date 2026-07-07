from agents.language_agent import LanguageAgent
from agents.intent_agent import IntentAgent


class AIBrain:

    def __init__(self):
        self.language_agent = LanguageAgent()
        self.intent_agent = IntentAgent()

    def process(self, text: str):

        language = self.language_agent.detect(text)
        intent = self.intent_agent.detect(text)

        return {
            "input": text,
            "language": language,
            "intent": intent
        }