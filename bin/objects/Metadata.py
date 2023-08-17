from datetime import datetime
from typing import List, Optional, Dict, Any, Union

from bin.attributes.Name import Name
from bin.entities.Person import Person
from bin.handlers.InputHandlers import validate_input
from bin.utils.date import convert_to_date


class Metadata:
    """
    Metadata class to store and manage metadata information.

    Attributes:
        author (Union[str, Person], optional): Name of the author or a Person object.
        creation_date (Union[datetime, str], optional): Date of creation.
        modification_date (Union[datetime, str], optional): Date of last modification.
        source (str, optional): Source of the metadata.
        tags (List[str], optional): List of tags associated with the metadata.
    """

    def __init__(self,
                 author: Optional[Union[str, Person]] = None,
                 creation_date: Optional[Union[datetime, str]] = None,
                 modification_date: Optional[Union[datetime, str]] = None,
                 source: Optional[str] = None,
                 tags: Optional[List[str]] = None):
        """Initialize Metadata instance."""

        # Validate input
        validate_input("Author", author, [str, Person])
        validate_input("Creation date", creation_date, [datetime, str])
        validate_input("Modification date", modification_date, [datetime, str])
        validate_input("Source", source, [str])
        if tags:
            for tag in tags:
                validate_input("Tag", tag, [str])

        # Initialize attributes
        self._author = author if isinstance(author, Person) else (
            Person(name=Name(author)) if author is not None else None)

        self._creation_date = creation_date if creation_date else datetime.now()
        self._modification_date = modification_date if modification_date else datetime.now()
        self._source = source
        self._tags = tags if tags else []
        self._custom_metadata: Dict[str, Any] = {}
    

    @property
    def author(self) -> Optional[Union[str, Person]]:
        """Return the author."""
        return self._author

    @author.setter
    def author(self, value: Optional[Union[str, Person]]):
        """Set the author."""
        validate_input("Author", value, [str, Person])
        self._author = value if isinstance(value, Person) else Person(name=Name(value))
        self.update_modification_date()

    @property
    def creation_date(self) -> datetime:
        """Return the creation date."""
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value: Union[str, datetime]):
        """Set the creation date."""
        validate_input("Creation date", value, [datetime, str])
        self._creation_date = value if isinstance(value, datetime) else convert_to_date(value)
        self.update_modification_date()

    @property
    def modification_date(self) -> datetime:
        """Return the modification date."""
        return self._modification_date

    @modification_date.setter
    def modification_date(self, value: datetime):
        """Set the modification date."""
        validate_input("Modification date", value, [datetime])
        self._modification_date = value

    @property
    def source(self) -> Optional[str]:
        """Return the source."""
        return self._source

    @source.setter
    def source(self, value: Optional[str]):
        """Set the source."""
        validate_input("Source", value, [str])
        self._source = value
        self.update_modification_date()

    @property
    def tags(self) -> List[str]:
        """Return the list of tags."""
        return self._tags

    @tags.setter
    def tags(self, value: List[str]):
        """Set the tags."""
        for tag in value:
            validate_input("Tag", tag, [str])
        self._tags = value
        self.update_modification_date()

    def add_custom_metadata(self, key: str, value: Any):
        """Add custom metadata."""
        validate_input("Key", key, [str])
        self._custom_metadata[key] = value
        self.update_modification_date()

    def get_custom_metadata(self, key: str) -> Any:
        """Retrieve a custom metadata value by key."""
        return self._custom_metadata.get(key, None)

    def delete_custom_metadata(self, key: str):
        """Delete a custom metadata entry by key."""
        validate_input("Key", key, [str])
        if key in self._custom_metadata:
            del self._custom_metadata[key]
            self.update_modification_date()

    def update_modification_date(self):
        """Update the modification date to the current datetime."""
        self._modification_date = datetime.now()
