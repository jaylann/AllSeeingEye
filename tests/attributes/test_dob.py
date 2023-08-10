import unittest
from datetime import datetime
from bin.attributes.BaseAttribute import BaseAttribute
from bin.attributes.DOB import DOB


class TestDOB(unittest.TestCase):

    def test_initialization(self):
        dob = DOB('2023-08-10', 'ID Proof')
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
            dob = DOB(date_str, 'ID Proof')
            self.assertEqual(10, dob.day)
            self.assertEqual(8, dob.month)
            self.assertEqual(2023, dob.year)

    def test_setters(self):
        dob = DOB('2023-08-10', 'ID Proof')
        dob.day = 15
        dob.month = 5
        dob.year = 2000
        self.assertEqual(dob.day, 15)
        self.assertEqual(dob.month, 5)
        self.assertEqual(dob.year, 2000)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            DOB('invalid-date', 'ID Proof')


if __name__ == '__main__':
    unittest.main()
