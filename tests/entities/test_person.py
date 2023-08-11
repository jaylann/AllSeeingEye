import unittest
from datetime import datetime

from bin.attributes.Address import Address
from bin.attributes.DOB import DOB
from bin.attributes.Name import Name
from bin.attributes.PhoneNumber import PhoneNumber
from bin.entities.Person import Person
from bin.objects.Proof import Proof


class TestPersonIntegration(unittest.TestCase):

    def setUp(self):
        proof = Proof("ID Card")  # Assuming Proof class is defined
        dob = DOB("15-08-1990", proof)
        name = "John"
        surname = "Doe"
        middlenames = ["William"]
        name_obj = Name(name, surname, proof, middlenames)
        addr = Address("123 Main St", "New York", "NY", "USA", 10001, proof)

        self.person = Person(dob, name_obj, addr)

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
        phone_number = PhoneNumber("+1-202-555-0172", proof="Proof not provided")  # US phone number
        self.person.phone_number = phone_number
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


if __name__ == "__main__":
    unittest.main()
