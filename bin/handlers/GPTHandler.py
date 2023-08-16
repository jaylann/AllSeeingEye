import openai
from enum import Enum
import tiktoken
import os

from bin.handlers.ConfigHandler import load_env_vars
from bin.handlers.PathHandlers import get_content_root
from bin.handlers.objects.GPTModels import Model
from bin.handlers.objects.GPTResponse import GPTResponse


class OpenAIAPI:
    def __init__(self):
        env_path = os.path.join(get_content_root(), '_internal', 'credentials', 'keys.env')

        load_env_vars(
            env_path)  # Replace later with functionality to call ConfigHandler at script execution

        self.api_key = os.getenv("OPENAIAPIKEY")
        self.encoder = tiktoken.get_encoding("cl100k_base")
        if not self.api_key:
            raise ValueError("OPENAIAPIKEY not found in keys.env")
        openai.api_key = self.api_key

    def count_tokens(self, text):
        return len(self.encoder.encode(text))

    def generate_text(self, prompt, model=Model.GPT3_5_TURBO, system_prompt="", max_tokens=150):
        messages = [{"role": "system", "content": system_prompt}] if system_prompt else []
        messages.append({"role": "user", "content": prompt})
        if max_tokens != -1:
            response = openai.ChatCompletion.create(
                model=model.value,
                messages=messages,
                max_tokens=max_tokens
            )
        else:
            response = openai.ChatCompletion.create(
                model=model.value,
                messages=messages,
            )
        gpt_response = GPTResponse().from_dict(response, prompt=prompt, system_prompt=system_prompt)
        return gpt_response



