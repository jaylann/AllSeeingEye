import unittest
from bin.attributes.PhoneNumber import PhoneNumber
from bin.objects.Proof import Proof


class TestPhoneNumber(unittest.TestCase):

    def test_valid_number(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+1 650-555-1234", proof)
        self.assertEqual(phone.country_code, 1)
        self.assertEqual(phone.local_number, "6505551234")
        self.assertEqual(phone.area_code, "650")

    def test_invalid_number(self):
        proof = Proof("Phone")
        with self.assertRaises(ValueError):
            PhoneNumber("invalid_number", proof)

    def test_area_code_us(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+1 212-555-1234", proof)
        self.assertEqual(phone.area_code, "212")

    def test_area_code_in(self):
        proof = Proof("Phone")

        phone = PhoneNumber("+91 22-5555-1234", proof)
        self.assertEqual(phone.area_code, "22")

    def test_area_code_unknown(self):
        proof = Proof("Phone")
        with self.assertRaises(ValueError):
            PhoneNumber("+123 456-7890", proof)  # Non-existent country code

    # Add more specific tests for other G20 countries as needed

    def test_valid_german_number(self):
        proof = Proof("Phone")
        phone = PhoneNumber("+491771231231", proof)
        self.assertEqual(phone.country_code, 49)
        self.assertEqual(phone.local_number, "1771231231")
        self.assertEqual(phone.area_code, "177")

    def test_local_number_with_context(self):
        proof = Proof("Phone")
        phone = PhoneNumber("01771231231", proof, "DE")  # Parsing with Germany context
        self.assertEqual(phone.country_code, 49)
        self.assertEqual(phone.local_number, "1771231231")
        self.assertEqual(phone.area_code, "177")

    def test_local_number_without_context(self):
        proof = Proof("Phone")
        # This test may fail without context, depending on how the class is implemented
        with self.assertRaises(ValueError):
            PhoneNumber("01771231231", proof)

    def test_short_number(self):
        proof = Proof("Phone")
        # This test may fail if short numbers are considered invalid
        with self.assertRaises(ValueError):
            PhoneNumber("12225", proof)


if __name__ == "__main__":
    unittest.main()
