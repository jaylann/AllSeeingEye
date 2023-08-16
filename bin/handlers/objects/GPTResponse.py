from typing import List, Dict, Optional


class GPTResponse:
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
        self._id = id
        self._object = object
        self._created = created
        self._model = model
        self._messages = messages if messages else []
        self._prompt_tokens = prompt_tokens
        self._completion_tokens = completion_tokens
        self._total_tokens = total_tokens
        self._prompt = prompt
        self._system_prompt = system_prompt

    @property
    def id(self) -> Optional[str]:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def object(self) -> Optional[str]:
        return self._object

    @object.setter
    def object(self, value: str):
        self._object = value

    @property
    def created(self) -> Optional[int]:
        return self._created

    @created.setter
    def created(self, value: int):
        self._created = value

    @property
    def model(self) -> Optional[str]:
        return self._model

    @model.setter
    def model(self, value: str):
        self._model = value

    @property
    def messages(self) -> List[str]:
        return self._messages

    @messages.setter
    def messages(self, value: List[str]):
        self._messages = value

    @property
    def prompt_tokens(self) -> int:
        return self._prompt_tokens

    @prompt_tokens.setter
    def prompt_tokens(self, value: int):
        self._prompt_tokens = value

    @property
    def completion_tokens(self) -> int:
        return self._completion_tokens

    @completion_tokens.setter
    def completion_tokens(self, value: int):
        self._completion_tokens = value

    @property
    def total_tokens(self) -> int:
        return self._total_tokens

    @total_tokens.setter
    def total_tokens(self, value: int):
        self._total_tokens = value

    @property
    def prompt(self) -> Optional[str]:
        return self._prompt

    @prompt.setter
    def prompt(self, value: str):
        self._prompt = value

    @property
    def system_prompt(self) -> Optional[str]:
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, value: str):
        self._system_prompt = value

    @classmethod
    def from_dict(cls, data_dict: Dict, prompt: Optional[str] = None, system_prompt: Optional[str] = None) -> 'GPTResponse':
        messages = [message["content"] for message in sorted([choice["message"] for choice in data_dict.get("choices", [])],
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

