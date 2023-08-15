from datetime import datetime


class Metadata:
    def __init__(self, author=None, creation_date=None, modification_date=None, source=None, tags=None):
        self._author = author
        self._creation_date = creation_date if creation_date else datetime.now()
        self._modification_date = modification_date if modification_date else datetime.now()
        self._source = source
        self._tags = tags if tags else []
        self._custom_metadata = {}

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
        self.update_modification_date()

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, value):
        self._creation_date = value
        self.update_modification_date()

    @property
    def modification_date(self):
        return self._modification_date

    @modification_date.setter
    def modification_date(self, value):
        self._modification_date = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self.update_modification_date()

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = value
            self.update_modification_date()

    def add_custom_metadata(self, key, value):
        self._custom_metadata[key] = value
        self.update_modification_date()

    def get_custom_metadata(self, key):
        return self._custom_metadata.get(key, None)

    def delete_custom_metadata(self, key):
        if key in self._custom_metadata:
            del self._custom_metadata[key]
            self.update_modification_date()

    def update_modification_date(self):
        self._modification_date = datetime.now()
