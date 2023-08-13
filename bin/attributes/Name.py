from typing import Union, List, Optional
from bin.attributes.BaseAttribute import BaseAttribute
from bin.objects.Proof import Proof


class Name(BaseAttribute):
    """
    Name class that extends BaseAttribute.
    It represents a person's name, including first name, surname, and middle names, with associated proof.

    Attributes:
        name (str): The first name.
        surname (str): The surname or last name.
        middlenames (List[str]): The middle names.
    """

    def __init__(self, name: Optional[str] = None, surname: Optional[str] = None,
                 middlenames: Union[str, List[str]] = None, proof: Optional[Proof] = None):
        """
        Initializes the Name object.

        Args:
            name (Optional[str], default=None): The first name.
            surname (Optional[str], default=None): The surname or last name.
            middlenames (Union[str, List[str]], default=None): The middle names, either as a string or a list of strings.
            proof (Optional[Proof], default=None): Proof associated with the name.
        """
        super().__init__(proof)
        self.name = name
        self.surname = surname
        self.middlenames = middlenames if middlenames else []

    @property
    def name(self) -> str:
        """Returns the first name."""
        return self._name

    @name.setter
    def name(self, value: Optional[str]):
        """Sets the first name, stripping any leading or trailing spaces."""
        self._name = value.strip() if value else ''

    @property
    def surname(self) -> str:
        """Returns the surname."""
        return self._surname

    @surname.setter
    def surname(self, value: Optional[str]):
        """Sets the surname, stripping any leading or trailing spaces."""
        self._surname = value.strip() if value else ''

    @property
    def middlenames(self) -> List[str]:
        """Returns the middle names."""
        return self._middlenames

    @middlenames.setter
    def middlenames(self, value: Union[str, List[str]]):
        """Sets the middle names, accepting either a string or a list of strings."""
        # Ensure value is a list if it's a string
        if isinstance(value, str):
            value = [value]
        self._middlenames = [name.strip() for name in value] if value else []

    @property
    def full_name(self) -> str:
        """Returns the full name, including all middle names if present."""
        middle_names_str = " ".join(self._middlenames)
        full_name_parts = [self._name, middle_names_str, self._surname]
        return " ".join(part for part in full_name_parts if part)  # Join only non-empty parts

    @property
    def initials(self) -> str:
        """Returns the initials of the name."""
        initials = [self._name[0]] if self._name else []
        initials += [name[0] for name in self._middlenames]
        initials.append(self._surname[0]) if self._surname else ''
        return ".".join(initials) + "." if initials else ''

    def __str__(self) -> str:
        """Returns the full name as a string."""
        return self.full_name

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the Name object, including proofs if available."""
        return {
            'name': self._name,
            'surname': self._surname,
            'middlenames': self._middlenames,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
