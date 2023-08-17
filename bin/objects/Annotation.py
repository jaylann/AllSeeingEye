from typing import List

from bin.handlers.InputHandlers import validate_input


class Annotation:
    def __init__(self, indexes: List[int], annotation: str) -> None:
        """Initialize an Annotation instance.

        Args:
            indexes (List[int]): List of indexes to be annotated.
            annotation (str): The annotation text.

        Raises:
            ValueError: If input types are incorrect.
        """
        validate_input("Annotation", annotation, [str])
        self._annotation = annotation

        validate_input("Indexes", indexes, [list])
        if not all(isinstance(i, int) for i in indexes):
            raise ValueError("All elements in the indexes list must be integers.")
        self._indexes = indexes

    @property
    def annotation(self) -> str:
        """Get the annotation text."""
        return self._annotation

    @annotation.setter
    def annotation(self, value: str) -> None:
        """Set the annotation text."""
        validate_input("Annotation", value, [str])
        self._annotation = value

    @property
    def indexes(self) -> List[int]:
        """Get the list of indexes."""
        return self._indexes

    @indexes.setter
    def indexes(self, value: List[int]) -> None:
        """Set the list of indexes."""
        validate_input("Indexes", value, [list])
        if not all(isinstance(i, int) for i in value):
            raise ValueError("All elements in the indexes list must be integers.")
        self._indexes = value

    def set_start_index(self, start_index: int) -> None:
        """Set the start index of the annotation.

        Args:
            start_index (int): The start index to be set.

        Raises:
            ValueError: If the start_index type is incorrect.
        """
        validate_input("Start Index", start_index, [int])
        if self._indexes:  # Only adjust if there are already indexes
            self._indexes[0] = start_index
        else:
            self._indexes.append(start_index)

    def set_end_index(self, end_index: int) -> None:
        """Set the end index of the annotation.

        Args:
            end_index (int): The end index to be set.

        Raises:
            ValueError: If the end_index type is incorrect.
        """
        validate_input("End Index", end_index, [int])
        if self._indexes:  # Only adjust if there are already indexes
            self._indexes[-1] = end_index
        else:
            self._indexes.append(end_index)
