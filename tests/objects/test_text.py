import unittest
from bin.objects.Annotation import Annotation
from bin.objects.Metadata import Metadata
from bin.objects.Text import Text


class TestText(unittest.TestCase):

    def setUp(self):
        self.text_obj = Text(text="This is a sample text.")

    def test_init(self):
        self.assertIsInstance(self.text_obj, Text)
        self.assertEqual(self.text_obj.text, "This is a sample text.")
        self.assertEqual(self.text_obj.annotations, [])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            Text()

        with self.assertRaises(ValueError):
            Text(text="")

    def test_annotations(self):
        self.text_obj.add_annotation([0, 1], "sample annotation")
        added_anno = self.text_obj.annotations[0]
        self.assertEqual(added_anno.indexes, [0, 1])
        self.assertEqual(added_anno.annotation, "sample annotation")

        self.text_obj.modify_annotation(added_anno, new_content="modified annotation")
        self.assertEqual(added_anno.annotation, "modified annotation")

        self.text_obj.delete_annotation(added_anno)
        self.assertEqual(self.text_obj.annotations, [])

    def test_metadata(self):
        self.text_obj.add_custom_metadata("key", "value")
        self.assertEqual(self.text_obj.get_custom_metadata("key"), "value")

        self.text_obj.delete_custom_metadata("key")
        self.assertIsNone(self.text_obj.get_custom_metadata("key"))

    def test_getters_setters(self):
        self.text_obj.text = "New text"
        self.assertEqual(self.text_obj.text, "New text")

        anno = Annotation([0, 1], "sample annotation")
        self.text_obj.annotations = [anno]
        self.assertEqual(self.text_obj.annotations, [anno])

        metadata = Metadata()
        self.text_obj.metadata = metadata
        self.assertEqual(self.text_obj.metadata, metadata)



    """
    def test_data_property(self):
        self.text_obj = Text(text="Sample", annotations=[Annotation([0], "Anno")], metadata=Metadata())
        expected_data = {
            'text': 'Sample',
            'annotations': [{'indexes': [0], 'annotation': 'Anno'}],
            'metadata': {
                # Assuming Metadata's default properties here. If Metadata has more properties, they should be added.
                'creation_date': self.text_obj.metadata.creation_date,
                'modification_date': self.text_obj.metadata.modification_date,
                'custom_metadata': {}
            },
            'summary': None,
            'associations': [],
            'references': []
        }
        self.assertEqual(self.text_obj.data, expected_data)
    """
    # First need to implement uid to Person and BaseObject
if __name__ == "__main__":
    unittest.main()
