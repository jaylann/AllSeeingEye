import re

from bin.attributes.BaseAttribute import BaseAttribute


class Email(BaseAttribute):
    def __init__(self, email: str, proof=None):
        super().__init__(proof)
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self._is_valid_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")

    @property
    def provider(self):
        return self._email.split("@")[1].split(".")[0]

    def _is_valid_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def __str__(self):
        return self.email

    def __dict__(self):
        return {
            'email': self.email,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None # Assuming proof is defined in the BaseAttribute class
        }