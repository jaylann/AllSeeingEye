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

    def test_case_insensitivity(self):
        # Testing with different capitalizations
        status1 = RelationshipStatus('single', self.proof)
        self.assertEqual(status1.status, 'Single')

        status2 = RelationshipStatus('In A RELATIONSHIP', self.proof)
        self.assertEqual(status2.status, 'In a Relationship')

        status3 = RelationshipStatus('DiVorced', self.proof)
        self.assertEqual(status3.status, 'Divorced')


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
