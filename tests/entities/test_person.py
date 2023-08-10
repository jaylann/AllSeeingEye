import unittest
from bin.entities.Person import Person
from bin.objects.Proof import Proof
from datetime import datetime
from bin.attributes.Name import Name
from bin.attributes.Address import Address
from bin.attributes.DOB import DOB


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
        self.assertEqual(self.person.name.full_name(), "John William Doe")
        self.assertEqual(self.person.name.initials(), "J.W.D.")

    def test_address(self):
        self.assertEqual(str(self.person.address), "123 Main St, New York, NY, USA - 10001")


if __name__ == "__main__":
    unittest.main()
