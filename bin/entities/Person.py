from datetime import datetime
from phonenumbers import region_code_for_country_code

from bin.attributes.PhoneNumber import PhoneNumber
from bin.attributes.Address import Address
from bin.attributes.DOB import DOB
from bin.attributes.Email import Email
from bin.attributes.EmploymentHistory import EmploymentHistory
from bin.attributes.Name import Name
from bin.attributes.Nationality import Nationality
from bin.attributes.Occupation import Occupation
from bin.attributes.RelationshipStatus import RelationshipStatus
from bin.attributes.Gender import Gender


class Person:
    def __init__(self, dob: DOB = None, name: Name = None, address: Address = None, phone_number: PhoneNumber = None,
                 nationality: Nationality = None, email: Email = None, employment_history: EmploymentHistory = None,
                 gender: Gender = None, occupation: Occupation = None,
                 relationship_status: RelationshipStatus = None):
        self._DOB = dob
        self._name = name
        self._address = address if address else Address(country=self.estimate_location()) \
            if self._phone_number else None
        self._phone_number = phone_number
        self._nationality = nationality
        self._email = email
        self._employment_history = employment_history
        self._gender = gender
        self._occupation = occupation
        self._relationship_status = relationship_status

    # DOB
    @property
    def DOB(self):
        return self._DOB

    @DOB.setter
    def DOB(self, value):
        self._DOB = value

    # Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    # Phone Number
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
        self.address = self.estimate_location() if not self.address else self.address

    # Nationality
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value

    # Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Employment History
    @property
    def employment_history(self):
        return self._employment_history

    @employment_history.setter
    def employment_history(self, value):
        self._employment_history = value

    # Gender
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    # Occupation
    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        self._occupation = value

    # Relationship Status
    @property
    def relationship_status(self):
        return self._relationship_status

    @relationship_status.setter
    def relationship_status(self, value):
        self._relationship_status = value

    @property
    def age(self):
        today = datetime.today()
        age = today.year - self._DOB.year - ((today.month, today.day) < (self._DOB.month, self._DOB.day))
        return age

    @age.setter
    def age(self, value):
        # Calculate the DOB based on the given age
        today = datetime.today()
        birth_year = today.year - value
        # Assuming the same month and day as the current DOB
        self._DOB = datetime(birth_year, self._DOB.month, self._DOB.day)

    def estimate_location(self):
        # Get the country code from the phone number
        country_code = self._phone_number.country_code
        # Get the region code for the country code (e.g., 'US' for country code 1)
        region_code = region_code_for_country_code(country_code)
        return region_code
