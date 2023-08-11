import unittest

from bin.attributes.Name import Name
from bin.objects.Proof import Proof


class TestName(unittest.TestCase):

    def test_initialization(self):
        proof = Proof('ID Proof')  # Example Proof object
        name = Name('John', 'Doe', proof, ['Michael', 'David'])
        self.assertEqual(name.name, 'John')
        self.assertEqual(name.surname, 'Doe')
        self.assertEqual(name.middlenames, ['Michael', 'David'])
        self.assertEqual(name.full_name, 'John Michael David Doe')
        self.assertEqual(name.initials, 'J.M.D.D.')

    def test_setters(self):
        proof = Proof('ID Proof')  # Example Proof object
        name = Name('John', 'Doe', proof)
        name.name = ' Jane '
        name.surname = ' Smith '
        name.middlenames = [' Alice ', ' Bob ']
        self.assertEqual(name.name, 'Jane')
        self.assertEqual(name.surname, 'Smith')
        self.assertEqual(name.middlenames, ['Alice', 'Bob'])

    def test_without_middlenames(self):
        proof = Proof('ID Proof')  # Example Proof object
        name = Name('John', 'Doe', proof)
        self.assertEqual(name.full_name, 'John Doe')
        self.assertEqual(name.initials, 'J.D.')

    def test_empty_initialization(self):
        name = Name()
        self.assertEqual(name.name, '')
        self.assertEqual(name.surname, '')
        self.assertEqual(name.middlenames, [])
        self.assertEqual(name.full_name, ' ')
        self.assertEqual(name.initials, '')

    def test_middlenames_as_string(self):
        proof = Proof('ID Proof')  # Example Proof object
        name = Name('John', 'Doe', proof, 'Michael')
        self.assertEqual(name.middlenames, ['Michael'])


if __name__ == '__main__':
    unittest.main()
