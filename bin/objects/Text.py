from typing import Optional, List, Union

from bin.entities.Person import Person
from bin.handlers.InputHandlers import validate_input
from bin.objects.Annotation import Annotation
from bin.handlers.GPTHandler import GPTHandler
from bin.objects.BaseObject import BaseObject
from bin.objects.Metadata import Metadata


class Text(BaseObject):

    def __init__(self,
                 text: Optional[str] = None,
                 annotations: Optional[Union[List[Annotation], Annotation]] = None,
                 metadata: Optional[Metadata] = None,
                 summary: Optional[str] = None,
                 associations: Optional[List[Person]] = None,
                 references: Optional[List[BaseObject]] = None) -> None:
        """
        Initialize a Text object.

        :param text: Raw text content.
        :param annotations: Annotations for the text.
        :param metadata: Metadata associated with the text.
        :param summary: Summary of the text.
        :param associations: List of associated people.
        :param references: List of associated references.
        """
        super().__init__()

        self._validate_inputs(text, annotations, metadata, summary, associations, references)

        self._text = text
        self._annotations = annotations if annotations else []
        self._metadata = metadata
        self._summary = summary
        self._associations = associations
        self._references = references
        self.openai = GPTHandler()

    def _validate_inputs(self,
                         text: Optional[str],
                         annotations: Union[List[Annotation], Annotation],
                         metadata: Optional[Metadata],
                         summary: Optional[str],
                         associations: Optional[List[Person]],
                         references: Optional[List[BaseObject]]) -> None:
        """
        Validate input arguments for the Text object.

        :param text: Raw text content.
        :param annotations: Annotations for the text.
        :param metadata: Metadata associated with the text.
        :param summary: Summary of the text.
        :param associations: List of associated people.
        :param references: List of associated references.
        """
        validate_input("text", text, [str, type(None)])
        validate_input("annotations", annotations, [list, Annotation, type(None)])
        validate_input("metadata", metadata, [Metadata, type(None)])
        validate_input("summary", summary, [str, type(None)])
        validate_input("associations", associations, [list, type(None)])
        validate_input("references", references, [list, type(None)])

        if not text:
            raise ValueError("The 'text' must be provided.")

    def generate_summary(self) -> str:
        """
        Generate a summary for the text using the GPTHandler.

        :return: Generated summary.
        """
        prompt = "Please summarize the following text as concise as possible while retaining all important information."
        result = self.openai.generate_text(prompt=self.text, system_prompt=prompt, max_tokens=-1)
        self.summary = result.messages[0]
        return self.summary

    @property
    def summary(self) -> str:
        """Getter for the text summary."""
        return self._summary

    @summary.setter
    def summary(self, value: str) -> None:
        """Setter for the text summary."""
        validate_input("summary", value, [str, type(None)])
        self._summary = value

    @property
    def text(self) -> str:
        """Getter for the raw text."""
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        """Setter for the raw text."""
        if not isinstance(value, str):
            raise TypeError("The 'text' attribute must be of type 'str'.")
        self._text = value

    @property
    def annotations(self) -> List[Annotation]:
        """Getter for the annotations."""
        return self._annotations

    @annotations.setter
    def annotations(self, value: Union[List[Annotation], Annotation]) -> None:
        """Setter for the annotations."""
        if isinstance(value, Annotation):
            value = [value]
        elif isinstance(value, list) and all(isinstance(v, Annotation) for v in value):
            pass
        else:
            raise TypeError(
                "The 'annotations' attribute must be a list of 'Annotation' objects or a single 'Annotation'.")
        self._annotations = value

    @property
    def metadata(self) -> Metadata:
        """Getter for the metadata."""
        return self._metadata

    @metadata.setter
    def metadata(self, value: Metadata) -> None:
        """Setter for the metadata."""
        if not isinstance(value, Metadata):
            raise TypeError("The 'metadata' attribute must be of type 'Metadata'.")
        self._metadata = value

    def add_annotation(self, indexes: List[int], content: str) -> None:
        """
        Add an annotation to the text.

        :param indexes: List of indexes for the annotation.
        :param content: Content of the annotation.
        """
        annotation = Annotation(indexes, content)
        self._annotations.append(annotation)

    def get_annotation(self, index: int) -> Optional[Annotation]:
        """
        Get an annotation by its index.

        :param index: Index of the annotation.
        :return: Matching Annotation or None if not found.
        """
        return next((anno for anno in self._annotations if index in anno.indexes), None)

    def delete_annotation(self, annotation: Annotation) -> None:
        """
        Delete a given annotation.

        :param annotation: The Annotation to delete.
        """
        if annotation in self._annotations:
            self._annotations.remove(annotation)

    def modify_annotation(self, annotation: Annotation, new_indexes: Optional[List[int]] = None,
                          new_content: Optional[str] = None) -> None:
        """
        Modify an existing annotation.

        :param annotation: The Annotation to modify.
        :param new_indexes: New indexes for the annotation.
        :param new_content: New content for the annotation.
        """
        if annotation in self._annotations:
            if new_indexes:
                annotation.indexes = new_indexes
            if new_content:
                annotation.annotation = new_content

    def get_indexes_of_word(self, word: str) -> List[int]:
        """
        Get indexes of a given word in the text.

        :param word: The word to search for.
        :return: List of indexes where the word is found.
        """
        return [index for index, w in enumerate(self._text.split()) if w == word]

    def delete_annotations_by_index(self, index: int) -> None:
        """
        Delete annotations by a given index.

        :param index: Index of the annotations to delete.
        """
        self._annotations = [anno for anno in self._annotations if index not in anno.indexes]

    def add_custom_metadata(self, key: str, value: Union[str, int, float]) -> None:
        """
        Add custom metadata to the text.

        :param key: Key of the metadata.
        :param value: Value of the metadata.
        """
        if not self._metadata:
            self._metadata = Metadata()
        self._metadata.add_custom_metadata(key, value)
        self._metadata.update_modification_date()

    def get_custom_metadata(self, key: str) -> Optional[Union[str, int, float]]:
        """
        Get a custom metadata by its key.

        :param key: Key of the metadata.
        :return: Value of the metadata or None if not found.
        """
        return self._metadata.get_custom_metadata(key) if self._metadata else None

    def delete_custom_metadata(self, key: str) -> None:
        """
        Delete a custom metadata by its key.

        :param key: Key of the metadata to delete.
        """
        if self._metadata:
            self._metadata.delete_custom_metadata(key)
            self._metadata.update_modification_date()

    @property
    def data(self) -> dict:
        """
        Get the data representation of the text.

        :return: Dictionary representation of the text.
        """
        return {
            'text': self._text,
            'annotations': [anno.__dict__ for anno in self._annotations] if self._annotations else [],
            'metadata': self._metadata.__dict__ if self._metadata else None,
            'summary': self._summary,
            'associations': [assoc.uid for assoc in self._associations] if self._associations else [],
            'references': [ref.uid for ref in self._references] if self._references else []
        }


