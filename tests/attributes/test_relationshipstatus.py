import unittest

from bin.attributes.RelationshipStatus import RelationshipStatus
from bin.objects.Proof import Proof


class TestRelationshipStatus(unittest.TestCase):

    def setUp(self):
        self.proof = Proof("Placeholder")  # Assuming Proof can be initialized without arguments

    def test_valid_status(self):
        status = RelationshipStatus('Single', self.proof)
        self.assertEqual(status.status, 'Single')

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            RelationshipStatus('Invalid Status', self.proof)

    def test_valid_statuses(self):
        for valid_status in RelationshipStatus.VALID_STATUSES:
            status = RelationshipStatus(valid_status, self.proof)
            self.assertEqual(status.status, valid_status)

    def test_string_representation(self):
        status = RelationshipStatus('Married', self.proof)
        self.assertEqual(str(status), 'Relationship Status: Married')

    def test_initialization_without_proof(self):
        status = RelationshipStatus('Single')
        self.assertEqual(status.status, 'Single')

    def test_case_sensitivity(self):
        # This test assumes that the status is case-sensitive. If it is not, the test should be adjusted accordingly.
        with self.assertRaises(ValueError):
            RelationshipStatus('single', self.proof)

    def test_dictionary_representation(self):
        status = RelationshipStatus('Married', self.proof)
        expected_dict = {
            'status': 'Married',
            'proof': [self.proof.__dict__()]  # Assuming the Proof object has a __dict__ method
        }
        self.assertEqual(status.__dict__(), expected_dict)

    def test_dictionary_representation_without_proof(self):
        status = RelationshipStatus('Married')
        expected_dict = {
            'status': 'Married',
            'proof': None
        }
        self.assertEqual(status.__dict__(), expected_dict)


if __name__ == '__main__':
    unittest.main()
