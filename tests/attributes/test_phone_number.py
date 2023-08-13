import unittest

from bin.attributes.PhoneNumber import PhoneNumber
from bin.objects.Proof import Proof


class TestPhoneNumber(unittest.TestCase):

    def test_valid_number(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+1 650-555-1234", proof=proof)
        self.assertEqual(phone.country_code, 1)
        self.assertEqual(phone.local_number, "6505551234")
        self.assertEqual(phone.area_code, "650")

    def test_invalid_number(self):
        proof = Proof("Phone")
        with self.assertRaises(ValueError):
            PhoneNumber("invalid_number", proof=proof)

    def test_area_code_us(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+1 212-555-1234", proof=proof)
        self.assertEqual(phone.area_code, "212")

    def test_area_code_in(self):
        proof = Proof("Phone")

        phone = PhoneNumber("+91 22-5555-1234", proof=proof)
        self.assertEqual(phone.area_code, "22")

    def test_area_code_unknown(self):
        proof = Proof("Phone")
        with self.assertRaises(ValueError):
            PhoneNumber("+123 456-7890", proof=proof)  # Non-existent country code

    # Add more specific tests for other G20 countries as needed

    def test_valid_german_number(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+491771231231", proof=proof)
        self.assertEqual(phone.country_code, 49)
        self.assertEqual(phone.local_number, "1771231231")
        self.assertEqual(phone.area_code, "177")

    def test_local_number_with_context(self):
        proof = Proof("Phone")
        phone = PhoneNumber("01771231231", proof=proof, country_context="DE")  # Parsing with Germany context
        self.assertEqual(phone.country_code, 49)
        self.assertEqual(phone.local_number, "1771231231")
        self.assertEqual(phone.area_code, "177")

    def test_local_number_without_context(self):
        proof = Proof("Phone")
        # This test may fail without context, depending on how the class is implemented
        with self.assertRaises(ValueError):
            PhoneNumber("01771231231", proof=proof)

    def test_short_number(self):
        proof = Proof("Phone")
        # This test may fail if short numbers are considered invalid
        with self.assertRaises(ValueError):
            PhoneNumber("12225", proof=proof)

    def test_number_without_area_code_mapping(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+65 6123-4567", proof=proof)  # Example of a valid Singapore (SG) number
        self.assertIsNone(phone.area_code)  # No area code mapping for Singapore

    def test_number_with_special_characters(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+1 (650)-555-1234 ext. 5678", proof=proof)
        self.assertEqual(phone.country_code, 1)
        self.assertEqual(phone.local_number, "6505551234")
        self.assertEqual(phone.area_code, "650")

    def test_empty_number(self):
        proof = Proof("Phone")
        with self.assertRaises(ValueError):
            PhoneNumber("", proof=proof)

    def test_number_with_extension(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+1-650-555-1234 ext. 5678", proof=proof)
        self.assertEqual(phone.country_code, 1)
        self.assertEqual(phone.local_number, "6505551234")
        self.assertEqual(phone.area_code, "650")


if __name__ == "__main__":
    unittest.main()
