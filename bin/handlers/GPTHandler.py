import openai
from enum import Enum
import tiktoken
import os

from bin.handlers.ConfigHandler import load_env_vars
from bin.handlers.PathHandlers import get_content_root
from bin.handlers.objects.GPTResponse import GPTResponse

# Load environment variables from the specified .env file
load_env_vars(
    "_internal/credentials/keys.env")  # Replace later with functionality to call ConfigHandler at script execution


class Model(Enum):
    GPT4 = "gpt-4"
    GPT4_0613 = "gpt-4-0613"
    GPT4_32K = "gpt-4-32k"
    GPT4_32K_0613 = "gpt-4-32k-0613"
    GPT4_0314 = "gpt-4-0314"
    GPT4_32K_0314 = "gpt-4-32k-0314"
    GPT3_5_TURBO = "gpt-3.5-turbo"
    GPT3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT3_5_TURBO_0613 = "gpt-3.5-turbo-0613"
    GPT3_5_TURBO_16K_0613 = "gpt-3.5-turbo-16k-0613"
    GPT3_5_TURBO_0301 = "gpt-3.5-turbo-0301"


class ModelCost(Enum):
    GPT4_8K_INPUT = 0.03
    GPT4_8K_OUTPUT = 0.06
    GPT4_32K_INPUT = 0.06
    GPT4_32K_OUTPUT = 0.12
    GPT3_5_TURBO_4K_INPUT = 0.0015
    GPT3_5_TURBO_4K_OUTPUT = 0.002
    GPT3_5_TURBO_16K_INPUT = 0.003
    GPT3_5_TURBO_16K_OUTPUT = 0.004
    ADA = 0.0016
    BABBAGE = 0.0024
    CURIE = 0.012
    DAVINCI = 0.12
    ADA_V2_EMBEDDING = 0.0001


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

    def calculate_cost(self, model: Model, tokens: int) -> float:
        """Calculate the cost based on the model and number of tokens."""
        cost_per_token = ModelCost[model.name].value / 1000
        return tokens * cost_per_token


