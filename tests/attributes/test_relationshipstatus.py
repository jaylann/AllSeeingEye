import unittest
from bin.attributes.BaseAttribute import BaseAttribute
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


if __name__ == '__main__':
    unittest.main()
