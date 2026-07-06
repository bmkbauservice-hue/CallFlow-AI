import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.model = os.getenv(
            "OPENAI_MODEL",
            "gpt-5.5"
        )

    def ask(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response.output_text 
