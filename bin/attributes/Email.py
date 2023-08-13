import re
from typing import Any, List
from bin.attributes.BaseAttribute import BaseAttribute


class Email(BaseAttribute):
    """
    Email class that extends BaseAttribute.
    It represents an email attribute with associated proof and provides validation.

    Attributes:
        email (str): The email address.
    """

    def __init__(self, email: str, proof: Any = None):
        """
        Initializes the Email object.

        Args:
            email (str): The email address.
            proof (Any, optional): Proof associated with the email. Defaults to None.

        Raises:
            ValueError: If the provided email is not in a valid format.
        """
        super().__init__(proof)
        self.email = email

    @property
    def email(self) -> str:
        """Returns the email address."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Sets the email address.

        Args:
            value (str): The email address to set.

        Raises:
            ValueError: If the provided email is not in a valid format.
        """
        if self._is_valid_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")

    @property
    def provider(self) -> str:
        """Returns the email provider by extracting it from the email address."""
        return self._email.split("@")[1].split(".")[0]

    def _is_valid_email(self, email: str) -> bool:
        """
        Validates the email address using a regex pattern.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def __str__(self) -> str:
        """Returns the string representation of the email address."""
        return self.email

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the Email object, including proofs if available."""
        return {
            'email': self.email,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
