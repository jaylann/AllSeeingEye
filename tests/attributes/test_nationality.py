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

    # Additional tests can be added here if necessary


if __name__ == '__main__':
    unittest.main()
