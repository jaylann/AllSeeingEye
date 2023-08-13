import unittest
from datetime import datetime

from bin.attributes.DOB import DOB
from bin.objects.Proof import Proof


class TestDOB(unittest.TestCase):

    def test_initialization(self):
        dob = DOB('2023-08-10', Proof('ID Proof'))
        self.assertEqual(dob.day, 10)
        self.assertEqual(dob.month, 8)
        self.assertEqual(dob.year, 2023)

    def test_date_formats(self):
        date_formats = [
            '10-08-2023', '10/08/2023', '10.08.2023', '10 August 2023',
            '10 Aug 2023', 'Thursday, 10 August 2023', 'Thu, 10 Aug 2023',
            '10-08-23', '10/08/23', '2023-08-10', '2023/08/10', '2023.08.10',
            '2023 August 10', '2023 Aug 10'
        ]
        for date_str in date_formats:
            dob = DOB(date_str, Proof('ID Proof'))
            self.assertEqual(10, dob.day)
            self.assertEqual(8, dob.month)
            self.assertEqual(2023, dob.year)

    def test_setters(self):
        dob = DOB('2023-08-10', Proof('ID Proof'))
        dob.day = 15
        dob.month = 5
        dob.year = 2000
        self.assertEqual(dob.day, 15)
        self.assertEqual(dob.month, 5)
        self.assertEqual(dob.year, 2000)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            DOB('invalid-date', Proof('ID Proof'))

    def test_initialization_with_datetime(self):
        from datetime import datetime
        dob_datetime = datetime(2023, 8, 10)
        dob = DOB(dob_datetime, Proof('ID Proof'))
        self.assertEqual(dob.day, 10)
        self.assertEqual(dob.month, 8)
        self.assertEqual(dob.year, 2023)

    def test_empty_date_string(self):
        with self.assertRaises(ValueError):
            DOB('', Proof('ID Proof'))

    def test_setters_with_invalid_values(self):
        dob = DOB('2023-08-10', Proof('ID Proof'))
        with self.assertRaises(ValueError):
            dob.day = 32
        with self.assertRaises(ValueError):
            dob.month = 13
        with self.assertRaises(ValueError):
            dob.year = -2023

    def test_dict_representation(self):
        dob = DOB('2023-08-10', Proof('ID Proof'))
        dob_dict = dob.__dict__()
        self.assertIsInstance(dob_dict['DOB'], datetime)
        self.assertEqual(dob_dict['DOB'].year, 2023)
        self.assertEqual(dob_dict['DOB'].month, 8)
        self.assertEqual(dob_dict['DOB'].day, 10)
        # Add additional assertions for 'proof' if needed


if __name__ == '__main__':
    unittest.main()
