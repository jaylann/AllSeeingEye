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

    def test_initialization_with_all_valid_values(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        for valid_gender in Gender.VALID_GENDERS:
            with self.subTest(gender=valid_gender):
                gender_obj = Gender(valid_gender, proof)
                self.assertEqual(gender_obj.gender, valid_gender)

    def test_setter_with_all_valid_values(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        gender_obj = Gender('Male', proof)
        for valid_gender in Gender.VALID_GENDERS:
            with self.subTest(gender=valid_gender):
                gender_obj.gender = valid_gender
                self.assertEqual(gender_obj.gender, valid_gender)

    def test_initialization_with_none_value(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        with self.assertRaises(ValueError):
            Gender(None, proof)

    def test_dict_representation(self):
        proof = Proof("Placeholder")  # Replace with actual initialization if required
        gender_obj = Gender('Male', proof)
        expected_dict = {
            'gender': 'Male',
            'proof': [proof.__dict__()]  # Adjust as needed based on Proof's __dict__ implementation
        }
        self.assertEqual(gender_obj.__dict__(), expected_dict)


if __name__ == '__main__':
    unittest.main()
