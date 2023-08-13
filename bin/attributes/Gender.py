from typing import Optional, List
from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Gender(BaseAttribute):
    """
    Gender class that extends BaseAttribute.
    It represents a gender attribute with associated proof.

    Attributes:
        gender (str): The gender, which must be one of 'Male', 'Female', or 'Other'.
    """

    VALID_GENDERS = ['Male', 'Female', 'Other']  # A list of valid gender values

    def __init__(self, gender: str, proof: Optional[Proof] = None):
        """
        Initializes the Gender object.

        Args:
            gender (str): The gender, which must be one of 'Male', 'Female', or 'Other'.
            proof (Proof, optional): Proof associated with the gender. Defaults to None.

        Raises:
            ValueError: If the provided gender is not one of the valid options.
        """
        super().__init__(proof)
        self.gender = gender

    @property
    def gender(self) -> str:
        """Returns the gender."""
        return self._gender

    @gender.setter
    def gender(self, value: str):
        """
        Sets the gender, ensuring it is one of the valid options.

        Args:
            value (str): The gender to set.

        Raises:
            ValueError: If the provided gender is not one of the valid options.
        """
        if value not in Gender.VALID_GENDERS:
            raise ValueError(f"Gender must be one of {', '.join(Gender.VALID_GENDERS)}")
        self._gender = value

    def __str__(self) -> str:
        """Returns the string representation of the gender."""
        return f"Gender: {self.gender}"

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the Gender object, including proofs if available."""
        return {
            'gender': self.gender,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
