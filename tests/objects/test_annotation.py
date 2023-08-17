import unittest

from bin.objects.Annotation import Annotation


class TestAnnotation(unittest.TestCase):

    def setUp(self):
        self.annotation = Annotation([0, 1, 2], "sample")

    def test_initialization(self):
        # Check basic initialization
        self.assertEqual(self.annotation.annotation, "sample")
        self.assertEqual(self.annotation.indexes, [0, 1, 2])

        # Check initialization type errors
        with self.assertRaises(ValueError):
            Annotation([0, 1, "two"], "sample")

        with self.assertRaises(ValueError):
            Annotation([0, 1, 2], 123)

    def test_annotation_setter_and_getter(self):
        new_annotation = "new sample"
        self.annotation.annotation = new_annotation
        self.assertEqual(self.annotation.annotation, new_annotation)

        with self.assertRaises(ValueError):
            self.annotation.annotation = 123

    def test_indexes_setter_and_getter(self):
        new_indexes = [3, 4, 5]
        self.annotation.indexes = new_indexes
        self.assertEqual(self.annotation.indexes, new_indexes)

        with self.assertRaises(ValueError):
            self.annotation.indexes = [1, 2, "three"]

        with self.assertRaises(ValueError):
            self.annotation.indexes = "1, 2, 3"

    def test_set_start_index(self):
        self.annotation.set_start_index(10)
        self.assertEqual(self.annotation.indexes[0], 10)

        # Test when indexes list is empty
        empty_annotation = Annotation([], "empty")
        empty_annotation.set_start_index(20)
        self.assertEqual(empty_annotation.indexes, [20])

        with self.assertRaises(ValueError):
            self.annotation.set_start_index("ten")

    def test_set_end_index(self):
        self.annotation.set_end_index(20)
        self.assertEqual(self.annotation.indexes[-1], 20)

        # Test when indexes list is empty
        empty_annotation = Annotation([], "empty")
        empty_annotation.set_end_index(30)
        self.assertEqual(empty_annotation.indexes, [30])

        with self.assertRaises(ValueError):
            self.annotation.set_end_index("twenty")


if __name__ == "__main__":
    unittest.main()
