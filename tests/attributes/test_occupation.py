import unittest
from datetime import datetime

from bin.attributes.Occupation import Occupation
from bin.objects.Proof import Proof


class TestOccupation(unittest.TestCase):

    def setUp(self):
        self.proof = Proof("Placeholder")  # You may need to pass the required arguments for the Proof object
        start_date = "2022-01-01"
        end_date = "2023-01-01"
        self.occupation = Occupation("Software Engineer", "TechCorp",
                                     "Technology", 5, start_date, end_date, self.proof)

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
        expected_str = ("Software Engineer at TechCorp, Technology industry - 5 years of experience from 2022-01-01 "
                        "00:00:00 to 2023-01-01 00:00:00")
        self.assertEqual(str(self.occupation), expected_str)

    def test_initialization_with_none_values(self):
        occupation = Occupation()
        self.assertIsNone(occupation.job_title)
        self.assertIsNone(occupation.company_name)
        self.assertIsNone(occupation.industry)
        self.assertEqual(occupation.years_experience, 0)
        self.assertIsNone(occupation.start_date)
        self.assertIsNone(occupation.end_date)

    def test_years_at_company_calculation(self):
        start_date = "2022-01-01"
        end_date = "2023-01-01"
        occupation = Occupation(start_date=start_date, end_date=end_date)
        self.assertAlmostEqual(occupation.years_at_company, 1.0)

    def test_start_date_after_end_date(self):
        start_date = "2023-01-01"
        end_date = "2022-01-01"
        with self.assertRaises(ValueError):
            Occupation(start_date=start_date, end_date=end_date)

        occupation = Occupation(start_date="2022-01-01", end_date="2023-01-01")
        # Test setting start_date after end_date
        with self.assertRaises(ValueError):
            occupation.start_date = "2024-01-01"
        # Test setting end_date before start_date
        with self.assertRaises(ValueError):
            occupation.end_date = "2021-01-01"

    def test_dict_representation(self):
        expected_dict = {
            'job_title': "Software Engineer",
            'company_name': "TechCorp",
            'industry': "Technology",
            'years_experience': 5,
            'start_date': datetime(2022, 1, 1),
            'end_date': datetime(2023, 1, 1),
            'proof': [self.proof.__dict__()]  # Assuming __dict__ method exists in Proof class
        }
        self.assertDictEqual(self.occupation.__dict__(), expected_dict)


if __name__ == "__main__":
    unittest.main()
