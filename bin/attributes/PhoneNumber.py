import phonenumbers
from phonenumbers import PhoneNumberFormat

from bin.attributes.BaseAttribute import BaseAttribute


class PhoneNumber(BaseAttribute):
    def __init__(self, number, proof, country_context=None):
        super().__init__(proof)
        self.number = self.validate_number(number, country_context)

    @property
    def country_code(self):
        return self.number.country_code

    @property
    def local_number(self):
        return str(self.number.national_number)

    @staticmethod
    def validate_number(number, country_context):
        try:
            parsed_number = phonenumbers.parse(number, country_context)
            if phonenumbers.is_valid_number(parsed_number):
                return parsed_number
        except phonenumbers.phonenumberutil.NumberParseException:
            pass

        raise ValueError("Invalid phone number format")

    @property
    def area_code(self):
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

    def __str__(self):
        return phonenumbers.format_number(self.number, PhoneNumberFormat.E164)

    def __dict__(self):
        return {
            'number': self.__str__(),
            'proof': [proof.__dict__() for proof in self.proof]  # Assuming proof is defined in the BaseAttribute class
        }