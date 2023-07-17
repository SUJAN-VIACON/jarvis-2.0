import openai
import json


class ChatGptTask:
    def __init__(self):
        self.GPT = openai
        self.GPT.api_key = "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"

    def ask_question(self, prompt):
        model = "gpt-3.5-turbo"
        response = openai.Completion.create(
            engine=model, prompt=prompt, max_tokens=100, n=1, stop=None, temperature=0.7
        )
        answer = response.choices[0].text.strip()
        return answer
