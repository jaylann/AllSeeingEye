import openai
from enum import Enum
import tiktoken
import os

from bin.handlers.ConfigHandler import load_env_vars

# Load environment variables from the specified .env file
load_env_vars(
    "_internal/credentials/keys.env")  # Replace later with functionality to call ConfigHandler at script execution


class Model(Enum):
    GPT4_8K = "gpt-4.8k"
    GPT4_32K = "gpt-4.32k"
    GPT3_5_TURBO_4K = "gpt-3.5-turbo.4k"
    GPT3_5_TURBO_16K = "gpt-3.5-turbo.16k"
    ADA = "ada"
    BABBAGE = "babbage"
    CURIE = "curie"
    DAVINCI = "davinci"
    ADA_V2_EMBEDDING = "ada-v2-embedding"


class ModelCost(Enum):
    GPT4_8K = 0.03
    GPT4_32K = 0.06
    GPT3_5_TURBO_4K = 0.0015
    GPT3_5_TURBO_16K = 0.003
    ADA = 0.0016
    BABBAGE = 0.0024
    CURIE = 0.012
    DAVINCI = 0.12
    ADA_V2_EMBEDDING = 0.0001


class OpenAIAPI:
    def __init__(self):
        self.api_key = os.getenv("OPENAIAPIKEY")
        self.encoder = tiktoken.get_encoding("cl100k_base")
        if not self.api_key:
            raise ValueError("OPENAIAPIKEY not found in keys.env")
        openai.api_key = self.api_key

    def count_tokens(self, text):
        return len(self.encoder.encode(text))

    def generate_text(self, prompt, model=Model.GPT3_5_TURBO_4K, system_prompt="", max_tokens=150):
        messages = [{"role": "system", "content": system_prompt}] if system_prompt else []
        messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=model.value,
            messages=messages,
            max_tokens=max_tokens
        )
        return response

    def calculate_cost(self, model: Model, tokens: int) -> float:
        """Calculate the cost based on the model and number of tokens."""
        cost_per_token = ModelCost[model.name].value / 1000
        return tokens * cost_per_token

