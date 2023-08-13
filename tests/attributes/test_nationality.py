import unittest

from bin.attributes.Nationality import Nationality
from bin.objects.Proof import Proof


class TestNationality(unittest.TestCase):

    def setUp(self):
        self.proof = Proof("Placeholder")  # Replace with actual instantiation if needed
        self.nationality = Nationality(country="United States", proof=self.proof)

    def test_country(self):
        self.assertEqual(self.nationality.country, "United States")

    def test_set_country(self):
        self.nationality.country = "Canada"
        self.assertEqual(self.nationality.country, "Canada")

    def test_str(self):
        self.assertEqual(str(self.nationality), "United States")

    def test_initialization_without_proof(self):
        nationality = Nationality(country="United States")
        self.assertEqual(nationality.country, "United States")
        self.assertIsNone(nationality.proof)

    def test_dict_representation(self):
        nationality = Nationality(country="United States", proof=self.proof)
        expected_dict = {
            'country': 'United States',
            'proof': [self.proof.__dict__()]  # Assuming __dict__ method exists in Proof class
        }
        self.assertDictEqual(nationality.__dict__(), expected_dict)

    def test_empty_country(self):
        nationality = Nationality(country="", proof=self.proof)
        self.assertEqual(nationality.country, "")



if __name__ == '__main__':
    unittest.main()
