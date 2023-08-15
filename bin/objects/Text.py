from bin.objects.Annotation import Annotation

from bin.objects.BaseObject import BaseObject
from bin.objects.Metadata import Metadata


class Text(BaseObject):
    def __init__(self, text, annotations=None, metadata=None):
        super().__init__()
        self._text = text
        self._annotations = annotations if annotations else []
        self._metadata = metadata

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def annotations(self):
        return self._annotations

    @annotations.setter
    def annotations(self, value):
        if isinstance(value, list) and all(isinstance(a, Annotation) for a in value):
            self._annotations = value

    def add_annotation(self, indexes, content):
        annotation = Annotation(indexes, content)
        self._annotations.append(annotation)

    def get_annotation(self, index):
        return next((anno for anno in self._annotations if index in anno.indexes), None)

    def delete_annotation(self, annotation):
        if annotation in self._annotations:
            self._annotations.remove(annotation)

    def modify_annotation(self, annotation, new_indexes=None, new_content=None):
        if annotation in self._annotations:
            if new_indexes:
                annotation.indexes = new_indexes
            if new_content:
                annotation.annotation = new_content

    def get_indexes_of_word(self, word):
        return [index for index, w in enumerate(self._text.split()) if w == word]

    def delete_annotations_by_index(self, index):
        self._annotations = [anno for anno in self._annotations if index not in anno.indexes]

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        if isinstance(value, Metadata):
            self._metadata = value

    def add_custom_metadata(self, key, value):
        if not self._metadata:
            self._metadata = Metadata()
        self._metadata.add_custom_metadata(key, value)
        self._metadata.update_modification_date()

    def get_custom_metadata(self, key):
        return self._metadata.get_custom_metadata(key) if self._metadata else None

    def delete_custom_metadata(self, key):
        if self._metadata:
            self._metadata.delete_custom_metadata(key)
            self._metadata.update_modification_date()
