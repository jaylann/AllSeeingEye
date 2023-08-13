import unittest

from bin.attributes.Email import Email
from bin.objects.Proof import Proof


class TestEmail(unittest.TestCase):

    def test_valid_email_creation(self):
        proof = Proof("Test Proof")
        email_obj = Email("john.doe@example.com", proof)
        self.assertEqual(str(email_obj), "john.doe@example.com")
        self.assertEqual(email_obj.provider, "example")

    def test_invalid_email_creation(self):
        proof = Proof("Test Proof")
        with self.assertRaises(ValueError):
            Email("invalid-email", proof)

    def test_provider_extraction(self):
        proof = Proof("Test Proof")
        email_obj = Email("user@google.com", proof)
        self.assertEqual(email_obj.provider, "google")

        email_obj = Email("user@company.co.uk", proof)
        self.assertEqual(email_obj.provider, "company")

    def test_email_update(self):
        proof = Proof("Test Proof")
        email_obj = Email("john.doe@example.com", proof)
        email_obj.email = "user@yahoo.com"
        self.assertEqual(email_obj.email, "user@yahoo.com")
        self.assertEqual(email_obj.provider, "yahoo")

    def test_invalid_email_update(self):
        proof = Proof("Test Proof")
        email_obj = Email("john.doe@example.com", proof)
        with self.assertRaises(ValueError):
            email_obj.email = "invalid-email"

    def test_initialization_with_empty_email(self):
        proof = Proof("Test Proof")
        with self.assertRaises(ValueError):
            Email("", proof)

    def test_emails_with_uncommon_formats(self):
        proof = Proof("Test Proof")
        email_obj = Email("user@sub.example.com", proof)
        self.assertEqual(email_obj.provider, "sub")

        email_obj = Email("user@subdomain.company.co.uk", proof)
        self.assertEqual(email_obj.provider, "subdomain")

    def test_email_with_multiple_errors(self):
        proof = Proof("Test Proof")
        with self.assertRaises(ValueError):
            Email("@missing-user-part.com", proof)
        with self.assertRaises(ValueError):
            Email("user@.missing-tld", proof)
        with self.assertRaises(ValueError):
            Email("user@missing-tld.", proof)

    def test_dict_representation(self):
        proof = Proof("Test Proof")
        email_obj = Email("john.doe@example.com", proof)
        expected_dict = {
            'email': "john.doe@example.com",
            'proof': [proof.__dict__()]  # Adjust as needed based on Proof's __dict__ implementation
        }
        self.assertEqual(email_obj.__dict__(), expected_dict)


if __name__ == "__main__":
    unittest.main()
