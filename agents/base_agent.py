from services.gemini_service import GeminiService


class BaseAgent:

    def __init__(self, name: str):

        self.name = name
        self.gemini = GeminiService()

    def generate(self, prompt: str):

        return self.gemini.generate(prompt)

    def generate_structured(self, prompt: str, schema):

        return self.gemini.generate_structured(
            prompt,
            schema
        )