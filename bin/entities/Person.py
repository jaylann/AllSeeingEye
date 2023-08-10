from datetime import datetime
from phonenumbers import region_code_for_country_code

from bin.attributes.PhoneNumber import PhoneNumber


class Person:
    def __init__(self, dob=None, name=None, address=None, phone_number=None, location=None):
        self.DOB = dob
        self.name = name
        self.address = address
        self._phone_number = phone_number
        self.location = location if location else self.estimate_location() if phone_number else None

    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age

    @age.setter
    def age(self, value):
        # Calculate the DOB based on the given age
        today = datetime.today()
        birth_year = today.year - value
        # Assuming the same month and day as the current DOB
        self.DOB = datetime(birth_year, self.DOB.month, self.DOB.day)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):

        self._phone_number = value
        self.location = self.estimate_location() if not self.location else self.location
    def estimate_location(self):
        # Get the country code from the phone number
        country_code = self.phone_number.country_code
        # Get the region code for the country code (e.g., 'US' for country code 1)
        region_code = region_code_for_country_code(country_code)
        return region_code
