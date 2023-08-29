import unittest
from datetime import datetime

from bson import ObjectId

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
from bin.entities.Person import Person
from bin.objects.Proof import Proof


class TestPersonIntegration(unittest.TestCase):

    def setUp(self):
        proof = Proof("ID Card")  # Assuming Proof class is defined
        dob = DOB("15-08-1990", proof)
        name = "John"
        surname = "Doe"
        middlenames = ["William"]
        name_obj = Name(name, surname, middlenames, proof=proof)
        addr = Address("123 Main St", "New York", "NY", "USA", 10001, proof=proof)
        phone_number = PhoneNumber("+1-202-555-0172", proof=proof)
        email = Email("john.doe@example.com", proof=proof)
        occupation = Occupation("Software Engineer", "Google", "Technology", 3, "23.08.2019", None, proof=proof)
        employment_history = EmploymentHistory([occupation])
        nationality = Nationality(addr.country, proof=proof)
        relationship = RelationshipStatus("Divorced", proof=proof)
        gender = Gender("Male", proof=proof)

        self.person = Person(dob, name_obj, addr, phone_number, nationality, email, gender, employment_history,
                             occupation, relationship)

    def test_dob(self):
        self.assertEqual(self.person.DOB.day, 15)
        self.assertEqual(self.person.DOB.month, 8)
        self.assertEqual(self.person.DOB.year, 1990)

    def test_age(self):
        today = datetime.today()
        expected_age = today.year - 1990 - ((today.month, today.day) < (8, 15))
        self.assertEqual(self.person.age, expected_age)

    def test_name(self):
        self.assertEqual(self.person.name.full_name, "John William Doe")
        self.assertEqual(self.person.name.initials, "J.W.D.")

    def test_address(self):
        self.assertEqual(str(self.person.address), "123 Main St, New York, NY, US - 10001")

    def test_location_with_phone_number(self):
        self.assertEqual(self.person.address.country, 'US')

    def test_location_with_explicit_location(self):
        phone_number = PhoneNumber("+1-202-555-0172", proof="Proof not provided")  # US phone number
        explicit_location = 'CA'  # Canada
        self.person.phone_number = phone_number
        self.person.address.country = explicit_location
        self.assertEqual(self.person.address.country, explicit_location)

    def test_location_with_german_phone_number(self):
        phone_number = PhoneNumber("+491771231231", proof="Proof not provided")  # German phone number
        self.person.phone_number = phone_number
        self.assertEqual(self.person.address.country, 'US')

    def test_nationality(self):
        self.assertEqual(self.person.nationality.country, 'US')

    def test_email(self):
        self.assertEqual(self.person.email.email, "john.doe@example.com")

    def test_employment_history(self):
        self.assertEqual(self.person.employment_history.occupations[0].company_name, "Google")

    def test_gender(self):
        self.assertEqual(self.person.gender.gender, "Male")

    def test_occupation(self):
        self.assertEqual(self.person.occupation.job_title, "Software Engineer")

    def test_relationship_status(self):
        self.assertEqual(self.person.relationship_status.status, "Divorced")

    def test_employment_history(self):
        self.assertEqual(self.person.employment_history.occupations[0].job_title, "Software Engineer")
        self.assertEqual(self.person.occupation.job_title, "Software Engineer")

    def test_phone(self):
        self.assertEqual(self.person.phone_number.number, PhoneNumber("+1-202-555-0172").number)

    def test_nationality_relationship(self):
        self.assertEqual(self.person.nationality.country, "US")
        self.assertEqual(self.person.relationship_status.status, "Divorced")

    def test_location_estimation(self):
        phone = PhoneNumber("+44-20-1234-5678")  # UK phone number
        person_UK = Person(phone_number=phone)
        self.assertEqual(person_UK.estimate_location(), 'GB')

    def test_age_update(self):
        self.person.age = 35
        today = datetime.today()
        expected_birth_year = today.year - 35
        self.assertEqual(self.person.DOB.year, expected_birth_year)

    def test_save_and_find(self):
        saved_person = self.person.save()
        fetched_persons = Person.find_by_attributes(name=self.person.name)
        self.assertTrue(fetched_persons)
        fetched_person = fetched_persons[0]
        self.assertEqual(self.person.name.full_name, fetched_person.name.full_name)
        self.person.remove()

    def test_person_from_dict_normal_case(self):
        person_dict = {
            '_id': ObjectId('64d75e648e361e6c365c75d2'),
            'DOB': {'DOB': datetime(1990, 8, 15), 'proof': [{'reason': 'placeholder'}]},
            'name': {'name': 'John', 'surname': 'Doe', 'middlenames': ['William'], 'proof': [{'reason': 'placeholder'}]},
            'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'country': 'US', 'postal_code': 10001, 'proof': [{'reason': 'placeholder'}]},
            'phone_number': {'number': '+12025550172', 'proof': [{'reason': 'placeholder'}]},
            'nationality': {'country': 'US', 'proof': [{'reason': 'placeholder'}]},
            'email': {'email': 'john.doe@example.com', 'proof': [{'reason': 'placeholder'}]},
            'employment_history': {'occupations': [{'job_title': 'Software Engineer', 'company_name': 'Google', 'industry': 'Technology', 'years_experience': 3, 'start_date': datetime(2019, 8, 23), 'end_date': None, 'proof': [{'reason': 'placeholder'}]}]},
            'gender': {'gender': 'Male', 'proof': [{'reason': 'placeholder'}]},
            'occupation': {'job_title': 'Software Engineer', 'company_name': 'Google', 'industry': 'Technology', 'years_experience': 3, 'start_date': datetime(2019, 8, 23), 'end_date': None, 'proof': [{'reason': 'placeholder'}]},
            'relationship_status': {'status': 'Divorced', 'proof': [{'reason': 'placeholder'}]}
        }
        person = Person.from_dict(person_dict)
        assert person.data == person_dict, "Test failed: Normal case"

    def test_person_from_dict_missing_fields(self):
        person_dict = {
            '_id': ObjectId('64d75e648e361e6c365c75d2'),
            'DOB': {'DOB': datetime(1990, 8, 15), 'proof': [{'reason': 'placeholder'}]},
            'name': {'name': 'John', 'surname': 'Doe', 'middlenames': ['William'],
                     'proof': [{'reason': 'placeholder'}]},
            'address': None, 'phone_number': None, 'email': None, 'employment_history': None, 'gender': None,
            'occupation': None, 'relationship_status': None, "nationality": None
        }
        person = Person.from_dict(person_dict)
        self.assertEqual(person.DOB.DOB, datetime(1990, 8, 15), "Test failed: Missing fields")
        self.assertEqual(person.name.name, 'John', "Test failed: Missing fields")
        self.assertIsNone(person.address, "Test failed: Missing fields")
        self.assertIsNone(person.phone_number, "Test failed: Missing fields")
        # Check other missing fields accordingly

    def test_person_from_dict_incorrect_fields(self):
        person_dict = {
            '_id': ObjectId('64d75e648e361e6c365c75d2'),
            'DOB': '15-08-1990',  # Incorrect: Should be a dictionary with datetime object
            'name': {'name': 'John', 'surname': 'Doe', 'middlenames': 'William', 'proof': 'ID Card'},
            # Incorrect: 'middlenames' should be a list, 'proof' should be a dictionary
            'address': None, 'phone_number': None, 'email': None, 'employment_history': None, 'gender': None,
            'occupation': None, 'relationship_status': None, "nationality": None
        }
        with self.assertRaises(Exception):
            Person.from_dict(person_dict)
            self.fail("Test failed: Incorrect fields")  # Should raise an exception

if __name__ == "__main__":
    unittest.main()
