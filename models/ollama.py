import ollama
from ollama import Client
import os

class OllamaModel:

    def __init__(self):
        self.use_host = False
        if os.getenv("OLLAMA_HOST"):
            self.use_host = True

    def chat(
            self,
            messages: list,  # {"role": "", "content": ""}
            model: str = "llama3.1",
            temperature: float = 0.3,
            stream: bool = True
    ):

        # customize host
        if self.use_host:
            client = Client(host=os.getenv("OLLAMA_HOST"))
            response = client.chat(model=model, messages=messages, options={"temperature": temperature}, stream=stream)
        else:
            response = ollama.chat(model=model, messages=messages, options={"temperature": temperature}, stream=stream)

        if stream:
            for chunk in response:
                yield chunk['message']['content'] or ""

        else:
            return response['message']['content']