from typing import Optional
from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Nationality(BaseAttribute):
    """
    Nationality class that extends BaseAttribute.
    It represents a person's nationality, identified by their country.

    Attributes:
        country (str): The country representing the nationality.
    """

    def __init__(self, country: str, proof: Optional[Proof] = None):
        """
        Initializes the Nationality object.

        Args:
            country (str): The country representing the nationality.
            proof (Optional[Proof], default=None): Proof associated with the nationality.
        """
        super().__init__(proof)
        self.country = country

    @property
    def country(self) -> str:
        """Returns the country representing the nationality."""
        return self._country

    @country.setter
    def country(self, value: str):
        """Sets the country representing the nationality.

        Args:
            value (str): The country to set.
        """
        self._country = value

    def __str__(self) -> str:
        """Returns the string representation of the nationality, which is the country."""
        return self.country

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the Nationality object, including proofs if available."""
        return {
            'country': self._country,
            # Convert proof objects to dictionaries if proof attribute is defined in the BaseAttribute class
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
