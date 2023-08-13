from typing import List
from bin.attributes.Occupation import Occupation


class EmploymentHistory:
    """
    EmploymentHistory class representing a person's employment history.

    Attributes:
        occupations (List[Occupation]): A sorted list of occupations by start date.
    """

    def __init__(self, occupations: List[Occupation]):
        """
        Initializes the EmploymentHistory object.

        Args:
            occupations (List[Occupation]): A list of Occupation objects.
        """
        # Sort occupations by start date during initialization
        self.occupations = sorted(occupations, key=lambda x: x.start_date)

    @property
    def occupations(self) -> List[Occupation]:
        """Returns the list of occupations."""
        return self._occupations

    @occupations.setter
    def occupations(self, value: List[Occupation]):
        """Sets the list of occupations."""
        self._occupations = value

    def add_occupation(self, occupation: Occupation):
        """
        Adds an occupation to the list and sorts the list by start date.

        Args:
            occupation (Occupation): The occupation to add.
        """
        self._occupations.append(occupation)
        self._occupations.sort(key=lambda x: x.start_date)

    def remove_occupation(self, occupation: Occupation):
        """
        Removes an occupation from the list.

        Args:
            occupation (Occupation): The occupation to remove.
        """
        self._occupations.remove(occupation)

    def __str__(self) -> str:
        """Returns the string representation of the employment history."""
        return "\n".join(str(occupation) for occupation in self._occupations)

    def __dict__(self) -> dict:
        """
        Returns a dictionary representation of the employment history,
        using either the occupation's __dict__ method or its string representation.
        """
        return {
            'occupations': [occupation.__dict__() if hasattr(occupation, '__dict__') else str(occupation) for occupation
                            in self._occupations]
        }
