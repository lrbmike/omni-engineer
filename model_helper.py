from models import GeminiModel
from models import OpenAIModel
from models import OllamaModel


def get_llm_streaming_response(messages, provider, model):
    if provider == "gemini":
        llm = GeminiModel()
        for chunk_content in llm.chat(messages=messages, model=model, stream=True):
            # return to the uniform format
            chunk_item = {'content': chunk_content}
            yield chunk_item

    elif provider == "openai":
        llm = OpenAIModel()
        for chunk_content in llm.chat(messages=messages, model=model, stream=True):
            chunk_item = {'content': chunk_content}
            yield chunk_item

    elif provider == "ollama":
        llm = OllamaModel()
        for chunk_content in llm.chat(messages=messages, model=model, stream=True):
            chunk_item = {'content': chunk_content}
            yield chunk_item