import unittest
from datetime import datetime
from bin.attributes.Name import Name
from bin.entities.Person import Person
from bin.objects.Metadata import Metadata


class TestMetadata(unittest.TestCase):

    def setUp(self):
        self.metadata = Metadata()

    def test_initialization(self):
        self.assertIsInstance(self.metadata.creation_date, datetime)
        self.assertIsInstance(self.metadata.modification_date, datetime)
        self.assertIsNone(self.metadata.author)
        self.assertIsNone(self.metadata.source)
        self.assertEqual(self.metadata.tags, [])

    def test_author_setter_and_getter(self):
        person = Person(name=Name("John Doe"))
        self.metadata.author = person
        self.assertEqual(self.metadata.author, person)

        self.metadata.author = "John Doe"
        self.assertIsInstance(self.metadata.author, Person)
        self.assertEqual(self.metadata.author.name.full_name, "John Doe")

        with self.assertRaises(ValueError):
            self.metadata.author = 123

    def test_creation_date_setter_and_getter(self):
        date_str = "2023-08-16"
        self.metadata.creation_date = date_str
        self.assertIsInstance(self.metadata.creation_date, datetime)

        now = datetime.now()
        self.metadata.creation_date = now
        self.assertEqual(self.metadata.creation_date, now)

        with self.assertRaises(ValueError):
            self.metadata.creation_date = []

    def test_modification_date_setter_and_getter(self):
        now = datetime.now()
        self.metadata.modification_date = now
        self.assertEqual(self.metadata.modification_date, now)

        with self.assertRaises(ValueError):
            self.metadata.modification_date = "2023-08-16"

    def test_source_setter_and_getter(self):
        source = "Test Source"
        self.metadata.source = source
        self.assertEqual(self.metadata.source, source)

        with self.assertRaises(ValueError):
            self.metadata.source = 123

    def test_tags_setter_and_getter(self):
        tags = ["tag1", "tag2"]
        self.metadata.tags = tags
        self.assertEqual(self.metadata.tags, tags)

        with self.assertRaises(ValueError):
            self.metadata.tags = ["tag1", 123]

    def test_custom_metadata(self):
        key = "custom_key"
        value = "custom_value"
        self.metadata.add_custom_metadata(key, value)
        self.assertEqual(self.metadata.get_custom_metadata(key), value)

        self.metadata.delete_custom_metadata(key)
        self.assertIsNone(self.metadata.get_custom_metadata(key))

        with self.assertRaises(ValueError):
            self.metadata.add_custom_metadata(123, value)

    def test_default_values(self):
        m = Metadata()
        self.assertIsNone(m.author)
        self.assertIsInstance(m.creation_date, datetime)
        self.assertIsInstance(m.modification_date, datetime)
        self.assertIsNone(m.source)
        self.assertEqual(m.tags, [])

    def test_future_date(self):
        future_date = "3023-08-16"
        self.metadata.creation_date = future_date
        self.assertIsInstance(self.metadata.creation_date, datetime)

    def test_past_date(self):
        past_date = "1923-08-16"
        self.metadata.creation_date = past_date
        self.assertIsInstance(self.metadata.creation_date, datetime)

    def test_error_messages(self):
        with self.assertRaisesRegex(ValueError,
                                    "Author must be one of the types: <class 'str'>, <class 'bin.entities.Person.Person'>."):
            self.metadata.author = []

        with self.assertRaisesRegex(ValueError, "Source must be one of the types: <class 'str'>."):
            self.metadata.source = 123

    def test_sequential_operations(self):
        self.metadata.author = "John Doe"
        self.metadata.tags = ["tag1", "tag2"]
        self.metadata.add_custom_metadata("key1", "value1")
        self.assertEqual(self.metadata.get_custom_metadata("key1"), "value1")

        self.metadata.delete_custom_metadata("key1")
        self.assertIsNone(self.metadata.get_custom_metadata("key1"))

        self.metadata.author = "Jane Doe"
        self.assertNotEqual(self.metadata.author.name.full_name, "John Doe")
        self.assertEqual(self.metadata.author.name.full_name, "Jane Doe")

    def test_integration_with_person(self):
        person = Person(name=Name("John Doe"))
        self.metadata.author = person
        self.assertEqual(self.metadata.author, person)

        self.metadata.author = "Jane Smith"
        self.assertIsInstance(self.metadata.author, Person)
        self.assertNotEqual(self.metadata.author, person)

if __name__ == "__main__":
    unittest.main()
