import unittest

from bin.attributes.EmploymentHistory import EmploymentHistory
from bin.attributes.Occupation import Occupation
from bin.objects.Proof import Proof


class TestEmploymentHistory(unittest.TestCase):

    def setUp(self):
        proof = Proof("Placeholder")  # You may need to pass the required arguments for the Proof object
        self.occupation1 = Occupation("Software Engineer", "TechCorp", "Technology", 5, "2022-01-01", "2023-01-01",
                                      proof)
        self.occupation2 = Occupation("Data Scientist", "DataCorp", "Data Science", 3, "2020-06-01", "2021-06-01",
                                      proof)
        self.employment_history = EmploymentHistory([self.occupation1, self.occupation2])

    def test_initialization(self):
        self.assertEqual(self.employment_history.occupations[0], self.occupation2)  # Sorted by start_date
        self.assertEqual(self.employment_history.occupations[1], self.occupation1)

    def test_add_occupation(self):
        proof = Proof("Placeholder")
        new_occupation = Occupation("Product Manager", "ProductCorp", "Management", 2, "2019-01-01", "2020-01-01",
                                    proof)
        self.employment_history.add_occupation(new_occupation)
        self.assertEqual(self.employment_history.occupations[0], new_occupation)  # Sorted by start_date

    def test_remove_occupation(self):
        self.employment_history.remove_occupation(self.occupation1)
        self.assertEqual(len(self.employment_history.occupations), 1)
        self.assertEqual(self.employment_history.occupations[0], self.occupation2)

    def test_string_representation(self):
        expected_str = str(self.occupation2) + "\n" + str(self.occupation1)  # Sorted by start_date
        self.assertEqual(str(self.employment_history), expected_str)


if __name__ == "__main__":
    unittest.main()
