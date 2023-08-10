import unittest
from bin.attributes.Name import Name


class TestName(unittest.TestCase):

    def test_initialization(self):
        name = Name('John', 'Doe', 'ID Proof', ['Michael', 'David'])
        self.assertEqual(name.name, 'John')
        self.assertEqual(name.surname, 'Doe')
        self.assertEqual(name.middlenames, ['Michael', 'David'])
        self.assertEqual(name.full_name(), 'John Michael David Doe')
        self.assertEqual(name.initials(), 'J.M.D.D.')

    def test_setters(self):
        name = Name('John', 'Doe', 'ID Proof')
        name.name = ' Jane '
        name.surname = ' Smith '
        name.middlenames = [' Alice ', ' Bob ']
        self.assertEqual(name.name, 'Jane')
        self.assertEqual(name.surname, 'Smith')
        self.assertEqual(name.middlenames, ['Alice', 'Bob'])

    def test_without_middlenames(self):
        name = Name('John', 'Doe', 'ID Proof')
        self.assertEqual(name.full_name(), 'John Doe')
        self.assertEqual(name.initials(), 'J.D.')


if __name__ == '__main__':
    unittest.main()
