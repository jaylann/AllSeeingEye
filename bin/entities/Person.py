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





class Person:
    def __init__(self, dob: DOB = None, name: Name = None, address: Address = None, phone_number: PhoneNumber = None,
                 nationality: Nationality = None, email: Email = None,
                 gender: Gender = None, employment_history:EmploymentHistory=None, occupation: Occupation = None,
                 relationship_status: RelationshipStatus = None):
        self._DOB = dob
        self._name = name
        self._phone_number = phone_number
        self._nationality = nationality
        self._email = email
        self._gender = gender
        self._occupation = occupation
        self._employment_history = EmploymentHistory([self.occupation]) if not employment_history and self.occupation else employment_history
        self._relationship_status = relationship_status
        self._address = address if address else Address(country=self.estimate_location()) \
            if self._phone_number else None

    @classmethod
    def from_dict(cls, person_dict):
        def create_proof(proof_data):
            return [Proof(**data) for data in proof_data] if proof_data else None

        # Extracting DOB
        dob_data = person_dict['DOB']
        dob = DOB(dob=dob_data['DOB'], proof=create_proof(dob_data['proof'])) if dob_data else None

        # Extracting Name
        name_data = person_dict['name']
        name = Name(name=name_data['name'], surname=name_data['surname'], middlenames=name_data['middlenames'],
                    proof=create_proof(name_data['proof'])) if name_data else None

        # Extracting Address
        address_data = person_dict['address']
        address = Address(street=address_data['street'], city=address_data['city'], state=address_data['state'],
                          country=address_data['country'], postal_code=address_data['postal_code'],
                          proof=create_proof(address_data['proof'])) if address_data else None

        # Extracting Phone Number
        phone_number_data = person_dict['phone_number']
        phone_number = PhoneNumber(number=phone_number_data['number'],
                                   proof=create_proof(phone_number_data['proof'])) if phone_number_data else None

        # Extracting Nationality
        nationality_data = person_dict['nationality']
        nationality = Nationality(country=nationality_data['country'],
                                  proof=create_proof(nationality_data['proof'])) if nationality_data else None

        # Extracting Email
        email_data = person_dict['email']
        email = Email(email=email_data['email'], proof=create_proof(email_data['proof'])) if email_data else None

        # Extracting Occupations and Employment History
        employment_history_data = person_dict['employment_history']
        occupations = [
            Occupation(job_title=occ['job_title'], company_name=occ['company_name'], industry=occ['industry'],
                       years_experience=occ['years_experience'], start_date=occ['start_date'], end_date=occ['end_date'],
                       proof=create_proof(occ['proof'])) for occ in
            employment_history_data['occupations']] if employment_history_data else []
        employment_history = EmploymentHistory(occupations=occupations) if employment_history_data else None

        # Extracting Gender
        gender_data = person_dict['gender']
        gender = Gender(gender=gender_data['gender'], proof=create_proof(gender_data['proof'])) if gender_data else None

        # Extracting Occupation
        occupation_data = person_dict['occupation']
        occupation = Occupation(job_title=occupation_data['job_title'], company_name=occupation_data['company_name'],
                                industry=occupation_data['industry'],
                                years_experience=occupation_data['years_experience'],
                                start_date=occupation_data['start_date'], end_date=occupation_data['end_date'],
                                proof=create_proof(occupation_data['proof'])) if occupation_data else None

        # Extracting Relationship Status
        relationship_status_data = person_dict['relationship_status']
        relationship_status = RelationshipStatus(status=relationship_status_data['status'], proof=create_proof(
            relationship_status_data['proof'])) if relationship_status_data else None

        # Constructing the Person object
        person = cls(
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
