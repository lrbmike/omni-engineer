Project forked from [Omni Engineer](https://github.com/Doriandarko/omni-engineer.git), the base project use [openrouter.ai](https://openrouter.ai/),  now a lot of llm models have been added to this new project, such as  `openai`、`gemini` and `ollama`

- In `main.py` 

```python
# define the default provider and model
DEFAULT_PROVIDER = "gemini"
DEFAULT_MODEL = "gemini-1.5-flash"
EDITOR_MODEL = "gemini-1.5-pro"

# ...

# edit the get_streaming_response function to use the new codes
def get_streaming_response(messages, model):
    stream = model_helper.get_llm_streaming_response(messages, "gemini", model)
    full_response = ""
    for chunk in stream:
        if chunk.get('content'):
            print_colored(chunk.get('content'), end="")
            full_response += chunk.get('content')
    return full_response.strip()
```

- In `models` folder, you can define the model which you want to use

- In `model_helper.py`, You need to adapt to the model you have defined

  ```python
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
  ```

  - Rename `.env.example` to `.env` , and add the `API_KEY` config what the model you use



