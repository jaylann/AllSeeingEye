import phonenumbers
from phonenumbers import PhoneNumberFormat
from typing import Optional, Union
from bin.attributes.BaseAttribute import BaseAttribute


class PhoneNumber(BaseAttribute):
    """
    PhoneNumber class that extends BaseAttribute.
    It represents a phone number, including its country code, local number, and area code.

    Attributes:
        number (phonenumbers.PhoneNumber): Parsed phone number object.
    """

    def __init__(self, number: str, country_context: Optional[str] = None, proof: Optional[Union[dict, list]] = None):
        """
        Initializes the PhoneNumber object.

        Args:
            number (str): The phone number string.
            country_context (Optional[str], default=None): The country context for parsing the phone number.
            proof (Optional[Union[dict, list]], default=None): Proof associated with the phone number.

        Raises:
            ValueError: If the phone number format is invalid.
        """
        super().__init__(proof)
        self.number = self.validate_number(number, country_context)

    @property
    def country_code(self) -> int:
        """Returns the country code of the phone number."""
        return self.number.country_code

    @property
    def local_number(self) -> str:
        """Returns the local (national) number part of the phone number."""
        return str(self.number.national_number)

    @staticmethod
    def validate_number(number: str, country_context: Optional[str]) -> phonenumbers.PhoneNumber:
        """
        Validates and parses the given phone number.

        Args:
            number (str): The phone number string.
            country_context (Optional[str]): The country context for parsing the phone number.

        Returns:
            phonenumbers.PhoneNumber: Parsed phone number object.

        Raises:
            ValueError: If the phone number format is invalid.
        """
        try:
            parsed_number = phonenumbers.parse(number, country_context)
            if phonenumbers.is_valid_number(parsed_number):
                return parsed_number
        except phonenumbers.phonenumberutil.NumberParseException:
            pass

        raise ValueError("Invalid phone number format")

    @property
    def area_code(self) -> Optional[str]:
        """
        Returns the area code of the phone number based on the country region.

        Note: The area code mapping is defined for specific countries, and it may require
        updates for new regions or changes in area code lengths.
        """
        country = phonenumbers.region_code_for_number(self.number)
        national_number = str(self.number.national_number)

        area_code_length = {
            'US': 3, 'CA': 3,  # North America
            'GB': 3, 'FR': 2, 'DE': 3, 'IT': 2,  # Europe
            'AU': 1, 'JP': 2, 'KR': 2,  # Asia-Pacific
            'CN': 2, 'IN': 2, 'RU': 3,  # Asia
            'BR': 2, 'MX': 2, 'AR': 2,  # Latin America
            'ZA': 2, 'TR': 2,  # Others
            'SA': 2,  # Middle East
            # Add more if needed
        }

        return national_number[:area_code_length.get(country, 0)] if country in area_code_length else None

    def __str__(self) -> str:
        """Returns the string representation of the phone number in E.164 format."""
        return phonenumbers.format_number(self.number, PhoneNumberFormat.E164)

    def __dict__(self) -> dict:
        """Returns a dictionary representation of the PhoneNumber object, including proofs if available."""
        return {
            'number': self.__str__(),
            'proof': [proof.__dict__() for proof in self.proof] if self.proof else None
        }
