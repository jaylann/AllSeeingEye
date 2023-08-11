import unittest
from bin.attributes.Occupation import Occupation
from bin.objects.Proof import Proof
from datetime import datetime


class TestOccupation(unittest.TestCase):

    def setUp(self):
        self.proof = Proof("Placeholder")  # You may need to pass the required arguments for the Proof object
        start_date = "2022-01-01"
        end_date = "2023-01-01"
        self.occupation = Occupation("Software Engineer", "TechCorp", "Technology", 5, start_date, end_date, self.proof)

    def test_initialization(self):
        self.assertEqual(self.occupation.job_title, "Software Engineer")
        self.assertEqual(self.occupation.company_name, "TechCorp")
        self.assertEqual(self.occupation.industry, "Technology")
        self.assertEqual(self.occupation.years_experience, 5)
        self.assertEqual(self.occupation.start_date, datetime(2022, 1, 1))
        self.assertEqual(self.occupation.end_date, datetime(2023, 1, 1))

    def test_setters(self):
        self.occupation.job_title = "Data Scientist"
        self.occupation.company_name = "DataCorp"
        self.occupation.industry = "Data Science"
        self.occupation.years_experience = 3
        self.occupation.start_date = "2020-06-01"
        self.occupation.end_date = "2021-06-01"

        self.assertEqual(self.occupation.job_title, "Data Scientist")
        self.assertEqual(self.occupation.company_name, "DataCorp")
        self.assertEqual(self.occupation.industry, "Data Science")
        self.assertEqual(self.occupation.years_experience, 3)
        self.assertEqual(self.occupation.start_date, datetime(2020, 6, 1))
        self.assertEqual(self.occupation.end_date, datetime(2021, 6, 1))

    def test_string_representation(self):
        expected_str = "Software Engineer at TechCorp, Technology industry - 5 years of experience from 2022-01-01 00:00:00 to 2023-01-01 00:00:00"
        self.assertEqual(str(self.occupation), expected_str)


if __name__ == "__main__":
    unittest.main()
