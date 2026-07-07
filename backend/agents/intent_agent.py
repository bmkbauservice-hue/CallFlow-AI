import json
from pathlib import Path

from services.llm_service import LLMService


class IntentAgent:

    def __init__(self):
        self.llm = LLMService()

    def detect(self, text: str):

        prompt = Path("prompts/intent.md").read_text(
            encoding="utf-8"
        )

        answer = self.llm.ask(
            system_prompt=prompt,
            user_prompt=text
        )

        return json.loads(answer)