import unittest
from bin.attributes.Gender import Gender
from bin.objects.Proof import Proof


class TestGender(unittest.TestCase):
    def test_gender_initialization(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        gender_obj = Gender('Male', proof)
        self.assertEqual(gender_obj.gender, 'Male')

    def test_gender_setter(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        gender_obj = Gender('Male', proof)
        gender_obj.gender = 'Female'
        self.assertEqual(gender_obj.gender, 'Female')

    def test_gender_invalid_value(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        with self.assertRaises(ValueError):
            Gender('InvalidGender', proof)

    def test_gender_str_representation(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        gender_obj = Gender('Other', proof)
        self.assertEqual(str(gender_obj), 'Gender: Other')


if __name__ == '__main__':
    unittest.main()
