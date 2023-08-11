import unittest
from bin.attributes.Occupation import Occupation
from bin.objects.Proof import Proof


class TestOccupation(unittest.TestCase):

    def setUp(self):
        self.proof = Proof("Placeholder")  # You may need to pass the required arguments for the Proof object
        self.occupation = Occupation("Software Engineer", "TechCorp", "Technology", 5, self.proof)

    def test_initialization(self):
        self.assertEqual(self.occupation.job_title, "Software Engineer")
        self.assertEqual(self.occupation.company_name, "TechCorp")
        self.assertEqual(self.occupation.industry, "Technology")
        self.assertEqual(self.occupation.years_experience, 5)

    def test_setters(self):
        self.occupation.job_title = "Data Scientist"
        self.occupation.company_name = "DataCorp"
        self.occupation.industry = "Data Science"
        self.occupation.years_experience = 3

        self.assertEqual(self.occupation.job_title, "Data Scientist")
        self.assertEqual(self.occupation.company_name, "DataCorp")
        self.assertEqual(self.occupation.industry, "Data Science")
        self.assertEqual(self.occupation.years_experience, 3)

    def test_string_representation(self):
        expected_str = "Software Engineer at TechCorp, Technology industry - 5 years of experience"
        self.assertEqual(str(self.occupation), expected_str)


if __name__ == "__main__":
    unittest.main()
