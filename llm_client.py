import os, openai

class LLMClient:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY", None)
        self.model = "gpt-4o-mini"
    def generate_report_text(self, results, final_report):
        return "Automated feedback: Good attempt. Work on accuracy and formula use."
