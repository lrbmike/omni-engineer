from openai import OpenAI
import os


class OpenAIModel:

    def __init__(self):
        if os.getenv("OPENAI_BASE_URL"):
            self.client = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_BASE_URL"),
            )
        else:
            self.client = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
            )

    def chat(
            self,
            messages: list,  # {"role": "", "content": ""}
            model: str = "gpt-4o",
            temperature: float = 0.3,
            stream: bool = True
    ):

        llm_response = self.client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=messages,
            stream=stream,
        )

        if stream:
            for chunk in llm_response:
                yield chunk.choices[0].delta.content or ""

        else:
            return llm_response.choices[0].message.content