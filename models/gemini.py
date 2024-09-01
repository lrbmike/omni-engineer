import os
import google.generativeai as genai


class GeminiModel:

    def __init__(
            self,
    ):
        if os.getenv("GOOGLE_API_ENDPOINT"):
            genai.configure(
                api_key=os.getenv("GOOGLE_API_KEY"),
                transport="rest",
                client_options={"api_endpoint": os.getenv("GOOGLE_API_ENDPOINT")}
            )

        else:
            genai.configure(
                api_key=os.getenv("GOOGLE_API_KEY")
            )

    def chat(
            self,
            messages: list,  # {"role": "", "content": ""}
            model: str = "gemini-1.5-flash",
            temperature: float = 0.3,
            stream: bool = True
    ):
        llm = genai.GenerativeModel(
            model,
            generation_config=genai.types.GenerationConfig(temperature=temperature)
        )

        # the last item is user input message
        user_input = messages[-1]
        # the user input message need to remove from gemini history
        del (messages[-1])

        chat_messages = []

        if len(messages):
            # format as gemini requirements
            for his in messages:
                if his['role'] == 'user':
                    user_gemini_message = {"parts": [{"text": his['content']}], "role": "user"}
                    chat_messages.append(user_gemini_message)
                else:
                    model_gemini_message = {"parts": [{"text": his['content']}], "role": "model"}
                    chat_messages.append(model_gemini_message)

        llm_response = llm.start_chat(history=chat_messages)

        if stream:
            for chunk in llm_response.send_message(user_input['content'], stream=True):
                yield chunk.text

        else:
            return llm_response.send_message(user_input['content'], stream=False)



