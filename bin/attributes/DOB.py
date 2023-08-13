from datetime import datetime
from typing import Union, List, Any
from bin.attributes.BaseAttribute import BaseAttribute
from bin.utils.date import convert_to_date


class DOB(BaseAttribute):
    """
    DOB (Date of Birth) class that extends BaseAttribute.
    It represents the date of birth attribute with associated proof.

    Attributes:
        DOB (datetime): The date of birth.
    """

    def __init__(self, dob: Union[str, datetime], proof: Any = None):
        """
        Initializes the DOB object.

        Args:
            dob (Union[str, datetime]): The date of birth, either as a string or a datetime object.
            proof (Any, optional): Proof associated with the DOB. Defaults to None.
        """
        super().__init__(proof)
        # Convert dob to a datetime object if it is provided as a string
        self.DOB = convert_to_date(dob) if isinstance(dob, str) else dob

    @property
    def day(self) -> int:
        """Returns the day component of the DOB."""
        return self.DOB.day

    @day.setter
    def day(self, value: int):
        """Sets the day component of the DOB."""
        self.DOB = datetime(self.DOB.year, self.DOB.month, value)

    @property
    def month(self) -> int:
        """Returns the month component of the DOB."""
        return self.DOB.month

    @month.setter
    def month(self, value: int):
        """Sets the month component of the DOB."""
        self.DOB = datetime(self.DOB.year, value, self.DOB.day)

    @property
    def year(self) -> int:
        """Returns the year component of the DOB."""
        return self.DOB.year

    @year.setter
    def year(self, value: int):
        """Sets the year component of the DOB."""
        self.DOB = datetime(value, self.DOB.month, self.DOB.day)

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the DOB object, including proofs if available."""
        return {
            'DOB': self.DOB,
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
