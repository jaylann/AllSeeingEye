from typing import List, Dict, Optional, Union

from bin.handlers.objects.GPTModels import Model
from bin.handlers.objects.GPTModelsCost import ModelCost


class GPTResponse:
    """
    A class to represent the response from the GPT model.
    """

    def __init__(self,
                 id: Optional[str] = None,
                 object: Optional[str] = None,
                 created: Optional[int] = None,
                 model: Optional[str] = None,
                 messages: Optional[List[Dict]] = None,
                 prompt_tokens: Optional[int] = 0,
                 completion_tokens: Optional[int] = 0,
                 total_tokens: Optional[int] = 0,
                 prompt: Optional[str] = None,
                 system_prompt: Optional[str] = None):
        """
        Initialize the GPTResponse object.

        :param id: Unique identifier for the response.
        :param object: Type of the object.
        :param created: Timestamp of creation.
        :param model: Model used for the response.
        :param messages: List of messages in the response.
        :param prompt_tokens: Number of tokens used in the prompt.
        :param completion_tokens: Number of tokens used in the completion.
        :param total_tokens: Total number of tokens used.
        :param prompt: The prompt used for the response.
        :param system_prompt: System prompt used for the response.
        """
        self._id = id
        self._object = object
        self._created = created
        self._model = model
        self._messages = messages or []
        self._prompt_tokens = prompt_tokens
        self._completion_tokens = completion_tokens
        self._total_tokens = total_tokens
        self._prompt = prompt
        self._system_prompt = system_prompt

    @property
    def id(self) -> Optional[str]:
        """Get the id of the response."""
        return self._id

    @id.setter
    def id(self, value: str):
        """Set the id of the response."""
        self._id = value

    @property
    def object(self) -> Optional[str]:
        """Get the object type of the response."""
        return self._object

    @object.setter
    def object(self, value: str):
        """Set the object type of the response."""
        self._object = value

    @property
    def created(self) -> Optional[int]:
        """Get the creation timestamp of the response."""
        return self._created

    @created.setter
    def created(self, value: int):
        """Set the creation timestamp of the response."""
        self._created = value

    @property
    def model(self) -> Optional[str]:
        """Get the model used for the response."""
        return self._model

    @model.setter
    def model(self, value: str):
        """Set the model used for the response."""
        self._model = value

    @property
    def messages(self) -> List[str]:
        """Get the messages in the response."""
        return self._messages

    @messages.setter
    def messages(self, value: List[str]):
        """Set the messages in the response."""
        self._messages = value

    @property
    def prompt_tokens(self) -> int:
        """Get the number of tokens used in the prompt."""
        return self._prompt_tokens

    @prompt_tokens.setter
    def prompt_tokens(self, value: int):
        """Set the number of tokens used in the prompt."""
        self._prompt_tokens = value

    @property
    def completion_tokens(self) -> int:
        """Get the number of tokens used in the completion."""
        return self._completion_tokens

    @completion_tokens.setter
    def completion_tokens(self, value: int):
        """Set the number of tokens used in the completion."""
        self._completion_tokens = value

    @property
    def total_tokens(self) -> int:
        """Get the total number of tokens used."""
        return self._total_tokens

    @total_tokens.setter
    def total_tokens(self, value: int):
        """Set the total number of tokens used."""
        self._total_tokens = value

    @property
    def prompt(self) -> Optional[str]:
        """Get the prompt used for the response."""
        return self._prompt

    @prompt.setter
    def prompt(self, value: str):
        """Set the prompt used for the response."""
        self._prompt = value

    @property
    def system_prompt(self) -> Optional[str]:
        """Get the system prompt used for the response."""
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, value: str):
        """Set the system prompt used for the response."""
        self._system_prompt = value

    @property
    def cost(self) -> float:
        """
        Calculate the cost based on the model and tokens used.

        :return: Total cost.
        """
        model_costs = {
            Model.GPT4.value: (ModelCost.GPT4_8K_INPUT.value, ModelCost.GPT4_8K_OUTPUT.value),
            Model.GPT4_0613.value: (ModelCost.GPT4_8K_INPUT.value, ModelCost.GPT4_8K_OUTPUT.value),
            Model.GPT4_0314.value: (ModelCost.GPT4_8K_INPUT.value, ModelCost.GPT4_8K_OUTPUT.value),
            Model.GPT4_32K.value: (ModelCost.GPT4_32K_INPUT.value, ModelCost.GPT4_32K_OUTPUT.value),
            Model.GPT4_32K_0613.value: (ModelCost.GPT4_32K_INPUT.value, ModelCost.GPT4_32K_OUTPUT.value),
            Model.GPT4_32K_0314.value: (ModelCost.GPT4_32K_INPUT.value, ModelCost.GPT4_32K_OUTPUT.value),
            Model.GPT3_5_TURBO.value: (ModelCost.GPT3_5_TURBO_4K_INPUT.value, ModelCost.GPT3_5_TURBO_4K_OUTPUT.value),
            Model.GPT3_5_TURBO_0613.value: (
                ModelCost.GPT3_5_TURBO_4K_INPUT.value, ModelCost.GPT3_5_TURBO_4K_OUTPUT.value),
            Model.GPT3_5_TURBO_0301.value: (
                ModelCost.GPT3_5_TURBO_4K_INPUT.value, ModelCost.GPT3_5_TURBO_4K_OUTPUT.value),
            Model.GPT3_5_TURBO_16K.value: (
                ModelCost.GPT3_5_TURBO_16K_INPUT.value, ModelCost.GPT3_5_TURBO_16K_OUTPUT.value),
            Model.GPT3_5_TURBO_16K_0613.value: (
                ModelCost.GPT3_5_TURBO_16K_INPUT.value, ModelCost.GPT3_5_TURBO_16K_OUTPUT.value)
        }

        input_cost_per_1000_tokens, output_cost_per_1000_tokens = model_costs.get(self._model, (0, 0))

        total_cost = ((self._prompt_tokens * input_cost_per_1000_tokens) +
                      (self._completion_tokens * output_cost_per_1000_tokens)) / 1000

        return total_cost

    @classmethod
    def from_dict(cls, data_dict: Dict, prompt: Optional[str] = None,
                  system_prompt: Optional[str] = None) -> 'GPTResponse':
        """
        Create a GPTResponse object from a dictionary.

        :param data_dict: Dictionary containing the response data.
        :param prompt: The prompt used for the response.
        :param system_prompt: System prompt used for the response.
        :return: GPTResponse object.
        """
        messages = [message["content"] for message in
                    sorted([choice["message"] for choice in data_dict.get("choices", [])],
                           key=lambda x: x.get("index", 0))]
        return cls(
            id=data_dict.get("id"),
            object=data_dict.get("object"),
            created=data_dict.get("created"),
            model=data_dict.get("model"),
            messages=messages,
            prompt_tokens=data_dict.get("usage", {}).get("prompt_tokens", 0),
            completion_tokens=data_dict.get("usage", {}).get("completion_tokens", 0),
            total_tokens=data_dict.get("usage", {}).get("total_tokens", 0),
            prompt=prompt,
            system_prompt=system_prompt
        )
