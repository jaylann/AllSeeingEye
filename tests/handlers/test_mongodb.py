import unittest
from pymongo import MongoClient

from bin.attributes.Address import Address
from bin.attributes.DOB import DOB
from bin.attributes.Email import Email
from bin.attributes.EmploymentHistory import EmploymentHistory
from bin.attributes.Gender import Gender
from bin.attributes.Name import Name
from bin.attributes.Nationality import Nationality
from bin.attributes.Occupation import Occupation
from bin.attributes.PhoneNumber import PhoneNumber
from bin.attributes.RelationshipStatus import RelationshipStatus
from bin.entities.Person import Person
from bin.handlers.mongodb import AllSeeingEye
from bin.objects.Proof import Proof


class TestAllSeeingEye(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Connect to the database
        cls.client = MongoClient('mongodb://localhost:27017/')
        cls.db = cls.client['TestAllSeeingEye']
        cls.persons_collection = cls.db['Persons']

        # Clear the test database
        cls.persons_collection.drop()

        # Create an instance of AllSeeingEye
        cls.eye = AllSeeingEye()

        # Sample data for testing
        cls.proof = Proof("ID Card")
        cls.dob = DOB("15-08-1990", cls.proof)
        cls.name_obj = Name(name="Justin", surname="Lanfermann")
        cls.addr = Address("123 Main St", "New York", "NY", "USA", 10001, proof=cls.proof)
        cls.phone_number = PhoneNumber("+1-202-555-0172", proof=cls.proof)
        cls.email = Email("john.doe@example.com", proof=cls.proof)
        cls.occupation = Occupation("Software Engineer", "Google", "Technology", 3, "23.08.2019", None, proof=cls.proof)
        cls.employment_history = EmploymentHistory([cls.occupation])
        cls.nationality = Nationality(cls.addr.country, proof=cls.proof)
        cls.relationship = RelationshipStatus("Divorced", proof=cls.proof)
        cls.gender = Gender("Male", proof=cls.proof)

        cls.person = Person(cls.dob, cls.name_obj, cls.addr, cls.phone_number, cls.nationality, cls.email, cls.gender, cls.employment_history, cls.occupation, cls.relationship)

    def test_add_person(self):
        # Test adding a person
        result_id = self.eye.add_person(self.person)
        self.assertIsNotNone(result_id)

    def test_get_persons_by_name(self):
        # Test fetching by name
        result = self.eye.get_persons(name=self.name_obj)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_DOB(self):
        # Test fetching by DOB
        result = self.eye.get_persons(DOB=self.dob)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_address(self):
        # Test fetching by address
        result = self.eye.get_persons(address=self.addr)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_phone_number(self):
        # Test fetching by phone number
        result = self.eye.get_persons(phone_number=self.phone_number)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_nationality(self):
        # Test fetching by nationality
        result = self.eye.get_persons(nationality=self.nationality)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_email(self):
        # Test fetching by email
        result = self.eye.get_persons(email=self.email)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_employment_history(self):
        # Test fetching by employment history
        result = self.eye.get_persons(employment_history=self.employment_history)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_gender(self):
        # Test fetching by gender
        result = self.eye.get_persons(gender=self.gender)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_occupation(self):
        # Test fetching by occupation
        result = self.eye.get_persons(occupation=self.occupation)
        self.assertTrue(len(result) > 0)

    def test_get_persons_by_relationship_status(self):
        # Test fetching by relationship status
        result = self.eye.get_persons(relationship_status=self.relationship)
        self.assertTrue(len(result) > 0)

    def test_remove_person(self):
        # Test removing a person
        result_id = self.eye.add_person(self.person)
        deleted_count = self.eye.remove_person(result_id)
        self.assertEqual(deleted_count, 1)

    @classmethod
    def tearDownClass(cls):
        # Clear the test database after all tests
        cls.persons_collection.drop()

if __name__ == "__main__":
    unittest.main()
