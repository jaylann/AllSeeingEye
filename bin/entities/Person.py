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
from bin.objects.Proof import Proof


def person_from_dict(person_dict):

    # Extracting DOB
    dob = DOB(
        dob=person_dict['DOB']['DOB'],
        proof=[Proof(**proof_data) for proof_data in person_dict['DOB']['proof']]
    )

    # Extracting Name
    name = Name(
        name=person_dict['name']['name'],
        surname=person_dict['name']['surname'],
        middlenames=person_dict['name']['middlenames'],
        proof=[Proof(**proof_data) for proof_data in person_dict['name']['proof']]
    )

    # Extracting Address
    address = Address(
        street=person_dict['address']['street'],
        city=person_dict['address']['city'],
        state=person_dict['address']['state'],
        country=person_dict['address']['country'],
        postal_code=person_dict['address']['postal_code'],
        proof=[Proof(**proof_data) for proof_data in person_dict['address']['proof']]
    )

    # Extracting Phone Number
    phone_number = PhoneNumber(
        number=person_dict['phone_number']['number'],
        proof=[Proof(**proof_data) for proof_data in person_dict['phone_number']['proof']]
    )

    # Extracting Nationality
    nationality = Nationality(
        country=person_dict['nationality']['country'],
        proof=[Proof(**proof_data) for proof_data in person_dict['nationality']['proof']]
    )

    # Extracting Email
    email = Email(
        email=person_dict['email']['email'],
        proof=[Proof(**proof_data) for proof_data in person_dict['email']['proof']]
    )

    # Extracting Occupations
    occupations = []
    for occupation_data in person_dict['employment_history']['occupations']:
        occupation = Occupation(
            job_title=occupation_data['job_title'],
            company_name=occupation_data['company_name'],
            industry=occupation_data['industry'],
            years_experience=occupation_data['years_experience'],
            start_date=occupation_data['start_date'],
            end_date=occupation_data['end_date'],
            proof=[Proof(**proof_data) for proof_data in occupation_data['proof']]
        )
        occupations.append(occupation)

    # Extracting Employment History
    employment_history = EmploymentHistory(
        occupations=occupations

    )

    # Extracting Gender
    gender = Gender(
        gender=person_dict['gender']['gender'],
        proof=[Proof(**proof_data) for proof_data in person_dict['gender']['proof']]
    )

    # Extracting Occupation
    occupation = Occupation(
        job_title=person_dict['occupation']['job_title'],
        company_name=person_dict['occupation']['company_name'],
        industry=person_dict['occupation']['industry'],
        years_experience=person_dict['occupation']['years_experience'],
        start_date=person_dict['occupation']['start_date'],
        end_date=person_dict['occupation']['end_date'],
        proof=[Proof(**proof_data) for proof_data in person_dict['occupation']['proof']]
    )

    # Extracting Relationship Status
    relationship_status = RelationshipStatus(
        status=person_dict['relationship_status']['status'],
        proof=[Proof(**proof_data) for proof_data in person_dict['relationship_status']['proof']]
    )

    # Constructing the Person object
    person = Person(
        dob=dob,
        name=name,
        address=address,
        phone_number=phone_number,
        nationality=nationality,
        email=email,
        employment_history=employment_history,
        gender=gender,
        occupation=occupation,
        relationship_status=relationship_status
    )

    return person

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

    @property
    def data(self):
        return {
            "DOB": self.DOB.__dict__() if self.DOB else None,
            "name": self.name.__dict__() if self.name else None,
            "address": self.address.__dict__() if self.address else None,
            "phone_number": self.phone_number.__dict__() if self.phone_number else None,
            "nationality": self.nationality.__dict__() if self.nationality else None,
            "email": self.email.__dict__() if self.email else None,
            "employment_history": self.employment_history.__dict__() if self.employment_history else None,
            "gender": self.gender.__dict__() if self.gender else None,
            "occupation": self.occupation.__dict__() if self.occupation else None,
            "relationship_status": self.relationship_status.__dict__() if self.relationship_status else None
        }
